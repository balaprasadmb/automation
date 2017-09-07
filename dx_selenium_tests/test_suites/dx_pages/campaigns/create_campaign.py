import csv
import xlrd
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from base.dx import Dx

class CreateCampaign(Dx):
    def fill_fields(self, campaign_attributes):
        self.type_campaign_name(campaign_attributes['campaign_name'])
        self.enter_start_date(campaign_attributes['start_date'])
        self.enter_insertion_order(campaign_attributes['order'])
        self.enter_cpa_goal(campaign_attributes['cpa'])
        self.enter_budget(campaign_attributes['budget'])
        self.enter_cpm(campaign_attributes['cpm'])
        self.enter_cogs(campaign_attributes['cogs'])
        self.enter_margin(campaign_attributes['margin'])

        if campaign_attributes['objective'] == 'performance':
            self.click_campaign_objective_performance()

            if campaign_attributes['model']:
                self.select_attribution_model(campaign_attributes['model'])

            if campaign_attributes['activity_pixel']:
                self.select_activity_pixel(campaign_attributes['activity_pixel'])

                if campaign_attributes['pixel_type']:
                     self.select_pixel_type(campaign_attributes['pixel_type'])

                if campaign_attributes['pixel_type'] == 'Conversion Pixel':
                     self.enter_conversion_pixel_value(campaign_attributes['pixel_value'])

                self.enter_filters(campaign_attributes['filters_value'])

                if campaign_attributes['tag_server']:
                     self.select_tag_server(campaign_attributes['tag_server'])
                self.enter_tag_id(campaign_attributes['tag_id'])
        elif campaign_attributes['objective'] == 'ctr':
            self.click_campaign_objective_ctr()
            self.wait_till_visible(['id', 'campaign_goal_ctr'])
            self.enter_goal_ctr(campaign_attributes['goal_ctr'])

        elif campaign_attributes['objective'] == 'distribution':
            self.click_campaign_objective_distribution()

        elif campaign_attributes['objective'] == 'views':
            self.click_campaign_objective_ad_views()

        self.click_add_new_tactic()
        if campaign_attributes['tactics']:
            self.select_tactic_name(campaign_attributes['tactics'])
            if campaign_attributes['tactics'] == 'Custom...':
                  self.enter_cutom_value(campaign_attributes['tactics_value'])
            self.enter_tactics_budget(campaign_attributes['tactics_budget'])
            self.enter_impression(campaign_attributes['icaps'])

        self.expand_add_on_cost()
        self.click_new_aoc()
        if campaign_attributes['aoc_name']:
            self.select_aoc_name(campaign_attributes['aoc_name'])

            if campaign_attributes['aoc_name'] == 'Custom...':
                self.enter_cutom_aoc_value(campaign_attributes['aoc_custom'])
            self.click_aoc_rate()
            self.enter_aoc_rate(campaign_attributes['aoc_rate'])

            if campaign_attributes['fee_type']:
                self.select_fee_type(campaign_attributes['fee_type'])

            if campaign_attributes['is_billable']:
                self.click_billable()

            if campaign_attributes['is_marketpalce']:
                self.click_is_marketplace()

        self.expand_external_ids()
        self.click_new_external_id()
        if campaign_attributes['source']:
            self.select_external_id_source(campaign_attributes['source'])
            self.enter_external_id_value(campaign_attributes['source_value'])

        self.expand_lang_targeting()

        if campaign_attributes['lang_target']:
            self.select_lang_targeting(campaign_attributes['lang_target'])
            self.click_move_selected_lang()

        if campaign_attributes['geo_target_type']:
            self.select_geo_targeting_type(campaign_attributes['geo_target_type'])
            if campaign_attributes['geo_target_type'] == 2:
                self.select_geo_target_country(campaign_attributes['geo_target_type'])
            if campaign_attributes['geo_target_type'] == 0:
                self.upload_geofenced_file(campaign_attributes['geofenced_file'])
                self.enter_geofenced_group_name(campaign_attributes['geofenced_group_name'])
                self.click_geofenced_submit()

        if campaign_attributes['geo_target']:
            self.select_avail_countries(campaign_attributes['geo_target'])
            self.click_move_selected_country()

        self.expand_brand_safety()
        if campaign_attributes['brand_safety_level']:
            brand_safety_configuration = { '1': 'click_brand_safety_level_one', '2': 'click_brand_safety_level_two',
                                          '3': 'click_brand_safety_level_three', '4': 'click_brand_safety_level_four' }
            getattr(self, brand_safety_configuration[campaign_attributes['brand_safety_level']])()
        self.enter_end_date(campaign_attributes['end_date'])
        self.click_element(self.campaign_name)
        self.wait_till_element_clickable(self.create_campaign_button)
        self.submit()

    def type_campaign_name(self, campaign):
        self.clear_and_send_value(campaign, self.campaign_name)

    def enter_start_date(self, start_date):
        self.send_keys(self.campaign_start_date, start_date)

    def click_start_date(self):
        self.click_element(self.campaign_start_date)

    def enter_end_date(self, end_date):
        self.send_keys(self.campaign_end_date, end_date)
        self.fill_field(self.campaign_end_date, Keys.ESCAPE)
        time.sleep(2)

    def enter_insertion_order(self, value):
        self.fill_field(self.insertion_order, value)

    def click_end_date(self):
        self.click_element(self.campaign_end_date)

    def select_cost_model(self, value):
        self.select_option(self.cost_model, value)

    def enter_cpa_goal(self, cpa):
        self.send_keys(self.cpa_goal, cpa)

    def enter_budget(self, budget):
        self.send_keys(self.order_budget, budget)

    def enter_cpm(self, cpm):
        self.send_keys(self.campaign_cpm, cpm)

    def enter_cogs(self, cogs):
        self.send_keys(self.campaign_cogs, cogs)

    def enter_margin(self, margin):
        self.send_keys(self.campaign_margin, margin)

    def click_auto_cruise_control(self):
        self.click_element(self.cruise_control_auto)

    def click_adhere_to_tactic(self):
        self.click_element(self.cruise_control_adhere)

    def click_campaign_objective_performance(self):
        self.click_element(self.campaign_objective_performance)

    def select_attribution_model(self, value):
        self.select_option(self.model, value)

    def select_activity_pixel(self, index):
        self.select_option(self.activity, index, 'index')

    def select_pixel_type(self, pixel):
        self.select_option(self.pixel, pixel)

    def enter_conversion_pixel_value(self, value):
        self.send_keys(self.pixel_value, value)

    def enter_filters(self, value):
        self.send_keys(self.filter, value)

    def select_tag_server(self, value):
        self.select_option(self.tag_server, value)

    def enter_tag_id(self, value):
        self.fill_field(self.tag_id, value)

    def click_bulk_assign_click(self):
        self.click_element(self.bulk_assign_pixel)

    def search_available_bulk_pixel(self, value):
        self.send_keys(self.bulk_available_search, value)

    def select_bulk_available_activities(self, activity_list):
        select = Select(self.find_element(self.bulk_available_activities))
        for activity in activity_list:
            select.select_by_visible_text(activity)

    def select_one_available_activity(self, activity):
        self.select_option(self.bulk_available_activities, activity)

    def enter_bulk_conversion_pixel_value(self, value):
        self.fill_field(self.pixel_type_learning, value)

    def click_add_pixel(self):
        self.wait_till_visible(self.add_pixel)
        self.click_element(self.add_pixel)

    def click_remove_activity(self):
        try:
            self.click_element(self.remove_activity)
        except (ElementNotVisibleException, NoSuchElementException):
            self.click_element(self.remove_bulk_asssign_pixel_activity)

    def close_popup(self):
        self.click_element(self.bulk_assign_popup_close)

    def click_campaign_objective_ctr(self):
        self.click_element(self.campaign_objective_ctr)

    def enter_goal_ctr(self, value):
        self.fill_field(self.campaign_goal_ctr, value)

    def click_campaign_objective_distribution(self):
        self.click_element(self.campaign_objective_distribution)

    def click_campaign_objective_ad_views(self):
        self.click_element(self.campaign_objective_ad_views)

    def select_vendor(self, value):
        self.select_option(self.viewability_vendor, value)

    def select_category(self, value):
        self.select_option(self.category, value)

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

    def enter_impression_caps(self, value):
        self.fill_field(self.impression_caps, value)

    def click_add_new_tactic(self):
        self.click_element(self.new_tactics)

    def select_tactic_name(self, value):
        self.select_option(self.tactic_name, value)
        time.sleep(1)

    def enter_tactics_budget_second(self , value):
       self.fill_field(self.tactics_budget_second, value)

    def enter_cutom_value(self, value):
        self.fill_field(self.custom_field, value)

    def enter_tactics_budget(self, value):
        self.fill_field(self.tactics_budget, value)

    def enter_impression(self, value):
        self.fill_field(self.tactics_impression, value)

    def remove_tactics(self):
        self.click_element(self.remove_tactics)

    def click_new_aoc(self):
        self.click_element(self.new_add_on_cost)
        time.sleep(2)

    def click_view_change_histry(self):
        self.click_element(self.view_change_history)

    def select_aoc_name(self, value):
        self.select_option(self.add_on_cost_name, value)

    def select_aoc_name_second(self, value):
        self.select_option(self.add_on_cost_name_second, value)

    def enter_cutom_aoc_value(self, value):
        self.clear_and_send_value(value, self.add_on_cost_custom)

    def enter_custom_aoc_value_second(self, value):
        self.clear_and_send_value(value, self.add_on_cost_custom_second)

    def click_aoc_rate(self):
        self.click_element(self.add_on_cost_rate)

    def click_aoc_rate_second(self):
        self.click_element(self.add_on_cost_rate_second)

    def enter_aoc_rate(self, value):
        self.clear_and_send_value(value, self.add_on_cost_rate)

    def enter_aoc_rate_second(self, value):
        self.clear_and_send_value(value, self.add_on_cost_rate_second)

    def select_fee_type(self, value):
        self.select_option(self.add_on_cost_fee_type, value)

    def click_billable(self):
        self.click_element(self.add_on_cost_billable)

    def click_is_marketplace(self):
        self.click_element(self.add_on_cost_marketplace)

    def click_on_remove_aoc_button(self):
        self.click_element(self.remove_add_on_cost)

    def click_on_remove_aoc_button_second(self):
        self.click_element(self.remove_add_on_cost_second)

    def click_new_external_id(self):
        self.click_element(self.new_external_ids)

    def select_external_id_source(self,value):
        self.select_option(self.external_id_source, value)

    def enter_external_id_value(self, value):
        self.fill_field(self.external_id_value, value)

    def remove_external_id(self):
        self.click_element(self.remove_external_id)

    def select_lang_targeting(self, value):
        self.select_option(self.lang_targeting_available, value)

    def click_move_selected_lang(self):
        self.click_element(self.move_selected_lang)

    def click_remove_selected_lang(self):
        self.click_element(self.remove_selected_lang)

    def click_move_all_selected_lang(self):
        self.click_element(self.move_all_selected_lang)

    def click_remove_all_selected_lang(self):
        self.click_element(self.remove_all_selected_lang)

    def select_lang_targeting_selected(self, value):
        self.select_option(self.lang_targeting_selected, value)

    def select_geo_targeting_type(self, value):
        self.select_option(self.geo_target_type, value, 'index')

    def search_avail_countries(self, value):
        self.send_keys(self.country_available_search, value)

    def select_avail_countries(self, value):
        self.select_option(self.country_available, value)

    def select_applied_countries(self, value):
        self.select_option(self.country_selected, value)

    def click_move_selected_country(self):
        self.click_element(self.move_selected_country)

    def click_remove_selected_country(self):
        self.click_element(self.remove_selected_country)

    def click_move_all_selected_countries(self):
        self.click_element(self.move_all_selected_country)

    def click_remove_all_selected_countries(self):
        self.click_element(self.remove_all_selected_country)

    def select_geo_target_country(self, value):
        self.select_option(self.geo_target_country_id, value)

    def select_area_type(self, value):
        self.select_option(self.geo_target_area_type, value ,'index')

    def search_avail_regions(self, value):
        self.send_keys(self.region_search, value)

    def select_avail_regions(self, value):
        self.select_option(self.avail_regions, value)

    def select_applied_regions(self, value):
        self.select_option(self.applied_regions, value)

    def click_move_selected_regions(self):
        self.click_element(self.move_selected_regions)

    def click_remove_selected_regions(self):
        self.click_element(self.remove_selected_regions)

    def click_move_all_selected_regions(self):
        self.click_element(self.move_all_selected_regions)

    def click_remove_all_selected_regions(self):
        self.click_element(self.remove_all_selected_regions)

    def search_metrocodes(self, value):
        self.send_keys(self.metrocodes_search, value)

    def select_avail_metrocodes(self, value):
        self.select_option(self.avail_metrocodes, value)

    def select_applied_metrocodes(self, value):
        self.select_option(self.applied_metrocodes, value)

    def click_move_selected_metrocodes(self):
        self.click_element(self.move_selected_metrocodes)

    def click_remove_selected_metrocodes(self):
        self.click_element(self.remove_selected_metrocodes)

    def click_move_all_selected_metrocodes(self):
        self.click_element(self.move_all_selected_metrocodes)

    def click_remove_all_selected_metrocodes(self):
        self.click_element(self.remove_all_selected_metrocodes)

    def upload_geofenced_file(self, value):
        self.fill_field(self.geofenced_file, value)

    def enter_geofenced_group_name(self, value):
        self.clear_and_send_value(value, self.geofenced_name)

    def click_geofenced_submit(self):
        self.click_element(self.geofenced_submit)

    def search_postalcodes(self, value):
        self.send_keys(self.postal_codes_search, value)

    def select_avail_postalcodes(self, value):
        self.select_option(self.avail_postal_codes, value)

    def select_applied_postalcodes(self, value):
        self.select_option(self.applied_postal_codes, value)

    def click_move_selected_postalcodes(self):
        self.click_element(self.move_selected_postal_codes)

    def click_remove_selected_postalcodes(self):
        self.click_element(self.remove_selected_postal_codes)

    def click_move_all_selected_postalcodes(self):
        self.click_element(self.move_all_selected_postal_codes)

    def click_remove_all_selected_postalcodes(self):
        self.click_element(self.remove_all_selected_postal_codes)

    def upload_postalcode_file(self, value):
        self.fill_field(self.postal_code_upload, value)

    def enter_postalcode_group_name(self, value):
        self.send_keys(self.postal_code_group_name, value)

    def click_postalcode_submit(self):
        self.click_element(self.postal_code_group_submit)

    def click_brand_safety_level_one(self):
        self.click_element(self.brand_safety_level_one)

    def click_brand_safety_level_two(self):
        self.click_element(self.brand_safety_level_two)

    def click_brand_safety_level_three(self):
        self.click_element(self.brand_safety_level_three)

    def click_brand_safety_level_four(self):
        self.click_element(self.brand_safety_level_four)

    def submit(self):
        self.click_element(self.create_campaign_button)

    def expand_impression_caps(self):
        self.click_element(self.impression)

    def enter_impression_caps(self, value):
        self.fill_field(self.impression_caps, value)

    def expand_tactics(self):
        self.click_element(self.tactics)

    def expand_add_on_cost(self):
        self.click_element(self.add_on_cost)
        time.sleep(2)

    def expand_external_ids(self):
        self.click_element(self.external_ids)

    def expand_lang_targeting(self):
        self.click_element(self.lang_targeting)

    def expand_brand_safety(self):
        self.click_element(self.brand_safety)

    def expand_whitelist(self):
        self.click_element(self.whitelist)

    def expand_blacklist(self):
        self.click_element(self.blacklist)

    def wait_for_campaign_details(self):
        self.wait_till_visible(self.campaign_details)

    def wait_for_bulk_assign_pixel(self):
        self.wait_till_visible(self.bulk_assign_pixel_popup)

    def wait_for_upload_error_message(self):
        self.wait_till_visible(self.geotargeting_upload_error)

    def wait_for_upload_success_message(self):
        self.wait_till_visible(self.geohash_upload_successfully)

    def select_bulk_pixel_type(self, value):
        self.select_option(self.pixel_type_value, value)

    def get_first_activity(self):
        select = Select(self.find_element(self.bulk_available_activities))
        for option in select.options:
            return option.text

    def get_first_pixel_type(self):
        select = Select(self.find_element(self.pixel))
        for option in select.options:
            if option.is_selected():
                return option.text

    def hover_and_visible(self, element, popover):
        ActionChains(self.driver).move_to_element(self.find_element(getattr(self, element))).perform()
        return True if EC.visibility_of_element_located(getattr(self, popover)) else False

    def assert_dropdown_options_not_in(self,loc,dropdown_option):
        widget=self.find_element(loc)
        select = Select(widget)
        for option in select.options:
            if option.text == dropdown_option:
                raise AssertionError

    def select_tactic_retargeting(self):
        self.select_tactic_name('Retargeting')

    def select_tactic_optimized(self):
        self.select_option(self.tactic_name_second, 'Optimized')

    def click_single_device(self):
        self.click_element(self.single_device_enabled)
        time.sleep(2)

    def click_high_precision(self):
        self.click_element(self.high_precision_enabled)

    def click_broad_reach(self):
        self.click_element(self.broad_reach_enabled)

    def click_oneview_popup_ok(self):
        self.click_element(self.oneview_popup_ok)

    def click_oneview_popup_cancel(self):
        self.click_element(self.oneview_popup_cancel)

    def get_investment_available_in_market(self):
        return self.get_content_text(self.investment_available_in_market)

    def get_impressions_available_in_market(self):
        return self.get_content_text(self.impressions_available_in_market)

    def get_impressions_budget(self):
        return self.get_content_text(self.impressions_budget)

    def click_oneview_popup_ok(self):
        self.click_element(self.oneview_popup_ok)

    def click_oneview_popup_cancel(self):
        self.click_element(self.oneview_popup_cancel)

    def check_dropdown_options(self, expected_list, loc):
        select = Select(self.find_element(loc))
        actual_list = []
        for opt in select.options:
            actual_list.append(opt.text)
        for option in expected_list:
            assert option in actual_list, "Actaul/Obtained list :- {0}/{1}".format(option, actual_list)

    def enter_budget_for_default_tactic(self, default_tactic_budget):
        self.send_keys(self.default_tactic_budget, default_tactic_budget)

    def enter_impression_cap_for_default_tactic(self, default_tactic_impression):
        self.send_keys(self.default_tactic_impression, default_tactic_impression)
