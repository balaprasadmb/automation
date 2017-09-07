import uuid
import random
import os
import time
import csv
from selenium.webdriver.common.keys import Keys
from dx_test.dx_test import DXTest
from configs.dx_constant import DXConstant
from lib.dx_date import DXDate
from lib.gui_tests import test_case
from campaign_test_helpers.campaign_test_helper import CampaignTestHelper
from common_helpers.common_helpers import CommonHelper

class OmniChannelTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.common_helper = CommonHelper()
        self.setup(DXConstant().user_by_role['campaign_manager'])

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
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button, 40)

    @test_case()
    def fill_create_campaign_fields(self, campaign_attributes):
        self.pages.create_campaign_page.fill_fields(campaign_attributes)

    @test_case()
    def go_to_campaign_edit(self):
        if self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.reports_link):
            time.sleep(5)
            self.pages.create_campaign_page.go_to_link('Edit')
            self.pages.create_campaign_page.wait_for_campaign_details()

    @test_case()
    def verify_contents_campaign_page(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Omni-Channel')
        self.pages.create_campaign_page.wait_for_campaign_details()
        elements = ['campaign_name', 'campaign_start_date', 'campaign_end_date', 'insertion_order','cost_model',
                    'cpa_goal', 'order_budget', 'campaign_cpm', 'campaign_cogs', 'campaign_margin',
                    'campaign_objective_performance', 'campaign_objective_ctr', 'campaign_objective_distribution',
                    'campaign_objective_ad_views', 'devices_available', 'move_selected_devices',
                    'remove_selected_devices', 'move_all_selected_devices', 'remove_all_selected_devices',
                    'devices_selected', 'new_tactics', 'tactic_name_default', 'new_add_on_cost', 'create_campaign_button' ]
        for element in elements:
            assert self.pages.create_campaign_page.is_element_present(getattr(self.pages.create_campaign_page, element))
        contents = ['Add new campaign', 'Advertiser', 'Agency', 'Campaign Type', 'Currency', 'Cost model',
                   'CPA', 'Budget', 'CPM', 'COGS', 'Margin', 'Maximize Performance and Distribution',
                   'Attribution Model', 'Maximize CTR', 'Maximize Distribution', 'Maximize Completed Ad Views',
                   'Device Types', 'Impression Caps', 'Tactics', 'Add On Costs', 'External IDs', 'Language Targeting',
                   'Geographic Targeting', 'Brand Safety', 'Blacklist' ]
        for content in contents:
            self.pages.create_campaign_page.page_should_contain(content)

    @test_case()
    def verify_defaults_in_device_types(self):
        device_types = [ 'SmartPhone', 'Tablet', 'Desktop/Laptop']
        self.pages.create_campaign_page.check_dropdown_options(device_types, self.pages.create_campaign_page.devices_selected)

    @test_case()
    def verify_option_in_device_types(self):
        self.device_types = ['Connected TV', 'Game Console', 'Other', 'SmartPhone', 'Tablet', 'Desktop/Laptop']
        self.pages.create_campaign_page.click_remove_all()
        time.sleep(10)
        self.pages.create_campaign_page.check_dropdown_options(self.device_types, self.pages.create_campaign_page.devices_available)

    @test_case()
    def working_of_buttons_in_device_types(self):
        self.pages.create_campaign_page.select_available_device_types('Game Console')
        self.pages.create_campaign_page.click_move_selected()
        time.sleep(3)
        self.pages.create_campaign_page.check_dropdown_options(['Game Console'], self.pages.create_campaign_page.devices_selected)
        self.pages.create_campaign_page.click_move_all()
        time.sleep(5)
        self.pages.create_campaign_page.check_dropdown_options(self.device_types, self.pages.create_campaign_page.devices_selected)
        self.pages.create_campaign_page.select_selected_device_types('Game Console')
        self.pages.create_campaign_page.click_remove_selected()
        time.sleep(3)
        self.pages.create_campaign_page.check_dropdown_options(['Game Console'], self.pages.create_campaign_page.devices_available)
        self.pages.create_campaign_page.click_remove_all()
        time.sleep(5)
        self.pages.create_campaign_page.check_dropdown_options(self.device_types, self.pages.create_campaign_page.devices_available)

    @test_case()
    def campaign_with_omni_channel(self):
        if self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.campaign_name):
            self.campaign_attributes = CampaignTestHelper().get_campaign_with_ad_views(self.pages.create_campaign_page.campaign_values)
            self.pages.create_campaign_page.click_move_all()
            self.pages.create_campaign_page = CampaignTestHelper().set_campaign_attributes(self.pages.create_campaign_page, self.campaign_attributes)
            self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row, 40)
        self.pages.fbs_page.go_to_link(self.pages.create_campaign_page.campaign_attributes['campaign_name'])
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.go_to_campaign_edit()
        self.pages.campaign_edit_page.page_should_contain('Omni-Channel')

    @test_case()
    def verify_selected_device_types(self):
        self.pages.campaign_edit_page.check_dropdown_options(self.device_types, self.pages.create_campaign_page.devices_selected)

    @test_case()
    def device_targeting_should_disabled(self):
        if self.pages.campaign_edit_page.is_element_present(self.pages.campaign_edit_page.campaign_name):
            self.pages.campaign_edit_page.submit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.go_to_link('Add Flights')
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        flight_name = DXConstant().test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(flight_name)
        self.pages.fbs_page.type_bid('3')
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)
        self.pages.create_flight_page.expand_device_types()
        time.sleep(5)
        self.pages.create_flight_page.click_override_device_types()
        time.sleep(5)
        self.pages.create_flight_page.click_remove_all()
        self.pages.create_flight_page.wait_till_visible(['css', '.device_type_errors'])
        self.pages.create_flight_page.page_should_contain(self.pages.create_flight_page.device_targeting_message)

    @test_case()
    def campaign_with_device_types(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Omni-Channel')
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_ad_views(self.pages.create_campaign_page.campaign_values)
        self.pages.create_campaign_page.click_remove_all()
        self.pages.create_campaign_page.select_available_device_types('SmartPhone')
        self.pages.create_campaign_page.click_move_selected()
        self.pages.create_campaign_page = CampaignTestHelper().set_campaign_attributes(self.pages.create_campaign_page, self.campaign_attributes)
        self.fill_create_campaign_fields(self.pages.create_campaign_page.campaign_attributes)
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        self.flight_name = DXConstant().test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(self.flight_name)
        self.pages.fbs_page.type_bid('3')
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)
        self.pages.create_flight_page.expand_device_types()
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.go_to_link(self.flight_name)
        self.pages.flight_show_page.wait_for_flight_basics()
        for content in ['Device Types', 'inherited from campaign:', 'SmartPhone']:
            self.pages.flight_show_page.page_should_contain(content)

    def fill_campaigns_required_fields(self):
        self.campaign = DXConstant().test_campaign_name + str(uuid.uuid4())
        self.pages.create_campaign_page.type_campaign_name(self.campaign)
        self.pages.create_campaign_page.enter_start_date(DXDate().date_after_two_days())
        self.pages.create_campaign_page.enter_cpa_goal(DXConstant().new_campaign_cpa)
        self.pages.create_campaign_page.enter_budget(DXConstant().new_campaign_budget)
        self.pages.create_campaign_page.enter_cpm(DXConstant().new_campaign_cpm)
        self.pages.create_campaign_page.click_campaign_objective_distribution()
        self.pages.create_campaign_page.enter_end_date(DXDate().last_date_of_current_month())
        self.pages.create_campaign_page.click_element(self.pages.create_campaign_page.campaign_name)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        return self.campaign

    @test_case()
    def verify_flights_type_for_omni_channel(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Omni-Channel')
        self.fill_campaigns_required_fields()
        flight_types = self.pages.fbs_page.get_list_items(self.pages.fbs_page.flight_type)
        assert 'Facebook' not in flight_types

    @test_case()
    def verify_media_types(self):
        media_types = self.pages.fbs_page.get_list_items(self.pages.fbs_page.media_type)
        for media_type in ['Banner', 'Video']:
            assert media_type in media_types

    @test_case()
    def verify_flights_page_for_omni_channel(self):
        if self.pages.fbs_page.is_element_present(self.pages.fbs_page.flights_row):
            self.flight = DXConstant().test_flight_name + self.pages.fbs_page.get_random_string()
            self.pages.fbs_page.fill_description(self.flight)
            self.pages.fbs_page.type_bid_normal(DXConstant().flight_bid)
            self.pages.fbs_page.click_on_save_continue()
            self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)
        elements = [
                    'edit_flight_name', 'flight_tactic', 'algorithm', 'start_date', 'end_date', 'spent',
                    'default_bid_usd', 'budget_usd', 'alloc', 'avail_inventory',
                    'move_select_inventory', 'move_all_inventory', 'remove_all_inventory', 'remove_select_inventory',
                    'applied_inventory', 'new_add_on_cost', 'save_and_exit', 'save_and_continue'
                    ]
        for element in elements:
            assert self.pages.create_flight_page.is_element_present(getattr(self.pages.create_flight_page, element))
        contents = ['Flight Details', 'Preferred Placement', 'Flight Budget and Spending', 'Delivery',
                    'Campaign Flight Budget Setup', 'Inventory Suppliers', 'Device Types', 'Deals', 'Add On Costs',
                    'Impression Caps', 'Frequency Cap', 'Content Channels', 'Connection Types', 'Environment',
                    'Devices','OS', 'Audience Targeting', 'Carrier'
                    ]
        for content in contents:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def verify_inventory_sources_for_banner(self):
        sources = ['AppNexus', 'Google Adx', 'Google Content Network', 'MoPub',
                   'Nexage', 'OpenX', 'PubMatic', 'Rubicon', 'Where.com']
        self.pages.create_flight_page.check_dropdown_options(sources, self.pages.create_flight_page.avail_inventory)

    @test_case()
    def verify_inventory_sources_for_video(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Omni-Channel')
        self.fill_campaigns_required_fields()
        self.flight = DXConstant().test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(self.flight)
        self.pages.fbs_page.type_bid_normal(DXConstant().flight_bid)
        self.pages.fbs_page.select_media_type('Video')
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)
        sources = ['BrightRoll', 'MoPub', 'Nexage', 'PubMatic', 'Tremor']
        self.pages.create_flight_page.check_dropdown_options(sources, self.pages.create_flight_page.avail_inventory)

    @test_case()
    def verify_inventory_sources_for_native(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Omni-Channel')
        self.fill_campaigns_required_fields()
        self.flight = DXConstant().test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(self.flight)
        self.pages.fbs_page.type_bid_normal(DXConstant().flight_bid)
        self.pages.fbs_page.select_media_type('Native')
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)
        self.pages.create_flight_page.check_dropdown_options(['Facebook'], self.pages.create_flight_page.applied_inventory)

    @test_case()
    def working_of_buttons_in_os(self):
        self.pages.create_flight_page.expand_os()
        time.sleep(5)
        self.pages.create_flight_page.select_available_os('Android')
        self.pages.create_flight_page.click_move_selected_os()
        time.sleep(3)
        self.pages.create_flight_page.check_dropdown_options(['Android'], self.pages.create_flight_page.os_selected)
        self.pages.create_flight_page.click_move_all_os()
        time.sleep(5)
        self.pages.create_flight_page.check_dropdown_options(self.pages.create_flight_page.platforms, self.pages.create_flight_page.os_selected)
        self.pages.create_flight_page.select_selected_os('Android')
        self.pages.create_flight_page.click_remove_selected_os()
        time.sleep(3)
        self.pages.create_flight_page.check_dropdown_options(['Android'], self.pages.create_flight_page.os_available)
        self.pages.create_flight_page.click_remove_all_os()
        time.sleep(5)
        self.pages.create_flight_page.check_dropdown_options(self.pages.create_flight_page.platforms, self.pages.create_flight_page.os_available)

    @test_case()
    def working_of_buttons_in_carrier(self):
        self.pages.create_flight_page.expand_carrier()
        time.sleep(5)
        self.pages.create_flight_page.select_available_carrier('NTT docomo')
        self.pages.create_flight_page.click_move_selected_carrier()
        time.sleep(3)
        self.pages.create_flight_page.check_dropdown_options(['NTT docomo'], self.pages.create_flight_page.carrier_selected)
        self.pages.create_flight_page.click_move_all_carrier()
        time.sleep(5)
        carriers = [
                     'AirTel', 'AT&T', 'BASE', 'BSNL', 'CellOne', 'China Mobile', 'DNA', 'Globe','Idea Cellular','KPN',
                     'LG U+', 'Maxis', 'MetroPCS', 'MTS', 'NetCom', 'Optus', 'Proximus', 'Reliance', 'SingTel',
                     'Smart', 'Swisscom', 'Telcel', 'Telecom Italia', 'Telenor', 'T-Mobile', 'US Cellular',
                     'Vietnamobile', 'Virgin Mobile', 'Vodafone', 'XL Axiata', 'Yoigo'
                     ]
        self.pages.create_flight_page.check_dropdown_options(carriers, self.pages.create_flight_page.carrier_selected)
        self.pages.create_flight_page.select_selected_carrier('NTT docomo')
        self.pages.create_flight_page.click_remove_selected_carrier()
        time.sleep(3)
        self.pages.create_flight_page.check_dropdown_options(['NTT docomo'], self.pages.create_flight_page.carrier_available)
        self.pages.create_flight_page.click_remove_all_carrier()
        time.sleep(5)
        self.pages.create_flight_page.check_dropdown_options(carriers, self.pages.create_flight_page.carrier_available)

    @test_case()
    def verify_environment_section(self):
        self.pages.create_flight_page.expand_enviroment()
        contents = ['Websites', 'Applications', 'Other']
        for content in contents:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def verify_devices_section(self):
        self.pages.create_flight_page.expand_devices()
        elements = ['devices_filter', 'designation', 'master_select', 'first_manufacturer', 'first_device']
        for element in elements:
            assert self.pages.create_flight_page.is_element_present(getattr(self.pages.create_flight_page, element))
        for content in ['Manufacturer and Model', 'Device Type']:
            self.pages.create_flight_page.page_should_contain(content)

    @test_case()
    def verify_os_section(self):
        elements = ['os_available', 'os_selected', 'move_selected_os', 'remove_selected_os',
                    'move_all_selected_os', 'remove_all_selected_os']
        for element in elements:
            assert self.pages.create_flight_page.is_element_present(getattr(self.pages.create_flight_page, element))
        self.pages.create_flight_page.check_dropdown_options(self.pages.create_flight_page.platforms, self.pages.create_flight_page.os_available)

    @test_case()
    def verify_deals_section_for_permissioned_user(self):
        self.pages.create_flight_page.expand_deals()
        elements = ['deals_filters', 'deals_table', 'master_select_deals', 'select_first_deal']
        for element in elements:
            assert self.pages.create_flight_page.is_element_present(getattr(self.pages.create_flight_page, element))

    def create_flights_with_different_types(self):
        self.first_flight_name = DXConstant().test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(self.first_flight_name)
        self.pages.fbs_page.select_flight_type(DXConstant().flight_type_spending)
        self.pages.fbs_page.type_bid('3')
        self.pages.fbs_page.click_on_add_flight()
        time.sleep(2)
        self.second_flight_name = DXConstant().test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(self.second_flight_name)
        self.pages.fbs_page.select_flight_type(DXConstant().flight_type_tracking)
        self.pages.fbs_page.type_bid('3')

    def fill_campaign_and_fbs_page(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Omni-Channel')
        self.fill_campaigns_required_fields()
        self.create_flights_with_different_types()

    @test_case()
    def create_flight_with_types(self):
        self.fill_campaign_and_fbs_page()
        self.pages.fbs_page.click_on_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.go_to_link(self.first_flight_name)
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain(DXConstant().flight_type_spending)
        self.pages.flight_show_page.go_to_link(self.campaign)
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.go_to_link(self.second_flight_name)
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain(DXConstant().flight_type_tracking)

    @test_case()
    def fill_complete_flights_page(self):
        self.fill_campaign_and_fbs_page()
        self.pages.fbs_page.select_media_type('Banner')
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)
        self.pages.create_flight_page.select_available_inventory('Google Adx')
        self.pages.create_flight_page.move_selected_inventory()
        self.pages.create_flight_page.expand_deals()
        self.pages.create_flight_page.filter_deals('deal')
        time.sleep(5)
        self.deal = self.pages.create_flight_page.get_filtered_search('first_deal')
        self.pages.create_flight_page.click_select_first_deal()
        self.pages.create_flight_page.expand_devices()
        self.pages.create_flight_page.filter_devices(self.pages.create_flight_page.inputs['devices'])
        time.sleep(5)
        self.devices = self.pages.create_flight_page.get_filtered_search('device_name')
        self.pages.create_flight_page.select_first()
        self.pages.create_flight_page.expand_os()
        time.sleep(5)
        self.pages.create_flight_page.select_available_os('Android')
        self.pages.create_flight_page.click_move_selected_os()
        self.pages.create_flight_page.expand_carrier()
        time.sleep(5)
        self.pages.create_flight_page.select_available_carrier('NTT docomo')
        self.pages.create_flight_page.click_move_selected_carrier()
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.go_to_link(self.first_flight_name)
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain(self.first_flight_name)

    @test_case()
    def flights_should_created_with_environment(self):
        self.pages.flight_show_page.page_should_contain('Websites')

    @test_case()
    def flights_should_created_with_devices(self):
        self.pages.flight_show_page.page_should_contain(self.devices)

    @test_case()
    def flights_should_created_with_os(self):
        self.pages.flight_show_page.page_should_contain('Android')

    @test_case()
    def flights_should_created_with_carriers(self):
        self.pages.flight_show_page.page_should_contain('NTT docomo')

    @test_case()
    def flights_should_created_with_deals(self):
        self.pages.flight_show_page.page_should_contain(self.deal)

    @test_case()
    def device_targeting_should_disabled_for_flight(self):
        self.fill_campaign_and_fbs_page()
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)
        self.pages.create_flight_page.expand_devices()
        self.pages.create_flight_page.filter_devices(self.pages.create_flight_page.inputs['devices'])
        time.sleep(10)
        if self.pages.create_flight_page.find_element(self.pages.create_flight_page.first_manufacturer).is_selected():
            self.pages.create_flight_page.select_first()
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.go_to_link(self.first_flight_name)
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain('Device Targeting is Disabled.')

    @test_case()
    def message_for_default_device_types(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Omni-Channel')
        self.fill_campaigns_required_fields()
        self.flight_name = DXConstant().test_flight_name + self.pages.fbs_page.get_random_string()
        self.pages.fbs_page.fill_description(self.flight_name)
        self.pages.fbs_page.type_bid('3')
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_till_visible(self.pages.create_flight_page.save_and_exit, 40)
        self.pages.create_flight_page.expand_device_types()
        self.pages.create_flight_page.wait_till_visible(['id', 'flight_inherit_device_types_true'])
        for content in ['Inherited from campaign', '- SmartPhone, Tablet, Desktop/Laptop']:
            self.pages.create_flight_page.page_should_contain(content)
        self.pages.create_flight_page.click_override_device_types()
        self.pages.create_flight_page.click_save_exit()
        self.pages.create_flight_page.wait_till_visible(['css','.error'])
        self.pages.create_flight_page.page_should_contain(self.pages.create_flight_page.no_device_types_message)
        self.pages.create_flight_page.expand_device_types()
        self.pages.create_flight_page.click_inherit_device_types()
        self.pages.create_flight_page.click_save_exit()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.go_to_link(self.flight_name)
        self.pages.flight_show_page.wait_for_flight_basics()
        device_types_messages = self.pages.flight_show_page.get_attribute_value(self.pages.flight_show_page.device_types_message)
        for content in ['SmartPhone', 'Tablet', 'Desktop/Laptop']:
            assert content in device_types_messages

    @test_case()
    def go_to_upload_flights(self):
        self.go_to_campaign_list_page()
        self.fill_advertiser_details('Omni-Channel')
        self.campaign_name = None
        self.campaign_name = self.fill_campaigns_required_fields()
        if self.pages.fbs_page.is_element_present(self.pages.fbs_page.description_filter):
            self.pages.fbs_page.go_to_link('Upload Flights')
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections)

    @test_case()
    def verify_sections_for_omni_channel(self):
        self.go_to_upload_flights()
        time.sleep(2)
        self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections['environment_devices'])
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.wifi)
        sections = ['Connection Types', 'Environment', 'Carrier', 'OS', 'Devices', 'Device Types']
        for section in sections:
            self.pages.upload_flights_page.page_should_contain(section)
        elements = ['wifi', 'carrier', 'other', 'environment_websites', 'environment_apps', 'environment_other',
                    'mobile_carrier_avail', 'mobile_carrier_applied', 'move_mobile_carrier', 'remove_mobile_carrier',
                    'move_all_mobile_carrier', 'remove_all_mobile_carrier', 'mobile_platform_avail',
                    'mobile_platform_applied', 'move_mobile_platform', 'remove_mobile_platform',
                    'move_all_mobile_platform', 'remove_all_mobile_platform', 'devices_filter', 'designation_filter',
                    'all_tabs', 'all_smartphones', 'all_feature_phones', 'master_select_devices', 'first_manufacturer',
                    'expand_first_model', 'inherit_device_types', 'override_device_types', 'connection_types_values',
                    'mobile_options_values', 'carrier_values', 'platform_values', 'devices_values', 'devices_types_values']
        for element in elements:
            self.pages.upload_flights_page.is_element_present(getattr(self.pages.upload_flights_page, element))

    @test_case()
    def goto_upload_flights_via_list_page(self):
        self.go_to_campaign_list_page()
        self.pages.upload_flights_page.wait_till_visible(['id', 'media_plan_campaigns'])
        self.go_to_link(self.campaign_name)
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page('Bulk Upload Flight')
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections)

    @test_case()
    def verify_section_and_inventory_suppliers(self):
        self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections['flight_details_inventory'])
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.frequency_cap)
        self.pages.upload_flights_page.select_flight_type('Spending Flight')
        self.pages.upload_flights_page.select_available_inventory('OpenX')
        time.sleep(50)
        elements = ['frequency_cap', 'frequency', 'frequency_type', 'flight_type', 'algorithm', 'placement_standard',
                    'use_grid', 'dayparting_sunday', 'dayparting_monday', 'dayparting_tuesday', 'dayparting_wednesday',
                    'dayparting_thursday', 'dayparting_friday', 'dayparting_saturday', 'select_all',
                    'frequency_cap_values', 'flight_type_values', 'media_type_values', 'algorithm_values', 'placement_values',
                    'dayparting_values', 'suppliers_values', 'one_view_section', 'one_view_policy_values']
        for element in elements:
            self.pages.upload_flights_page.is_element_present(getattr(self.pages.upload_flights_page, element))
        cap_type = ['Day(s)', 'Hour(s)', 'Week(s)', 'Flight Duration']
        self.pages.upload_flights_page.check_dropdown_options(cap_type, self.pages.upload_flights_page.frequency_type)
        self.pages.upload_flights_page.assert_value('suppliers_values', 'OpenX')

    def verify_count(self, counts):
        for count in counts:
            self.pages.upload_flights_page.page_should_contain(str(count))

    @test_case()
    def verify_campaign_inheritance_message(self):
        self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections['environment_devices'])
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.devices_filter)
        self.pages.upload_flights_page.click_override_device_types()
        self.pages.upload_flights_page.page_should_contain(self.pages.upload_flights_page.messages['inheritance'])

    @test_case()
    def verify_platforms_section(self):
        oss = ['Android', 'iOS', 'OS X', 'Symbian/S60', 'Windows']
        total = int(self.pages.upload_flights_page.get_attribute_value(self.pages.upload_flights_page.platform_count, 'innerHTML'))
        selected = len(oss)
        for os in oss:
            self.pages.upload_flights_page.select_platform(os)
        self.pages.upload_flights_page.click_select_platform()
        platforms = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.platform_values)
        for os in oss:
            assert os in platforms
        self.verify_count([total - selected, selected])
        self.pages.upload_flights_page.select_applied_platform('OS X')
        self.pages.upload_flights_page.click_remove_platform()
        platforms = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.platform_values)
        assert 'OS X' not in platforms
        selected -= 1
        self.verify_count([total - selected, selected])
        self.pages.upload_flights_page.click_select_all_platform()
        time.sleep(5)
        platforms = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.platform_values)
        for os in oss:
            assert os in platforms
        self.verify_count(['0', total])
        self.pages.upload_flights_page.click_remove_all_platform()
        time.sleep(5)
        platforms = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.platform_values)
        assert '' == platforms
        self.verify_count([total,'0'])
        self.pages.upload_flights_page.click_inherit_device_types()
        device_types_message = self.pages.upload_flights_page.get_attribute_value(self.pages.upload_flights_page.device_types_message)
        for content in ['Desktop/Laptop', 'SmartPhone', 'Tablet']:
            assert content in device_types_message
        device_types = ['Connected TV', 'Game Console', 'SmartPhone', 'Tablet', 'Desktop/Laptop']
        total = int(self.pages.upload_flights_page.get_attribute_value(self.pages.upload_flights_page.device_types_count, 'innerHTML'))
        selected = len(device_types)
        self.pages.upload_flights_page.click_override_device_types()
        time.sleep(5)
        self.pages.upload_flights_page.check_dropdown_options(device_types, self.pages.upload_flights_page.device_types_avail)
        for device in device_types:
            self.pages.upload_flights_page.select_available_device_types(device)
        self.pages.upload_flights_page.click_move_selected()
        devices = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.devices_types_values)
        for device in device_types:
            assert device in devices
        self.verify_count([total - selected, selected])
        self.pages.upload_flights_page.select_selected_device_types('SmartPhone')
        self.pages.upload_flights_page.click_remove_selected()
        devices = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.devices_types_values)
        assert 'SmartPhone' not in devices
        selected -= 1
        self.verify_count([total - selected, selected])
        self.pages.upload_flights_page.click_move_all()
        time.sleep(5)
        devices = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.devices_types_values)
        for device in device_types:
            assert device in devices
        self.verify_count(['0', total])
        self.pages.upload_flights_page.click_remove_all()
        time.sleep(5)
        devices = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.devices_types_values)
        assert '' == devices
        self.verify_count([total,'0'])

    @test_case()
    def working_of_spreadsheet_values_for_environment(self):
        self.pages.upload_flights_page.click_wifi_gateway()
        self.pages.upload_flights_page.click_carrier_gateway()
        self.pages.upload_flights_page.click_other_gateway()
        gateways = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.connection_types_values)
        for gateway in ['WiFi', 'Carrier Gateway', 'Unknown / Other']:
            assert gateway in gateways
        self.pages.upload_flights_page.click_environment_website()
        self.pages.upload_flights_page.click_environment_apps()
        self.pages.upload_flights_page.click_environment_other()
        environments = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.mobile_options_values)
        for environment in ['Websites', 'Applications', 'Other']:
            assert environment in environments
        carriers = ['AirTel', 'BSNL', 'CellOne', 'DNA', 'MTS', 'NTT docomo', 'Reliance', 'US Cellular','Vodafone']
        total = int(self.pages.upload_flights_page.get_attribute_value(self.pages.upload_flights_page.carrier_count, 'innerHTML'))
        selected = len(carriers)
        for carrier in carriers:
            self.pages.upload_flights_page.select_carrier(carrier)
        self.pages.upload_flights_page.click_select_carrier()
        carriers_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.carrier_values)
        for carrier in carriers:
            assert carrier in carriers_values
        self.verify_count([total - selected, selected])
        self.pages.upload_flights_page.select_applied_carrier('MTS')
        self.pages.upload_flights_page.click_remove_carrier()
        carriers_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.carrier_values)
        assert 'MTS' not in carriers_values
        selected -= 1
        self.verify_count([total - selected, selected])
        self.pages.upload_flights_page.click_select_all_carrier()
        time.sleep(5)
        carriers_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.carrier_values)
        for carrier in carriers:
            assert carrier in carriers_values
        self.verify_count(['0', total])
        self.pages.upload_flights_page.click_remove_all_carrier()
        time.sleep(5)
        carriers_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.carrier_values)
        assert '' == carriers_values
        self.verify_count([total,'0'])
        self.verify_platforms_section()

    @test_case()
    def verify_channel_and_languages_section(self):
        self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections['channels_languages'])
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.avail_channels)
        self.pages.upload_flights_page.click_separate_lang_targeting()
        for content in ['Inherit targeting from campaign', 'Separate Language Targeting for this flight']:
            self.pages.upload_flights_page.page_should_contain(content)
        elements = ['avail_channels', 'selected_channels', 'select_channels', 'remove_channels', 'select_all_channels',
                    'remove_all_channels', 'inherit_lang_targeting', 'separate_lang_targeting',
                    'avail_langs', 'selected_channels', 'select_langs', 'remove_channels', 'select_all_channels',
                    'remove_all_channels', 'channels_values', 'langs_values']
        for element in elements:
            self.pages.upload_flights_page.is_element_present(getattr(self.pages.upload_flights_page, element))

    @test_case()
    def verify_working_of_languages_section(self):
        lang = {'French':'fr', 'Spanish':'es', 'Dutch':'nl', 'English':'en', 'Japanese':'ja',
                    'Hindi':'hi', 'Russian':'ru', 'German':'de', 'Chinese':'zh'}
        total = int(self.pages.upload_flights_page.get_attribute_value(self.pages.upload_flights_page.lang_count, 'innerHTML'))
        selected = len(lang)
        for language in lang.keys():
                self.pages.upload_flights_page.select_avail_langs(language)
        self.pages.upload_flights_page.click_select_langs()
        languages = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.langs_values)
        for language in lang.values():
            assert language in languages
        self.verify_count([total - selected, selected])
        self.pages.upload_flights_page.select_applied_langs('German')
        self.pages.upload_flights_page.click_remove_langs()
        languages = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.langs_values)
        assert lang['German'] not in languages
        selected -= 1
        self.verify_count([total - selected, selected])
        self.pages.upload_flights_page.click_select_all_langs()
        time.sleep(5)
        languages = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.langs_values)
        for language in lang.values():
            assert language in languages
        self.verify_count(['0',total])
        self.pages.upload_flights_page.click_remove_all_langs()
        time.sleep(5)
        languages = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.langs_values)
        assert '' == languages
        self.verify_count([total,'0'])

    @test_case()
    def working_of_spreadsheet_values_for_channels(self):
        channels = {'Arts & Entertainment':'IAB1', 'Business':'IAB3', 'Careers':'IAB4', 'Education':'IAB5',
                        'Hobbies & Interests':'IAB9', 'News':'IAB12', 'Real Estate':'IAB21', 'Science':'IAB15',
                        'Style & Fashion':'IAB18', 'Technology & Computing':'IAB19', 'Travel':'IAB20'}
        total = int(self.pages.upload_flights_page.get_attribute_value(self.pages.upload_flights_page.channel_count, 'innerHTML'))
        selected = len(channels)
        for channel in channels.keys():
            self.pages.upload_flights_page.select_avail_channel(channel)
        self.pages.upload_flights_page.click_select_channels()
        channel_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.channels_values)
        for channel in channels.values():
            assert channel in channel_values
        self.verify_count([total - selected, selected])
        self.pages.upload_flights_page.select_applied_channel('Technology & Computing')
        self.pages.upload_flights_page.click_remove_channels()
        channel_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.channels_values)
        assert channels['Technology & Computing'] not in channel_values
        selected -= 1
        self.verify_count([total - selected, selected])
        self.pages.upload_flights_page.click_select_all_channels()
        time.sleep(5)
        channel_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.channels_values)
        for channel in channels.values():
            assert channel in channel_values
        self.verify_count(['0', total])
        self.pages.upload_flights_page.click_remove_all_channels()
        time.sleep(5)
        channel_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.channels_values)
        assert '' == channel_values
        self.verify_count([total,'0'])
        self.verify_working_of_languages_section()

    @test_case()
    def verify_geo_targeting_section(self):
        self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections['geographic_targeting'])
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.inherit_geo_targeting)
        self.pages.upload_flights_page.click_separate_geo_targeting()
        for content in ['Inherit options from campaign', 'Separate Geotargeting for this flight']:
            self.pages.upload_flights_page.page_should_contain(content)
        types = ['Target GeoFenced regions', 'Target the entirety of one or more countries', 'Specify regions within...']
        self.pages.upload_flights_page.check_dropdown_options(types, self.pages.upload_flights_page.geo_target_type)
        elements = ['inherit_geo_targeting', 'separate_geo_targeting', 'geo_target_type', 'search_countries',
                    'avail_countries', 'selected_countries', 'select_countries', 'remove_countries',
                    'select_all_countries','remove_all_countries', 'geo_target_type_values', 'geo_target_values']
        for element in elements:
            self.pages.upload_flights_page.is_element_present(getattr(self.pages.upload_flights_page, element))
        assert 'international' == self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.geo_target_type_values)
        self.pages.upload_flights_page.select_avail_country('United States')
        self.pages.upload_flights_page.click_select_country()
        assert 'US' in self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.geo_target_values)
        self.pages.upload_flights_page.select_applied_country('United States')
        self.pages.upload_flights_page.click_remove_country()
        assert 'US' not in self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.geo_target_values)
        countries = {'United States':'US', 'Brazil':'BR', 'Poland':'PL'}
        self.pages.upload_flights_page.click_select_all_countries()
        country_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.geo_target_values)
        for country in countries.values():
            assert country in country_values
        self.pages.upload_flights_page.select_geo_targeting_type(2)
        time.sleep(3)
        self.pages.upload_flights_page.page_should_contain(self.pages.upload_flights_page.messages['geo_targeting'])
        for element in ['country', 'area_type']:
            self.pages.upload_flights_page.is_element_present(getattr(self.pages.upload_flights_page, element))
        countries = ['Argentina', 'Brazil', 'Costa Rica', 'France', 'Japan', 'Mexico', 'Spain', 'United States']
        self.pages.upload_flights_page.check_dropdown_options(countries, self.pages.upload_flights_page.country)
        states = ['States & Territories', 'Metrocodes', 'Postal Codes']
        self.pages.upload_flights_page.check_dropdown_options(states, self.pages.upload_flights_page.area_type)
        regions = {'Alabama':'AL', 'New York':'NY', 'Pennsylvania':'PA', 'Texas':'TX', 'Washington':'WA'}
        for region in regions.keys():
            self.pages.upload_flights_page.select_avail_region(region)
        self.pages.upload_flights_page.click_move_regions()
        country_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.geo_target_values)
        for region in regions.values():
            assert region in country_values
        self.pages.upload_flights_page.select_geo_target_country('France')
        time.sleep(5)
        country_values = self.pages.upload_flights_page.get_content_value(self.pages.upload_flights_page.geo_target_type_values)
        assert 'regions|FR' == country_values
        regions = ['Alsace', 'Bretagne', 'Lorraine', 'Picardie', 'Rhone-Alpes']
        self.pages.upload_flights_page.check_dropdown_options(regions, self.pages.upload_flights_page.avail_region)

    @test_case()
    def verify_creative_assignment_section(self):
        self.pages.upload_flights_page.go_to_link(self.pages.upload_flights_page.sections['creatives'])
        self.pages.upload_flights_page.wait_till_visible(['id', 'available_creatives_table'])
        time.sleep(5)
        self.pages.upload_flights_page.search_creatives(self.pages.upload_flights_page.inputs['creative'])
        element = self.pages.upload_flights_page.find_element(self.pages.upload_flights_page.first_creative)
        creative = str(element.get_attribute('innerHTML')).replace('<wbr>', '').strip()
        self.pages.upload_flights_page.select_first_creative()
        self.pages.upload_flights_page.assert_value('creative_values', creative)

    @test_case()
    def omni_channel_guaranteed_inventory(self):
        self.pages.search_page.click_inventory_link()
        self.pages.inventory_list_page.wait_till_visible(['id', 'ui-tabs-1'])
        self.pages.inventory_list_page.click_on_organization_dropdown()
        self.pages.inventory_list_page.fill_organization_text_box(DXConstant().advertiser_name)
        self.pages.inventory_list_page.fill_field(self.pages.inventory_list_page.advertiser_input, Keys.ENTER)
        time.sleep(10)
        self.pages.inventory_list_page.click_on_new_guaranteed_media_button()
        self.pages.guaranteed_inventory_edit_page.wait_till_visible(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_form)
        payload = self.pages.guaranteed_inventory_edit_page.get_random_string(5)
        self.pages.guaranteed_inventory_edit_page.enter_guaranteed_inventory_publisher_name('Guaranteed-Media-Publisher' + payload)
        inventory_name = 'Guaranteed-Inventory' + payload
        self.pages.guaranteed_inventory_edit_page.enter_guaranteed_inventory_placement_name(inventory_name)
        self.pages.guaranteed_inventory_edit_page.select_guaranteed_inventory_media_type('Omni-Channel')
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_save_button()
        self.pages.inventory_list_page.wait_till_visible(['id', 'ui-tabs-1'])
        self.pages.inventory_list_page.page_should_contain('Guaranteed Medium {0} was created successfully'.format(inventory_name))

    @test_case()
    def omni_channel_custom_inventory(self):
        self.pages.search_page.click_inventory_link()
        self.pages.inventory_list_page.wait_till_visible(['id', 'ui-tabs-1'])
        self.pages.inventory_list_page.click_on_custom_inventory_tab()
        self.pages.inventory_list_page.wait_till_visible(['id', 'custom_inventory'])
        self.pages.inventory_list_page.click_on_new_custom_inventory_button()
        self.pages.custom_inventory_edit_page.wait_till_visible(self.pages.custom_inventory_edit_page.custom_inventory_form)
        payload = self.pages.custom_inventory_edit_page.get_random_string(5)
        self.pages.custom_inventory_edit_page.enter_custom_inventory_publisher_name('Custom-Media-Publisher' + payload)
        inventory_name = 'Custom-Inventory' + payload
        self.pages.custom_inventory_edit_page.enter_custom_inventory_placement_name(inventory_name)
        self.pages.custom_inventory_edit_page.select_custom_inventory_media_type('Omni-Channel')
        self.pages.custom_inventory_edit_page.click_on_save_custom_inventory_button()
        self.pages.inventory_list_page.wait_till_visible(['id', 'custom_inventory'])
        self.pages.inventory_list_page.page_should_contain('Custom Inventory {0} was created successfully'.format(inventory_name))

    @test_case()
    def flight_upload_with_all_data(self):
        self.go_to_upload_flights()
        self.common_helper.process_flight_file_with_name_and_date('omni_channel_flights', 'Omni-Channel')
        self.pages.upload_flights_page.select_file(os.path.dirname(__file__)+ '/../../../data/flights_upload/omni_channel_flights.csv')
        self.pages.upload_flights_page.click_upload_file()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.flight_uploads, 90)
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.flight_submit)
        self.pages.upload_flights_page.click_flights_submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row, 150)
        self.pages.fbs_page.page_should_contain('All flights have been saved successfully.')
        self.pages.fbs_page.click_on_save_exit()

    @test_case()
    def verify_uploaded_device_types(self):
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        flight_names = self.common_helper.get_flights_name_from_file('omni_channel_flights')
        self.pages.campaign_show_page.go_to_link(flight_names[0])
        self.pages.flight_show_page.wait_for_flight_basics()
        self.pages.flight_show_page.page_should_contain('Connected TV, Desktop/Laptop, Game Console, Other, SmartPhone, Tablet')

    @test_case()
    def verify_uploaded_media_type(self):
        self.pages.flight_show_page.page_should_contain('Banner')

    @test_case()
    def verify_uploaded_environment_options(self):
        for option in ['Websites', 'Applications', 'Other']:
            self.pages.flight_show_page.page_should_contain(option)

    @test_case()
    def verify_uploaded_platforms(self):
        for option in ['Android', 'Blackberry', 'iOS', 'S40', 'Symbian/S60', 'Windows Mobile', 'Unknown', 'Other', 'OS X', 'Windows']:
            self.pages.flight_show_page.page_should_contain(option)

    @test_case()
    def verify_uploaded_devices(self):
        for content in ['Device Targeting is Enabled.', 'Targeting 2148 devices.']:
            self.pages.flight_show_page.page_should_contain(content)
