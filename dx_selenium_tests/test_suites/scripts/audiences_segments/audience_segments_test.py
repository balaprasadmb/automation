# -*- coding: utf-8 -*-
import uuid
import time
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from common_helpers.common_helpers import CommonHelper

class AudienceTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.setup(self.dx_constant.user_by_role['campaign_manager'])
        self.common_helper = CommonHelper()

    @test_case()
    def click_on_audience_tab_and_select_advertiser(self):
        self.pages.search_page.click_audience_link()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        self.pages.audience_segment_list_page.select_orgnization(self.dx_constant.advertiser_name)
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)

    @test_case()
    def check_audience_list_page_contents(self):
        self.click_on_audience_tab_and_select_advertiser()
        for content in self.pages.audience_segment_list_page.audience_list_page_contents:
            self.pages.audience_segment_list_page.page_should_contain(content)
        for element in self.pages.audience_segment_list_page.audience_list_page_elements:
            assert self.pages.audience_segment_list_page.is_element_present(getattr(self.pages.audience_segment_list_page, element))

    @test_case()
    def hide_audiences_checkbox_should_unchecked_default(self):
        assert not self.pages.audience_segment_list_page.find_element(self.pages.audience_segment_list_page.hide_audiences_checkbox).is_selected()

    @test_case()
    def functionality_of_hide_audiences_checkbox_checked(self):
        self.pages.audience_segment_list_page.check_hide_audiences_checkbox()
        self.pages.audience_segment_list_page.page_should_contain(self.pages.audience_segment_list_page.search_message)
        assert not self.pages.audience_segment_list_page.is_element_present(self.pages.audience_segment_list_page.first_audience_edit_icon)

    @test_case()
    def functionality_of_hide_audiences_checkbox_unchecked(self):
        self.pages.audience_segment_list_page.check_hide_audiences_checkbox()
        assert self.pages.audience_segment_list_page.is_element_present(self.pages.audience_segment_list_page.first_audience_edit_icon)
        self.pages.audience_segment_list_page.page_should_not_contain(self.pages.audience_segment_list_page.search_message)

    @test_case()
    def functionality_of_create_new_audiences_button(self):
        self.pages.audience_segment_list_page.click_on_create_new_audience_button()
        self.pages.audience_create_page.wait_till_visible(self.pages.audience_create_page.first_segment_checkbox)
        self.pages.audience_create_page.page_should_contain("Create a Composed Audience")

    @test_case()
    def create_audience_page_contents(self):
        for element in self.pages.audience_create_page.create_audience_page_elements:
            assert self.pages.audience_create_page.is_element_present(getattr(self.pages.audience_create_page, element))

    @test_case()
    def functionality_cancel_button_from_create_audience_page(self):
        self.pages.audience_create_page.click_cancel_button()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        assert self.pages.audience_segment_list_page.is_element_present(self.pages.audience_segment_list_page.create_new_audience_button)

    @test_case()
    def functionality_of_audience_name_link(self):
        expected_audience_name = self.pages.audience_segment_list_page.get_first_element_from_list("first_audience_name")
        self.pages.audience_segment_list_page.click_first_audience_name_link()
        self.pages.audience_show_page.wait_till_visible(self.pages.audience_show_page.audience_detail_section)
        self.pages.audience_show_page.page_should_contain(expected_audience_name)

    @test_case()
    def audience_show_page_contents(self):
        for page_content in self.pages.audience_show_page.audience_show_page_contents:
            self.pages.audience_show_page.page_should_contain(page_content)
        for element in self.pages.audience_show_page.audience_show_page_elements:
            assert self.pages.audience_show_page.is_element_present(getattr(self.pages.audience_show_page, element))

    @test_case()
    def functionality_of_currency_dropdown(self):
        self.pages.audience_show_page.select_currency("British Pound (GBP)")
        for element in self.pages.audience_show_page.currency_checklist:
            for loc in ['cost_value_after_currency_change', 'rate_card_value_after_currency_change']:
                assert element in self.pages.audience_show_page.get_inner_html_value(loc)

    @test_case()
    def functionality_of_edit_link_from_audience_show_page(self):
        self.pages.audience_show_page.click_edit_link()
        self.pages.audience_create_page.wait_till_visible(self.pages.audience_create_page.create_audience_button)
        self.pages.audience_create_page.page_should_contain("Edit Audience:")
        self.pages.audience_create_page.click_cancel_button()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)

    @test_case()
    def functionality_of_view_all_link_from_audience_show_page(self):
        self.pages.audience_segment_list_page.click_first_audience_name_link()
        self.pages.audience_show_page.wait_till_visible(self.pages.audience_show_page.audience_detail_section)
        expected_advertiser_name = self.pages.audience_show_page.get_inner_html_value('advertiser_link')
        self.pages.audience_show_page.click_view_all_link()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        actual_advertiser_name = self.pages.audience_segment_list_page.get_selected_advertiser_name()
        assert actual_advertiser_name in expected_advertiser_name

    @test_case()
    def functionality_of_edit_icon_from_audience_list_page(self):
        expected_audience_name = self.pages.audience_segment_list_page.get_first_element_from_list("first_audience_name")
        self.pages.audience_segment_list_page.click_first_edit_icon()
        self.pages.audience_create_page.wait_till_visible(self.pages.audience_create_page.create_audience_button)
        actual_audience_name = self.pages.audience_create_page.get_inner_html_value('audience_name_textbox', attribute = 'value')
        assert actual_audience_name in expected_audience_name
        self.pages.audience_create_page.page_should_contain("Edit Audience:")

    @test_case()
    def updating_existing_audience(self):
        audience_name = 'Updated-Audience-' + self.pages.audience_create_page.get_random_string(10)
        self.pages.audience_create_page.enter_audience_name(audience_name)
        if not self.pages.audience_create_page.find_element(self.pages.audience_create_page.use_advance_mode_checkbox).is_selected():
            self.pages.audience_create_page.click_use_advance_mode_checkbox()
        self.pages.audience_create_page.click_remove_button()
        self.pages.audience_create_page.click_composed_audience_master_checkbox()
        self.pages.audience_create_page.click_and_button()
        self.pages.audience_create_page.click_or_button()
        self.pages.audience_create_page.click_create_audience_button()
        self.pages.audience_show_page.wait_till_visible(self.pages.audience_show_page.audience_detail_section)
        self.pages.audience_show_page.page_should_contain(self.pages.audience_show_page.update_success_message.format(audience_name))

    @test_case()
    def creation_of_new_audience_and_search_with_valid_string(self):
        self.click_on_audience_tab_and_select_advertiser()
        self.functionality_of_create_new_audiences_button()
        expected_audience_name = 'New_Audience-' + self.pages.audience_create_page.get_random_string(10)
        self.pages.audience_create_page.select_first_segment_from_segment_table()
        self.pages.audience_create_page.select_first_audience_marketplace_from_audience_marketplace_table()
        self.pages.audience_create_page.click_use_advance_mode_checkbox()
        self.pages.audience_create_page.click_and_button()
        self.pages.audience_create_page.enter_audience_name(expected_audience_name)
        self.pages.audience_create_page.click_create_audience_button()
        self.pages.audience_show_page.wait_till_visible(self.pages.audience_show_page.audience_detail_section)
        self.pages.audience_show_page.page_should_contain(self.pages.audience_show_page.creation_sucess_message.format(expected_audience_name))
        self.click_on_audience_tab_and_select_advertiser()
        self.pages.audience_segment_list_page.search_audience(expected_audience_name)
        actual_audience_name = self.pages.audience_segment_list_page.get_first_element_from_list("first_audience_name")
        assert expected_audience_name in actual_audience_name

    @test_case()
    def search_with_invalid_string(self):
        self.pages.audience_segment_list_page.search_audience("abcd")
        self.pages.audience_segment_list_page.page_should_contain(self.pages.audience_segment_list_page.search_message)
        assert not self.pages.audience_segment_list_page.is_element_present(self.pages.audience_segment_list_page.first_audience_edit_icon)

    @test_case()
    def functionality_of_composed_audience_table(self):
        self.functionality_of_create_new_audiences_button()
        self.pages.audience_create_page.select_first_audience_marketplace_from_audience_marketplace_table()
        time.sleep(2)
        self.results = []
        for element in ['first_audience_marketplace_segment_name', 'first_audience_marketplace_rate_card_value', 'first_audience_marketplace_segment_size_value',
                        'first_composed_audience_name', 'first_composed_audience_rate_card_value', 'first_composed_audience_segment_size_value']:
            if element == 'first_composed_audience_rate_card_value':
                self.results.append(self.pages.audience_create_page.get_inner_html_value(element, attribute = 'value'))
            else:
                self.results.append(self.pages.audience_create_page.get_inner_html_value(element))
        for key, value in dict((self.results[i], self.results[i+3]) for i in range(0,3)).iteritems():
            assert value in key
        self.pages.audience_create_page.click_use_advance_mode_checkbox()
        audience_name = 'composed_audience-' + self.pages.audience_create_page.get_random_string(10)
        self.pages.audience_create_page.enter_audience_name(audience_name)
        self.pages.audience_create_page.click_create_audience_button()
        time.sleep(3)
        self.pages.audience_create_page.page_should_contain("Expression can't be blank")
        after_segment_name = self.pages.audience_create_page.get_inner_html_value('first_composed_audience_name')
        assert after_segment_name in self.results[3]
        expected_updated_rate_card_value = '5.66'
        self.pages.audience_create_page.enter_composed_audience_rate_card_value(expected_updated_rate_card_value)
        self.pages.audience_create_page.click_composed_audience_master_checkbox()
        self.pages.audience_create_page.click_and_button()
        self.pages.audience_create_page.click_create_audience_button()
        self.pages.audience_show_page.wait_till_visible(self.pages.audience_show_page.audience_detail_section)
        actual_update_rate_card_value = self.pages.audience_show_page.get_inner_html_value('rate_card_value')
        assert actual_update_rate_card_value in expected_updated_rate_card_value

    @test_case()
    def go_to_segment_list_page(self):
        self.click_on_audience_tab_and_select_advertiser()
        self.pages.audience_segment_list_page.click_segment_tab()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.segment_table)
        
    @test_case()
    def check_default_selected_segment_filter_dropdown_option(self):
        self.go_to_segment_list_page()
        expected_option = 'Active Only'
        actual_option = self.pages.audience_segment_list_page.get_dropdown_selected_value(self.pages.audience_segment_list_page.segment_filter_dropdown)
        assert expected_option == actual_option

    @test_case()
    def functionality_of_segment_filter_dropdwon(self):
        for option in ['Inactive Only', 'View All']:
            self.pages.audience_segment_list_page.select_option_from_segment_filter_dropdown(option)
            actual_option = self.pages.audience_segment_list_page.get_dropdown_selected_value(self.pages.audience_segment_list_page.segment_filter_dropdown)
            assert option == actual_option
            if option == 'View All':
                self.pages.audience_segment_list_page.is_element_present(self.pages.audience_segment_list_page.first_segment_name)

    @test_case()
    def segment_list_page_contents(self):
        for content in self.pages.audience_segment_list_page.segment_list_page_contents:
            self.pages.audience_segment_list_page.page_should_contain(content)
        for element in self.pages.audience_segment_list_page.segment_list_page_elements:
            assert self.pages.audience_segment_list_page.is_element_present(getattr(self.pages.audience_segment_list_page, element))
        self.pages.audience_segment_list_page.check_dropdown_options(self.pages.audience_segment_list_page.segment_filter_dropdown_options,
                                                       self.pages.audience_segment_list_page.segment_filter_dropdown)

    @test_case()
    def segment_create_page_contents(self):
        self.pages.audience_segment_list_page.click_on_create_first_party_segment_button()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        self.pages.segment_create_page.page_should_contain("Create new Segment for " + self.dx_constant.advertiser_name)
        for element in self.pages.segment_create_page.segment_create_page_elements:
            assert self.pages.segment_create_page.is_element_present(getattr(self.pages.segment_create_page, element))

    @test_case()
    def set_segment_name_and_save(self, segment_name):
        self.pages.segment_create_page.enter_segment_name(segment_name)
        self.pages.segment_create_page.click_on_create_segment_button()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)

    @test_case()
    def segment_with_blank_name(self):
        self.set_segment_name_and_save("")
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.segment_blank_name_error)

    @test_case()
    def segment_name_with_more_than_255_char(self):
        self.set_segment_name_and_save(self.pages.segment_create_page.get_random_string(256))
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.segment_name_255_error)

    @test_case()
    def set_expiration_field_value_and_save(self, expiration_value, unit):
        self.pages.segment_create_page.enter_segment_expiration_value(expiration_value)
        self.pages.segment_create_page.select_segment_expiration_unit(unit)
        self.pages.segment_create_page.click_on_create_segment_button()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)

    @test_case()
    def segment_expiration_days_with_more_than_upper_limit(self):
        self.pages.segment_create_page.enter_segment_name(self.pages.segment_create_page.get_random_string())
        self.set_expiration_field_value_and_save("5477", "days")
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.expiration_upper_limit_error)

    @test_case()
    def segment_expiration_days_with_zero(self):
        self.set_expiration_field_value_and_save("0", "days")
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.expiration_zero_error)

    @test_case()
    def segment_expiration_days_as_chars(self):
        self.set_expiration_field_value_and_save("abcd", "days")
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.expiration_chars_error)

    @test_case()
    def segment_expiration_hours_with_more_than_upper_limit(self):
        self.set_expiration_field_value_and_save("131405", "hours")
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.expiration_upper_limit_error)

    @test_case()
    def segment_expiration_hours_with_zero(self):
        self.set_expiration_field_value_and_save("0", "hours")
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.expiration_zero_error)

    @test_case()
    def segment_expiration_hours_as_chars(self):
        self.set_expiration_field_value_and_save("abcd", "hours")
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.expiration_chars_error)

    @test_case()
    def segment_expiration_minutes_with_more_than_upper_limit(self):
        self.set_expiration_field_value_and_save("7884005", "minutes")
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.expiration_upper_limit_error)

    @test_case()
    def segment_expiration_minutes_with_zero(self):
        self.set_expiration_field_value_and_save("0", "minutes")
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.expiration_zero_error)

    @test_case()
    def segment_expiration_minutes_as_chars(self):
        self.set_expiration_field_value_and_save("abcd", "minutes")
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.expiration_chars_error)

    @test_case()
    def functionality_of_cancel_button(self):
        self.pages.segment_create_page.click_on_cancel_button()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        assert self.pages.audience_segment_list_page.is_element_present(self.pages.audience_segment_list_page.create_first_party_segment_button)

    @test_case()
    def functionality_of_back_to_list_link(self):
        self.pages.audience_segment_list_page.click_on_create_first_party_segment_button()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        self.pages.segment_create_page.click_back_to_list_link()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        assert self.pages.audience_segment_list_page.is_element_present(self.pages.audience_segment_list_page.create_first_party_segment_button)

    @test_case()
    def fill_segments_fields_with_given_input(self, segment_name, expiration_value, expiration_unit):
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        self.pages.segment_create_page.enter_segment_name(segment_name)
        self.pages.segment_create_page.enter_segment_expiration_value(expiration_value)
        self.pages.segment_create_page.select_segment_expiration_unit(expiration_unit)
        self.pages.segment_create_page.click_on_create_segment_button()
        self.pages.segment_show_page.wait_till_visible(self.pages.segment_show_page.add_pixel_activity_button)

    @test_case()
    def creation_of_segment_with_given_input(self, segment_name, expiration_value, expiration_unit):
        self.pages.audience_segment_list_page.click_on_create_first_party_segment_button()
        self.fill_segments_fields_with_given_input(segment_name, expiration_value, expiration_unit)
        self.pages.segment_show_page.page_should_contain(self.pages.segment_show_page.segment_creation_success_message.format(segment_name))

    @test_case()
    def segment_with_255_chars_and_5475_expiration_days(self):
        segment_name = self.pages.audience_segment_list_page.get_random_string(255)
        self.creation_of_segment_with_given_input(segment_name, "5475", "days")

    @test_case()
    def update_segment(self, segment_name, expiration_value, expiration_unit):
        self.pages.segment_show_page.click_on_edit_link()
        self.fill_segments_fields_with_given_input(segment_name, expiration_value, expiration_unit)
        self.pages.segment_show_page.page_should_contain(self.pages.segment_show_page.segment_update_message.format(segment_name))

    @test_case()
    def segment_with_special_chars_and_131400_expiration_hours(self):
        segment_name = "!@#$%" + self.pages.segment_create_page.get_random_string(10)
        self.update_segment(segment_name, "131400", "hours")

    @test_case()
    def segment_with_valid_name_and_7884000_expiration_minutes(self):
        segment_name = self.pages.segment_create_page.get_random_string()
        self.update_segment(segment_name, "7884000", "minutes")

    @test_case()
    def functionality_of_add_pixel_activity_button(self):
        self.pages.segment_show_page.click_on_edit_link()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        self.pages.segment_create_page.click_on_add_pixel_activity_button()
        self.pages.segment_create_page.wait_till_element_clickable(self.pages.segment_create_page.pixel_popup_add_selected_button)
        for content in self.pages.segment_create_page.pixel_popup_contents:
            self.pages.segment_create_page.page_should_contain(content)
        for element in self.pages.segment_create_page.pixel_popup_elements:
            assert self.pages.segment_create_page.is_element_present(getattr(self.pages.segment_create_page, element))

    @test_case()
    def check_all_checkboxes_are_checked(self, criteria=True):
        elements = [self.pages.segment_create_page.pixel_popup_master_checkbox, self.pages.segment_create_page.pixel_popup_first_activity_checkbox]
        for element in elements:
            self.common_helper.assert_is_selected(self.pages.segment_create_page, element, criteria)

    @test_case()
    def functionality_of_pixel_popup_master_checkbox(self):
        self.pages.segment_create_page.click_on_pixels_master_checkbox()
        self.check_all_checkboxes_are_checked()
        self.pages.segment_create_page.click_on_pixels_master_checkbox()
        self.check_all_checkboxes_are_checked(criteria=False)

    @test_case()
    def functionality_of_pixel_popup_add_selected_button(self):
        self.pages.segment_create_page.search_activity_pixels("test-activity-")
        expected_pixel_name = self.pages.segment_create_page.get_innerhtml_text("pixel_popup_first_activity_name")
        self.pages.segment_create_page.select_first_pixel_activity_from_popup()
        self.pages.segment_create_page.click_on_add_selected_pixels_button()
        self.pages.segment_create_page.wait_till_element_clickable(self.pages.segment_create_page.create_segment_button)
        actual_pixel_name = self.pages.segment_create_page.get_innerhtml_text("added_pixel_activity_name")
        assert expected_pixel_name in actual_pixel_name

    @test_case()
    def functionality_of_edit_link_for_added_pixel_activity(self):
        expected_activity_name = self.pages.segment_create_page.get_innerhtml_text("added_pixel_activity_name")
        self.pages.segment_create_page.click_added_pixel_edit_link()
        self.pages.activity_edit_page.wait_till_visible(self.pages.activity_edit_page.create_activity_button)
        self.pages.activity_edit_page.page_should_contain("Edit activity")
        actual_activity_name = self.pages.activity_edit_page.get_activity_name()
        assert actual_activity_name in expected_activity_name

    @test_case()
    def functionality_of_show_link_from_segment_edit_page(self):
        self.pages.activity_edit_page.go_back()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        expected_segment_name = self.pages.segment_create_page.get_innerhtml_text("segment_name_text_box", "value")
        self.pages.segment_create_page.enter_segment_name(self.pages.segment_create_page.get_random_string())
        self.pages.segment_create_page.click_show_link()
        self.pages.segment_show_page.wait_till_visible(self.pages.segment_show_page.add_pixel_activity_button)
        self.pages.segment_show_page.page_should_contain(self.pages.segment_show_page.segment_show_page_heading.format(expected_segment_name))

    @test_case()
    def functionality_of_see_all_pixels_link(self):
        expected_advertiser_name = self.dx_constant.advertiser_name
        self.pages.segment_show_page.click_see_all_pixels_link()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        actual_advertiser_name = self.pages.activity_list_page.get_innerhtml_text("seleceted_organization_name")
        assert expected_advertiser_name == actual_advertiser_name
        assert self.pages.activity_list_page.is_element_present(self.pages.activity_list_page.create_activity_button)

    @test_case()
    def functionality_of_edit_link_from_list_page(self):
        self.pages.search_page.click_audience_link()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        self.pages.audience_segment_list_page.click_segment_tab()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.segment_table)
        self.pages.audience_segment_list_page.select_option_from_segment_filter_dropdown("View All")
        self.pages.audience_segment_list_page.click_first_segment_gear_icon()
        self.pages.audience_segment_list_page.click_first_segment_edit_link()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        self.pages.segment_create_page.page_should_contain("Update Segment:")

    @test_case()
    def functionality_of_view_all_link_from_segment_edit_page(self):
        self.pages.segment_create_page.click_view_all_link()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        assert self.pages.audience_segment_list_page.is_element_present(self.pages.audience_segment_list_page.create_first_party_segment_button)

    @test_case()
    def functionality_of_view_link_from_list_page(self):
        self.pages.audience_segment_list_page.click_segment_tab()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.segment_table)
        self.pages.audience_segment_list_page.select_option_from_segment_filter_dropdown("View All")
        self.pages.audience_segment_list_page.click_first_segment_gear_icon()
        self.pages.audience_segment_list_page.click_first_segment_view_link()
        self.pages.segment_show_page.wait_till_visible(self.pages.segment_show_page.add_pixel_activity_button)
        for content in self.pages.segment_show_page.segment_show_page_contents:
            self.pages.segment_show_page.page_should_contain(content)
        for element in self.pages.segment_show_page.segment_show_page_elements:
            assert self.pages.segment_show_page.is_element_present(getattr(self.pages.segment_show_page, element))

    @test_case()
    def functionality_of_view_all_link_from_segment_show_page(self):
        self.pages.segment_show_page.click_on_view_all_link()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        assert self.pages.audience_segment_list_page.is_element_present(self.pages.audience_segment_list_page.create_first_party_segment_button)

    @test_case()
    def segment_blank_expiration_field_and_existing_segment_name(self):
        expected_segment_name = self.pages.audience_segment_list_page.get_random_string()
        self.creation_of_segment_with_given_input(expected_segment_name, "", "days")
        self.pages.segment_show_page.page_should_contain("30 days")
        self.pages.segment_show_page.click_on_view_all_link()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        self.pages.audience_segment_list_page.click_on_create_first_party_segment_button()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        self.pages.segment_create_page.enter_segment_name(expected_segment_name)
        self.pages.segment_create_page.click_on_create_segment_button()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        self.pages.segment_create_page.page_should_contain("Name already exists for advertiser.")
        self.go_to_segment_list_page()
        self.pages.audience_segment_list_page.select_option_from_segment_filter_dropdown("View All")
        self.pages.audience_segment_list_page.search_segment(expected_segment_name)
        actual_segment_name = self.pages.audience_segment_list_page.get_first_element_from_list("first_segment_name")
        assert expected_segment_name in actual_segment_name
        self.pages.audience_segment_list_page.search_segment("abcd#")
        self.pages.audience_segment_list_page.page_should_contain("No segments match the applied filters.")

    @test_case()
    def segment_sharing(self):
        self.pages.audience_segment_list_page.click_on_create_first_party_segment_button()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        self.pages.segment_create_page.enter_segment_name(self.pages.segment_create_page.get_random_string())
        self.pages.segment_create_page.check_enable_sharing_checkbox()
        expected_organization_name = self.pages.segment_create_page.get_innerhtml_text("sharing_agency_group_name")
        self.pages.segment_create_page.check_organization_master_checkbox()
        self.pages.segment_create_page.click_on_create_segment_button()
        self.pages.segment_show_page.wait_till_visible(self.pages.segment_show_page.shared_organization_name)
        show_page_oraganization_name = self.pages.segment_show_page.get_innerhtml_text("shared_organization_name")
        assert expected_organization_name in show_page_oraganization_name
