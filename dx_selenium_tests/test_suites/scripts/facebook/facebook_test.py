#coding: utf-8
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from lib.dx_date import DXDate
from common_helpers.common_helpers import CommonHelper
from flight_helper import FlightHelper
import time
import os
import csv

class FacebookTest(DXTest):

    @test_case()
    def login_as_dx_admin(self):
        self.common_helper = CommonHelper()
        self.dx_date = DXDate()
        self.setup()

    @test_case()
    def facebook_exchange_authentication_workflow(self):
        expected_facebook_popup_title = 'Facebook RTB Seat Configuration'
        expected_authenticated_account = 'DataXu_Test'
        self.pages.admin_page.click_on_agency_group_link()
        self.pages.agency_group_list_page.wait_till_visible(self.pages.agency_group_list_page.agency_group_list_table)
        self.pages.agency_group_list_page.search_agency_group(self.dx_constant.agency_group_name)
        self.pages.agency_group_list_page.click_first_edit_icon()
        self.pages.agency_group_edit_page.wait_till_visible(self.pages.agency_group_edit_page.facebook_rtb_edit_icon)
        self.pages.agency_group_edit_page.click_on_facebook_rtb_edit_icon()
        actual_facebook_popup_title = self.pages.agency_group_edit_page.get_attribute_value(self.pages.agency_group_edit_page.facebook_popup_title)
        assert expected_facebook_popup_title in actual_facebook_popup_title
        self.pages.agency_group_edit_page.click_on_own_facebook_seat_radio_button()
        self.pages.agency_group_edit_page.enter_bussiness_id(self.pages.agency_group_edit_page.agency_group_fb_bussiness_id)
        self.pages.agency_group_edit_page.enter_access_token(self.pages.agency_group_edit_page.agency_group_fb_access_token)
        self.pages.agency_group_edit_page.click_on_authenticate_button()
        self.pages.agency_group_edit_page.wait_till_visible(self.pages.agency_group_edit_page.facebook_authentication_save_button)
        actual_authenticated_account = self.pages.agency_group_edit_page.get_attribute_value(self.pages.agency_group_edit_page.facebook_authenticated_user)
        assert expected_authenticated_account in actual_authenticated_account
        self.pages.agency_group_edit_page.click_on_facebook_authentication_save_button()
        self.pages.agency_group_edit_page.click_on_save_agency_group_button()
        self.pages.agency_group_details_page.page_should_contain(self.pages.agency_group_details_page.success_message.format(self.dx_constant.agency_group_name))
        self.pages.agency_group_details_page.wait_till_visible(self.pages.agency_group_details_page.details_div)
        self.pages.agency_group_details_page.go_to_link(self.dx_constant.agency_name)
        self.pages.agency_details_page.wait_till_visible(self.pages.agency_details_page.details_section)
        expected_agency_facebook_seat = "Inheriting Seat"
        actual_agency_facebook_seat = self.pages.agency_details_page.get_attribute_value(self.pages.agency_details_page.agency_facebook_seat_value)
        assert expected_agency_facebook_seat in actual_agency_facebook_seat
        self.pages.agency_details_page.go_to_link(self.dx_constant.advertiser_name)
        self.pages.advertiser_details_page.wait_till_visible(self.pages.advertiser_details_page.details_section)
        self.pages.advertiser_details_page.click_edit_details()
        self.pages.advertiser_edit_page.wait_till_visible(self.pages.advertiser_edit_page.facebook_section)
        self.pages.advertiser_edit_page.click_on_facebook_rtb_edit_icon()
        self.pages.advertiser_edit_page.click_on_existing_acc_id_radio_button()
        self.pages.advertiser_edit_page.enter_acc_id(self.pages.advertiser_edit_page.facebook_account_id)
        self.pages.advertiser_edit_page.click_on_authenticate_button()
        self.pages.advertiser_edit_page.wait_till_visible(self.pages.advertiser_edit_page.facebook_authentication_save_button)
        self.pages.advertiser_edit_page.click_on_facebook_authentication_save_button()
        self.pages.advertiser_edit_page.enter_facebook_page_id_textbox(self.pages.advertiser_edit_page.facebook_page_id)
        self.pages.advertiser_edit_page.click_facebook_add_page_button()
        self.pages.advertiser_edit_page.page_should_contain("Gathering page details from Facebook...")
        self.pages.advertiser_edit_page.wait_till_visible(self.pages.advertiser_edit_page.facebook_resync_link)
        self.pages.advertiser_edit_page.click_on_save_advertiser_button()
        self.pages.advertiser_details_page.wait_till_visible(self.pages.advertiser_details_page.edit_details_button)
        self.pages.advertiser_details_page.page_should_contain(self.pages.advertiser_details_page.advertiser_update_success_message.format(self.dx_constant.advertiser_name))

    @test_case()
    def functionality_of_resync_link(self):
        self.pages.advertiser_details_page.click_edit_details()
        self.pages.advertiser_edit_page.wait_till_visible(self.pages.advertiser_edit_page.facebook_section)
        self.pages.advertiser_edit_page.click_on_facebook_resync_link()
        self.pages.advertiser_edit_page.page_should_contain("Gathering page details from Facebook...")
        self.pages.advertiser_edit_page.wait_till_visible(self.pages.advertiser_edit_page.facebook_resync_link)
        assert self.pages.advertiser_edit_page.is_element_present(self.pages.advertiser_edit_page.facebook_resync_link)

    @test_case()
    def check_authenticated_advertiser_facebook_details(self):
        expected_advertiser_facebook_seat_status = "Using Own Seat"
        actual_advertiser_facebook_seat_status = self.pages.advertiser_edit_page.get_attribute_value(self.pages.advertiser_edit_page.advertiser_facebook_seat_status)
        assert expected_advertiser_facebook_seat_status in actual_advertiser_facebook_seat_status
        self.pages.advertiser_edit_page.click_on_facebook_rtb_edit_icon()
        expected_authenticated_email = "fbx_advertiser_01@dataxu.com"
        actual_authenticated_email = self.pages.advertiser_edit_page.get_attribute_value(self.pages.advertiser_edit_page.authenticated_email)
        assert expected_authenticated_email in actual_authenticated_email
        self.pages.advertiser_edit_page.click_facebook_popup_close_button()
        self.pages.advertiser_edit_page.click_on_save_advertiser_button()
        self.pages.advertiser_details_page.wait_till_visible(self.pages.advertiser_details_page.edit_details_button)
        expected_advertiser_facebook_seat_value = self.pages.advertiser_edit_page.facebook_account_id
        actual_advertiser_facebook_seat_value = self.pages.advertiser_details_page.get_attribute_value(self.pages.advertiser_details_page.advertiser_facebook_seat_value)
        assert expected_advertiser_facebook_seat_value in actual_advertiser_facebook_seat_value

    @test_case()
    def check_authenticated_agency_group_facebook_details(self):
        self.pages.advertiser_details_page.go_to_link(self.dx_constant.agency_group_name)
        self.pages.agency_group_details_page.wait_till_visible(self.pages.agency_group_details_page.edit_details)
        self.pages.agency_group_details_page.click_edit_details()
        self.pages.agency_group_edit_page.wait_till_visible(self.pages.agency_group_edit_page.facebook_rtb_edit_icon)
        expected_agency_group_facebook_seat_status = "Using Own Seat"
        actual_agency_group_facebook_seat_status = self.pages.agency_group_edit_page.get_attribute_value(self.pages.agency_group_edit_page.agency_group_facebook_seat_value)
        assert expected_agency_group_facebook_seat_status in actual_agency_group_facebook_seat_status
        self.pages.agency_group_edit_page.click_on_facebook_rtb_edit_icon()
        self.common_helper.assert_is_selected(self.pages.agency_group_edit_page, self.pages.agency_group_edit_page.own_facebook_seat_radio_button)
        for element in self.pages.agency_group_edit_page.facebook_popup_elements:
            assert self.pages.agency_group_edit_page.is_element_present(getattr(self.pages.agency_group_edit_page, element))
        self.pages.agency_group_edit_page.click_facebook_popup_close_button()
        self.pages.agency_group_edit_page.click_on_save_agency_group_button()
        self.pages.agency_group_details_page.wait_till_visible(self.pages.agency_group_details_page.details_div)
        expected_facebook_seat_id_value = self.pages.agency_group_edit_page.agency_group_fb_bussiness_id
        actual_facebook_seat_id_value = self.pages.agency_group_details_page.get_attribute_value(self.pages.agency_group_details_page.facebook_seat_id_value)
        assert expected_facebook_seat_id_value in actual_facebook_seat_id_value

    @test_case()
    def availability_of_fbx_and_ppa_product_feature(self):
        self.pages.admin_page.go_to_link('Admin')
        self.pages.admin_page.wait_till_visible(self.pages.admin_page.product_feature_link)
        self.pages.admin_page.click_on_product_feature_link()
        for content in ['Facebook Exchange', 'Facebook Page Post Ads (PPA)']:
            self.pages.admin_page.page_should_contain(content)

    @test_case()
    def go_to_campaign_list_page(self):
        self.pages.search_page.click_campaign_link()
        self.pages.campaign_list_page.wait_till_visible(self.pages.campaign_list_page.campaign_list_table)
        self.pages.campaign_list_page.click_element(self.pages.campaign_list_page.search_box)
        self.pages.campaign_list_page.wait_till_element_clickable(self.pages.campaign_list_page.new_campaign_button)

    @test_case()
    def go_to_creative_list_page(self):
        self.pages.search_page.click_creative_link()
        self.pages.search_page.accept_alert()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.creative_table)
        self.pages.creative_list_page.click_element(self.pages.creative_list_page.filters)

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
    def fill_campaigns_required_fields(self, campaign_type='Online'):
        self.pages.create_campaign_page.type_campaign_name("Facebook_Campaign_" + self.pages.create_campaign_page.get_random_string())
        self.pages.create_campaign_page.enter_start_date(self.dx_date.date_after_two_days())
        self.pages.create_campaign_page.enter_cpa_goal(self.dx_constant.new_campaign_cpa)
        self.pages.create_campaign_page.enter_budget(self.dx_constant.new_campaign_budget)
        self.pages.create_campaign_page.enter_cpm(self.dx_constant.new_campaign_cpm)
        if campaign_type == 'Online':
            self.pages.create_campaign_page.select_activity_pixel(1)
            self.pages.create_campaign_page.select_pixel_type('Learning Pixel')
        if campaign_type in ['Mobile', 'Video']:
            self.pages.create_campaign_page.click_campaign_objective_distribution()
        self.pages.create_campaign_page.enter_end_date(self.dx_date.last_date_of_current_month())
        self.pages.create_campaign_page.click_element(self.pages.create_campaign_page.campaign_name)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)

    @test_case()
    def fill_fields_fbs_page(self):
        flight_name = self.dx_constant.test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(flight_name)
        self.pages.fbs_page.type_bid_enter(self.dx_constant.flight_bid)
        self.pages.fbs_page.type_budget_enter(self.dx_constant.flight_budget)
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_for_flight_details()
        return flight_name

    @test_case()
    def check_flight_type_dropdown_options(self, expected_flight_type, campaign_type='Online'):
        elements = self.pages.fbs_page.find_elements(self.pages.fbs_page.flight_type_dropdwon_options)
        actual_option_list = []
        for element in elements:
            actual_option_list.append(element.get_attribute('innerHTML'))
        if campaign_type == "Online":
            assert expected_flight_type in actual_option_list
        if campaign_type in ['Mobile', 'Video']:
            assert not expected_flight_type in actual_option_list

    @test_case()
    def set_campaign_objective_and_verify_flight_type(self, campaign_objective):
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.edit()
        self.pages.create_campaign_page.wait_till_visible(self.pages.create_campaign_page.create_campaign_button, 40)
        if campaign_objective == "Distribution":
            self.pages.create_campaign_page.click_campaign_objective_distribution()
        if campaign_objective == "CTR":
            self.pages.create_campaign_page.click_campaign_objective_ctr()
            self.pages.create_campaign_page.enter_goal_ctr('10')
        self.pages.create_campaign_page.submit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.add_flights()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row, 40)
        time.sleep(2)
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flight_type_listbox['link'].values())
        self.check_flight_type_dropdown_options("FBX")

    @test_case()
    def fbx_flight_type_and_algorithm_for_performance_distribution_objective(self):
        self.common_helper.logout_and_login_by_new_user(self.pages.login_page.driver, 'campaign_manager')
        self.go_to_campaign_list_page()
        self.create_campaign_popup(self.dx_constant.advertiser_name)
        self.fill_campaigns_required_fields()
        expected_flight_type = "FBX"
        self.check_flight_type_dropdown_options(expected_flight_type)
        self.pages.fbs_page.select_flight_type(expected_flight_type)
        time.sleep(1)
        expected_algorithm = 'Facebook Flat Bid - DX-001'
        actual_algorithm_fbs = self.pages.fbs_page.get_attribute_value(self.pages.fbs_page.selected_decision_algorithm)
        assert expected_algorithm == actual_algorithm_fbs
        self.flight_name = self.fill_fields_fbs_page()
        for content in [expected_flight_type, expected_algorithm]:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def preferred_placement_options_for_fbx_flight(self):
        self.pages.create_flight_page.check_dropdown_options(['Right Hand Side', 'News Feed'], self.pages.create_flight_page.preferred_placement)
        self.pages.create_flight_page.click_save_exit()

    @test_case()
    def flight_type_for_distribution_objective(self):
        self.set_campaign_objective_and_verify_flight_type("Distribution")

    @test_case()
    def flight_type_for_ctr_objective(self):
        self.pages.fbs_page.click_on_campaign_link()
        self.set_campaign_objective_and_verify_flight_type("CTR")

    @test_case()
    def campaign_id_and_flight_details_for_facebook_flight(self):
        self.pages.fbs_page.click_on_campaign_link()
        self.pages.campaign_show_page.wait_for_loading()
        self.pages.campaign_show_page.go_to_link(self.flight_name)
        self.pages.flight_show_page.wait_for_flight_basics()
        for content in ['FBX', 'Facebook Flat Bid - DX-001']:
            self.pages.flight_show_page.page_should_contain(content)
        assert self.pages.flight_show_page.get_attribute_value(self.pages.flight_show_page.fb_campaign_id).isdigit()

    @test_case()
    def verify_inventory_and_viewability_section(self, page_object):
        for section in ['Inventory Suppliers', 'Private Inventory', 'Viewability']:
            page_object.page_should_not_contain(section)

    @test_case()
    def inventory_and_viewability_section_for_fbx_flight(self):
        self.verify_inventory_and_viewability_section(self.pages.flight_show_page)
        self.pages.flight_show_page.edit()
        self.pages.create_flight_page.wait_for_flight_details()
        self.verify_inventory_and_viewability_section(self.pages.create_flight_page)

    @test_case()
    def upload_fbx_flight_file(self):
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections, 60)
        self.common_helper.process_flight_file_with_name_and_date('facebook_flights', 'Online')
        self.pages.upload_flights_page.select_file(os.path.dirname(__file__)+ '/../../../data/flights_upload/facebook_flights.csv')
        self.pages.upload_flights_page.click_upload_file()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.flight_submit, 150)

    @test_case()
    def upload_fbx_flight_with_rhs_newsfeed(self):
        self.pages.create_flight_page.click_on_campaign_name_link()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.bulk_upload_flights_buttons)
        self.pages.campaign_show_page.bulk_upload_flights()
        self.upload_fbx_flight_file()
        self.pages.upload_flights_page.click_flights_submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row, 180)
        self.pages.fbs_page.page_should_contain('All flights have been saved successfully.')
        self.pages.fbs_page.click_on_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        facebook_flight_name = []
        facebook_flight_name = self.common_helper.get_flights_name_from_file('facebook_flights')
        self.pages.campaign_show_page.go_to_link(facebook_flight_name[0])
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain('Right Hand Side')
        self.pages.flight_show_page.click_campaign_link()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.go_to_link(facebook_flight_name[1])
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain('News Feed')

    @test_case()
    def ensure_fbx_flight_type(self, campaign_type):
        self.go_to_campaign_list_page()
        self.create_campaign_popup(self.dx_constant.advertiser_name, campaign_type)
        self.fill_campaigns_required_fields(campaign_type)
        self.check_flight_type_dropdown_options('FBX', campaign_type)

    @test_case()
    def fbx_flight_type_for_mobile_campaign(self):
        self.ensure_fbx_flight_type("Mobile")

    @test_case()
    def fbx_flight_type_for_video_campaign(self):
        self.ensure_fbx_flight_type("Video")

    @test_case()
    def fbx_creative_edit_page_contents(self):
        self.go_to_creative_list_page()
        self.pages.creative_list_page.click_new_creatives()
        self.pages.bulk_edit_creative_page.wait_for_creative_forms()
        self.pages.bulk_edit_creative_page.go_to_link('Detailed Edit')
        self.pages.detailed_edit_creatives.wait_for_detailed_form()
        self.pages.detailed_edit_creatives.select_first_ad_type('Facebook')
        time.sleep(2)
        for content in ['Facebook Standard Size', 'Ad Name']:
            self.pages.detailed_edit_creatives.page_should_contain(content)
        for element in self.pages.detailed_edit_creatives.fb_creative_detail_edit_page_element:
            assert self.pages.detailed_edit_creatives.is_element_present(getattr(self.pages.detailed_edit_creatives, element))
        for key, value in { 'first_ad_type':'Facebook', 'first_ad_feature':'Facebook Standard', 'first_tag_type':'Facebook' }.iteritems():
            assert value == self.pages.detailed_edit_creatives.get_dropdown_selected_value(getattr(self.pages.detailed_edit_creatives, key))
 
    @test_case()
    def availability_of_external_id(self):
        assert self.pages.detailed_edit_creatives.is_element_present(self.pages.detailed_edit_creatives.first_new_external_id)
        self.pages.detailed_edit_creatives.click_first_external_id()
        for element in self.pages.detailed_edit_creatives.external_id_row_elements:
            assert self.pages.detailed_edit_creatives.is_element_present(getattr(self.pages.detailed_edit_creatives, element))
        assert 'DFA' == self.pages.detailed_edit_creatives.get_dropdown_selected_value(self.pages.detailed_edit_creatives.first_external_id_source)
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.external_id_source_dropdown_options,
                                                               self.pages.detailed_edit_creatives.first_external_id_source)
 
    @test_case()
    def set_fbx_creative_required_fields_and_validate(self, creative_name, destination_url):
        self.pages.detailed_edit_creatives.input_first_creative_name(creative_name)
        self.pages.detailed_edit_creatives.input_first_concept(self.pages.detailed_edit_creatives.get_random_string())
        self.pages.detailed_edit_creatives.enter_fb_destination_url(destination_url)
        self.pages.detailed_edit_creatives.fill_fbx_creative_title_field('title-' + self.pages.detailed_edit_creatives.get_random_string())
        self.pages.detailed_edit_creatives.fill_fbx_creative_body_field('body-' + self.pages.detailed_edit_creatives.get_random_string())
        self.pages.detailed_edit_creatives.click_validate_first()

    @test_case()
    def validate_fbx_creative_name_destination_url_field(self):
        self.set_fbx_creative_required_fields_and_validate(self.pages.detailed_edit_creatives.get_random_string(40), 'https://www.dataxu.com')
        self.pages.detailed_edit_creatives.page_should_contain('Name is too long (maximum is 35 characters)')

    @test_case()
    def destination_url_field_without_protocol(self):
        self.set_fbx_creative_required_fields_and_validate(self.pages.detailed_edit_creatives.get_random_string(30), 'www.dataxu.com')
        self.pages.detailed_edit_creatives.page_should_contain('Facebook Destination Url is not a valid URL')

    @test_case()
    def functionality_of_validate_button(self):
        self.set_fbx_creative_required_fields_and_validate(self.pages.detailed_edit_creatives.get_random_string(20), 'http://www.dataxu.com')
        self.pages.detailed_edit_creatives.page_should_not_contain('Name is too long (maximum is 35 characters)')
        self.pages.detailed_edit_creatives.page_should_not_contain('Facebook Destination Url is not a valid URL')

    @test_case()
    def functionality_of_cancel_button(self):
        self.pages.detailed_edit_creatives.click_cancel_first()
        self.pages.detailed_edit_creatives.accept_alert()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.creative_table)
        assert self.pages.creative_list_page.is_element_present(self.pages.creative_list_page.new_creative_button)

    @test_case()
    def fbx_flight_type_for_non_permission_user_organization(self):
        self.common_helper.logout_and_login_by_new_user(self.pages.login_page.driver, 'campaign_manager_one_view')
        self.go_to_campaign_list_page()
        self.create_campaign_popup(self.dx_constant.advertiser_name)
        self.fill_campaigns_required_fields()
        elements = self.pages.fbs_page.find_elements(self.pages.fbs_page.flight_type_dropdwon_options)
        actual_option_list = []
        for element in elements:
            actual_option_list.append(element.get_attribute('innerHTML'))
        assert not 'FBX' in actual_option_list

    @test_case()
    def fbx_flight_upload_for_non_permission_user_organization(self):
        self.pages.fbs_page.click_on_upload_flights_button()
        self.upload_fbx_flight_file()
        self.pages.upload_flights_page.page_should_contain('The following 2 flights have errors:')
