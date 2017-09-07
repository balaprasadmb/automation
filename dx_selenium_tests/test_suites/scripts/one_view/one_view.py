#coding: utf-8
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from common_helpers.common_helpers import CommonHelper
from flight_helper import FlightHelper
from lib.dx_date import DXDate
import csv
import os
import time
from selenium.webdriver.common.keys import Keys

class OneView(DXTest):

    @test_case()
    def login_as_dx_admin(self):
        self.common_helper = CommonHelper()
        self.message = self.pages.advertiser_list_page.success_message
        self.setup()

    @test_case()
    def validate_one_view_for_agency_group_and_agency(self):
        self.pages.new_agency_group_page.open()
        self.common_helper.assert_is_element_present(self.pages.new_agency_group_page, 'one_view_section', criteria=False)
        self.pages.new_agency_page.open()
        self.common_helper.assert_is_element_present(self.pages.new_agency_page, 'one_view_section', criteria=False)

    @test_case()
    def assert_data_in_list(self, page_object, loc, data_list):
        data = page_object.get_content_text(loc)
        assert data in data_list

    @test_case()
    def validate_one_view_for_advertiser(self):
        self.pages.admin_page.go_to_link('Admin')
        self.pages.admin_page.wait_till_visible(self.pages.admin_page.advertiser_link)
        self.pages.admin_page.go_to_link('Advertisers')
        self.pages.advertiser_list_page.wait_till_visible(self.pages.advertiser_list_page.advertiser_list)
        self.pages.advertiser_list_page.click_on_new_advrtiser_button()
        self.pages.new_advertiser_page.wait_till_visible(self.pages.new_advertiser_page.submit_button)
        self.common_helper.assert_is_element_present(self.pages.new_advertiser_page, self.pages.new_advertiser_page.one_view_section['policies_table'].values())
        for i in range(3, 6):
            self.assert_data_in_list(self.pages.new_advertiser_page, ['css selector', self.pages.new_advertiser_page.one_view_section['data_policy_text']['value'].format(i)],
                                     ['Single Device', 'High Precision', 'Broad Reach'])

    @test_case()
    def policy_selection_helper(self, element):
        locators = {'single': 3, 'high': 4, 'broad': 5}
        self.pages.new_advertiser_page.click_element([self.pages.new_advertiser_page.one_view_section['policy_radio_buttons']['by'],
                                                self.pages.new_advertiser_page.one_view_section['policy_radio_buttons']['value'].format(locators[element])])
        locators.pop(element)
        for key, value in locators.iteritems():
            self.common_helper.assert_is_selected(self.pages.new_advertiser_page,
                                                  [self.pages.new_advertiser_page.one_view_section['policy_radio_buttons']['by'],
                                                   self.pages.new_advertiser_page.one_view_section['policy_radio_buttons']['value'].format(value)],
                                                  criteria=False)

    @test_case()
    def validate_one_view_policy_selection(self):
        self.pages.new_advertiser_page.open()
        for i in range(1, 7):
            self.assert_data_in_list(self.pages.new_advertiser_page, ['css selector', self.pages.new_advertiser_page.one_view_section['column_headers']['value'].format(i)],
                                     ['Make Available', 'Default Policy', 'Data Policy', 'Aliases Used', 'Links Used', 'Notes'])
        for element in ['lock_policy_checkbox', 'single_policy_default_checked_checkbox']:
            self.common_helper.assert_is_element_present(self.pages.new_advertiser_page,
                                                         self.pages.new_advertiser_page.one_view_section[element].values())
        self.pages.new_advertiser_page.click_high_precision_policy_checkbox()
        time.sleep(2)
        self.pages.new_advertiser_page.click_broad_reach_policy_checkbox()
        for element in ['high_precision_policy_checkbox', 'broad_reach_policy_checkbox']:
            self.common_helper.assert_is_selected(self.pages.new_advertiser_page, self.pages.new_advertiser_page.one_view_section[element].values())
        for element in ['single', 'high', 'broad']:
            self.policy_selection_helper(element)

    @test_case()
    def creation_of_advertiser_with_lock_oneview_policy(self):
        self.pages.agency_list_page.open()
        self.pages.agency_list_page.filter_agency_name_in_filterbox(self.dx_constant.agency_name)
        time.sleep(3)
        self.pages.agency_list_page.click_first_agency()
        self.pages.agency_details_page.wait_till_visible(self.pages.agency_details_page.add_advertiser_button)
        self.pages.agency_details_page.add_new_advertiser()
        time.sleep(5)
        self.advertiser_high_precision_lock = 'High_Precision_Advertiser_Lock_' + self.pages.new_advertiser_page.get_random_string(10)
        self.pages.new_advertiser_page.type_organization_name(self.advertiser_high_precision_lock)
        self.pages.new_advertiser_page.type_advertiser_domain('www.yahoo.com')
        self.common_helper.validate_add_on_cost(self.pages.new_advertiser_page, 'add_on_cost_name', 'DXU-ONV-009 - DataXu OneView', 'value')
        self.pages.new_advertiser_page.click_high_precision_policy_checkbox()
        self.pages.new_advertiser_page.click_broad_reach_policy_checkbox()
        self.policy_selection_helper('high')
        self.pages.new_advertiser_page.click_lock_policy_checkbox()
        time.sleep(2)
        self.pages.new_advertiser_page.click_create_advetiser_button()
        time.sleep(5)
        self.pages.advertiser_list_page.page_should_contain(self.message.format(self.advertiser_high_precision_lock))

    @test_case()
    def creation_of_advertiser_with_oneview_policy(self, one_view_advertiser, policy_type):
        self.advertiser_name = ''
        self.pages.agency_list_page.open()
        self.pages.agency_list_page.filter_agency_name_in_filterbox(self.dx_constant.agency_name)
        time.sleep(3)
        self.pages.agency_list_page.click_first_agency()
        self.pages.agency_details_page.wait_till_visible(self.pages.agency_details_page.add_advertiser_button)
        self.pages.agency_details_page.add_new_advertiser()
        self.pages.new_advertiser_page.wait_till_visible(self.pages.new_advertiser_page.submit_button)
        time.sleep(3)
        self.advertiser_name = one_view_advertiser + self.pages.new_advertiser_page.get_random_string(10)
        self.pages.new_advertiser_page.type_organization_name(self.advertiser_name)
        self.pages.new_advertiser_page.type_advertiser_domain('www.yahoo.com')
        self.common_helper.validate_add_on_cost(self.pages.new_advertiser_page, 'add_on_cost_name', 'DXU-ONV-009 - DataXu OneView', 'value')
        self.pages.new_advertiser_page.click_high_precision_policy_checkbox()
        self.pages.new_advertiser_page.click_broad_reach_policy_checkbox()
        self.policy_selection_helper(policy_type)
        time.sleep(3)
        self.pages.new_advertiser_page.click_create_advetiser_button()
        self.pages.advertiser_list_page.wait_till_visible(self.pages.advertiser_list_page.advertiser_list)
        self.pages.advertiser_list_page.page_should_contain(self.message.format(self.advertiser_name))
        return self.advertiser_name

    @test_case()
    def validate_advertiser_with_one_view(self):
        self.advertiser_high_precision = self.creation_of_advertiser_with_oneview_policy('High_Precision_Advertiser_Unlock_', 'high')
        self.pages.advertiser_list_page.type_advertiser_name_in_filterbox(self.advertiser_high_precision)
        time.sleep(3)
        self.pages.advertiser_list_page.click_first_advertiser()
        time.sleep(3)
        self.common_helper.validate_add_on_cost(self.pages.advertiser_details_page, 'add_on_cost_name', 'DXU-ONV-009 - DataXu OneView')
        for i in range(1, 4):
            self.assert_data_in_list(self.pages.advertiser_details_page, ['css selector', self.pages.advertiser_details_page.one_view_section['data_policy_text']['value'].format(i)],
                                     ['Single Device', 'High Precision', 'Broad Reach'])
        self.common_helper.assert_is_element_present(self.pages.advertiser_details_page,self.pages.advertiser_details_page.one_view_section['green_tick'].values())

    @test_case()
    def fill_campaigns_required_fields(self):
        self.pages.create_campaign_page.type_campaign_name(self.dx_constant.test_campaign_name + self.pages.create_campaign_page.get_random_string())
        self.pages.create_campaign_page.enter_start_date(DXDate().date_after_two_days())
        self.pages.create_campaign_page.enter_cpa_goal(self.dx_constant.new_campaign_cpa)
        self.pages.create_campaign_page.enter_budget(self.dx_constant.new_campaign_budget)
        self.pages.create_campaign_page.enter_cpm(self.dx_constant.new_campaign_cpm)
        self.pages.create_campaign_page.click_campaign_objective_distribution()
        self.pages.create_campaign_page.enter_end_date(DXDate().last_date_of_current_month())
        self.pages.create_campaign_page.click_element(self.pages.create_campaign_page.campaign_name)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)

    @test_case()
    def go_to_campaign_list_page(self):
        self.pages.search_page.click_campaign_link()
        self.pages.campaign_list_page.wait_till_visible(self.pages.campaign_list_page.campaign_list_table)
        self.pages.campaign_list_page.click_element(self.pages.campaign_list_page.search_box)
        self.pages.campaign_list_page.wait_till_element_clickable(self.pages.campaign_list_page.new_campaign_button)

    @test_case()
    def create_campaign_popup(self, advertiser_name, channel_type = 'Online', counter=0):
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
            if counter < 5:
                self.create_campaign_popup(advertiser_name, channel_type, counter)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)

    @test_case()
    def campaign_check_oneview_aoc(self):
        self.pages.create_campaign_page.expand_add_on_cost()
        self.pages.create_campaign_page.click_new_aoc()
        self.pages.create_campaign_page.assert_dropdown_options_not_in(self.pages.create_campaign_page.add_on_cost_name, 'DXU-ONV-009 - DataXu OneView')
        self.pages.create_campaign_page.click_on_remove_aoc_button()

    @test_case()
    def fill_fields_fbs_page(self):
        flight_name = self.dx_constant.test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(flight_name)
        self.pages.fbs_page.type_bid_enter(self.dx_constant.flight_bid)
        self.pages.fbs_page.type_budget_enter(self.dx_constant.flight_budget)
        return flight_name

    @test_case()
    def flight_bulk_upload_page(self):
        self.pages.create_flight_page.go_to_link('Bulk Upload Flights')
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections, 60)
        self.pages.upload_flights_page.select_flight_type(self.dx_constant.flight_type_spending)

    @test_case()
    def sys_admin_oneview_validate_one_view_for_advertiser(self):
        self.common_helper.logout_and_login_by_new_user(self.pages.login_page.driver, 'sys_admin_one_view')
        self.validate_one_view_for_advertiser()

    @test_case()
    def sys_admin_oneview_creation_of_advertiser_with_oneview(self):
        self.validate_advertiser_with_one_view()
        self.creation_of_advertiser_with_lock_oneview_policy()
        self.advertiser_single_device = self.creation_of_advertiser_with_oneview_policy('Single_Device_Advertiser_Unlock_', 'single')
        self.advertiser_broad_reach = self.creation_of_advertiser_with_oneview_policy('Broad_Reach_Advertiser_Unlock_', 'broad')
    
    @test_case()
    def validate_campaign_flight_with_one_view_permission(self):
        self.common_helper.logout_and_login_by_new_user(self.pages.login_page.driver, 'campaign_manager_one_view')
        self.go_to_campaign_list_page()
        self.create_campaign_popup(self.advertiser_high_precision)
        self.common_helper.assert_is_element_present(self.pages.create_campaign_page, 'one_view_section_enabled')
        self.campaign_check_oneview_aoc()
        self.fill_campaigns_required_fields()
        self.fill_fields_fbs_page()
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_for_flight_details()
        self.common_helper.assert_is_element_present(self.pages.create_flight_page, 'one_view_section_enabled')
        self.pages.create_flight_page.expand_add_on_cost()
        self.pages.create_flight_page.click_new_aoc()
        self.pages.create_flight_page.check_dropdown_options(['DXU-ONV-009 - DataXu OneView'], self.pages.create_flight_page.add_on_cost_name)
        self.pages.create_flight_page.click_on_aoc_remove_button()
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_for_loading()
        self.flight_bulk_upload_page()
        self.common_helper.assert_is_element_present(self.pages.upload_flights_page, 'one_view_section')

    @test_case()
    def oneview_section_status(self, page_object, flag):
        for policy in page_object.one_view_policies_disabled:
            self.common_helper.assert_is_element_present(page_object, policy, criteria=flag)

    @test_case()
    def oneview_editable_for_campaign_flight(self):
        self.go_to_campaign_list_page()
        self.create_campaign_popup(self.advertiser_high_precision)
        self.oneview_section_status(self.pages.create_campaign_page, False)
        self.fill_campaigns_required_fields()
        self.fill_fields_fbs_page()
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_for_flight_details()
        self.oneview_section_status(self.pages.create_flight_page, False)
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_for_loading()
        self.flight_bulk_upload_page()
        for policy in self.pages.upload_flights_page.one_view_policies_flight_upload:
            self.common_helper.assert_is_element_present(self.pages.upload_flights_page, policy)

    @test_case()
    def oneview_not_editable_for_campaign_flight(self):
        self.go_to_campaign_list_page()
        self.create_campaign_popup(self.advertiser_high_precision_lock)
        self.oneview_section_status(self.pages.create_campaign_page, True)
        self.fill_campaigns_required_fields()
        self.fill_fields_fbs_page()
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_for_flight_details()
        self.oneview_section_status(self.pages.create_flight_page, True)
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_for_loading()
        self.flight_bulk_upload_page()
        self.common_helper.assert_is_element_present(self.pages.upload_flights_page, self.pages.upload_flights_page.one_view_policies_flight_upload[0])
        for policy in self.pages.upload_flights_page.one_view_policies_flight_upload[1:]:
            self.common_helper.assert_is_element_present(self.pages.upload_flights_page, policy, criteria=False)

    @test_case()
    def updating_oneview_aoc_as_per_policy(self):
        self.go_to_campaign_list_page()
        self.create_campaign_popup(self.advertiser_high_precision)
        self.fill_campaigns_required_fields()
        self.fill_fields_fbs_page()
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_for_flight_details()
        for policy in self.pages.create_flight_page.one_view_policies_enabled[:2]:
            self.pages.create_flight_page.click_element(getattr(self.pages.create_flight_page, policy))
            time.sleep(3)
            assert self.pages.create_flight_page.is_element_present(self.pages.create_flight_page.oneview_aoc_name)
        self.pages.create_flight_page.click_single_device()
        time.sleep(3)
        assert not self.pages.create_flight_page.is_element_present(self.pages.create_flight_page.oneview_aoc_name)

    @test_case()
    def oneview_policy_warning(self, page_object):
        page_object.click_single_device()
        time.sleep(2)
        assert not page_object.is_element_present(page_object.oneview_warning_popup)
        for policy in page_object.single_device_warning:
            page_object.click_element(getattr(page_object, policy))
            time.sleep(2)
            assert page_object.is_element_present(page_object.oneview_warning_popup)
            page_object.click_oneview_popup_cancel()
        page_object.click_high_precision()
        time.sleep(2)
        page_object.click_oneview_popup_ok()
        time.sleep(2)
        page_object.click_broad_reach()
        time.sleep(2)
        assert not page_object.find_element(page_object.oneview_warning_popup).is_displayed()
        time.sleep(2)
        for policy in page_object.broad_reach_warning:
            page_object.click_element(getattr(page_object, policy))
            time.sleep(2)
            assert not page_object.find_element(page_object.oneview_warning_popup).is_displayed()
            page_object.click_broad_reach()
            time.sleep(2)
            if page_object.find_element(page_object.oneview_warning_popup).is_displayed():
                  page_object.click_oneview_popup_ok()
                  time.sleep(2)
        page_object.click_high_precision()

    @test_case()
    def oneview_policy_confirmation_popup(self):
        self.go_to_campaign_list_page()
        self.create_campaign_popup(self.advertiser_high_precision)
        self.oneview_policy_warning(self.pages.create_campaign_page)
        self.fill_campaigns_required_fields()
        self.fill_fields_fbs_page()
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_for_flight_details()
        self.oneview_policy_warning(self.pages.create_flight_page)

    @test_case()
    def updating_policy_for_campaign_flight(self):
        self.go_to_campaign_list_page()
        self.create_campaign_popup(self.advertiser_high_precision)
        self.fill_campaigns_required_fields()
        flight1 =  self.fill_fields_fbs_page()        
        self.pages.fbs_page.click_on_add_flight()
        flight2 = self.fill_fields_fbs_page()
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.high_precision_enabled)
        self.common_helper.assert_is_selected(self.pages.create_flight_page, self.pages.create_flight_page.high_precision_enabled)
        self.pages.create_flight_page.click_save_and_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.broad_reach_enabled)
        self.pages.create_flight_page.click_broad_reach()
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_for_loading()
        self.pages.campaign_show_page.edit()
        self.pages.create_campaign_page.wait_till_visible(self.pages.create_campaign_page.single_device_enabled)
        self.pages.create_campaign_page.click_single_device()
        self.pages.create_campaign_page.submit()
        self.pages.campaign_show_page.wait_for_loading()
        self.pages.campaign_show_page.go_to_link(flight1)
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain('Single Device')
        self.pages.flight_show_page.click_campaign_link()
        self.pages.campaign_show_page.wait_for_loading()
        self.pages.campaign_show_page.go_to_link(flight2)
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain('Broad Reach')

    @test_case()
    def oneview_policy_workflow(self, policy_advertiser, policy_name):
        self.go_to_campaign_list_page()
        self.create_campaign_popup(policy_advertiser)
        self.common_helper.assert_is_selected(self.pages.create_campaign_page, getattr(self.pages.create_campaign_page, policy_name))
        self.campaign_check_oneview_aoc()
        self.pages.create_campaign_page.page_should_not_contain('DXU-ONV-009 - DataXu OneView')
        self.fill_campaigns_required_fields()
        self.fill_fields_fbs_page()
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_for_flight_details()
        self.common_helper.assert_is_selected(self.pages.create_flight_page, getattr(self.pages.create_flight_page, policy_name))
        if self.pages.create_flight_page.find_element(self.pages.create_flight_page.single_device_enabled).is_selected():
            self.pages.create_flight_page.expand_add_on_cost()
            self.pages.create_flight_page.page_should_not_contain('DXU-ONV-009 - DataXu OneView')
        else:
            self.pages.create_flight_page.page_should_contain('DXU-ONV-009 - DataXu OneView')
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_for_loading()
        self.flight_bulk_upload_page()
        for policy in self.pages.upload_flights_page.one_view_policies_flight_upload:
            self.common_helper.assert_is_element_present(self.pages.upload_flights_page, policy)
            
    @test_case()
    def flight_upload_policy_workflow(self, flight_speadsheet, policy1, policy2):
        self.common_helper.process_flight_file_with_name_and_date(flight_speadsheet, 'Online')
        self.pages.upload_flights_page.select_file(os.path.dirname(__file__)+ '/../../../data/flights_upload/' + flight_speadsheet + '.csv')
        self.pages.upload_flights_page.click_upload_file()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.flight_submit, 120)
        self.pages.upload_flights_page.click_flights_submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row, 180)
        self.pages.fbs_page.page_should_contain('All flights have been saved successfully.')
        self.pages.fbs_page.click_on_save_exit()
        self.pages.campaign_show_page.wait_for_loading()
        oneview_flight_name = self.common_helper.get_flights_name_from_file(flight_speadsheet)
        self.pages.campaign_show_page.go_to_link(oneview_flight_name[0])
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain(policy1)
        self.pages.flight_show_page.click_campaign_link()
        self.pages.campaign_show_page.wait_for_loading()
        self.pages.campaign_show_page.go_to_link(oneview_flight_name[1])
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain(policy1)
        self.pages.flight_show_page.click_campaign_link()
        self.pages.campaign_show_page.wait_for_loading()
        self.pages.campaign_show_page.go_to_link(oneview_flight_name[2])
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain(policy2)

    @test_case()
    def single_device_policy_workflow(self):
        self.oneview_policy_workflow(self.advertiser_single_device, 'single_device_enabled')
        self.flight_upload_policy_workflow('Single_Device_Flights', 'Single Device', 'High Precision')

    @test_case()
    def high_precision_policy_workflow(self):
        self.oneview_policy_workflow(self.advertiser_high_precision, 'high_precision_enabled')
        self.flight_upload_policy_workflow('High_Precision_Flights', 'High Precision', 'Single Device')

    @test_case()
    def broad_reach_policy_workflow(self):
        self.oneview_policy_workflow(self.advertiser_broad_reach, 'broad_reach_enabled')
        self.flight_upload_policy_workflow('Broad_Reach_Flights', 'Broad Reach', 'High Precision')
