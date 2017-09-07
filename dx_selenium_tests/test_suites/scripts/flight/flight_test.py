#coding: utf-8
import uuid
from dx_test.dx_test import DXTest
from lib.dx_date import DXDate
from lib.gui_tests import test_case
import time

class FlightTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.setup(self.dx_constant.user_by_role['campaign_manager'])

    @test_case()
    def go_to_campaign_list_page(self):
        self.pages.search_page.click_campaign_link()
        self.pages.campaign_list_page.wait_till_visible(self.pages.campaign_list_page.campaign_list_table)
        self.pages.campaign_list_page.click_element(self.pages.campaign_list_page.search_box)
        self.pages.campaign_list_page.wait_till_element_clickable(self.pages.campaign_list_page.new_campaign_button)

    @test_case()
    def fill_advertiser_details(self, channel = 'Online', counter=0):
        self.pages.new_campaign_pop_up.click_new_campaign_link()
        self.pages.new_campaign_pop_up.wait_till_visible(self.pages.new_campaign_pop_up.popup_create_campaign_button)
        try:
            self.pages.new_campaign_pop_up.type_advertiser(self.dx_constant.advertiser_name)
            self.pages.new_campaign_pop_up.select_campaign_channel(channel)
            self.pages.new_campaign_pop_up.submit()
        except Exception:
            counter += 1
            self.pages.new_campaign_pop_up.generate_and_accept_javascript_alert()
            self.pages.new_campaign_pop_up.close()
            if counter < 5:
                self.fill_advertiser_details(channel, counter)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)

    @test_case()
    def fill_campaigns_required_fields(self):
        self.campaign = self.dx_constant.test_campaign_name + str(uuid.uuid4())
        self.pages.create_campaign_page.type_campaign_name(self.campaign)
        self.pages.create_campaign_page.enter_start_date(DXDate().todays_date())
        self.pages.create_campaign_page.enter_cpa_goal(self.dx_constant.new_campaign_cpa)
        self.pages.create_campaign_page.enter_budget(self.dx_constant.new_campaign_budget)
        self.pages.create_campaign_page.enter_cpm(self.dx_constant.new_campaign_cpm)
        self.pages.create_campaign_page.enter_cogs(self.dx_constant.new_campaign_cogs)
        self.pages.create_campaign_page.click_campaign_objective_distribution()
        self.pages.create_campaign_page.enter_end_date(DXDate().date_after_two_days())
        self.pages.create_campaign_page.click_element(self.pages.create_campaign_page.campaign_name)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)

    @test_case()
    def creation_of_campaign_with_tactics(self):
        self.pages.create_campaign_page.click_add_new_tactic()
        time.sleep(2)
        self.pages.create_campaign_page.select_tactic_retargeting()
        self.pages.create_campaign_page.enter_tactics_budget('5000')
        self.pages.create_campaign_page.click_add_new_tactic()
        time.sleep(2)
        self.pages.create_campaign_page.select_tactic_optimized()
        self.pages.create_campaign_page.enter_tactics_budget_second('5000')
        self.fill_campaigns_required_fields()

    @test_case()
    def fill_flight_details(self):
        self.flight_name = self.dx_constant.test_flight_name + str(uuid.uuid4())
        self.pages.fbs_page.fill_description(self.flight_name)
        self.pages.fbs_page.type_bid_normal(self.dx_constant.flight_bid)
        self.pages.fbs_page.type_budget(self.dx_constant.flight_budget)
        time.sleep(2)
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit)

    @test_case()
    def complete_fbs_workflow(self, attribute):
        self.flight_name = self.dx_constant.test_flight_name + str(uuid.uuid4())
        self.pages.fbs_page.fill_description(self.flight_name)
        self.pages.fbs_page.type_single_frequency_cap(attribute['single_frequency_cap_attribute'])
        self.pages.fbs_page.type_impressions(attribute['impressions_attribute'])
        self.pages.fbs_page.type_bid(attribute['bid_attribute'])
        self.pages.fbs_page.type_budget(attribute['budget_attribute'])
        time.sleep(2)
        self.pages.fbs_page.click_on_save_continue()

    @test_case()
    def go_to_create_flight_page(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details()
        self.fill_campaigns_required_fields()
        self.fill_flight_details()

    @test_case()
    def verify_flight_created(self):
        self.pages.campaign_show_page.wait_for_loading()
        self.pages.campaign_show_page.page_should_contain(self.flight_name)

    @test_case()
    def edit_flight_description_validation(self):
        self.go_to_create_flight_page()
        flight_name = self.dx_constant.special_char + str(uuid.uuid4())
        self.pages.create_flight_page.edit_flight_description(flight_name)

    @test_case()
    def success_edit_flight_creation(self):
        self.pages.bulk_upload_new_creative.page_should_contain('Upload File')

    @test_case()
    def verify_long_flight_name_validation(self):
        self.go_to_create_flight_page()
        self.pages.create_flight_page.clear_description_filter()
        flight_description = self.pages.create_flight_page.get_random_string(256)
        self.pages.create_flight_page.type_in_edit_description_filter(flight_description)
        flight_description = self.pages.create_flight_page.get_content_value(self.pages.create_flight_page.edit_flight_name)
        assert len(flight_description) == 100
        self.pages.create_flight_page.click_save_and_continue()
        time.sleep(5)

    @test_case()
    def blank_message_validation(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details()
        self.fill_campaigns_required_fields()
        self.pages.fbs_page.clear_budget_field()
        self.pages.fbs_page.click_on_save_continue()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_errors)

    @test_case()
    def verify_blank_flight_name(self):
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.blank_msgs['flight_name'])

    @test_case()
    def verify_blank_bid_name(self):
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.blank_msgs['bid'])

    @test_case()
    def verify_blank_budget_name(self):
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.blank_msgs['budget'])

    def fill_fields_with_negative_values(self):
        for field in ['bid_attribute', 'budget_attribute', 'day_cap_attribute', 'single_frequency_cap_attribute', 'impressions_attribute']:
            self.pages.fbs_page.flight_attribute[field] = self.dx_constant.negative_value
        self.complete_fbs_workflow(self.pages.fbs_page.flight_attribute)

    @test_case()
    def verify_negative_bid(self):
        self.pages.fbs_page.wait_till_element_clickable(self.pages.fbs_page.save_continue_button)
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.negative_msg['negative_bid'])

    @test_case()
    def verify_negative_budget(self):
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.negative_msg['negative_budget'])

    @test_case()
    def verify_negative_day_cap(self):
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.negative_msg['negative_day_cap'])

    def fill_fields_with_alphanumeric_values(self):
        for field in ['bid_attribute', 'budget_attribute', 'day_cap_attribute', 'single_frequency_cap_attribute', 'impressions_attribute']:
            self.pages.fbs_page.flight_attribute[field] = self.dx_constant.alphanumeric_value
        self.complete_fbs_workflow(self.pages.fbs_page.flight_attribute)

    @test_case()
    def verify_alphanumeric_values_for_frequency_cap(self):
        self.pages.fbs_page.wait_till_element_clickable(self.pages.fbs_page.save_continue_button)
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.alphanumeric_msg['alphanumeric_frequency_cap'])

    @test_case()
    def verify_alphanumeric_values_for_impression_cap(self):
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.alphanumeric_msg['alphanumeric_impression_cap'])

    @test_case()
    def valid_flight_flow(self):
        self.go_to_create_flight_page()
        self.pages.create_flight_page.page_should_contain(self.flight_name)

    @test_case()
    def create_flight_with_valid_data(self):
        self.pages.create_flight_page.page_should_contain(self.flight_name)

    @test_case()
    def to_check_fbs_content(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details()
        self.fill_campaigns_required_fields()
        contents = ['Description', 'Tactic', 'Flight Type', 'Decision Algorithm', 'Start', 'End', 'Frequency Cap']
        self.pages.fbs_page.wait_till_visible(['id', 'flights'])
        for fbs_content in contents:
            self.pages.fbs_page.page_should_contain(fbs_content)
            elements = [
                     'bid_name','delivery_name','budget_name','allocated_name',
                      'save_exit_button', 'save_continue_button'
                    ]
        for element in elements:
            assert self.pages.fbs_page.is_element_present(getattr(self.pages.fbs_page, element))

    @test_case()
    def to_check_master_checkbox(self):
        self.pages.fbs_page.select_all_flights()
        assert self.pages.fbs_page.is_element_present(self.pages.fbs_page.edit_selected)

    @test_case()
    def to_check_description_filter_functionality(self):
        self.pages.fbs_page.type_in_description_filter('QW2')
        time.sleep(5)
        self.pages.fbs_page.page_should_contain("No flights to browse")
        self.pages.fbs_page.clear_description_filter()

    @test_case()
    def to_check_tactic_filter_functionality(self):
        self.pages.fbs_page.select_tactic_filter('Default')

    @test_case()
    def to_check_add_flight_functionality(self):
        self.pages.fbs_page.click_on_add_flight()

    @test_case()
    def to_check_save_and_exit_button_functionality(self):
        self.pages.fbs_page.click_on_save_exit()
        self.verify_blank_flight_name()

    @test_case()
    def campaign_with_multiple_flights(self, channel):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details(channel)
        self.creation_of_campaign_with_tactics()
        self.flight_name = self.dx_constant.test_flight_name + str(uuid.uuid4())
        self.pages.fbs_page.fill_description(self.flight_name)
        self.pages.fbs_page.select_tactic(self.dx_constant.tactic_option_optimized)
        self.pages.fbs_page.select_flight_type(self.dx_constant.flight_type_spending)
        self.pages.fbs_page.type_bid(self.dx_constant.flight_bid)
        self.pages.fbs_page.click_on_add_flight()
        time.sleep(2)
        self.flight_name = self.dx_constant.test_flight_name + str(uuid.uuid4())
        self.pages.fbs_page.fill_description(self.flight_name)
        self.pages.fbs_page.select_tactic(self.dx_constant.tactic_option_retargeting)
        self.pages.fbs_page.select_flight_type(self.dx_constant.flight_type_tracking)
        self.pages.fbs_page.type_bid(self.dx_constant.flight_bid)
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit)
        self.pages.create_flight_page.page_should_contain(self.flight_name)

    @test_case()
    def online_campaign_with_multiple_flights(self):
        self.campaign_with_multiple_flights('Online')

    @test_case()
    def mobile_campaign_with_multiple_flights(self):
        self.campaign_with_multiple_flights('Mobile')

    @test_case()
    def video_campaign_with_multiple_flights(self):
        self.campaign_with_multiple_flights('Video')

    @test_case()
    def validation_for_blank_scenarios(self):
        self.go_to_create_flight_page()
        self.pages.create_flight_page.type_start_date('')
        self.pages.create_flight_page.type_end_date('')
        self.pages.create_flight_page.click_save_exit()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit)
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.error_div)

    @test_case()
    def start_date_blank_message(self):
        self.pages.create_flight_page.page_should_contain(self.pages.create_flight_page.blank_error_message["start_date_blank"])

    @test_case()
    def end_date_blank_message(self):
        self.pages.create_flight_page.page_should_contain(self.pages.create_flight_page.blank_error_message["end_date_blank"])

    def fill_campaign_details_for_inheritance(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details()
        self.pages.create_campaign_page.expand_add_on_cost()
        self.pages.create_campaign_page.click_new_aoc()
        self.pages.create_campaign_page.select_aoc_name(self.pages.create_campaign_page.campaign_values['custom_value'])
        self.aoc_name = 'test-add-on-cost-' + self.pages.create_campaign_page.get_random_string()
        self.pages.create_campaign_page.enter_cutom_aoc_value(self.aoc_name)
        self.pages.create_campaign_page.enter_aoc_rate('19.03')
        self.pages.create_campaign_page.expand_lang_targeting()
        self.lang_target = self.pages.create_campaign_page.campaign_values['first_lang_target']
        self.pages.create_campaign_page.select_lang_targeting(self.lang_target)
        self.pages.create_campaign_page.click_move_selected_lang()
        self.geo_target = self.pages.create_campaign_page.campaign_values['first_geo_target']
        self.pages.create_campaign_page.select_avail_countries(self.geo_target)
        self.pages.create_campaign_page.expand_brand_safety()
        self.pages.create_campaign_page.click_brand_safety_level_four()
        self.fill_campaigns_required_fields()
        self.pages.fbs_page.fill_description(self.dx_constant.test_flight_name + self.pages.fbs_page.get_random_string())
        self.pages.fbs_page.type_bid_normal(self.dx_constant.flight_bid)
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit)
        self.pages.create_flight_page.expand_lang_targeting()
        self.pages.create_flight_page.expand_geo_targeting()

    @test_case()
    def verify_inherited_add_on_cost(self):
        for content in [self.aoc_name, '19.03']:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def verify_inherited_lang_target(self):
        for content in [self.lang_target]:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def verify_inherited_geo_target(self):
        self.pages.create_flight_page.page_should_contain(self.geo_target)

    @test_case()
    def verify_lang_target_not_inherited(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details()
        self.fill_campaigns_required_fields()
        self.flight = self.dx_constant.test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(self.flight)
        self.pages.fbs_page.type_bid_normal(self.dx_constant.flight_bid)
        self.pages.fbs_page.click_on_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.go_to_link(self.flight)
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain('Language not targeted for this flight')

    @test_case()
    def verify_geo_target_not_inherited(self):
        self.pages.flight_show_page.page_should_contain('United States')

    @test_case()
    def working_of_master_checkbox(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details()
        self.fill_campaigns_required_fields()
        self.pages.fbs_page.select_all_flights()
        assert self.pages.fbs_page.find_element(self.pages.fbs_page.select_single_flight).is_selected()
        self.pages.fbs_page.select_all_flights()
        assert not self.pages.fbs_page.find_element(self.pages.fbs_page.select_single_flight).is_selected()

    @test_case()
    def working_of_flights_checkbox(self):
        self.pages.fbs_page.select_first_flight()
        assert self.pages.fbs_page.find_element(self.pages.fbs_page.edit_selected).is_displayed()
        self.pages.fbs_page.select_first_flight()

    @test_case()
    def flights_created_with_blank_dates(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details()
        self.creation_of_campaign_with_tactics()
        flight_name = self.dx_constant.test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(flight_name)
        self.pages.fbs_page.type_bid_normal('3')
        self.pages.fbs_page.type_start_date('')
        self.pages.fbs_page.type_end_date('')
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit)
        self.pages.create_flight_page.page_should_contain('Flight: '+flight_name)

    @test_case()
    def spent_should_disabled(self):
        self.pages.create_flight_page.wait_for_flight_details()
        assert not self.pages.create_flight_page.find_element(self.pages.create_flight_page.spent).is_enabled()

    @test_case()
    def verify_contents_of_audience_targeting(self):
        self.pages.create_flight_page.expand_audience_targeting()
        contents = [
                    'audience_search', 'avail_audience', 'included_audience', 'excluded_audience',
                    'include_audience','include_all_audience', 'exclude_audience', 'exclude_all_audience',
                    'remove_audience', 'remove_all_audience'
                    ]
        for element in contents:
            assert self.pages.create_flight_page.is_element_present(getattr(self.pages.create_flight_page, element))

    @test_case()
    def verify_deals_section_available(self):
        self.pages.create_flight_page.expand_deals()
        assert self.pages.create_flight_page.is_element_present(getattr(self.pages.create_flight_page, 'deals_table'))

    @test_case()
    def verify_contents_of_deals(self):
        for element in ['deals_filters', 'deals_table', 'master_select_deals', 'select_first_deal']:
            assert self.pages.create_flight_page.is_element_present(getattr(self.pages.create_flight_page, element))
        for content in ['Deal Name', 'Deal ID', 'Exchange', 'Cost (CPM)', 'Dates']:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def search_for_invalid_data(self):
        self.deal_name = self.pages.create_flight_page.get_filtered_search('first_deal')
        self.pages.create_flight_page.filter_deals('abc!@#$%^&')
        time.sleep(5)
        self.pages.create_flight_page.page_should_contain('No matching records found')

    @test_case()
    def search_for_valid_data(self):
        self.pages.create_flight_page.filter_deals(self.pages.create_flight_page.search_text)
        time.sleep(5)
        assert self.pages.create_flight_page.search_text in self.pages.create_flight_page.get_filtered_search('first_deal')

    @test_case()
    def search_for_blank_data(self):
        self.pages.create_flight_page.filter_deals('')
        time.sleep(2)
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.first_deal)
        assert self.deal_name == self.pages.create_flight_page.get_filtered_search('first_deal')

    @test_case()
    def working_of_checkbox(self):
        self.pages.create_flight_page.click_select_first_deal()
        assert self.pages.create_flight_page.find_element(self.pages.create_flight_page.select_first_deal).is_selected()

    @test_case()
    def verify_content_of_private_inventory(self):
        self.pages.create_flight_page.expand_private_inventory()
        assert self.pages.create_flight_page.is_element_present(getattr(self.pages.create_flight_page, 'first_private_inventory'))
        for content in ['Inventory ', 'CPM']:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def working_of_checkbox_in_inventory(self):
        self.pages.create_flight_page.select_first_private_inventory()
        time.sleep(3)
        assert self.pages.create_flight_page.find_element(self.pages.create_flight_page.first_private_inventory).is_selected()
        self.pages.create_flight_page.select_first_private_inventory()
        time.sleep(3)
        assert not self.pages.create_flight_page.find_element(self.pages.create_flight_page.first_private_inventory).is_selected()

    @test_case()
    def verify_content_of_blacklist(self):
        self.pages.create_flight_page.expand_blacklist()
        self.pages.create_flight_page.page_should_contain(self.pages.create_flight_page.blacklist_message_text)
        assert self.pages.create_flight_page.is_element_present(self.pages.create_flight_page.edit_blacklist_link)

    @test_case()
    def verify_content_of_whitelist(self):
        self.pages.create_flight_page.expand_whitelist()
        self.pages.create_flight_page.page_should_contain(self.pages.create_flight_page.whitelist_message_text)
        assert self.pages.create_flight_page.is_element_present(self.pages.create_flight_page.edit_whitelist_link)

    @test_case()
    def working_of_tactic(self):
        tactics = ['Retargeting', 'Optimized', 'Default']
        for tactic in tactics:
            self.pages.create_flight_page.select_tactic(tactic)
            assert tactic == self.pages.create_flight_page.get_dropdown_selected_value(self.pages.create_flight_page.flight_tactic)

    @test_case()
    def inventory_section_on_flight_page(self):
        self.pages.create_flight_page.do_hover()
        contents = [
                    'Can I expect to see spend on all these exchanges?',
                    'Flights will only spend on exchanges that serve within the set geographic targeting.',
                    'These exchanges serve countries and regions across the globe.',
                    'For more information on the specific countries and regions each exchange is available for,'
                    ]
        for content in contents:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def working_of_link(self):
        if self.pages.create_flight_page.is_element_present(self.pages.create_flight_page.edit_flight_name):
            self.pages.create_flight_page.go_to_link('Campaign Flight Budget Setup')
            self.pages.fbs_page.wait_for_flights()
        self.pages.fbs_page.page_should_contain('Flight budget and schedule setup')

    @test_case()
    def verify_buttons_in_inventory_section(self):
        self.inventory = self.pages.create_flight_page.get_inventory('avail_inventory')
        self.pages.create_flight_page.select_available_inventory(self.inventory)
        self.pages.create_flight_page.move_selected_inventory()
        self.pages.create_flight_page.check_dropdown_options([self.inventory], self.pages.create_flight_page.applied_inventory)
        self.pages.create_flight_page.move_all_selected_inventory()
        self.inventory_list = self.pages.create_flight_page.get_inventory('avail_inventory', 10)
        self.pages.create_flight_page.check_dropdown_options(self.inventory_list, self.pages.create_flight_page.applied_inventory)
        self.pages.create_flight_page.select_applied_inventory(self.inventory)
        self.pages.create_flight_page.remove_selected_inventory()
        self.pages.create_flight_page.check_dropdown_options([self.inventory], self.pages.create_flight_page.avail_inventory)
        self.pages.create_flight_page.remove_all_selected_inventory()
        self.pages.create_flight_page.check_dropdown_options(self.inventory_list, self.pages.create_flight_page.avail_inventory)
        self.pages.create_flight_page.move_all_selected_inventory()

    @test_case()
    def working_of_buttons_in_inventory_section(self):
        self.go_to_create_flight_page()
        self.verify_buttons_in_inventory_section()
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.go_to_link(self.flight_name)
        self.pages.flight_show_page.wait_for_flight_basics()
        for inventory in self.inventory_list:
            self.pages.flight_show_page.page_should_contain(inventory)
        self.pages.flight_show_page.go_to_link('Edit')
        self.pages.create_flight_page.wait_for_flight_details()
        self.pages.create_flight_page.check_dropdown_options(self.inventory_list, self.pages.create_flight_page.applied_inventory)
        self.pages.create_flight_page.remove_all_selected_inventory()
        self.verify_buttons_in_inventory_section()

    @test_case()
    def create_campaign_with_channel_inventory(self, channel, media = None, counter=0):
        self.go_to_campaign_list_page()
        self.pages.new_campaign_pop_up.click_new_campaign_link()
        self.pages.new_campaign_pop_up.wait_till_visible(self.pages.new_campaign_pop_up.popup_create_campaign_button)
        try:
            self.pages.new_campaign_pop_up.type_advertiser(self.dx_constant.advertiser_name)
            self.pages.new_campaign_pop_up.select_campaign_currency('Euro (EUR)')
            self.pages.new_campaign_pop_up.select_campaign_channel(channel)
            if media == 'guaranteed':
                self.pages.new_campaign_pop_up.select_campaign_inventory('Guaranteed Media')
            self.pages.new_campaign_pop_up.submit()
        except Exception:
            counter += 1
            self.pages.new_campaign_pop_up.generate_and_accept_javascript_alert()
            self.pages.new_campaign_pop_up.close()
            if counter < 5:
                self.create_campaign_with_channel_inventory(channel, media, counter)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)

    @test_case()
    def fill_campaign_details_with_aoc(self, type = None):
        self.pages.create_campaign_page.expand_add_on_cost()
        self.pages.create_campaign_page.click_new_aoc()
        if type == 'custom':
            self.pages.create_campaign_page.select_aoc_name(self.pages.create_campaign_page.campaign_values['custom_value'])
            self.aoc_name = 'test-add-on-cost-' + self.pages.create_campaign_page.get_random_string()
            self.pages.create_campaign_page.enter_cutom_aoc_value(self.aoc_name)
            self.pages.create_campaign_page.enter_aoc_rate('19')
        else:
            self.pages.create_campaign_page.select_aoc_name(self.dx_constant.dxas_video)
        self.fill_campaigns_required_fields()
        self.pages.fbs_page.fill_description(self.dx_constant.test_flight_name + self.pages.fbs_page.get_random_string())
        self.pages.fbs_page.type_bid_normal(self.dx_constant.flight_bid)
        self.pages.fbs_page.wait_till_element_clickable(self.pages.fbs_page.save_continue_button)
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_for_flight_details()

    def verify_currency_and_aoc(self, campaign_type):
        self.create_campaign_with_channel_inventory(campaign_type)
        self.fill_campaign_details_with_aoc('custom')
        for content in [u'\u20AC', self.aoc_name, 'CPM (EUR)']:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def get_online_campaign_with_exchange_media(self):
        self.verify_currency_and_aoc('Online')

    @test_case()
    def get_mobile_campaign_with_exchange_media(self):
        self.verify_currency_and_aoc('Mobile')

    @test_case()
    def get_video_campaign_with_exchange_media(self):
        self.verify_currency_and_aoc('Video')

    @test_case()
    def verify_one_ad_per_page(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Mobile')
        self.fill_campaigns_required_fields()
        self.flight = self.dx_constant.test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(self.flight)
        self.pages.fbs_page.type_bid_normal(self.dx_constant.flight_bid)
        self.pages.fbs_page.click_on_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.page_should_contain('1 per page view')
        self.pages.campaign_show_page.go_to_link(self.flight)
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain('Limit One Impression Per Page View')

    @test_case()
    def verify_mopub_exchange(self):
        if self.pages.flight_show_page.is_element_present(self.pages.flight_show_page.edit_link):
            self.pages.flight_show_page.go_to_link('Edit')
            self.pages.flight_edit_page.wait_till_visible(self.pages.flight_edit_page.media_type)
        self.pages.flight_edit_page.select_media_types('Video')
        time.sleep(5)
        self.pages.flight_edit_page.select_available_inventory('MoPub')
        self.pages.flight_edit_page.move_selected_inventory()
        self.pages.flight_edit_page.click_save_exit()
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain('MoPub')
