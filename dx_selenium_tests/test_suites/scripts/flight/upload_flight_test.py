import random
import os
import time
import csv
from dx_test.dx_test import DXTest
from lib.dx_date import DXDate
from lib.gui_tests import test_case
from common_helpers.common_helpers import CommonHelper

class UploadFlightTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.common_helper = CommonHelper()
        self.setup(self.dx_constant.user_by_role['campaign_manager'])

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

    def fill_campaign_page(self):
        self.campaign = "Flight-upload-campaign-" + self.pages.create_campaign_page.get_random_string(5)
        self.pages.create_campaign_page.type_campaign_name(self.campaign)
        self.pages.create_campaign_page.enter_start_date(DXDate().todays_date())
        self.pages.create_campaign_page.click_element(self.pages.create_campaign_page.campaign_name)
        self.pages.create_campaign_page.enter_cpa_goal('10')
        self.pages.create_campaign_page.enter_budget('5000')
        self.pages.create_campaign_page.enter_cpm('10')
        self.pages.create_campaign_page.click_campaign_objective_distribution()
        self.pages.create_campaign_page.enter_end_date(DXDate().last_date_of_current_month())
        self.pages.create_campaign_page.click_element(self.pages.create_campaign_page.campaign_name)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)

    def go_to_upload_flight_page(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details()
        if self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.campaign_name):
            self.fill_campaign_page()
        if self.pages.fbs_page.is_element_present(self.pages.fbs_page.description_filter):
            self.pages.fbs_page.go_to_link('Upload Flights')
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.one_view_policy_values, 60)

    def verify_contents(self, link, contents):
        time.sleep(2)
        if link != '':
            self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections[link])
        for element in contents:
            print element
            assert self.pages.upload_flights_page.is_element_present(getattr(self.pages.upload_flights_page, element))

    @test_case()
    def verify_flights_details_inventory(self):
        contents = [
                    'frequency_cap', 'frequency', 'frequency_type', 'flight_type', 'algorithm', 'placement_standard',
                    'use_grid', 'dayparting_sunday', 'dayparting_monday', 'dayparting_tuesday', 'dayparting_wednesday',
                    'dayparting_thursday', 'dayparting_friday', 'dayparting_saturday', 'select_all',
                    'frequency_cap_values', 'flight_type_values', 'media_type_values', 'algorithm_values',
                    'placement_values', 'dayparting_values', 'suppliers_values', 'one_view_section',
                    'one_view_policy_values'
                    ]
        self.verify_contents('flight_details_inventory', contents)

    @test_case()
    def working_of_frequency_cap(self):
        self.pages.upload_flights_page.type_frequency_cap(self.dx_constant.value)
        expected_text = self.dx_constant.value + '/1 day'
        self.pages.upload_flights_page.assert_value('frequency_cap_values', expected_text)

    @test_case()
    def working_of_flight_types_avail(self):
        self.pages.upload_flights_page.select_flight_type(self.dx_constant.flight_type_spending)
        self.pages.upload_flights_page.assert_value('flight_type_values', self.dx_constant.flight_type_spending)

    @test_case()
    def working_of_dayparting(self):
        self.pages.upload_flights_page.assert_value('dayparting_values', self.pages.upload_flights_page.inputs['day_parting'])

    @test_case()
    def working_of_algorithms(self):
        self.pages.upload_flights_page.assert_value('algorithm_values', self.pages.upload_flights_page.inputs['algorithms'])

    @test_case()
    def working_of_placement(self):
        self.pages.upload_flights_page.select_placement(self.pages.upload_flights_page.inputs['placement'])
        self.pages.upload_flights_page.assert_value('placement_values', self.pages.upload_flights_page.inputs['placement'])

    @test_case()
    def working_of_inventory_suppliers(self):
        self.pages.upload_flights_page.click_first_suppliers()
        self.pages.upload_flights_page.assert_value('suppliers_values', self.pages.upload_flights_page.inputs['suppliers'])

    @test_case()
    def verify_channels_language(self):
        self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections['channels_languages'])
        self.pages.upload_flights_page.click_separate_lang_targeting()
        contents = [
                    'avail_channels', 'selected_channels', 'select_channels', 'remove_channels', 'select_all_channels',
                    'remove_all_channels', 'inherit_lang_targeting', 'separate_lang_targeting',
                    'avail_langs', 'selected_channels', 'select_langs', 'remove_channels', 'select_all_channels',
                    'remove_all_channels', 'channels_values', 'langs_values'
                    ]
        self.verify_contents('', contents)

    @test_case()
    def working_of_buttons(self):
        self.pages.upload_flights_page.select_avail_channel(self.pages.upload_flights_page.channels[0])
        self.pages.upload_flights_page.click_select_channels()
        self.pages.upload_flights_page.verify_selected_values('selected_channels',self.pages.upload_flights_page.channels[0])
        self.pages.upload_flights_page.select_applied_channel(self.pages.upload_flights_page.channels[0])
        self.pages.upload_flights_page.click_remove_channels()
        self.pages.upload_flights_page.verify_selected_values('avail_channels',self.pages.upload_flights_page.channels[0])
        self.pages.upload_flights_page.click_select_all_channels()
        self.pages.upload_flights_page.verify_selected_values('selected_channels',None,self.pages.upload_flights_page.channels)
        self.pages.upload_flights_page.click_remove_all_channels()
        self.pages.upload_flights_page.verify_selected_values('avail_channels',None,self.pages.upload_flights_page.channels)

    @test_case()
    def working_of_content_channel(self):
        self.pages.upload_flights_page.select_avail_channel(self.pages.upload_flights_page.channels[0])
        self.pages.upload_flights_page.click_select_channels()
        self.pages.upload_flights_page.assert_value('channels_values', self.pages.upload_flights_page.inputs['channels'])

    @test_case()
    def working_of_lang_source_and_section(self):
        self.pages.upload_flights_page.click_separate_lang_targeting()
        self.pages.upload_flights_page.is_element_present(self.pages.upload_flights_page.lang_targeting_section)

    @test_case()
    def working_of_languages(self):
        for lang in self.pages.upload_flights_page.languages:
            self.pages.upload_flights_page.select_avail_langs(lang)
        self.pages.upload_flights_page.click_select_langs()
        self.pages.upload_flights_page.assert_value('langs_values', self.pages.upload_flights_page.inputs['lang_targeting'])

    @test_case()
    def verify_geo_targeting(self):
        self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections['geographic_targeting'])
        self.pages.upload_flights_page.click_separate_geo_targeting()
        time.sleep(5)
        contents = [
                    'inherit_geo_targeting', 'separate_geo_targeting', 'geo_target_type', 'search_countries',
                    'avail_countries', 'selected_countries', 'select_countries', 'remove_countries',
                    'select_all_countries','remove_all_countries', 'geo_target_type_values', 'geo_target_values'
                    ]
        self.verify_contents('', contents)

    @test_case()
    def working_of_buttons_in_geo_targeting(self):
        self.pages.upload_flights_page.click_separate_geo_targeting()
        self.pages.upload_flights_page.select_avail_country('Denmark')
        self.pages.upload_flights_page.click_select_country()
        self.pages.upload_flights_page.verify_selected_values('selected_countries', 'Denmark')
        self.pages.upload_flights_page.select_applied_country('Denmark')
        self.pages.upload_flights_page.click_remove_country()
        self.pages.upload_flights_page.verify_selected_values('avail_countries', 'Denmark')
        self.pages.upload_flights_page.click_select_all_countries()
        self.pages.upload_flights_page.verify_selected_values('selected_countries', None, self.pages.upload_flights_page.countries)
        self.pages.upload_flights_page.click_remove_all_countries()
        self.pages.upload_flights_page.verify_selected_values('avail_countries', None, self.pages.upload_flights_page.countries)

    @test_case()
    def search_in_geographic_targeting(self):
        self.pages.upload_flights_page.search_country('India')
        self.pages.upload_flights_page.verify_selected_values('avail_countries', 'India')

    @test_case()
    def verify_creative_assignment(self):
        self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections['creatives'])
        self.pages.upload_flights_page.search_creatives(self.pages.upload_flights_page.inputs['creative'])
        time.sleep(5)
        contents = [
                    'creative_search', 'master_select', 'first_select', 'creative_values'
                    ]
        self.verify_contents('', contents)

    @test_case()
    def search_in_creative_assignment(self):
        self.pages.upload_flights_page.search_creatives(self.pages.upload_flights_page.inputs['creative'])
        creative = str(self.pages.upload_flights_page.find_element(self.pages.upload_flights_page.first_creative).get_attribute('innerHTML')).replace('<wbr>', '').replace('_', ' ')
        flag = creative.find(str(self.pages.upload_flights_page.inputs['creative']))
        assert not flag < 0, 'searching creative not present'

    @test_case()
    def working_of_checkboxes(self):
        self.pages.upload_flights_page.select_all_creatives()
        assert (self.pages.upload_flights_page.find_element(self.pages.upload_flights_page.first_select).is_selected() and
                self.pages.upload_flights_page.find_element(self.pages.upload_flights_page.master_select).is_selected())
        self.pages.upload_flights_page.select_all_creatives()
        assert not (self.pages.upload_flights_page.find_element(self.pages.upload_flights_page.first_select).is_selected() and
                self.pages.upload_flights_page.find_element(self.pages.upload_flights_page.master_select).is_selected())
        self.pages.upload_flights_page.select_first_creative()
        assert self.pages.upload_flights_page.find_element(self.pages.upload_flights_page.first_select).is_selected()
        self.pages.upload_flights_page.select_first_creative()
        assert not self.pages.upload_flights_page.find_element(self.pages.upload_flights_page.first_select).is_selected()

    @test_case()
    def working_of_creatives(self):
        self.pages.upload_flights_page.select_first_creative()
        creative = str(self.pages.upload_flights_page.find_element(self.pages.upload_flights_page.first_creative).get_attribute('innerHTML')).replace('<wbr>', '').strip()
        self.pages.upload_flights_page.assert_value('creative_values', creative)

    @test_case()
    def verify_audience_targeting(self):
        self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections['audience_targeting'])
        contents = [
                    'avail_audience', 'included_audience', 'excluded_audience', 'move_included_audience',
                    'move_all_included_audience', 'remove_audience', 'remove_all_audience',
                    'move_excluded_audience', 'move_all_excluded_audience', 'included_audience_values',
                    'excluded_audience_values'
                    ]
        self.verify_contents('', contents)

    @test_case()
    def buttons_in_audience_targeting(self):
        audience = self.pages.upload_flights_page.get_audiences('avail_audience')
        self.pages.upload_flights_page.select_avail_audience(0)
        self.pages.upload_flights_page.include_audience()
        self.pages.upload_flights_page.verify_selected_values('included_audience', audience)
        self.pages.upload_flights_page.select_included_audience(0)
        self.pages.upload_flights_page.click_remove_audience()
        self.pages.upload_flights_page.verify_selected_values('avail_audience', audience)
        audience = self.pages.upload_flights_page.get_audiences('avail_audience')
        self.pages.upload_flights_page.include_all_audience()
        time.sleep(5)
        self.pages.upload_flights_page.verify_selected_values('included_audience', audience)
        self.pages.upload_flights_page.click_remove_all_audience()
        time.sleep(5)
        self.pages.upload_flights_page.verify_selected_values('avail_audience', audience)
        audience = self.pages.upload_flights_page.get_audiences('avail_audience')
        self.pages.upload_flights_page.select_avail_audience(0)
        self.pages.upload_flights_page.exclude_audience()
        self.pages.upload_flights_page.verify_selected_values('excluded_audience', audience)
        self.pages.upload_flights_page.select_excluded_audience(0)
        self.pages.upload_flights_page.click_remove_audience()
        self.pages.upload_flights_page.verify_selected_values('avail_audience', audience)
        audience = self.pages.upload_flights_page.get_audiences('avail_audience')
        self.pages.upload_flights_page.exclude_all_audience()
        time.sleep(5)
        self.pages.upload_flights_page.verify_selected_values('excluded_audience', audience)
        self.pages.upload_flights_page.click_remove_all_audience()
        time.sleep(5)
        self.pages.upload_flights_page.verify_selected_values('avail_audience', audience)

    @test_case()
    def working_of_included_audience(self):
        audience = str(self.pages.upload_flights_page.get_audiences('avail_audience').split('(')[0]).strip()
        self.pages.upload_flights_page.select_avail_audience(0)
        self.pages.upload_flights_page.include_audience()
        time.sleep(5)
        self.pages.upload_flights_page.assert_value('included_audience_values',audience)

    @test_case()
    def working_of_excluded_audience(self):
        audience = str(self.pages.upload_flights_page.get_audiences('avail_audience').split('(')[0]).strip()
        self.pages.upload_flights_page.select_avail_audience(0)
        self.pages.upload_flights_page.exclude_audience()
        time.sleep(10)
        self.pages.upload_flights_page.assert_value('excluded_audience_values',audience)

    @test_case()
    def verify_uploads(self):
        with open(os.path.dirname(__file__)+ '/../../../data/flights_upload/test_valid_flights.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            first = False
            for reader in csvreader:
                if first:
                    self.pages.upload_flights_page.page_should_contain(reader[0])
                first = True

    @test_case()
    def upload_file(self, filename):
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections)
        self.pages.upload_flights_page.select_file(os.path.dirname(__file__)+ '/../../../data/flights_upload/' + filename)
        self.pages.upload_flights_page.click_upload_file()

    @test_case()
    def upload_blank_file(self):
        self.upload_file('blank.csv')
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.errors)
        self.pages.upload_flights_page.page_should_contain(self.pages.upload_flights_page.messages['blank_file'])

    @test_case()
    def upload_invalid_format_file(self):
        self.upload_file('text.txt')
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.errors)
        self.pages.upload_flights_page.page_should_contain(self.pages.upload_flights_page.messages['invalid_format'])

    @test_case()
    def upload_invalid_file(self):
        self.upload_file('flights_invalid.csv')
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.flight_uploads, 90)
        self.pages.upload_flights_page.page_should_contain(self.pages.upload_flights_page.messages['invalid_data'])

    @test_case()
    def validate_flight_uploads(self, filename, message_key):
        self.pages.upload_flights_page.click_cancel_delete()
        self.upload_file(filename)
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.flight_uploads, 90)
        self.pages.upload_flights_page.page_should_contain(self.pages.upload_flights_page.messages[message_key])

    @test_case()
    def upload_blank_description_file(self):
        self.validate_flight_uploads('blank_description.csv', 'blank_description')

    @test_case()
    def upload_oveflow_description_file(self):
        self.validate_flight_uploads('overflow.csv', 'overflow')

    @test_case()
    def upload_valid_flights(self, filename):
        self.pages.upload_flights_page.select_file(os.path.dirname(__file__)+ '/../../../data/flights_upload/' + filename + '.csv')
        self.pages.upload_flights_page.click_upload_file()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.flight_uploads, 180)
        self.pages.upload_flights_page.click_flights_submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row, 240)
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.flight_upload_success_message)

    @test_case()
    def upload_flights_file(self):
        self.go_to_upload_flight_page()
        self.common_helper.process_flight_file_with_name_and_date('test_valid_flights', 'Online')
        self.upload_valid_flights('test_valid_flights')
        self.pages.fbs_page.click_on_save_exit()

    @test_case()
    def upload_flights_special_limit(self):
        self.pages.fbs_page.wait_till_visible(['id', 'tactic_flight_table'])
        self.pages.upload_flights_page.go_to_link('Bulk Upload Flights')
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections, 60)
        self.common_helper.process_flight_file_with_name_and_date('special_chars', 'Online', self.dx_constant.special_char)
        self.upload_valid_flights('special_chars')

    @test_case()
    def upload_flights_special_chars(self):
        self.pages.upload_flights_page.page_should_contain('All flights have been saved successfully.')

    @test_case()
    def verify_contents_of_mobile_options(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Mobile')
        if self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.campaign_name):
            self.fill_campaign_page()
        if self.pages.fbs_page.is_element_present(self.pages.fbs_page.description_filter):
            self.pages.fbs_page.go_to_link('Upload Flights')
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections, 60)
        contents = [
                    'wifi', 'carrier', 'other', 'environment_websites', 'environment_apps', 'environment_other',
                    'mobile_carrier_avail', 'mobile_carrier_applied', 'move_mobile_carrier', 'remove_mobile_carrier',
                    'move_all_mobile_carrier', 'remove_all_mobile_carrier', 'mobile_platform_avail',
                    'mobile_platform_applied', 'move_mobile_platform', 'remove_mobile_platform',
                    'move_all_mobile_platform', 'remove_all_mobile_platform', 'devices_filter', 'designation_filter',
                    'all_tabs', 'all_smartphones', 'all_feature_phones', 'master_select_devices', 'first_manufacturer',
                    'expand_first_model', 'first_model', 'connection_types_values', 'mobile_options_values',
                    'carrier_values', 'platform_values', 'devices_values'
                    ]
        self.verify_contents('environment_devices', contents)

    @test_case()
    def working_of_gateway(self):
        self.pages.upload_flights_page.click_wifi_gateway()
        self.pages.upload_flights_page.assert_value('connection_types_values',self.pages.upload_flights_page.inputs['gateway'])

    @test_case()
    def working_of_options(self):
        self.pages.upload_flights_page.click_environment_apps()
        self.pages.upload_flights_page.assert_value('mobile_options_values',self.pages.upload_flights_page.inputs['options'])

    @test_case()
    def working_of_carrier(self):
        self.pages.upload_flights_page.select_carrier(self.pages.upload_flights_page.inputs['carrier'])
        self.pages.upload_flights_page.click_select_carrier()
        self.pages.upload_flights_page.assert_value('carrier_values',self.pages.upload_flights_page.inputs['carrier'])

    @test_case()
    def working_of_platform(self):
        self.pages.upload_flights_page.select_platform(self.pages.upload_flights_page.inputs['platform'])
        self.pages.upload_flights_page.click_select_platform()
        self.pages.upload_flights_page.assert_value('platform_values',self.pages.upload_flights_page.inputs['platform'])

    @test_case()
    def working_of_devices(self):
        self.pages.upload_flights_page.click_all_smartphones()
        self.pages.upload_flights_page.assert_value('devices_values',self.pages.upload_flights_page.inputs['devices'])

    @test_case()
    def buttons_in_mobile_carrier(self):
        self.pages.upload_flights_page.click_remove_all_carrier()
        self.pages.upload_flights_page.select_carrier(self.pages.upload_flights_page.inputs['carrier'])
        self.pages.upload_flights_page.click_select_carrier()
        self.pages.upload_flights_page.verify_selected_values('mobile_carrier_applied', self.pages.upload_flights_page.inputs['carrier'])
        self.pages.upload_flights_page.select_applied_carrier(self.pages.upload_flights_page.inputs['carrier'])
        self.pages.upload_flights_page.click_remove_carrier()
        self.pages.upload_flights_page.verify_selected_values('mobile_carrier_avail', self.pages.upload_flights_page.inputs['carrier'])
        self.pages.upload_flights_page.click_remove_all_carrier()
        self.pages.upload_flights_page.verify_selected_values('mobile_carrier_avail', self.pages.upload_flights_page.inputs['carrier'])
        self.pages.upload_flights_page.click_select_all_carrier()
        self.pages.upload_flights_page.verify_selected_values('mobile_carrier_applied', self.pages.upload_flights_page.inputs['carrier'])

    @test_case()
    def search_in_mobile_devices(self):
        self.pages.upload_flights_page.filter_mobile_devices(self.pages.upload_flights_page.inputs['search'])
        time.sleep(5)
        self.pages.upload_flights_page.search_devices()

    @test_case()
    def buttons_in_mobile_platform(self):
        self.pages.upload_flights_page.click_remove_all_platform()
        self.pages.upload_flights_page.select_platform(self.pages.upload_flights_page.inputs['platform'])
        self.pages.upload_flights_page.click_select_platform()
        self.pages.upload_flights_page.verify_selected_values('mobile_platform_applied', self.pages.upload_flights_page.inputs['platform'])
        self.pages.upload_flights_page.select_applied_platform(self.pages.upload_flights_page.inputs['platform'])
        self.pages.upload_flights_page.click_remove_platform()
        self.pages.upload_flights_page.verify_selected_values('mobile_platform_avail', self.pages.upload_flights_page.inputs['platform'])
        self.pages.upload_flights_page.click_remove_all_platform()
        self.pages.upload_flights_page.verify_selected_values('mobile_platform_avail', self.pages.upload_flights_page.inputs['platform'])
        self.pages.upload_flights_page.click_select_all_platform()
        self.pages.upload_flights_page.verify_selected_values('mobile_platform_applied', self.pages.upload_flights_page.inputs['platform'])

    @test_case()
    def set_flight_required_fileds_on_fbs_page(self):
        flight_name = 'test-upload-' + self.pages.fbs_page.get_random_string(5)
        self.pages.fbs_page.fill_description(flight_name)
        self.pages.fbs_page.type_bid_enter(self.dx_constant.flight_bid)
        self.pages.fbs_page.type_budget_enter('5')
        time.sleep(1)
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)

    @test_case()
    def create_domain_list(self, domain_list_type, domain_list):
        self.pages.domain_list_management_page.click_on_new_list_button()
        domain_list_name = domain_list_type + self.pages.domain_list_management_page.get_random_string(5)
        self.pages.domain_list_management_page.set_domain_list_name(domain_list_name)
        self.pages.domain_list_management_page.wait_till_enabled(self.pages.domain_list_management_page.domain_list_name_submit_button)
        self.pages.domain_list_management_page.click_on_save_button()
        self.pages.domain_list_management_page.wait_till_visible(self.pages.domain_list_management_page.domain_list_checked_checkbox)
        self.pages.domain_list_management_page.click_on_edit_button()
        for domain_name in domain_list:
            self.pages.domain_list_management_page.enter_domain_name_in_domain_text_area(domain_name + "\n")
        self.pages.domain_list_management_page.wait_till_enabled(self.pages.domain_list_management_page.domain_list_submit_button)
        self.pages.domain_list_management_page.click_on_domain_list_submit_button()
        self.pages.domain_list_management_page.wait_till_visible(self.pages.domain_list_management_page.domain_list_remove_button_column)
        time.sleep(3)
        return domain_list_name

    @test_case()
    def upload_flights_with_domains(self, campaign_channel, file_name):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details(campaign_channel)
        self.fill_campaign_page()
        if campaign_channel == 'Online':
            self.set_flight_required_fileds_on_fbs_page()
            self.pages.flight_edit_page.expand_blacklist()
            self.pages.flight_edit_page.click_on_edit_blacklist_link()
            self.pages.creative_assign_dashboard_page.wait_till_visible(self.pages.creative_assign_dashboard_page.blacklist_inherit_slider, 80)
            time.sleep(2)
            self.pages.creative_assign_dashboard_page.click_on_blacklist_inherit_slider()
            self.pages.creative_assign_dashboard_page.wait_till_visible(self.pages.creative_assign_dashboard_page.blacklist_search_available_domain_lists_link, 60)
            availabel_domain_list_count = self.pages.creative_assign_dashboard_page.get_attribute_value(self.pages.creative_assign_dashboard_page.domains_available_button)
            self.pages.creative_assign_dashboard_page.click_on_domains_available_button()
            if availabel_domain_list_count == '(0)':
                self.pages.creative_assign_dashboard_page.wait_till_visible(self.pages.creative_assign_dashboard_page.create_domains_list_link)
                self.pages.creative_assign_dashboard_page.click_on_create_domains_list_link()
                self.pages.domain_list_management_page.wait_till_visible(self.pages.domain_list_management_page.new_list_button)
                self.whitelist_name = self.create_domain_list('whitelist-domains-', self.pages.domain_list_management_page.whitelist_domains)
                self.blacklist_name = self.create_domain_list('blacklist-domains-', self.pages.domain_list_management_page.blacklist_domains)
                self.pages.domain_list_management_page.click_on_back_button()
                self.pages.creative_assign_dashboard_page.wait_till_visible(self.pages.creative_assign_dashboard_page.domains_available_button, 60)
            else:
                time.sleep(2)
                self.pages.creative_assign_dashboard_page.wait_till_visible(self.pages.creative_assign_dashboard_page.blacklist_domain_list_panel)
                domain_list_name = []
                domain_list_name_elements = self.pages.creative_assign_dashboard_page.find_elements(self.pages.creative_assign_dashboard_page.blacklist_domain_list_name_row)
                for element in domain_list_name_elements:
                    domain_list_name.append(str(element.get_attribute('innerHTML')).strip())
                self.whitelist_name = domain_list_name[0]
                self.blacklist_name = domain_list_name[1]
            self.pages.creative_assign_dashboard_page.click_on_edit_flight_button()
            self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        self.pages.fbs_page.click_on_upload_flights_button()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections, 60)
        self.common_helper.process_flight_file_with_domains(file_name, campaign_channel, self.whitelist_name, self.blacklist_name)
        self.upload_valid_flights(file_name)
        self.pages.fbs_page.click_on_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.click_first_flight_edit_icon()
        self.pages.create_flight_page.wait_for_flight_details()
        for element in [self.whitelist_name, self.blacklist_name]:
            self.pages.create_flight_page.page_should_contain(element)

    @test_case()
    def upload_flights_with_domains_for_online_campaign(self):
        self.upload_flights_with_domains('Online', 'online_all_fields')

    @test_case()
    def upload_flights_with_domains_for_mobile_campaign(self):
        self.upload_flights_with_domains('Mobile', 'mobile_all_fields')

    @test_case()
    def upload_flights_with_domains_for_video_campaign(self):
        self.upload_flights_with_domains('Video', 'video_all_fields')

    @test_case()
    def upload_flights_with_domains_for_omni_channel_campaign(self):
        self.upload_flights_with_domains('Omni-Channel', 'omni_channel_all_fields')
