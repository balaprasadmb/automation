import uuid
import random
import os
import time
from dx_test.dx_test import DXTest
from lib.dx_date import DXDate
from lib.gui_tests import test_case
from campaign_test_helpers.campaign_test_helper import CampaignTestHelper

class CampaignTest(DXTest):

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
    def go_to_create_campaign_page(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details()

    @test_case()
    def fill_create_campaign_fields(self, campaign_attributes):
        self.pages.create_campaign_page.fill_fields(campaign_attributes)

    @test_case()
    def datepicker_should_visible(self, date_type):
        self.go_to_create_campaign_page()
        if date_type == 'start':
            self.pages.create_campaign_page.click_start_date()
        elif date_type == 'end':
            self.pages.create_campaign_page.click_end_date()
        assert self.pages.create_campaign_page.find_element(self.pages.create_campaign_page.date_picker).is_displayed()

    def validate_blank_field_error_message(self, element_name):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.blank_msgs[element_name])

    @test_case()
    def validate_blank_field_error_message_for_campaign_name(self):
        self.go_to_create_campaign_page()
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.blank_msgs['campaign_name'])

    @test_case()
    def validate_special_chars_input_error_message(self, element):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.special_character_msgs[element])

    @test_case()
    def validate_special_chars_input_error_message_for_cpa(self):
        self.go_to_create_campaign_page()
        for field  in ['cpa', 'cpm', 'cogs', 'budget', 'insertion_order' 'tag_id']:
            self.pages.create_campaign_page.campaign_attributes[field] = self.dx_constant.special_char
            self.pages.create_campaign_page.campaign_attributes['activity_pixel'] = 1
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.special_character_msgs['cpa'])

    @test_case()
    def campaign_name_with_html_script_tag(self):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.special_character_msgs['campaign_name'])

    @test_case()
    def validate_string_input_error_message(self, element):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.string_msgs[element])

    @test_case()
    def validate_string_input_error_message_for_cpa(self):
        self.go_to_create_campaign_page()
        for field  in ['cpa', 'cpm', 'cogs', 'budget', 'tactics_budget', 'icaps' ]:
            self.pages.create_campaign_page.campaign_attributes[field] = self.dx_constant.strings
            self.pages.create_campaign_page.campaign_attributes['tactics'] = self.dx_constant.tactics
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.string_msgs['cpa'])

    @test_case()
    def validate_limit_error_message(self, element):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.range_msgs[element])

    @test_case()
    def validate_limit_error_message_for_cpa_field(self):
        self.go_to_create_campaign_page()
        for key, value in {'cpa': 'limit_ten_thousand', 'budget': 'limit_ninty_lacs','cogs':'limit_ten'}.iteritems():
            self.pages.create_campaign_page.campaign_attributes[key] = getattr(self.dx_constant, value)
        self.pages.create_campaign_page.campaign_attributes['objective'] = 'ctr'
        for field  in ['cpm', 'goal_ctr' ]:
            self.pages.create_campaign_page.campaign_attributes[ field ] = self.dx_constant.limit_hundread
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.range_msgs['cpa'])

    @test_case()
    def geo_target_section(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.select_geo_targeting_type(2)
        for element in ['geo_target_country_id', 'geo_target_area_type']:
            self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def select_specify_region_within(self):
        self.pages.create_campaign_page.select_geo_targeting_type(2)

    @test_case()
    def select_region_and_validate_available_regions_list(self, country):
        self.pages.create_campaign_page.select_geo_target_country(country)
        self.pages.create_campaign_page.check_dropdown_options(self.pages.create_campaign_page.regions[country], self.pages.create_campaign_page.avail_regions)

    @test_case()
    def geo_target_section_metrocodes(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.select_geo_targeting_type(2)
        for element in ['geo_target_country_id', 'geo_target_area_type']:
            self.pages.create_campaign_page.click_element(getattr(self.pages.create_campaign_page, element))
        self.pages.create_campaign_page.select_geo_target_country('United States')
        self.pages.create_campaign_page.select_area_type(1)

    @test_case()
    def metrocodes_shown_for_us(self):
        self.select_specify_region_within()
        self.pages.create_campaign_page.select_geo_target_country('United States')
        self.pages.create_campaign_page.select_area_type(1)
        self.pages.create_campaign_page.wait_till_visible(['id', 'campaign_dmas_input'])
        for metro_country in ['500 Portland-Auburn ME', '506 Boston MA-Manchester NH', '519 Charleston SC']:
            self.pages.create_campaign_page.select_avail_countries_metro(metro_country)

    @test_case()
    def metrocodes_not_shown_for_others(self, country):
        self.select_specify_region_within()
        self.pages.create_campaign_page.select_geo_target_country(country)
        self.pages.create_campaign_page.assert_options()

    def negative_value_validation(self, element):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.negative_value_message[element])

    @test_case()
    def negative_value_cpm(self):
        self.negative_value_validation('cpm')

    @test_case()
    def negative_value_third_party_tag_id(self):
        self.go_to_create_campaign_page()
        for field in ['cpm', 'tag_id', 'filters_value']:
            self.pages.create_campaign_page.campaign_attributes[field] = self.dx_constant.negative_value
        self.pages.create_campaign_page.campaign_attributes['objective'] = 'performance'
        self.pages.create_campaign_page.campaign_attributes['activity_pixel'] = 1
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.negative_value_validation('third_party_tag_id')

    @test_case()
    def negative_value_filter_values(self):
        self.negative_value_validation('activity_value')

    @test_case()
    def negative_value_ctr_goal(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.campaign_attributes['goal_ctr'] =  self.dx_constant.negative_value
        self.pages.create_campaign_page.campaign_attributes['objective'] = 'ctr'
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.negative_value_message['ctr_goal'])

    @test_case()
    def alphanumeric_value_third_party_tag_id(self):
        self.go_to_create_campaign_page()
        for field in ['tag_id','filters_value']:
            self.pages.create_campaign_page.campaign_attributes[field] = self.dx_constant.alphanumeric_value
        self.pages.create_campaign_page.campaign_attributes['objective'] = 'performance'
        self.pages.create_campaign_page.campaign_attributes['activity_pixel'] = 1
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.negative_value_validation('third_party_tag_id')

    @test_case()
    def alphanumeric_value_filter_values(self):
        self.negative_value_validation('activity_value')

    @test_case()
    def language_targeting_page_content(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.expand_lang_targeting()
        for element in ['move_selected_lang', 'remove_selected_lang', 'move_all_selected_lang', 'remove_all_selected_lang']:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def select_button_functionality(self):
        self.pages.create_campaign_page.select_lang_targeting("Dutch")
        self.pages.create_campaign_page.click_move_all_selected_lang()
        self.pages.create_campaign_page.click_remove_all_selected_lang()

    @test_case()
    def complete_flow_with_distribution(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_distribution(self.pages.create_campaign_page.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def go_to_campaign_show_page(self):
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        self.pages.fbs_page.go_to_link(self.campaign_attributes['campaign_name'])
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)

    @test_case()
    def go_to_campaign_edit(self):
        if self.pages.campaign_show_page.is_element_present(self.pages.campaign_show_page.reports_link):
            self.pages.campaign_show_page.go_to_link('Edit')
            self.pages.campaign_edit_page.wait_till_visible(self.pages.campaign_edit_page.create_campaign_button, 35)

    @test_case()
    def assert_campaign_name(self):
        if len(self.campaign_attributes['campaign_name']) > 77:
            self.pages.create_campaign_page.page_should_contain(self.campaign_attributes['campaign_name'][0:77])
        else:
            self.pages.create_campaign_page.page_should_contain(self.campaign_attributes['campaign_name'])

    @test_case()
    def assert_campaign_attribute(self, element):
        self.pages.create_campaign_page.page_should_contain(self.campaign_attributes[element])

    @test_case()
    def assert_insertion_order(self):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.campaign_attributes['order'])

    @test_case()
    def assert_objective(self):
        objective_dict = {
            'performance' : 'Maximize Performance and Distribution',
            'ctr' : 'Maximize CTR',
            'distribution': 'Maximize Distribution',
            'views': 'Maximize Completed Ad Views'
        }
        self.pages.create_campaign_page.page_should_contain(objective_dict[self.campaign_attributes['objective']])

    @test_case()
    def assert_tactics(self):
        for content in ['Default', self.campaign_attributes['tactics_value']]:
            self.pages.create_campaign_page.page_should_contain(content)

    @test_case()
    def assert_tactics_budget(self):
        self.pages.create_campaign_page.page_should_contain(self.campaign_attributes['tactics_budget'])

    @test_case()
    def assert_tactics_impression_cap(self):
        self.pages.create_campaign_page.page_should_contain(self.campaign_attributes['value'])

    @test_case()
    def assert_external_id_source(self):
        self.pages.create_campaign_page.page_should_contain(self.campaign_attributes['source'])

    @test_case()
    def assert_external_id_value(self):
        self.pages.create_campaign_page.page_should_contain(self.campaign_attributes['source_value'])

    @test_case()
    def assert_brand_safety(self):
        try:
            brand_safety_dict = {
            '1': 'Level One',
            '2': 'Level Two',
            '3': 'Level Three',
            '4': 'Level Four'
            }
            self.pages.create_campaign_page.page_should_contain(brand_safety_dict[self.campaign_attributes['brand_safety_level']])
        except KeyError:
            self.pages.create_campaign_page.page_should_contain('Level Two')

    @test_case()
    def assert_aoc_name(self):
        time.sleep(5)
        self.pages.create_campaign_page.page_should_contain(self.campaign_attributes['aoc_custom'])

    @test_case()
    def assert_aoc_cpm_value(self):
        self.pages.create_campaign_page.page_should_contain(self.campaign_attributes['value'])

    @test_case()
    def complete_flow_with_ctr(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_ctr(self.pages.create_campaign_page.campaign_values)
        self.pages.create_campaign_page = CampaignTestHelper().set_campaign_attributes(self.pages.create_campaign_page, self.campaign_attributes)
        self.pages.create_campaign_page.campaign_attributes['goal_ctr'] = self.pages.create_campaign_page.campaign_values['ctr_goal']
        self.pages.create_campaign_page.campaign_attributes['order'] = self.pages.create_campaign_page.get_random_characters()
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)

    def complete_flow_helper(self):
        self.pages.create_campaign_page = CampaignTestHelper().set_campaign_attributes(self.pages.create_campaign_page, self.campaign_attributes)
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)

    @test_case()
    def complete_flow_with_future_dates(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_future_date(self.pages.create_campaign_page.campaign_values)
        self.pages.create_campaign_page.campaign_attributes['order'] = self.pages.create_campaign_page.get_random_string()
        self.campaign_attributes['campaign_name'] = self.dx_constant.test_campaign_name + self.dx_constant.special_char
        self.complete_flow_helper()

    @test_case()
    def complete_flow_with_retargeting_xls(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_retargeting(self.pages.create_campaign_page.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def complete_flow_with_optimized_xlsx(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_optimized(self.pages.create_campaign_page.campaign_values)
        self.campaign_attributes['campaign_name'] = self.pages.create_campaign_page.get_random_string(255)
        self.campaign_attributes['order'] = self.pages.create_campaign_page.get_random_string(255)
        self.complete_flow_helper()

    @test_case()
    def complete_flow_with_channel_xlsx(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_channel(self.pages.create_campaign_page.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def date_ahead(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.enter_start_date(DXDate().date_after_two_days())
        self.pages.create_campaign_page.enter_end_date(DXDate().todays_date())
        self.pages.create_campaign_page.click_element(self.pages.create_campaign_page.campaign_name)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.submit()
        self.pages.create_campaign_page.wait_till_visible(self.pages.create_campaign_page.create_campaign_button)

    def date_helper(self):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.date_ahead_msgs)

    @test_case()
    def start_date_exceeds(self):
        self.date_helper()

    @test_case()
    def end_date_before(self):
        self.date_helper()

    @test_case()
    def create_campaign_with_completed_ad_views(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Mobile')
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_ad_views(self.pages.create_campaign_page.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def assert_aoc_number_name(self):
        self.pages.create_campaign_page.page_should_contain(self.campaign_attributes['aoc_custom'])

    @test_case()
    def assert_aoc_rate(self):
        self.pages.create_campaign_page.page_should_contain(self.campaign_attributes['aoc_rate'])

    @test_case()
    def verify_max_performance_distribution(self):
        self.go_to_create_campaign_page()
        contents = ['model', 'activity', 'pixel', 'tag_server', 'filter', 'tag_id']
        for element in contents:
            self.pages.create_campaign_page.click_element(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def verify_max_ctr(self):
        self.pages.create_campaign_page.click_campaign_objective_ctr()
        self.pages.create_campaign_page.click_element(self.pages.create_campaign_page.campaign_goal_ctr)

    @test_case()
    def verify_campaign_objectives(self, new_objective= None):
        objective_elements = ['campaign_objective_performance', 'campaign_objective_ctr', 'campaign_objective_distribution']
        if new_objective:
            objective_elements.append(new_objective)
        for element in objective_elements:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def verify_campaign_objective_with_channel(self, channel):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details(channel)
        self.verify_campaign_objectives('campaign_objective_ad_views')

    @test_case()
    def verify_campaign_objective_under_mobile(self):
        self.verify_campaign_objective_with_channel('Mobile')

    @test_case()
    def verify_campaign_objective_under_video(self):
        self.verify_campaign_objective_with_channel('Video')

    @test_case()
    def verify_add_on_cost_contents(self):
        self.pages.create_campaign_page.expand_add_on_cost()
        contents = ['View Change History', 'Name', 'Rate', 'Fee Type', 'Billable', 'DataXu Marketplace']
        for content in contents:
            self.pages.create_campaign_page.page_should_contain(content)
        assert self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.new_add_on_cost)
        self.pages.create_campaign_page.click_new_aoc()
        for element in ['add_on_cost_name', 'add_on_cost_rate', 'add_on_cost_billable', 'remove_add_on_cost']:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def verify_budget_spending(self):
        for element in ['cost_model', 'cpa_goal', 'order_budget', 'campaign_cpm', 'campaign_cogs', 'campaign_margin']:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def verify_cost_model(self):
        self.pages.create_campaign_page.check_dropdown_options(['CPA', 'CPM'], self.pages.create_campaign_page.cost_model)

    @test_case()
    def verify_tactics(self):
        self.pages.create_campaign_page.page_should_contain('Default')

    @test_case()
    def verify_tactics_contents(self):
        contents = ['Tactic name', 'Budget', 'Impression Cap']
        for content in contents:
            self.pages.create_campaign_page.page_should_contain(content)
        assert self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.new_tactics)
        self.pages.create_campaign_page.click_add_new_tactic()
        for element in ['tactic_name', 'tactics_budget', 'tactics_impression', 'remove_tactics']:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def verify_tactics_name_contents(self):
        tactics_list = ['Retargeting', 'Optimized', 'GeoTargeting', 'Channel', 'Custom...']
        self.pages.create_campaign_page.check_dropdown_options(tactics_list, self.pages.create_campaign_page.tactic_name_default)

    @test_case()
    def verify_external_ids_contents(self):
        self.pages.create_campaign_page.expand_external_ids()
        assert self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.new_external_ids)
        self.pages.create_campaign_page.click_new_external_id()
        for element in ['external_id_source', 'external_id_value', 'remove_external_id']:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))
        external_ids_list = [
                    'RMX', 'DFA', 'Atlas', 'BlueKai', 'WURFL', 'MediaMind',
                    'Facebook', 'Facebook Campaign', 'Facebook Page Post Ad'
                    ]
        self.pages.create_campaign_page.check_dropdown_options(external_ids_list, self.pages.create_campaign_page.external_id_source)

    @test_case()
    def verify_geographic_targeting_section(self):
        for element in ['geo_target_type', 'country_available_search', 'country_available', 'country_selected']:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))
        self.pages.create_campaign_page.click_remove_all_selected_countries()
        countries = [
                     'United States', 'Brazil', 'Canada', 'France', 'Germany',
                     'Great Britain', 'Ireland', 'Italy', 'Poland', 'Spain'
                    ]
        self.pages.create_campaign_page.check_dropdown_options(countries, self.pages.create_campaign_page.country_available)

    @test_case()
    def verify_buttons_in_geographic_targeting(self):
        self.pages.create_campaign_page.select_avail_countries('Brazil')
        self.pages.create_campaign_page.click_move_selected_country()
        self.pages.create_campaign_page.assert_geographic_selected_country(self.pages.create_campaign_page.country_selected, 'Brazil')
        self.pages.create_campaign_page.select_applied_countries('Brazil')
        self.pages.create_campaign_page.click_remove_selected_country()
        self.pages.create_campaign_page.assert_geographic_selected_country(self.pages.create_campaign_page.country_available, 'Brazil')
        self.pages.create_campaign_page.click_remove_selected_country()
        countries = [
                     'United States', 'Brazil', 'Canada', 'France', 'Germany',
                      'Great Britain', 'Ireland', 'Italy', 'Poland', 'Spain'
                    ]
        self.pages.create_campaign_page.click_move_all_selected_countries()
        self.pages.create_campaign_page.assert_geographic_selected_country(self.pages.create_campaign_page.country_selected, None, countries)
        self.pages.create_campaign_page.click_remove_all_selected_countries()
        self.pages.create_campaign_page.assert_geographic_selected_country(self.pages.create_campaign_page.country_available, None, countries)

    @test_case()
    def verify_search_in_geographic_targeting(self):
        self.pages.create_campaign_page.search_avail_countries('India')
        self.pages.create_campaign_page.assert_geographic_selected_country(self.pages.create_campaign_page.country_available, 'India')

    @test_case()
    def verify_postal_codes_in_geo_target(self):
        self.select_specify_region_within()
        self.pages.create_campaign_page.select_area_type(2)
        contents = [
                    'geo_target_type', 'geo_target_country_id', 'geo_target_area_type',
                     'postal_code_group_name', 'postal_code_group_submit'
                     ]
        for element in contents:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def verify_geofenced_in_geo_target(self):
        self.pages.create_campaign_page.select_geo_targeting_type(0)
        elements = [
                    'geo_target_type', 'geofenced_search', 'geofenced_available',
                    'geofenced_applied', 'geofenced_file', 'geofenced_name', 'geofenced_submit'
                    ]
        for element in elements:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def verify_blacklist_section(self):
        self.pages.create_campaign_page.expand_blacklist()
        self.pages.create_campaign_page.page_should_contain('Blacklists have been moved to the end of the campaign workflow.')

    @test_case()
    def verify_whitelist_section(self):
        self.pages.create_campaign_page.expand_whitelist()
        self.pages.create_campaign_page.page_should_contain('Whitelists have been moved to the end of the campaign workflow.')

    @test_case()
    def verify_brandsafety_section(self):
        self.pages.create_campaign_page.expand_brand_safety()
        self.pages.create_campaign_page.page_should_contain('Defaults to Level 2')
        self.pages.create_campaign_page.expand_brand_safety()
        for content in range(1, 18):
            self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.contents[content])
        elements = [
                    'brand_safety_level_one', 'brand_safety_level_two',
                    'brand_safety_level_three', 'brand_safety_level_four'
                    ]
        for element in elements:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def fill_fields_with_limit_data(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.campaign_attributes['objective'] = 'performance'
        self.pages.create_campaign_page.campaign_attributes['activity_pixel'] = 1
        self.pages.create_campaign_page.campaign_attributes['tag_id'] = self.dx_constant.four_len_value
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.wait_till_visible(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.limit_msgs['activity'])

    @test_case()
    def blank_ctr_goal(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.campaign_attributes['objective'] = 'ctr'
        self.pages.create_campaign_page.campaign_attributes['goal_ctr'] = ''
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.wait_till_visible(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.blank_msgs['ctr_goal'])

    @test_case()
    def special_chars_ctr_goal(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.campaign_attributes['campaign_name'] =  self.dx_constant.html_tag
        self.pages.create_campaign_page.campaign_attributes['goal_ctr'] =  self.dx_constant.special_char
        self.pages.create_campaign_page.campaign_attributes['objective'] = 'ctr'
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.special_character_msgs['ctr_goal'])

    @test_case()
    def fill_activity_with_max_limit(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_max_limit(self.pages.create_campaign_page.campaign_values)
        self.pages.create_campaign_page = CampaignTestHelper().set_campaign_attributes(self.pages.create_campaign_page, self.campaign_attributes)
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.go_to_campaign_show_page()
        self.go_to_campaign_edit()
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.campaign_attributes['aoc_custom'])

    @test_case()
    def aoc_name_exceeding_limit(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.campaign_attributes['campaign_name'] = self.pages.create_campaign_page.get_random_string(260)
        self.pages.create_campaign_page.campaign_attributes['order'] = self.pages.create_campaign_page.get_random_digits(256)
        self.pages.create_campaign_page.campaign_attributes['objective'] = 'distribution'
        self.pages.create_campaign_page.campaign_attributes['aoc_name'] = 'Custom...'
        activity = self.dx_constant.activity_name + self.pages.create_campaign_page.get_random_digits(248)
        self.pages.create_campaign_page.campaign_attributes['aoc_custom'] = activity
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.limit_msgs['aoc'])

    @test_case()
    def campaign_name_exceeding_limit(self):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.limit_msgs['campaign_name'])

    @test_case()
    def insertion_order_exceeding_limit(self):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.limit_msgs['insertion_order'])

    @test_case()
    def fill_cpm_with_max_limit(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().fill_cpm_max_limit(self.pages.create_campaign_page.campaign_values)
        self.pages.create_campaign_page = CampaignTestHelper().set_campaign_attributes(self.pages.create_campaign_page, self.campaign_attributes)
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.go_to_campaign_show_page()
        self.go_to_campaign_edit()
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.campaign_attributes['aoc_custom'])

    @test_case()
    def fill_cpm_alphanumeric_value(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.campaign_attributes['objective'] = 'distribution'
        self.pages.create_campaign_page.campaign_attributes['aoc_rate'] = self.dx_constant.alphanumeric_value
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.alphanumeric_value_msgs['aoc_rate'])

    @test_case()
    def fill_tactics_name_with_limit(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.campaign_attributes['objective'] = 'distribution'
        self.pages.create_campaign_page.campaign_attributes['tactics'] = 'Custom...'
        tactics = self.dx_constant.tactics_name + self.pages.create_campaign_page.get_random_digits(249)
        self.pages.create_campaign_page.campaign_attributes['tactics_value'] = tactics
        self.pages.create_campaign_page.campaign_attributes['order'] = ''
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.limit_msgs['tactics'])

    @test_case()
    def fill_tactics_name_with_limit_data(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().fill_fields_with_tactics(self.pages.create_campaign_page.campaign_values)
        self.pages.create_campaign_page = CampaignTestHelper().set_campaign_attributes(self.pages.create_campaign_page, self.campaign_attributes)
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.go_to_campaign_show_page()
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.campaign_attributes['tactics_value'])

    @test_case()
    def fill_fields_with_facebook_campaign(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().fill_fields_with_facebook_campaign(self.pages.create_campaign_page.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def fill_fields_with_brand_safety_one(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().fill_fields_with_brand_safety_one(self.pages.create_campaign_page.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def verify_bulk_assign_pixels(self):
        self.go_to_create_campaign_page()
        assert self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.bulk_assign_pixel)

    @test_case()
    def verify_bulk_assign_pixels_contents(self):
        self.pages.create_campaign_page.click_bulk_assign_click()
        self.pages.create_campaign_page.wait_for_bulk_assign_pixel()
        self.pages.create_campaign_page.page_should_contain('Bulk Assign Pixels')
        contents = ['bulk_available_search', 'bulk_available_activities', 'pixel_type_value', 'pixel_type_filter', 'add_pixel']
        for element in contents:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))

    @test_case()
    def verify_bulk_pixel_type(self):
        for option in ['Conversion Pixel', 'Learning Pixel']:
            self.pages.create_campaign_page.select_bulk_pixel_type(option)

    @test_case()
    def verify_no_new_textbox_appear(self):
        self.pages.create_campaign_page.select_bulk_pixel_type('Learning Pixel')
        assert not self.pages.create_campaign_page.find_element(self.pages.create_campaign_page.pixel_type_value).is_selected()

    @test_case()
    def verify_new_textbox_appear(self):
        self.pages.create_campaign_page.select_bulk_pixel_type('Conversion Pixel')
        assert self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.pixel_type_learning)

    @test_case()
    def verify_search_activities(self):
        self.pages.create_campaign_page.search_available_bulk_pixel('activity')
        activity = str(self.pages.create_campaign_page.get_first_activity())
        assert activity.find('activity') != -1, 'Searching activity not present'

    @test_case()
    def verify_conversion_value_char_data(self):
        self.pages.create_campaign_page.search_available_bulk_pixel('')
        activity=self.pages.create_campaign_page.get_first_activity()
        self.pages.create_campaign_page.select_one_available_activity(activity)
        self.pages.create_campaign_page.select_bulk_pixel_type('Conversion Pixel')
        self.pages.create_campaign_page.enter_bulk_conversion_pixel_value('abcde')
        self.pages.create_campaign_page.click_add_pixel()
        element = self.pages.create_campaign_page.find_element(self.pages.create_campaign_page.first_value_field)
        assert str(element.get_attribute('placeholder')) == '0.0', 'Conversion value error'

    @test_case()
    def conversion_helper(self, pixel):
        self.pages.create_campaign_page.click_bulk_assign_click()
        self.pages.create_campaign_page.wait_for_bulk_assign_pixel()
        self.pages.create_campaign_page.search_available_bulk_pixel('test-activity')
        time.sleep(5)
        self.activity = self.pages.create_campaign_page.get_first_activity()
        self.pages.create_campaign_page.search_available_bulk_pixel('')
        self.pages.create_campaign_page.select_one_available_activity(self.activity)
        self.pages.create_campaign_page.select_bulk_pixel_type(pixel)

    @test_case()
    def verify_conversion_value_special_chars(self):
        self.pages.create_campaign_page.click_remove_activity()
        self.conversion_helper('Conversion Pixel')
        self.pages.create_campaign_page.enter_bulk_conversion_pixel_value('!@#$%^&')
        self.pages.create_campaign_page.click_add_pixel()
        element = self.pages.create_campaign_page.find_element(self.pages.create_campaign_page.second_value_field)
        assert str(element.get_attribute('placeholder')) == '0.0', 'Conversion value error'
        self.pages.create_campaign_page.page_should_contain(self.activity)

    @test_case()
    def popup_should_close(self):
        self.pages.create_campaign_page.click_bulk_assign_click()
        self.pages.create_campaign_page.wait_for_bulk_assign_pixel()
        self.pages.create_campaign_page.close_popup()

    @test_case()
    def assign_learning_pixel_type(self, pixel_type = 'Learning Pixel'):
        if self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.campaign_name):
            self.conversion_helper(pixel_type)
            if pixel_type == 'Conversion Pixel':
                self.pages.create_campaign_page.enter_bulk_conversion_pixel_value('19')
            self.pages.create_campaign_page.click_add_pixel()
            self.campaign_attributes = CampaignTestHelper().get_campaign_with_objective_performance(self.pages.create_campaign_page.campaign_values)
            self.campaign_attributes['activity_pixel'] = None
            self.complete_flow_helper()
        self.go_to_campaign_show_page()
        self.go_to_campaign_edit()
        self.pages.create_campaign_page.page_should_contain(self.activity)
        assert str(self.pages.create_campaign_page.get_first_pixel_type()) == pixel_type, '%s not present'%(pixel_type)

    @test_case()
    def assign_conversion_pixel_type(self):
        self.assign_learning_pixel_type('Conversion Pixel')

    @test_case()
    def external_id_value_blank(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_blank_external_value(self.pages.create_campaign_page.campaign_values)
        self.complete_flow_helper()
        self.go_to_campaign_show_page()
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.campaign_attributes['source'])

    @test_case()
    def edit_external_id_value(self):
        self.go_to_campaign_edit()
        self.pages.campaign_edit_page.select_external_id_source('DFA')
        self.pages.campaign_edit_page.enter_external_id_value('19')
        self.pages.campaign_edit_page.submit()
        self.pages.campaign_edit_page.page_should_contain('DFA')
        self.pages.campaign_edit_page.page_should_contain('19')

    def split_messages(self, message):
        msg = (str(message)).split(',')
        return msg

    @test_case()
    def geofenced_region_valid_file(self):
        self.pages.create_campaign_page.select_geo_targeting_type(0)
        self.pages.create_campaign_page.upload_geofenced_file(os.path.dirname(__file__)+ '/../../../data/geohash_files/valid_geohash_with_headers.csv')
        geofence_name = self.dx_constant.geofenced_group_name + str(uuid.uuid4()) + '193'
        for i in range(1,42):
            geofence_name += '13579'
        self.pages.create_campaign_page.enter_geofenced_group_name(geofence_name)
        self.pages.create_campaign_page.click_geofenced_submit()
        self.pages.create_campaign_page.wait_till_enabled(self.pages.create_campaign_page.geofenced_submit)
        time.sleep(3)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.geofenced_msgs['valid'])

    @test_case()
    def geofenced_invalid_name(self):
        geofence_name = self.dx_constant.geofenced_group_name + str(uuid.uuid4())
        for i in range(1,43):
            geofence_name += '13579'
        self.pages.create_campaign_page.upload_geofenced_file(os.path.dirname(__file__)+ '/../../../data/geohash_files/valid_geohash_with_headers.csv')
        self.pages.create_campaign_page.enter_geofenced_group_name(geofence_name)
        self.pages.create_campaign_page.click_geofenced_submit()
        self.pages.create_campaign_page.wait_till_enabled(self.pages.create_campaign_page.geofenced_submit)
        time.sleep(3)
        messages = self.split_messages(self.pages.create_campaign_page.geofenced_msgs['invalid_name'])
        for message in messages:
            self.pages.create_campaign_page.page_should_contain(message)

    @test_case()
    def geofenced_region_invalid_file(self):
        self.pages.create_campaign_page.upload_geofenced_file(os.path.dirname(__file__)+ '/../../../data/geohash_files/invalid_geohashes.xls')
        self.pages.create_campaign_page.click_geofenced_submit()
        self.pages.create_campaign_page.wait_till_enabled(self.pages.create_campaign_page.geofenced_submit)
        time.sleep(3)
        messages = self.split_messages(self.pages.create_campaign_page.geofenced_msgs['invalid_csv'])
        for message in messages:
            self.pages.create_campaign_page.page_should_contain(message)

    @test_case()
    def geofenced_region_alphanumeric_name(self):
        self.pages.create_campaign_page.upload_geofenced_file(os.path.dirname(__file__)+ '/../../../data/geohash_files/valid_geohash_with_headers.csv')
        geofence_name = self.dx_constant.geofenced_group_name + str(uuid.uuid4())
        self.pages.create_campaign_page.enter_geofenced_group_name(geofence_name)
        self.pages.create_campaign_page.click_geofenced_submit()
        self.pages.create_campaign_page.wait_till_enabled(self.pages.create_campaign_page.geofenced_submit)
        time.sleep(3)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.geofenced_msgs['valid'])

    @test_case()
    def campaign_with_brand_safety_three(self):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_brand_safety_three(self.pages.create_campaign_page.campaign_values)
        self.complete_flow_helper()
        self.go_to_campaign_show_page()
        self.assert_brand_safety()

    @test_case()
    def verify_blank_csv_present(self):
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.campaign_success_msg)
        time.sleep(10)
        self.pages.create_campaign_page.go_to_link(self.pages.create_campaign_page.campaign_attributes['campaign_name'])

    @test_case()
    def fill_fbs_details(self):
        self.pages.fbs_page.wait_for_flights()
        flight_name = self.dx_constant.test_flight_name + str(uuid.uuid4())
        self.pages.fbs_page.fill_description(flight_name)
        self.pages.fbs_page.type_bid(self.dx_constant.flight_bid)
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_for_flight_details()
        self.pages.create_flight_page.expand_lang_targeting()
        time.sleep(5)
        assert self.pages.create_flight_page.find_element(self.pages.create_flight_page.inherit_lang_targeting).is_selected()
        return flight_name

    @test_case()
    def lang_target_base_settings(self ,base_type):
        self.go_to_create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_lang_targeting(self.pages.create_campaign_page.campaign_values, base_type)
        self.pages.create_campaign_page = CampaignTestHelper().set_campaign_attributes(self.pages.create_campaign_page, self.campaign_attributes)
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        flight = self.fill_fbs_details()
        self.pages.create_flight_page.page_should_contain('English')

    @test_case()
    def edit_lang_target_base_settings(self):
        self.go_to_create_campaign_page()
        base_type = 1
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_lang_targeting(self.pages.create_campaign_page.campaign_values, base_type)
        self.pages.create_campaign_page = CampaignTestHelper().set_campaign_attributes(self.pages.create_campaign_page, self.campaign_attributes)
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        flight = self.fill_fbs_details()
        self.pages.create_flight_page.page_should_contain('English')
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_for_loading()
        self.go_to_campaign_edit()
        self.pages.campaign_edit_page.select_lang_targeting_selected('English')
        self.pages.campaign_edit_page.click_remove_selected_lang()
        self.pages.campaign_edit_page.select_lang_targeting('Spanish')
        self.pages.campaign_edit_page.click_move_selected_lang()
        self.pages.campaign_edit_page.submit()
        self.pages.create_flight_page.go_to_link(flight)
        self.pages.create_flight_page.go_to_link('Edit')
        self.pages.create_flight_page.wait_for_flight_details()
        for content in ['Spanish']:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def verify_applied_country(self):
        self.go_to_create_campaign_page()
        self.pages.create_campaign_page.wait_for_campaign_details()
        countries = ['Brazil', 'Canada', 'France', 'Germany', 'Great Britain',
                     'Ireland', 'Italy', 'Poland', 'Spain']
        for country in countries:
            self.pages.create_campaign_page.select_avail_countries(country)
        self.pages.create_campaign_page.click_move_selected_country()
        self.campaign_attributes = CampaignTestHelper().get_campaign_without_geo_target(self.pages.create_campaign_page.campaign_values)
        self.pages.create_campaign_page = CampaignTestHelper().set_campaign_attributes(self.pages.create_campaign_page, self.campaign_attributes)
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        self.pages.create_campaign_page.go_to_link(self.pages.create_campaign_page.campaign_attributes['campaign_name'])
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.go_to_campaign_edit()

    @test_case()
    def verify_applied_country_on_edit_page(self, country):
        self.pages.campaign_edit_page.assert_geographic_selected_country(self.pages.campaign_edit_page.country_selected, country)
