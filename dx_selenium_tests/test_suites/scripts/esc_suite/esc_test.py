from selenium.webdriver.common.keys import Keys
from dx_test.dx_test import DXTest
from selenium.webdriver.common.by import By
from lib.gui_tests import test_case
from lib.dx_date import DXDate
from dx_search_file_path import SearchFilePath
from common_helpers.common_helpers import CommonHelper
import time
import os
import csv

class EscTest(DXTest):

    @test_case()
    def login_as_admin(self):
        self.dx_date = DXDate()
        self.common_helper = CommonHelper()
        self.setup()

    @test_case()
    def go_to_admin_page(self):
        self.pages.admin_page.open()
        self.pages.admin_page.wait_till_visible(self.pages.admin_page.system_message_table)

    @test_case()
    def user_email_validation_with_standard_domain(self):
        self.pages.admin_page.click_on_users_link()
        self.pages.user_list_page.wait_till_visible(self.pages.user_list_page.list_pagination_setup)
        self.pages.user_list_page.click_on_new_user_button()
        self.pages.new_user_page.wait_till_visible(self.pages.new_user_page.add_user_role_button)
        self.pages.new_user_page.enter_user_email_id(self.pages.new_user_page.get_random_string(5)+'@gmail.com')
        self.pages.new_user_page.select_organization(self.dx_constant.agency_group_name)
        self.pages.new_user_page.click_on_add_user_role_button()
        self.pages.new_user_page.select_organization_to_add_role(self.dx_constant.agency_group_name)
        self.pages.new_user_page.select_user_role('Campaign Manager')
        self.pages.new_user_page.click_on_submit_button()
        self.pages.user_show_page.wait_till_visible(self.pages.user_show_page.edit_link)
        self.pages.user_show_page.page_should_contain(self.pages.user_show_page.user_creation_success_message)

    @test_case()
    def user_email_validation_with_custom_domain(self):
        self.pages.user_show_page.click_on_edit_link()
        self.pages.user_edit_page.wait_till_visible(self.pages.user_edit_page.add_user_role_button)
        self.pages.user_edit_page.enter_user_email_id(self.pages.user_edit_page.get_random_string(5)+'@xyz.pqr')
        self.pages.user_edit_page.click_on_submit_button()
        self.pages.user_show_page.wait_till_visible(self.pages.user_show_page.edit_link)
        self.pages.user_show_page.page_should_contain(self.pages.user_show_page.user_update_message)

    @test_case()
    def verify_live_nation_canada_advertiser_update_successfully(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_advertisers_link()
        self.pages.advertiser_list_page.wait_till_visible(self.pages.advertiser_list_page.advertiser_list)
        self.pages.advertiser_list_page.search_advertiser('Live Nation Canada')
        self.pages.advertiser_list_page.click_first_edit_icon()
        self.pages.advertiser_edit_page.wait_till_element_clickable(self.pages.advertiser_edit_page.save_advertiser_button, 40)
        self.pages.advertiser_edit_page.click_on_save_advertiser_button()
        self.pages.advertiser_details_page.wait_till_visible(self.pages.advertiser_details_page.edit_details_button)
        self.pages.advertiser_details_page.page_should_contain(self.pages.advertiser_details_page.advertiser_update_success_message.format('Live Nation Canada'))

    @test_case()
    def set_agency_group_fields_and_save(self):
        self.agency_group_name = 'Esc-agency-group-' + self.pages.new_agency_group_page.get_random_string(5)
        self.pages.new_agency_group_page.type_organization_name(self.agency_group_name)
        self.pages.new_agency_group_page.type_email("smoke_test@dataxu.com")
        self.pages.new_agency_group_page.type_contact_name("DataXu")
        self.pages.new_agency_group_page.check_select_all_currencies()
        self.pages.new_agency_group_page.upload_rate_card(os.getcwd() + '/data/rate_cards/rate_card_USD.xls')
        for media in self.dx_constant.media_type:
            self.pages.new_agency_group_page.click_media_type_checkbox(media)
        self.pages.new_agency_group_page.select_all_inventory()
        if self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.dx_technical_exchange):
            self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.dx_technical_exchange).click()
        for insight in self.pages.new_agency_group_page.insight_list:
            self.pages.new_agency_group_page.select_insights(insight)
        self.pages.new_agency_group_page.click_targeting_checkbox()
        self.pages.new_agency_group_page.click_cost_model_type('CPA')
        self.pages.new_agency_group_page.click_create_agency_group_button()
        self.pages.agency_group_details_page.wait_till_visible(self.pages.agency_group_details_page.edit_details)

    @test_case()
    def set_agency_fields_and_save(self):
        self.agency_name = 'Esc-agency-' + self.pages.new_agency_group_page.get_random_string(5)
        self.pages.new_agency_page.type_organization_name(self.agency_name)
        self.pages.new_agency_page.click_create_agency_button()
        self.pages.agency_details_page.wait_till_visible(self.pages.agency_details_page.edit_details_button)

    @test_case()
    def set_advertiser_fields_and_save(self):
        self.advertiser_name = 'Esc-advertiser-' + self.pages.new_advertiser_page.get_random_string(5)
        self.pages.new_advertiser_page.type_organization_name(self.advertiser_name)
        self.pages.new_advertiser_page.type_advertiser_domain('www.esc.com')
        self.pages.new_advertiser_page.click_create_advetiser_button()
        self.pages.advertiser_list_page.wait_till_visible(self.pages.advertiser_list_page.advertiser_list)

    @test_case()
    def add_google_adx_seat_from_organization_edit_page(self, page_object):
        page_object.click_on_google_adx_seat_edit_icon()
        page_object.wait_till_visible(page_object.configure_seats_pop_up['override_checkbox'].values())
        page_object.click_seats_override_radio_button()
        page_object.type_seat_name(page_object.get_random_string(5))
        page_object.type_seat_id(page_object.get_random_digits(8))
        page_object.click_seats_ok_button()

    @test_case()
    def verify_google_seat_from_organization_show_page(self, page_object):
        self.google_adx_seat = page_object.get_attribute_value_with_strip(getattr(page_object, 'google_adx_seat'))
        self.google_content_network_seat = page_object.get_attribute_value_with_strip(getattr(page_object, 'google_content_network_seat'))
        assert self.google_adx_seat == self.google_content_network_seat

    @test_case()
    def google_adx_seat_name_and_id_inherit_to_google_content_network(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_agency_group_link()
        self.pages.agency_group_list_page.wait_till_visible(self.pages.agency_group_list_page.agency_group_list_table)
        self.pages.agency_group_list_page.go_to_new_agency()
        self.pages.new_agency_group_page.wait_till_visible(self.pages.new_agency_group_page.submit_button)
        self.add_google_adx_seat_from_organization_edit_page(self.pages.new_agency_group_page)
        self.set_agency_group_fields_and_save()
        self.verify_google_seat_from_organization_show_page(self.pages.agency_group_details_page)
        self.pages.agency_group_details_page.click_add_agency()
        self.pages.new_agency_page.wait_till_visible(self.pages.new_agency_page.submit_button)
        self.add_google_adx_seat_from_organization_edit_page(self.pages.new_agency_page)
        self.set_agency_fields_and_save()
        self.verify_google_seat_from_organization_show_page(self.pages.agency_details_page)
        self.pages.agency_details_page.add_new_advertiser()
        self.pages.new_advertiser_page.wait_till_visible(self.pages.new_advertiser_page.submit_button)
        self.add_google_adx_seat_from_organization_edit_page(self.pages.new_advertiser_page)
        self.set_advertiser_fields_and_save()
        self.pages.advertiser_list_page.search_advertiser(self.advertiser_name)
        self.pages.advertiser_list_page.click_first_advertiser()
        self.pages.advertiser_details_page.wait_till_visible(self.pages.advertiser_details_page.edit_details_button)
        self.verify_google_seat_from_organization_show_page(self.pages.advertiser_details_page)

    @test_case()
    def click_fbs_save_and_continue_wait_for_flight_edit_page(self):
        self.pages.fbs_page.click_on_save_continue()
        if self.pages.fbs_page.is_element_present(self.pages.fbs_page.continue_as_normal_button):
            self.pages.fbs_page.click_on_continue_as_normal_button()
            time.sleep(2)
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)

    @test_case()
    def google_seat_id_for_flight(self):
        self.go_to_campaign_list_page()
        self.go_to_create_campaign_page(self.advertiser_name)
        self.set_campaign_required_fields_and_save('1000', False)
        self.set_flight_required_fileds_on_fbs_page('100')
        self.click_fbs_save_and_continue_wait_for_flight_edit_page()
        for inventory_supplier in ['Google Adx', 'Google Content Network']:
            self.pages.create_flight_page.select_available_inventory(inventory_supplier)
        self.pages.create_flight_page.move_selected_inventory()
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.click_flights_link()
        self.pages.flight_show_page.wait_for_flight_basics()
        flight_google_adx = 'Google Adx (ID: ' + self.google_adx_seat + ')'
        flight_google_content_network = 'Google Content Network (ID: ' + self.google_adx_seat + ')'
        for google_seat in [flight_google_adx, flight_google_content_network]:
            self.pages.flight_show_page.page_should_contain(google_seat)
        self.pages.flight_show_page.click_campaign_link()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.bulk_upload_flights()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections, 60)
        self.pages.upload_flights_page.select_flight_type('Spending Flight')
        for google_seat in [flight_google_adx, flight_google_content_network]:
            self.pages.upload_flights_page.page_should_contain(google_seat)

    @test_case()
    def go_to_audience_list_page(self):
        self.pages.search_page.click_audience_link()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        self.pages.audience_segment_list_page.click_element(self.pages.audience_segment_list_page.audience_search_text_box)

    @test_case()
    def verify_segment_size_column_values(self):
        self.common_helper.logout_and_login_by_new_user(self.pages.login_page.driver, 'campaign_manager')
        self.go_to_audience_list_page()
        self.pages.audience_segment_list_page.click_on_create_new_audience_button()
        self.pages.audience_create_page.wait_till_visible(self.pages.audience_create_page.segment_table)
        audience_marketplace_segment_size_elements = self.pages.audience_create_page.find_elements(self.pages.audience_create_page.audience_marketplace_segment_size_values)
        for element in audience_marketplace_segment_size_elements:
            assert element.get_attribute('innerHTML') is not ''
        audience_marketplace_segment_size_list= []
        composed_audience_segment_size_list = []
        def iterate_element(element_list, criteria):
            selected_segment = 0
            for element in element_list:
                if criteria == 'marketplace':
                    element.click()
                if criteria == 'marketplace_size':
                    audience_marketplace_segment_size_list.append(str(element.get_attribute('innerHTML')).replace(',', ''))
                if criteria == 'composed_size':
                    composed_audience_segment_size_list.append(str(element.get_attribute('innerHTML')).replace(',', ''))
                selected_segment += 1
                if selected_segment == 2:
                    break
        audience_marketplace_checkbox = self.pages.audience_create_page.find_elements(self.pages.audience_create_page.audience_marketplace_checkboxes)
        iterate_element(audience_marketplace_checkbox, criteria='marketplace')
        iterate_element(audience_marketplace_segment_size_elements, criteria='marketplace_size')
        time.sleep(3)
        composed_audience_segment_size_elements = self.pages.audience_create_page.find_elements(self.pages.audience_create_page.composed_audience_segment_size_value)
        iterate_element(composed_audience_segment_size_elements, criteria='composed_size')
        audience_marketplace_segment_size_list.sort() == composed_audience_segment_size_list.sort()

    @test_case()
    def go_to_campaign_list_page(self):
        self.pages.search_page.click_campaign_link()
        self.pages.campaign_list_page.wait_till_visible(self.pages.campaign_list_page.campaign_list_table)
        self.pages.campaign_list_page.click_element(self.pages.campaign_list_page.search_box)
        self.pages.campaign_list_page.wait_till_element_clickable(self.pages.campaign_list_page.new_campaign_button)

    @test_case()
    def go_to_create_campaign_page(self, advertiser_name, channel_type='Online', counter=0):
        self.pages.campaign_list_page.click_new_campaign_link()
        self.pages.new_campaign_pop_up.wait_till_visible(self.pages.new_campaign_pop_up.popup_create_campaign_button)
        try:
            self.pages.new_campaign_pop_up.type_advertiser(advertiser_name)
            self.pages.new_campaign_pop_up.select_campaign_channel(channel_type)
            self.pages.new_campaign_pop_up.submit()
        except Exception:
            counter += 1
            self.pages.new_campaign_pop_up.generate_and_accept_javascript_alert()
            self.pages.new_campaign_pop_up.close()
            if counter <= 5:
                self.go_to_create_campaign_page(advertiser_name, channel_type, counter)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)

    @test_case()
    def set_campaign_required_fields_and_save(self, budget, error_check=True):
        campaign_name = "Esc-test-campaign-" + self.pages.create_campaign_page.get_random_string(5)
        self.pages.create_campaign_page.type_campaign_name(campaign_name)
        self.pages.create_campaign_page.enter_start_date(self.dx_date.date_after_two_days())
        self.pages.create_campaign_page.enter_cpa_goal(self.dx_constant.new_campaign_cpa)
        self.pages.create_campaign_page.enter_budget(budget)
        self.pages.create_campaign_page.enter_cpm(self.dx_constant.new_campaign_cpm)
        self.pages.create_campaign_page.click_campaign_objective_distribution()
        self.pages.create_campaign_page.enter_end_date(self.dx_date.last_date_of_current_month())
        self.pages.create_campaign_page.click_element(self.pages.create_campaign_page.campaign_name)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.submit()
        if error_check:
            self.pages.create_campaign_page.wait_till_visible(self.pages.create_campaign_page.create_campaign_button)
        else:
            self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        return campaign_name

    @test_case()
    def set_flight_required_fileds_on_fbs_page(self, flight_budget):
        flight_name = 'Smoke-test-flight-' + self.pages.fbs_page.get_random_string(5)
        self.pages.fbs_page.fill_description(flight_name)
        self.pages.fbs_page.type_bid_enter(self.dx_constant.flight_bid)
        self.pages.fbs_page.type_budget_enter(flight_budget)
        time.sleep(1)
        return flight_name

    @test_case()
    def campaign_adhere_to_tactic_budgets_checkbox_functionality(self):
        self.go_to_campaign_list_page()
        self.go_to_create_campaign_page(self.dx_constant.advertiser_name)
        assert self.pages.create_campaign_page.find_element(self.pages.create_campaign_page.cruise_control_adhere).is_enabled()
        self.pages.create_campaign_page.click_adhere_to_tactic()
        campaign_name = self.set_campaign_required_fields_and_save('1000')
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.adhere_to_tactic_budget_error)
        self.pages.create_campaign_page.enter_budget_for_default_tactic('10')
        self.pages.create_campaign_page.enter_impression_cap_for_default_tactic('1')
        campaign_name = self.set_campaign_required_fields_and_save('1000', False)
        self.pages.fbs_page.click_on_campaign_link()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.edit()
        self.pages.create_campaign_page.wait_till_visible(self.pages.create_campaign_page.create_campaign_button, 40)
        assert self.pages.create_campaign_page.find_element(self.pages.create_campaign_page.cruise_control_adhere).is_selected()
        self.pages.create_campaign_page.submit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)

    @test_case()
    def creation_of_flights_with_entering_campaign_total_budget(self):
        self.pages.campaign_show_page.add_flights()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        flight_name_01 = self.set_flight_required_fileds_on_fbs_page('300.25')
        self.pages.fbs_page.click_on_add_flight()
        flight_name_02 = self.set_flight_required_fileds_on_fbs_page('699.75')
        self.pages.fbs_page.click_on_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        assert self.pages.campaign_show_page.is_element_present(self.pages.campaign_show_page.edit_budget_schedules_buttons)

    @test_case()
    def upload_csv_file_for_geofenced(self, page_object, geohash_file, csv_header = True):
        file_name = SearchFilePath(geohash_file, os.path.abspath(os.path.dirname(__file__) + '/../../../data/')).file_name
        page_object.upload_geofenced_file(file_name)
        page_object.enter_geofenced_group_name(page_object.get_random_string(8))
        page_object.click_geofenced_submit()
        if csv_header:
            page_object.wait_for_upload_success_message()
            page_object.page_should_contain(page_object.geofenced_msgs['valid'])
        else:
            page_object.wait_for_upload_error_message()
            page_object.page_should_contain(page_object.geofenced_msgs['without_header_error'])

    @test_case()
    def uploading_geohash_file_for_campaign_flights(self):
        self.go_to_campaign_list_page()
        self.go_to_create_campaign_page(self.dx_constant.advertiser_name)
        self.pages.create_campaign_page.wait_till_visible(self.pages.create_campaign_page.geo_target_type)
        self.pages.create_campaign_page.select_geo_targeting_type(0)
        self.upload_csv_file_for_geofenced(self.pages.create_campaign_page, 'geohash_without_headers.csv', False)
        self.upload_csv_file_for_geofenced(self.pages.create_campaign_page, 'valid_geohash_with_headers.csv')
        campaign_name = self.set_campaign_required_fields_and_save('1000', False)
        flight_name = self.set_flight_required_fileds_on_fbs_page('100')
        self.click_fbs_save_and_continue_wait_for_flight_edit_page()
        self.pages.create_flight_page.expand_geo_targeting()
        self.pages.create_flight_page.click_separate_geo_targeting()
        self.pages.create_flight_page.select_geo_target_region('Target GeoFenced regions')
        self.upload_csv_file_for_geofenced(self.pages.create_flight_page, 'geohash_without_headers.csv', False)
        self.upload_csv_file_for_geofenced(self.pages.create_flight_page, 'valid_geohash_with_headers.csv')
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.bulk_upload_flights()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections, 60)
        self.pages.upload_flights_page.go_to_link('Geographic Targeting')
        self.pages.upload_flights_page.click_separate_geo_targeting()
        self.pages.upload_flights_page.select_geo_targeting_type(0)
        self.upload_csv_file_for_geofenced(self.pages.upload_flights_page, 'geohash_without_headers.csv', False)

    @test_case()
    def upload_postal_code_for_flight(self):
        self.go_to_campaign_list_page()
        self.go_to_create_campaign_page(self.dx_constant.advertiser_name)
        campaign_name = self.set_campaign_required_fields_and_save('1000', False)
        flight_name = self.set_flight_required_fileds_on_fbs_page('100')
        self.click_fbs_save_and_continue_wait_for_flight_edit_page()
        self.pages.create_flight_page.expand_geo_targeting()
        self.pages.create_flight_page.click_separate_geo_targeting()
        self.pages.create_flight_page.select_geo_target_region('Specify regions within...')
        self.pages.create_flight_page.select_geo_target_codes('Postal Codes')
        usd_postal_code_file = SearchFilePath('usd_postal_code.csv', os.path.abspath(os.path.dirname(__file__) + '/../../../data/')).file_name
        self.driver.driver.execute_script("$('#postal_code_group_file').show();")
        self.pages.create_flight_page.upload_postal_code_file(usd_postal_code_file)
        self.pages.create_flight_page.enter_postal_code_group_name('Postal-code-group-'+self.pages.create_flight_page.get_random_string(5))
        self.pages.create_flight_page.click_on_upload_postal_codes_button()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.postal_code_list_table)
        for message in ['geo_targeting_warning_message', 'geo_targeting_error_message']:
            self.pages.create_flight_page.page_should_not_contain(getattr(self.pages.create_flight_page, message))

    @test_case()
    def add_duplicate_add_on_cost(self, aoc_name):
        self.pages.create_campaign_page.expand_add_on_cost()
        self.pages.create_campaign_page.click_new_aoc()
        self.pages.create_campaign_page.select_aoc_name('Custom...')
        self.pages.create_campaign_page.enter_cutom_aoc_value(aoc_name)
        self.pages.create_campaign_page.click_aoc_rate()
        self.pages.create_campaign_page.enter_aoc_rate('10')
        self.pages.create_campaign_page.click_new_aoc()
        self.pages.create_campaign_page.select_aoc_name_second('Custom...')
        self.pages.create_campaign_page.enter_custom_aoc_value_second(aoc_name)
        self.pages.create_campaign_page.click_aoc_rate_second()
        self.pages.create_campaign_page.enter_aoc_rate_second('10')

    @test_case()
    def campaign_flight_with_duplicate_add_on_cost(self):
        self.go_to_campaign_list_page()
        self.go_to_create_campaign_page(self.dx_constant.advertiser_name)
        aoc_name = self.pages.create_campaign_page.get_random_string(5)
        self.add_duplicate_add_on_cost(aoc_name)
        campaign_name = self.set_campaign_required_fields_and_save('500')
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.duplicate_aoc_error)
        self.pages.create_campaign_page.click_on_remove_aoc_button_second()
        campaign_name = self.set_campaign_required_fields_and_save('500', False)
        flight_name = self.set_flight_required_fileds_on_fbs_page('25')
        self.click_fbs_save_and_continue_wait_for_flight_edit_page()
        self.pages.create_flight_page.click_new_aoc()
        self.pages.create_flight_page.select_aoc_name('Custom...')
        self.pages.create_flight_page.enter_custom_aoc_name_second(aoc_name)
        self.pages.create_flight_page.enter_aoc_rate_value_second('10')
        self.pages.create_flight_page.click_save_exit()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit)
        self.pages.create_flight_page.page_should_contain(self.pages.create_flight_page.duplicate_aoc_error)

    @test_case()
    def verify_deal_on_flight_show_page(self, flight_name, deal_name):
        self.pages.campaign_show_page.go_to_link(flight_name)
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain(deal_name)

    @test_case()
    def uploading_and_exporting_flight_with_deals(self):
        self.go_to_campaign_list_page()
        self.go_to_create_campaign_page(self.dx_constant.advertiser_name)
        campaign_name = self.set_campaign_required_fields_and_save('1000', False)
        flight_name = self.set_flight_required_fileds_on_fbs_page('100')
        self.click_fbs_save_and_continue_wait_for_flight_edit_page()
        self.pages.create_flight_page.expand_deals()
        self.pages.create_flight_page.click_select_first_deal()
        deal_name = self.pages.create_flight_page.get_filtered_search('first_deal')
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.verify_deal_on_flight_show_page(flight_name, deal_name)
        self.pages.flight_show_page.click_campaign_link()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.export_flights()
        exported_flight_file_name = self.dx_constant.advertiser_name + ' ' + campaign_name + ' ' + 'Flight Configuration.csv'
        csvdatalist = []
        with open(os.path.dirname(__file__)+ '/../../../data/downloaded_files/' + exported_flight_file_name, 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            for data in csvreader:
                csvdatalist.append(data)
        csvfile.close()
        assert csvdatalist[1][13] == deal_name
        csvdatalist[1][0] = upload_flight_name = 'smoke-test-flight02-' + self.pages.fbs_page.get_random_string(5) 
        data_line = ''
        for line in csvdatalist:
            data_line += ",".join(line) + '\n'
        with open(os.path.dirname(__file__)+ '/../../../data/downloaded_files/' + exported_flight_file_name, 'wb') as csvfile:
            csvfile.write(data_line)
        csvfile.close()
        self.pages.campaign_show_page.bulk_upload_flights()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections, 60)
        self.pages.upload_flights_page.select_file(os.path.dirname(__file__)+ '/../../../data/downloaded_files/' + exported_flight_file_name)
        self.pages.upload_flights_page.click_upload_file()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.flight_submit, 120)
        self.pages.upload_flights_page.click_flights_submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row, 180)
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.flight_upload_success_message)
        self.pages.fbs_page.click_on_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.verify_deal_on_flight_show_page(upload_flight_name, deal_name)
        self.pages.flight_show_page.edit()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit)
        self.pages.create_flight_page.filter_deals(deal_name)
        time.sleep(2)
        assert self.pages.create_flight_page.find_element(self.pages.create_flight_page.select_first_deal).is_selected()

    @test_case()
    def verify_environment_section_validation_for_mobile_flight(self):
        self.go_to_campaign_list_page()
        self.go_to_create_campaign_page(self.dx_constant.advertiser_name, 'Mobile')
        campaign_name = self.set_campaign_required_fields_and_save('1000', False)
        flight_name = self.set_flight_required_fileds_on_fbs_page('100')
        self.click_fbs_save_and_continue_wait_for_flight_edit_page()
        self.pages.create_flight_page.expand_enviroment()
        self.pages.create_flight_page.click_environment_websites_checkbox()
        self.pages.create_flight_page.click_environment_applications_checkbox()
        self.pages.create_flight_page.click_environment_other_checkbox()
        self.pages.create_flight_page.click_save_exit()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)
        self.pages.create_flight_page.page_should_contain(self.pages.create_flight_page.environment_validation_error)
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.edit_budget_schedules()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        self.pages.fbs_page.click_on_copy_flight_icon()
        self.pages.fbs_page.accept_alert()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.copy_flight_success_message.format(flight_name))

    @test_case()
    def delete_newly_created_draft_flight(self):
        self.go_to_campaign_list_page()
        self.go_to_create_campaign_page(self.dx_constant.advertiser_name)
        self.newly_created_campaign_name = self.set_campaign_required_fields_and_save('1000', False)
        flight_name_01 = self.set_flight_required_fileds_on_fbs_page('100')
        self.pages.fbs_page.click_on_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.click_first_flight_delete_icon()
        self.pages.campaign_show_page.accept_alert()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.page_should_contain(self.pages.campaign_show_page.delete_flight_success_message.format(flight_name_01))
  
    @test_case()
    def delete_newly_created_running_flight(self):
        self.pages.campaign_show_page.edit_budget_schedules()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        flight_name_02 = self.set_flight_required_fileds_on_fbs_page('100')
        self.click_fbs_save_and_continue_wait_for_flight_edit_page()
        time.sleep(2)
        self.pages.create_flight_page.select_available_inventory('Admax')
        self.pages.create_flight_page.move_selected_inventory()
        time.sleep(2)
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.click_flight_assign_creatives_link()
        self.pages.creative_assign_dashboard_page.wait_till_visible(self.pages.creative_assign_dashboard_page.first_flight_checkbox, 80)
        self.pages.creative_assign_dashboard_page.click_on_first_flight_checkbox()
        time.sleep(3)
        self.pages.creative_assign_dashboard_page.wait_till_enabled(self.pages.creative_assign_dashboard_page.creatives_available_button)
        self.pages.creative_assign_dashboard_page.click_on_creatives_available_button()
        self.pages.creative_assign_dashboard_page.click_on_first_creative_add_button()
        if self.pages.creative_assign_dashboard_page.is_element_present(self.pages.creative_assign_dashboard_page.message_div_close_button):
            self.pages.creative_assign_dashboard_page.close_flash_message_div()
        self.go_to_campaign_list_page()
        self.pages.campaign_list_page.select_orgnization(self.dx_constant.advertiser_name)
        self.pages.campaign_list_page.wait_till_visible(self.pages.campaign_list_page.campaign_list_table)
        time.sleep(2)
        self.pages.campaign_list_page.search_campaign(self.newly_created_campaign_name)
        self.pages.campaign_list_page.go_to_link(self.newly_created_campaign_name)
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.click_on_first_flight_play_pause_button()
        self.pages.campaign_show_page.edit_budget_schedules()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        expected_delete_button_title = 'Cannot Delete'
        actual_delete_button_title = self.pages.fbs_page.get_attribute_value(self.pages.fbs_page.delete_flight, 'title')
        assert expected_delete_button_title == actual_delete_button_title

    @test_case()
    def go_to_creative_list_page(self):
        self.pages.search_page.click_creative_link()
        time.sleep(2)
        self.pages.search_page.accept_alert()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.asset_list_table)
        self.pages.creative_list_page.click_element(self.pages.creative_list_page.filters)

    @test_case()
    def search_creative_and_go_to_edit_page(self, creative_name):
        self.pages.creative_list_page.search_creative(creative_name)
        self.pages.creative_list_page.wait_till_element_visible_and_invisible(self.pages.creative_list_page.creative_tag_spinner)
        self.pages.creative_list_page.click_on_first_creative_gear_icon()
        self.pages.creative_list_page.click_on_first_creative_edit_link()
        self.pages.creative_edit_page.wait_till_visible(self.pages.creative_edit_page.submit_button)

    @test_case()
    def add_companion_assets_to_dxas_video_creative(self):
        self.go_to_creative_list_page()
        self.pages.creative_list_page.click_on_new_assets_button()
        self.pages.upload_assets_page.wait_till_visible(self.pages.upload_assets_page.upload_assets_button)
        asset_file_path = SearchFilePath('mp4_asset.mp4', os.path.abspath(os.path.dirname(__file__) + '/../../../data/')).file_name
        self.pages.upload_assets_page.select_asset_file(asset_file_path)
        self.pages.upload_assets_page.click_generate_creatives_checkbox()
        self.pages.upload_assets_page.click_upload_assets_button()
        self.pages.generate_creative_page.wait_till_visible(self.pages.generate_creative_page.ok_button)
        creative_name = 'esc-test-asset-'+self.pages.generate_creative_page.get_random_string(5)
        self.pages.generate_creative_page.enter_creative_name(creative_name)
        self.pages.generate_creative_page.click_ok_button()
        self.pages.detailed_edit_creatives.wait_for_detailed_form()
        self.pages.detailed_edit_creatives.click_on_assign_campanion_link()
        self.pages.detailed_edit_creatives.wait_till_visible(self.pages.detailed_edit_creatives.assing_asset_table)
        self.pages.detailed_edit_creatives.click_first_asset_radio_button()
        asset_name = self.pages.detailed_edit_creatives.get_innerhtml_text('first_asset_name')
        self.pages.detailed_edit_creatives.click_on_assign_asset_button()
        self.pages.detailed_edit_creatives.save_creative()
        self.pages.detailed_edit_creatives.wait_till_element_visible_and_invisible(self.pages.detailed_edit_creatives.creative_save_loader)
        if self.pages.detailed_edit_creatives.is_element_present(self.pages.detailed_edit_creatives.first_save):
            self.pages.detailed_edit_creatives.save_creative()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.creative_table)
        self.pages.creative_list_page.page_should_contain(self.pages.creative_list_page.creative_success_message)
        self.search_creative_and_go_to_edit_page(creative_name)
        assigned_asset_name = self.pages.creative_edit_page.get_innerhtml_text('assigned_asset_link')
        assert assigned_asset_name == asset_name

    @test_case()
    def verify_video_creative_secure_tag_from_creative_edit_page(self):
        self.go_to_creative_list_page()
        self.pages.creative_list_page.click_new_creatives()
        self.pages.bulk_edit_creative_page.wait_for_creative_forms()
        self.pages.bulk_edit_creative_page.go_to_link('Detailed Edit')
        self.pages.detailed_edit_creatives.wait_for_detailed_form()
        video_creative_tag_file = open(os.path.dirname(__file__) + '/../../../data/bulk_upload_creative_files/video_creative_tag.txt')
        video_creative_tag =  video_creative_tag_file.read()
        video_creative_tag_file.close()
        self.pages.detailed_edit_creatives.input_first_tags(video_creative_tag)
        creative_name = 'Video-creative-name-' + self.pages.detailed_edit_creatives.get_random_string(5)
        self.pages.detailed_edit_creatives.input_first_creative_name(creative_name)
        self.pages.detailed_edit_creatives.input_first_concept(self.pages.detailed_edit_creatives.get_random_string(8))
        self.pages.detailed_edit_creatives.fill_field(self.pages.detailed_edit_creatives.first_concept, Keys.TAB)
        self.pages.detailed_edit_creatives.save_creative()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.creative_table)
        self.search_creative_and_go_to_edit_page(creative_name)
        self.pages.creative_edit_page.click_on_creative_tag_link()
        video_creative_tag_snippet = self.pages.creative_edit_page.get_innerhtml_text('original_tag_text_area')
        video_creative_tag_snippet = video_creative_tag_snippet.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
        assert video_creative_tag in video_creative_tag_snippet

    @test_case()
    def flight_creation_with_over_budget_by_non_dataxu_user(self):
        self.common_helper.logout_and_login_by_new_user(self.pages.login_page.driver, 'non_dataxu_domain_campaign_user')
        self.go_to_campaign_list_page()
        self.go_to_create_campaign_page(self.dx_constant.advertiser_name)
        self.set_campaign_required_fields_and_save('500', False)
        self.set_flight_required_fileds_on_fbs_page('501')
        self.pages.fbs_page.click_on_save_exit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.error_div)
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.flight_over_budget_error)
