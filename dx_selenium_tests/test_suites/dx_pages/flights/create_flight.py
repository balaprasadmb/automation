from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from base.dx import Dx
import time

class CreateFlight(Dx):

    def fill_fields(self , flight_attributes):
        self.expand_lang_targeting()
        self.click_separate_language_targeting()
        self.select_lang_targeting()
        self.click_move_selected_lang()
        self.expand_geo_targeting()
        self.click_separate_geo_targeting()
        self.select_avail_countries()
        self.click_move_selected_country()
        self.click_save_exit()

    def fill_fields_validation(self, flight_attributes_validation):
        self.type_start_date(flight_attributes_validation['start_date'])
        self.enter_default_bid(flight_attributes_validation['deafault_bid_usd'])
        self.enter_budget_usd(flight_attributes_validation['Budget_usd'])
        self.type_end_date(flight_attributes_validation['end_date'])
        self.click_save_exit()

    def edit_flight_description(self, flight_description):
        self.clear_description_filter()
        self.type_in_edit_description_filter(flight_description)
        self.click_save_and_continue()

    def expand_add_on_cost(self):
        self.wait_till_visible(self.edit_flight_name)
        element = self.find_element(self.new_add_on_cost)
        if not element.is_displayed():
            self.click_element(self.add_on_cost_expand)

    def type_in_edit_description_filter(self, description):
        self.fill_field(self.edit_flight_name, description)

    def clear_description_filter(self):
        self.clear(self.edit_flight_name)

    def select_tactic(self, value):
        self.select_option(self.flight_tactic, value)

    def select_media_type(self, value):
        self.select_option(self.media_type, value)

    def type_start_date(self, value):
        self.send_keys(self.start_date, value)

    def type_end_date(self, value):
        self.send_keys(self.end_date, value)
        self.fill_field(self.end_date, Keys.ESCAPE)
        time.sleep(2)
        self.click_element(self.edit_flight_name)

    def enter_default_bid(self, values):
        self.send_keys(self.default_bid_usd, values)

    def enter_budget_usd(self, values): 
        self.send_keys(self.budget_usd, values)

    def enter_allocated_percentage(self, values):
        self.send_keys(self.alloc, values)

    def select_available_inventory(self, value):
        self.select_option(self.avail_inventory, value)

    def select_applied_inventory(self, value):
        self.select_option(self.applied_inventory, value)

    def move_selected_inventory(self):
        self.click_element(self.move_select_inventory)

    def remove_selected_inventory(self):
        self.click_element(self.remove_select_inventory)

    def move_all_selected_inventory(self):
        self.click_element(self.move_all_inventory)

    def remove_all_selected_inventory(self):
        self.click_element(self.remove_all_inventory)

    def expand_deals(self):
        self.click_element(self.deals)

    def filter_deals(self, value):
        self.send_keys(self.deals_filters, value)
        self.fill_field(self.deals_filters, Keys.ENTER)

    def click_master_select(self):
        self.click_element(self.master_select_deals)

    def click_select_first_deal(self):
        self.click_element(self.select_first_deal)

    def click_new_aoc(self):
        self.click_element(self.new_add_on_cost)

    def select_aoc_name(self, value):
        self.select_option(self.add_on_cost_name, value)

    def select_aoc_name_second(self, value):
        self.select_option(self.add_on_cost_name_second, value)

    def enter_cutom_aoc_value(self, value):
        self.fill_field(self.add_on_cost_custom, value)

    def enter_custom_aoc_name_second(self, value):
        self.fill_field(self.add_on_cost_custom_second, value)

    def click_aoc_rate(self):
        self.click_element(self.add_on_cost_rate)

    def enter_aoc_rate(self, value):
        self.fill_field(self.add_on_cost_rate, value)

    def enter_aoc_rate_value_second(self, value):
        self.click_element(self.add_on_cost_rate_second)
        self.fill_field(self.add_on_cost_rate_second, value)

    def select_fee_type(self, value):
        self.select_option(self.add_on_cost_fee_type, value)

    def click_billable(self):
        self.click_element(self.add_on_cost_billable)

    def click_is_marketplace(self):
        self.click_element(self.add_on_cost_marketplace)

    def click_on_aoc_remove_button(self):
        self.click_element(self.aoc_remove_button)

    def expand_private_inventory(self):
        self.click_element(self.private_inventory)

    def select_first_private_inventory(self):
        self.click_element(self.first_private_inventory)

    def expand_device_types(self):
        self.click_element(self.device_types)

    def click_inherit_device_types(self):
        self.click_element(self.inherit_device_types)

    def click_override_device_types(self):
        self.click_element(self.separate_device_types)

    def select_available_device_types(self, value):
        self.select_option(self.devices_available, value)

    def select_selected_device_types(self, value):
        self.select_option(self.devices_selected, value)

    def click_move_selected(self):
        self.click_element(self.move_selected_devices)

    def click_remove_selected(self):
        self.click_element(self.remove_selected_devices)

    def click_move_all(self):
        self.click_element(self.move_all_selected_devices)

    def click_remove_all(self):
        self.click_element(self.remove_all_selected_devices)

    def expand_deals(self):
        self.click_element(self.deals)

    def filter_deals(self, value):
        self.send_keys(self.deals_filters, value)

    def expand_gateway(self):
        self.click_element(self.gateway)

    def expand_enviroment(self):
        self.click_element(self.enviroment)

    def click_environment_websites_checkbox(self):
        self.click_element(self.environment_websites)

    def click_environment_applications_checkbox(self):
        self.click_element(self.environment_applications)

    def click_environment_other_checkbox(self):
        self.click_element(self.environment_other)

    def expand_devices(self):
        self.click_element(self.devices)

    def filter_devices(self, value):
        self.send_keys(self.devices_filter, value)

    def select_designation(self, value):
        self.select_option(self.designation, value)

    def select_all_devices(self):
        self.click_element(self.master_select)

    def select_first(self):
        self.click_element(self.first_manufacturer)

    def expand_os(self):
        self.click_element(self.os)

    def select_available_os(self, value):
        self.select_option(self.os_available, value)

    def select_selected_os(self, value):
        self.select_option(self.os_selected, value)

    def click_move_selected_os(self):
        self.click_element(self.move_selected_os)

    def click_remove_selected_os(self):
        self.click_element(self.remove_selected_os)

    def click_move_all_os(self):
        self.click_element(self.move_all_selected_os)

    def click_remove_all_os(self):
        self.click_element(self.remove_all_selected_os)

    def expand_carrier(self):
        self.click_element(self.carrier)

    def select_available_carrier(self, value):
        self.select_option(self.carrier_available, value)

    def select_selected_carrier(self, value):
        self.select_option(self.carrier_selected, value)

    def click_move_selected_carrier(self):
        self.click_element(self.move_selected_carrier)

    def click_remove_selected_carrier(self):
        self.click_element(self.remove_selected_carrier)

    def click_move_all_carrier(self):
        self.click_element(self.move_all_selected_carrier)

    def click_remove_all_carrier(self):
        self.click_element(self.remove_all_selected_carrier)

    def expand_lang_targeting(self):
        self.click_element(self.lang_targeting)

    def click_separate_language_targeting(self):
        self.click_element(self.separate_language_targeting)

    def select_lang_targeting(self):
        self.click_element(self.select_first_lang)

    def click_move_selected_lang(self):
        self.click_element(self.move_selected_lang)

    def click_remove_selected_lang(self):
        self.click_element(self.remove_selected_lang)

    def click_move_all_selected_lang(self):
        self.click_element(self.move_all_selected_lang)

    def click_remove_all_selected_lang(self):
        self.click_element(self.remove_all_selected_lang)

    def expand_geo_targeting(self):
        self.click_element(self.geographic_targeting)

    def click_separate_geo_targeting(self):
        self.click_element(self.separate_geo_targeting)

    def select_geo_target_region(self, geo_target_region):
        self.select_option(self.geo_target_region_dropdown, geo_target_region)

    def upload_geofenced_file(self, value):
        self.fill_field(self.geofenced_file, value)

    def enter_geofenced_group_name(self, value):
        self.send_keys(self.geofenced_name, value)

    def click_geofenced_submit(self):
        self.click_element(self.geofenced_submit)

    def wait_for_upload_error_message(self):
        self.wait_till_visible(self.geotargeting_upload_error)

    def wait_for_upload_success_message(self):
        self.wait_till_visible(self.geohash_upload_successfully)

    def select_geo_target_country(self, geo_target_country):
        self.select_option(self.geo_target_country_dropdown, geo_target_country)

    def select_geo_target_codes(self, geo_target_codes):
        self.select_option(self.geo_target_codes_dropdown, geo_target_codes)
        time.sleep(2)

    def upload_postal_code_file(self, postal_code_file_path):
        self.upload_file(postal_code_file_path, self.geo_targeting_file_upload)

    def enter_postal_code_group_name(self, postal_code_group_name):
        self.send_keys(self.postal_code_group_name_textbox, postal_code_group_name)

    def click_on_upload_postal_codes_button(self):
        self.click_element(self.upload_postal_codes_button)

    def select_selected_countries(self, value):
        self.click_element(self.country_selected, value)

    def click_move_selected_country(self):
        self.click_element(self.move_selected_country)

    def click_remove_selected_country(self):
        self.click_element(self.remove_selected_country)

    def click_move_all_selected_countries(self):
        self.click_element(self.move_all_selected_country)

    def click_remove_all_selected_countries(self):
        self.click_element(self.remove_all_selected_country)

    def select_avail_countries(self):
        self.click_element(self.country_first_select)

    def expand_whitelist(self):
        self.click_element(self.whitelist)

    def expand_blacklist(self):
        self.click_element(self.blacklist)

    def expand_audience_targeting(self):
        self.click_element(self.audience_targeting)

    def click_save_exit(self):
        self.click_element(self.save_and_exit)

    def click_save_and_continue(self):
        self.click_element(self.save_and_continue)    

    def select_preferred_placement(self , value):
        self.select_option(self.preferred_placement, value)

    def wait_for_flight_details(self):
        self.wait_till_visible(self.flight_details)

    def get_filtered_search(self, element):
        search_text = str(self.find_element(getattr(self, element)).get_attribute('innerHTML'))
        return search_text.replace('<wbr>', '')

    def do_hover(self):
        ActionChains(self.driver).move_to_element(self.find_element(self.inventory_suppliers))

    def get_inventory(self, element, count = 1):
        widget = self.find_element(getattr(self, element))
        select = Select(widget)
        selected = []
        for option in select.options:
            if count == 1:
                return option.text
            else:
                selected.append(option.text)
        return selected

    def click_single_device(self):
        self.click_element(self.single_device_enabled)

    def click_high_precision(self):
        self.click_element(self.high_precision_enabled)

    def click_broad_reach(self):
        self.click_element(self.broad_reach_enabled)

    def click_oneview_popup_cancel(self):
        self.click_element(self.oneview_popup_cancel)

    def click_oneview_popup_ok(self):
        self.click_element(self.oneview_popup_ok)

    def click_on_campaign_name_link(self):
        self.click_element(self.campaign_name_link)
