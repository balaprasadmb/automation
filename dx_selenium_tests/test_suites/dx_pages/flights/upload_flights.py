from base.dx import Dx
from selenium.webdriver.support.ui import Select
import time

class UploadFlights(Dx):

    def select_file(self, value):
        self.fill_field(self.browse_file, value)
        time.sleep(2)

    def click_upload_file(self):
        self.click_element(self.upload_file)

    def click_flights_submit(self):
        self.click_element(self.flight_submit)

    def click_cancel_delete(self):
        self.click_element(self.cancel)

    def type_frequency_cap(self, value):
        self.fill_field(self.frequency_cap, value)

    def type_frequency(self, value):
        self.fill_field(self.frequency, value)

    def select_frequency_type(self, value):
        self.select_option(self.frequency_type, value)

    def select_flight_type(self, value):
        self.select_option(self.flight_type, value)

    def select_algorithm_for_fbx(self, value):
        self.select_option(self.fbx_algorithm, value)

    def select_placement_for_fbx(self, value):
        self.select_option(self.placement_fbx, value)

    def select_algorithm(self, value):
        self.select_option(self.algorithm, value)

    def select_placement(self, value):
        self.select_option(self.placement_standard, value)

    def select_viewability_vendors(self, value):
        self.select_option(self.viewability, value)

    def select_viewability_selections(self, value):
        self.select_option(self.selections, value)

    def select_placement_for_tracking(self, value):
        self.select_option(self.placement_tracking, value)

    def click_dayparting_sunday(self):
        self.click_element(self.dayparting_sunday)

    def click_dayparting_monday(self):
        self.click_element(self.dayparting_monday)

    def click_dayparting_tuesday(self):
        self.click_element(self.dayparting_tuesday)

    def click_dayparting_wednesday(self):
        self.click_element(self.dayparting_wednesday)

    def click_dayparting_thursday(self):
        self.click_element(self.dayparting_thursday)

    def click_dayparting_friday(self):
        self.click_element(self.dayparting_friday)

    def click_dayparting_saturday(self):
        self.click_element(self.dayparting_saturday)

    def click_select_all(self):
        self.click_element(self.select_all)

    def click_first_suppliers(self):
        self.click_element(self.select_first)

    def click_select_all_tracking(self):
        self.click_element(self.select_all_tracking_inventory)

    def select_available_inventory(self, value):
        self.inventory_avail[1] = self.inventory_avail[1].format(value)
        self.click_element(self.inventory_avail)

    def select_avail_channel(self, value):
        self.select_option(self.avail_channels, value)

    def select_applied_channel(self, value):
        self.select_option(self.selected_channels, value)

    def click_select_channels(self):
        self.click_element(self.select_channels)

    def click_remove_channels(self):
        self.click_element(self.remove_channels)

    def click_select_all_channels(self):
        self.click_element(self.select_all_channels)

    def click_remove_all_channels(self):
        self.click_element(self.remove_all_channels)

    def click_inherit_lang_targeting(self):
        self.click_element(self.inherit_lang_targeting)

    def click_separate_lang_targeting(self):
        self.click_element(self.separate_lang_targeting)

    def select_avail_langs(self, value):
        self.select_option(self.avail_langs, value)

    def select_applied_langs(self, value):
        self.select_option(self.selected_langs, value)

    def click_select_langs(self):
        self.click_element(self.select_langs)

    def click_remove_langs(self):
        self.click_element(self.remove_langs)

    def click_select_all_langs(self):
        self.click_element(self.select_all_langs)

    def click_remove_all_langs(self):
        self.click_element(self.remove_all_langs)

    def click_inherit_geo_targeting(self):
        self.click_element(self.inherit_geo_targeting)

    def click_separate_geo_targeting(self):
        self.click_element(self.separate_geo_targeting)

    def select_geo_targeting_type(self, index):
        self.select_option(self.geo_target_type, index, 'index')

    def search_country(self, value):
        self.fill_field(self.search_countries, value)

    def select_avail_country(self, value):
        self.select_option(self.avail_countries, value)

    def select_applied_country(self, value):
        self.select_option(self.selected_countries, value)

    def click_select_country(self):
        self.click_element(self.select_countries)

    def click_remove_country(self):
        self.click_element(self.remove_countries)

    def click_select_all_countries(self):
        self.click_element(self.select_all_countries)

    def click_remove_all_countries(self):
        self.click_element(self.remove_all_countries)

    def search_geofenced_country(self, value):
        self.fill_field(self.geofenced_search_countries, value)

    def select_avail_geofenced_country(self, value):
        self.select_option(self.geofenced_avail_countries, value)

    def select_applied_geofenced_country(self, value):
        self.select_option(self.geofenced_selected_countries, value)

    def click_select_geofenced_country(self):
        self.click_element(self.geofenced_select_countries)

    def click_remove_geofenced_country(self):
        self.click_element(self.geofenced_remove_countries)

    def click_select_all_geofenced_countries(self):
        self.click_element(self.geofenced_select_all_countries)

    def click_remove_all_geofenced_countries(self):
        self.click_element(self.geofenced_remove_all_countries)

    def upload_geofenced_file(self, value):
        self.fill_field(self.geofenced_browse_file, value)

    def enter_geofenced_group_name(self, value):
        self.fill_field(self.geofenced_name, value)

    def click_geofenced_submit(self):
        self.click_element(self.geofenced_group_submit)

    def wait_for_upload_error_message(self):
        self.wait_till_visible(self.geotargeting_upload_error)

    def wait_for_upload_success_message(self):
        self.wait_till_visible(self.geohash_upload_successfully)

    def select_geo_target_country(self, value):
        self.select_option(self.country, value)

    def select_geo_target_area_type(self, value):
        self.select_option(self.area_type, value)

    def search_regions(self, value):
        self.fill_field(self.region_search, value)

    def select_avail_region(self, value):
        self.select_option(self.avail_region, value)

    def select_applied_region(self, value):
        self.select_option(self.selected_region, value)

    def click_move_regions(self):
        self.click_element(self.select_region)

    def click_remove_regions(self):
        self.click_element(self.remove_region)

    def click_select_all_regions(self):
        self.click_element(self.select_all_regions)

    def click_remove_all_regions(self):
        self.click_element(self.remove_all_regions)

    def search_metrocodes_country(self, value):
        self.fill_field(self.search_metrocodes, value)

    def select_avail_metrocodes_country(self, value):
        self.select_option(self.avail_metrocodes, value)

    def select_applied_metrocodes_country(self, value):
        self.select_option(self.selected_metrocodes, value)

    def click_select_metrocodes_country(self):
        self.click_element(self.select_metrocodes)

    def click_remove_metrocodes_country(self):
        self.click_element(self.remove_metrocodes)

    def click_select_all_metrocodes_countries(self):
        self.click_element(self.select_all_metrocodes)

    def click_remove_all_metrocodes_countries(self):
        self.click_element(self.remove_all_metrocodes)

    def search_postal_codes(self, value):
        self.fill_field(self.postal_codes_search, value)

    def select_avail_postal_codes(self, value):
        self.select_option(self.avail_postal_codes, value)

    def select_applied_postal_codes(self, value):
        self.select_option(self.selected_postal_codes, value)

    def click_select_postal_codes(self):
        self.click_element(self.select_postal_codes)

    def click_remove_postal_codes(self):
        self.click_element(self.remove_postal_codes)

    def click_select_all_postal_codes(self):
        self.click_element(self.select_all_postal_codes)

    def click_remove_all_postal_codes(self):
        self.click_element(self.remove_all_postal_codes)

    def search_creatives(self, value):
        self.send_keys(self.creative_search, value)
        time.sleep(2)

    def clear_search(self):
        self.clear(self.creative_search)

    def select_all_creatives(self):
        self.click_element(self.master_select)

    def select_first_creative(self):
        self.click_element(self.first_select)

    def select_avail_audience(self, value, method = 'index'):
        self.select_option(self.avail_audience, value, method)

    def select_included_audience(self, value, method = 'index'):
        self.select_option(self.included_audience, value, method)

    def select_excluded_audience(self, value, method = 'index'):
        self.select_option(self.excluded_audience, value, method)

    def include_audience(self):
        self.click_element(self.move_included_audience)

    def exclude_audience(self):
        self.click_element(self.move_excluded_audience)

    def include_all_audience(self):
        self.click_element(self.move_all_included_audience)

    def exclude_all_audience(self):
        self.click_element(self.move_all_excluded_audience)

    def click_remove_audience(self):
        self.click_element(self.remove_audience)

    def click_remove_all_audience(self):
        self.click_element(self.remove_all_audience)

    def click_wifi_gateway(self):
        self.click_element(self.wifi)

    def click_carrier_gateway(self):
        self.click_element(self.carrier)

    def click_other_gateway(self):
        self.click_element(self.other)

    def click_environment_website(self):
        self.click_element(self.environment_websites)

    def click_environment_apps(self):
        self.click_element(self.environment_apps)

    def click_environment_other(self):
        self.click_element(self.environment_other)

    def select_carrier(self, value):
        self.select_option(self.mobile_carrier_avail, value)

    def select_applied_carrier(self, value):
        self.select_option(self.mobile_carrier_applied, value)

    def click_select_carrier(self):
        self.click_element(self.move_mobile_carrier)

    def click_remove_carrier(self):
        self.click_element(self.remove_mobile_carrier)

    def click_select_all_carrier(self):
        self.click_element(self.move_all_mobile_carrier)

    def click_remove_all_carrier(self):
        self.click_element(self.remove_all_mobile_carrier)

    def select_platform(self, value):
        self.select_option(self.mobile_platform_avail, value)

    def select_applied_platform(self, value):
        self.select_option(self.mobile_platform_applied, value)

    def click_select_platform(self):
        self.click_element(self.move_mobile_platform)

    def click_remove_platform(self):
        self.click_element(self.remove_mobile_platform)

    def click_select_all_platform(self):
        self.click_element(self.move_all_mobile_platform)

    def click_remove_all_platform(self):
        self.click_element(self.remove_all_mobile_platform)

    def filter_mobile_devices(self, value):
        self.fill_field(self.devices_filter, value)

    def select_designation_filter(self, value):
        self.select_option(self.designation_filter, value)

    def click_all_tabs(self):
        self.click_element(self.all_tabs)

    def click_all_smartphones(self):
        self.click_element(self.all_smartphones)

    def click_all_featurephones(self):
        self.click_element(self.all_feature_phones)

    def select_all_devices(self):
        self.click_element(self.master_select_devices)

    def expand_first(self):
        self.click_element(self.expand_first_model)

    def select_first_manufacturer(self):
        self.click_element(self.first_manufacturer)

    def select_first_model(self):
        self.click_element(self.first_model)

    def click_inherit_device_types(self):
        self.click_element(self.inherit_device_types)

    def click_override_device_types(self):
        self.click_element(self.override_device_types)

    def select_available_device_types(self, value):
        self.select_option(self.device_types_avail, value)

    def select_selected_device_types(self, value):
        self.select_option(self.device_types_applied, value)

    def click_move_selected(self):
        self.click_element(self.move_device_types)

    def click_remove_selected(self):
        self.click_element(self.remove_device_types)

    def click_move_all(self):
        self.click_element(self.move_all_device_types)

    def click_remove_all(self):
        self.click_element(self.remove_all_device_types)

    def assert_value(self, element, expected_value):
        element = self.find_element(getattr(self, element))
        actual_value = str(element.get_attribute('value')).strip()
        assert actual_value == expected_value, 'actual value is {0} , expected {1}'.format(actual_value, expected_value)

    def verify_selected_values(self, element, channel = None, channels = None):
        widget = self.find_element(getattr(self, element))
        select = Select(widget)
        selected = []
        for option in select.options:
            selected.append(option.text)
        if channel:
            assert channel in selected, 'option not present'
        else:
            for channel in channels:
                assert channel in selected, 'option not present'

    def get_audiences(self, element, index = 0):
        widget = self.find_element(getattr(self, element))
        select = Select(widget)
        selected = []
        for option in select.options:
            return option.text

    def search_devices(self):
        device = str(self.find_element(self.devices_td).get_attribute('innerHTML'))
        flag = device.find(str(self.inputs['search']))
        assert not flag < 0, 'searching devices not present'
