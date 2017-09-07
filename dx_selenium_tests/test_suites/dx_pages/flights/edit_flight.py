from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from base.dx import Dx
import time
class EditFlight(Dx):

    def type_in_edit_description(self, description):
        self.fill_field(self.edit_flight_name, description)

    def clear_description_filter(self):
        self.clear(self.edit_flight_name)

    def select_tactic(self, value):
        self.select_option(self.flight_tactic, value)

    def type_start_date(self, value):
        self.send_keys(self.start_date, value)

    def type_end_date(self, value):
        self.send_keys(self.end_date, value)
        self.fill_field(self.end_date, Keys.ESCAPE)
        self.click_element(self.edit_flight_name)
        time.sleep(2)

    def enter_default_bid(self, values):
        self.send_keys(self.deafault_bid_usd, values)

    def enter_budget_usd(self, values): 
        self.send_keys(self.budget_usd, values)

    def enter_allocated_percentage(self, values):
        self.send_keys(self.alloc, values)

    def select_media_types(self, value):
        self.select_option(self.media_type, value)

    def select_avail_inventory(self):
        self.click_element(self.select_inventory)

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

    def enter_aoc_rate(self, value):
        self.fill_field(self.add_on_cost_rate, value)

    def select_fee_type(self, value):
        self.select_option(self.add_on_cost_fee_type, value)

    def click_billable(self):
        self.click_element(self.add_on_cost_billable)

    def click_is_marketplace(self):
        self.click_element(self.add_on_cost_marketplace)

    def expand_inventory(self):
        self.click_element(self.inventory_targeting)

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

    def select_environment(self, value):
        self.select_option(self.flight_environment, value)

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
        self.click_element(self.geography_targeting)

    def click_separate_geography_targeting(self):
        self.click_element(self.separate_geography_targeting)

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

    def click_on_edit_blacklist_link(self):
        self.click_element(self.edit_blacklist_link)

    def expand_audience_targeting(self):
        self.click_element(self.audience_targeting)

    def click_save_exit(self):
        self.click_element(self.save_and_exit)

    def click_save_and_continue(self):
        self.click_element(self.save_and_continue)    

    def select_preferred_placement(self , value):
        self.select_option(self.preferred_placement, value)
