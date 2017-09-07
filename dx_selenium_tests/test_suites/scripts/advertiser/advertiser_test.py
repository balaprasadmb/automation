# -*- coding: utf-8 -*-
import os
import time

from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from common_helpers.common_helpers import CommonHelper

class AdvertiserTest(DXTest):

    @test_case()
    def login_as_advertiser_manager(self):
        self.common_helper = CommonHelper()
        self.setup(self.dx_constant.user_by_role['system_level_organization_administrator_three'])

    def open_new_advertiser_page(self):
        self.pages.new_advertiser_page.open()

    def open_advertiser_list_page(self):
        self.pages.advertiser_list_page.open()

    @test_case()
    def validate_presence_of_new_inventories(self):
        self.open_new_advertiser_page()
        time.sleep(5)
        inventory_list = self.pages.new_advertiser_page.get_content_text_list(self.pages.new_advertiser_page.advertiser_invenotry_supplier_label)
        for inventory in self.dx_constant.new_inventory_list:
            assert inventory in inventory_list, '{0} inventory is not available'.format(inventory)

    @test_case()
    def assert_is_element_present(self, page_object, loc, criteria=True):
        self.common_helper.assert_is_element_present(page_object, loc, criteria)

    @test_case()
    def validate_add_on_cost_section_permission_user(self):
        for element in self.pages.new_advertiser_page.add_on_cost_headers:
            self.assert_is_element_present(self.pages.new_advertiser_page, self.pages.new_advertiser_page.add_on_cost_section_headers[element].values())
        self.assert_is_element_present(self.pages.new_advertiser_page, 'new_add_on_cost')
        self.pages.new_advertiser_page.click_new_add_on_cost_button()
        for element in self.pages.new_advertiser_page.add_on_cost_controls:
            self.assert_is_element_present(self.pages.new_advertiser_page, element)

    @test_case()
    def validate_channel_dropdown_guaranteed_media_permission(self):
        self.pages.new_advertiser_page.check_dropdown_options(self.dx_constant.add_on_cost_channel_options, self.pages.new_advertiser_page.add_on_cost_channel)

    @test_case()
    def add_on_cost_delete_functionality(self):
        self.element_count = len(self.pages.new_advertiser_page.find_elements(self.pages.new_advertiser_page.add_on_cost_name))
        self.pages.new_advertiser_page.remove_add_on_cost_functionality()
        count = len(self.pages.new_advertiser_page.find_elements(self.pages.new_advertiser_page.add_on_cost_name))
        assert count < self.element_count, count

    @test_case()
    def validate_grayed_out_field(self):
        for element in self.pages.new_advertiser_page.grayed_out_controls:
            self.assert_is_element_present(self.pages.new_advertiser_page, element)
        self.assert_is_element_present(self.pages.new_advertiser_page, 'agency_group_grayed_out', criteria=False)

    @test_case()
    def validate_agency_grayed_out(self):
        self.pages.new_advertiser_page.select_agency_group('DataXu Managed Services')
        time.sleep(10)
        self.assert_is_element_present(self.pages.new_advertiser_page, 'agency_grayed_out', criteria=False)
        self.pages.new_advertiser_page.select_agency_group(0, 'index')
        self.assert_is_element_present(self.pages.new_advertiser_page, 'agency_grayed_out')
        time.sleep(3)

    @test_case()
    def validate_cogs_value_inherited(self):
        data = self.pages.new_advertiser_page.get_content_value(self.pages.new_advertiser_page.cogs_textbox)
        assert data != '', data
        self.assert_is_selected(self.pages.new_advertiser_page, 'cogs_inherited_checkbox')

    def check_data(self, page_object, element_name, editable=False):
        element_locator = self.dx_constant.default_setting_element
        checkbox_locator = self.dx_constant.default_setting_locator
        data = page_object.get_content_value(getattr(page_object, element_locator[element_name]))
        if editable:
            assert data == '', data
            self.assert_is_selected(page_object, checkbox_locator[element_name], criteria=False)
        else:
            assert data != '', data
            self.assert_is_selected(page_object, checkbox_locator[element_name])

    @test_case()
    def validate_cogs_checkbox_editable(self):
        self.pages.new_advertiser_page.click_cogs_inherited_value_checkbox()
        self.check_data(self.pages.new_advertiser_page, 'cogs', editable=True)

    @test_case()
    def validate_cogs_currency(self):
        data = self.pages.new_advertiser_page.get_content_text(self.pages.new_advertiser_page.cogs_currency)
        assert data == 'USD', data

    @test_case()
    def validate_margin_value_inherited(self):
        data = self.pages.new_advertiser_page.get_content_value(self.pages.new_advertiser_page.margin_textbox)
        assert data != '', data
        self.assert_is_selected(self.pages.new_advertiser_page, 'margin_inherited_checkbox')

    @test_case()
    def validate_margin_checkbox_editable(self):
        self.pages.new_advertiser_page.click_margin_inherited_value_checkbox()
        data = self.pages.new_advertiser_page.get_content_value(self.pages.new_advertiser_page.margin_textbox)
        assert data == '', data

    @test_case()
    def validate_contracted_currency_grayed_out(self):
        self.assert_is_element_present(self.pages.new_advertiser_page, 'disabled_currency_drop_down')

    @test_case()
    def validate_select_all_currency_checkbox(self):
        self.pages.new_advertiser_page.check_select_all_currencies()
        self.assert_is_selected(self.pages.new_advertiser_page, 'euro_currency_checkbox')
        self.pages.new_advertiser_page.check_select_all_currencies()
        self.assert_is_selected(self.pages.new_advertiser_page, 'euro_currency_checkbox', criteria=False)

    @test_case()
    def assert_is_selected(self, page_object, loc, criteria=True):
        self.common_helper.assert_is_selected(page_object, loc, criteria)

    @test_case()
    def validate_individual_checkbox(self):
        self.pages.new_advertiser_page.check_select_all_currencies()
        self.assert_is_selected(self.pages.new_advertiser_page, 'select_all_currency')
        self.pages.new_advertiser_page.check_select_all_currencies()
        self.assert_is_selected(self.pages.new_advertiser_page, 'select_all_currency', criteria=False)
        self.pages.new_advertiser_page.click_inherit_licenses_checkbox()
        self.assert_is_selected(self.pages.new_advertiser_page, 'inherit_licensing_checkbox', criteria=False)
        self.pages.new_advertiser_page.select_all_inventory()
        self.assert_is_selected(self.pages.new_advertiser_page, 'select_all_inventories')
        self.pages.new_advertiser_page.select_all_inventory()
        self.assert_is_selected(self.pages.new_advertiser_page, 'select_all_inventories', criteria=False)
        self.pages.new_advertiser_page.click_inherit_licenses_checkbox()
        self.assert_is_selected(self.pages.new_advertiser_page, 'inherit_licensing_checkbox')

    @test_case()
    def validate_grayed_out_fields(self):
        for element in self.pages.new_advertiser_page.grayed_out_field:
            if element == 'inherit_licensing_checkbox':
                self.assert_is_selected(self.pages.new_advertiser_page, 'inherit_licensing_checkbox')
            else:
                self.assert_is_element_present(self.pages.new_advertiser_page, element)

    @test_case()
    def validate_inherit_value_checkbox_functionality(self):
        self.pages.new_advertiser_page.click_inherit_licenses_checkbox()
        self.assert_is_selected(self.pages.new_advertiser_page, 'inherit_licensing_checkbox', criteria=False)
        for element in self.pages.new_advertiser_page.inherit_value_controls:
            self.assert_is_element_present(self.pages.new_advertiser_page, element, criteria=False)

    @test_case()
    def validate_media_types(self):
        for media_type in self.pages.new_advertiser_page.media_types:
            self.assert_is_element_present(self.pages.new_advertiser_page, self.pages.new_advertiser_page.online_media_type_checkbox[media_type].values())

    @test_case()
    def validate_available_inventory_supplier(self):
        element_list = self.pages.new_advertiser_page.find_elements(self.pages.new_advertiser_page.advertiser_invenotry_supplier_label)
        for element in element_list:
            actual_inventory_supplier = self.pages.new_advertiser_page.get_content_text(element)
            assert actual_inventory_supplier in self.dx_constant.invenotry_supplier_label_list, "{0} inventory supplier not found in expected list".format(actual_inventory_supplier)

    @test_case()
    def validate_available_insights(self):
        self.pages.new_advertiser_page.click_inherit_licenses_checkbox()
        for insight in self.dx_constant.insight_element:
            self.assert_is_element_present(self.pages.new_advertiser_page, self.pages.new_advertiser_page.insights[insight].values())

    @test_case()
    def validate_configure_seat_section(self):
        for insight in self.pages.new_advertiser_page.configure_seat_controls:
            self.assert_is_element_present(self.pages.new_advertiser_page, self.pages.new_advertiser_page.configure_seat_section[insight].values())
        seat_names = self.pages.new_advertiser_page.get_content_text_list(self.pages.new_advertiser_page.seat_names_locator)
        available_seats = self.dx_constant.configure_seat_name
        for seat_name in seat_names:
            if seat_name:
                assert seat_name.encode() in available_seats, "{0} found new in this list".format(seat_name)

    @test_case()
    def validate_dfa_seat_under_configure_seat_section(self):
        self.pages.new_advertiser_page.select_platform_type("Intelligence")
        seat_names = self.pages.new_advertiser_page.get_content_text_list(self.pages.new_advertiser_page.seat_names_locator)
        assert "DFA" in seat_names

    @test_case()
    def validate_contents_of_list_page(self):
        self.open_advertiser_list_page()
        assert 'Advertisers' == self.pages.advertiser_list_page.get_content_text(self.pages.advertiser_list_page.page_header)
        for element in self.pages.advertiser_list_page.list_page_contents:
            self.assert_is_element_present(self.pages.advertiser_list_page, element)

    @test_case()
    def validate_edit_icon_on_list_page(self):
        self.pages.advertiser_list_page.click_first_edit_icon()
        time.sleep(10)
        assert 'Edit Organization' == self.pages.advertiser_edit_page.get_content_text(self.pages.advertiser_edit_page.page_header).encode()
        self.pages.advertiser_edit_page.go_back()

    @test_case()
    def fill_fields_with_blank_value(self):
        attributes = self.pages.new_advertiser_page.attributes
        attributes['email'] = '@dataxu.com'
        self.pages.new_advertiser_page.fill_fields(attributes)
        self.message_list = self.pages.new_advertiser_page.error_message_for_blank

    @test_case()
    def message_validator(self, message_key):
        page_object = self.get_page_object()
        page_object.page_should_contain(self.message_list[message_key])

    @test_case()
    def validate_add_on_cost_name_with_blank(self):
        self.message_validator('add_on_cost_name')

    @test_case()
    def validate_add_on_cost_cpm_with_blank(self):
        self.message_validator('add_on_cost_cpm')

    @test_case()
    def validate_advertiser_name_with_blank(self):
        self.message_validator('advertiser_name')

    @test_case()
    def fill_fields_with_260_character(self):
        long_string = self.pages.new_advertiser_page.get_random_characters(260)
        long_number = self.pages.new_advertiser_page.get_random_digits(260)
        attributes = self.pages.new_advertiser_page.attributes
        for key, value in attributes.iteritems():
            attributes[key] = long_string
        attributes['add_on_cost_value'] = long_number
        attributes['rate_card'] = os.getcwd() + '/data/rate_cards/rate_card_PLN.xls'
        self.pages.new_advertiser_page.fill_fields(attributes)
        self.message_list = self.pages.new_advertiser_page.error_message_for_260_characters

    @test_case()
    def validate_add_on_cost_name_with_260_char(self):
        self.message_validator('add_on_cost_name')

    @test_case()
    def validate_add_on_cost_cpm_with_260_char(self):
        self.message_validator('add_on_cost_cpm')

    @test_case()
    def validate_advertiser_name_with_260_char(self):
        self.message_validator('advertiser_name')

    @test_case()
    def validate_email_with_260_char(self):
        self.message_validator('email')

    @test_case()
    def validate_contact_name_with_260_char(self):
        self.message_validator('contact_name')

    @test_case()
    def validate_rate_card_with_other_currency(self):
        self.message_validator('rate_card')

    @test_case()
    def fill_fields_with_special_char(self):
        long_string = "!@#$_" + self.pages.new_advertiser_page.get_random_string(5)
        self.pages.new_advertiser_page.type_email('test@')
        self.pages.new_advertiser_page.type_contact_name(long_string)
        self.pages.new_advertiser_page.click_cogs_inherited_value_checkbox()
        self.pages.new_advertiser_page.type_cogs_value(11)
        self.pages.new_advertiser_page.click_margin_inherited_value_checkbox()
        self.pages.new_advertiser_page.type_margin_value(101)
        self.pages.new_advertiser_page.click_create_advetiser_button()
        self.message_list = self.pages.new_advertiser_page.error_message_for_special_char

    @test_case()
    def validate_contact_name_with_special_char(self):
        self.message_validator('contact_name')

    @test_case()
    def validate_cogs_value_more_than_10(self):
        self.pages.new_advertiser_page.page_should_contain(self.pages.new_advertiser_page.cogs_more_than_10)

    @test_case()
    def validate_margin_value_more_than_100(self):
        self.pages.new_advertiser_page.page_should_contain(self.pages.new_advertiser_page.margin_more_than_100)

    @test_case()
    def validate_email_with_invalid_value(self):
        self.message_validator('email')

    @test_case()
    def fill_fields_with_html_tag(self):
        html_tag_value = self.dx_constant.html_tag
        self.pages.new_advertiser_page.type_organization_name(html_tag_value)
        self.pages.new_advertiser_page.type_email(html_tag_value)
        self.pages.new_advertiser_page.type_contact_name(html_tag_value)
        self.pages.new_advertiser_page.type_margin_value(-1)
        self.pages.new_advertiser_page.click_create_advetiser_button()
        self.message_list = self.pages.new_advertiser_page.error_message_for_html_tag

    @test_case()
    def validate_contact_name_with_html_tag(self):
        self.message_validator('contact_name')

    @test_case()
    def validate_margin_value_with_negative_value(self):
        self.message_validator('margin')

    @test_case()
    def validate_email_with_html_tag(self):
        self.message_validator('email')

    @test_case()
    def validate_advertiser_name_with_html_tag(self):
        self.message_validator('advertiser_name')

    @test_case()
    def validate_margin_with_alphanumeric_value(self):
        self.pages.new_advertiser_page.type_margin_value("abcdefg1234")
        self.pages.new_advertiser_page.click_create_advetiser_button()
        self.pages.new_advertiser_page.page_should_contain(self.pages.new_advertiser_page.error_message_for_alphanumeric['margin'])

    @test_case()
    def validate_margin_with_special_char(self):
        self.pages.new_advertiser_page.type_margin_value("!@#$")
        self.pages.new_advertiser_page.click_create_advetiser_button()
        self.pages.new_advertiser_page.page_should_contain(self.pages.new_advertiser_page.error_message_for_special_char['margin'])

    @test_case()
    def validate_agency_list_appearance(self):
        self.assert_is_element_present(self.pages.new_advertiser_page, 'agency_grayed_out')
        self.pages.new_advertiser_page.select_agency_group("DataXu Managed Services")
        time.sleep(5)
        self.assert_is_element_present(self.pages.new_advertiser_page, 'agency_grayed_out', criteria=False)
        self.pages.new_advertiser_page.select_agency(2, 'index')

    @test_case()
    def validate_currency_for_cpm(self):
        self.pages.new_advertiser_page.click_new_add_on_cost_button()
        self.pages.new_advertiser_page.check_dropdown_options(['CPM (USD)'], self.pages.new_advertiser_page.add_on_cost_fee_type)
        self.pages.new_advertiser_page.remove_add_on_cost_functionality()

    @test_case()
    def validate_oba_compliance_section(self):
        for element in self.pages.new_advertiser_page.oba_controls:
            self.assert_is_element_present(self.pages.new_advertiser_page, element)
        for message in self.pages.new_advertiser_page.oba_message:
            self.pages.new_advertiser_page.page_should_contain(message)

    @test_case()
    def fill_fields_with_valid_data(self):
        self.pages.new_advertiser_page.click_inherit_licenses_checkbox()
        self.pages.new_advertiser_page.select_inventories(self.dx_constant.inventory_list)
        insight_list = self.pages.new_advertiser_page.insight_list
        for insight in insight_list: 
            self.pages.new_advertiser_page.select_insights(insight)
        if self.pages.new_advertiser_page.find_element(self.pages.new_advertiser_page.cogs_inherited_checkbox).is_selected():
            self.pages.new_advertiser_page.click_cogs_inherited_value_checkbox()
        if self.pages.new_advertiser_page.find_element(self.pages.new_advertiser_page.margin_inherited_checkbox).is_selected():
            self.pages.new_advertiser_page.click_margin_inherited_value_checkbox()
        self.pages.new_advertiser_page.type_cogs_value('0.155')
        self.pages.new_advertiser_page.type_margin_value('0.155')
        long_string = self.pages.new_advertiser_page.get_random_characters(255)
        attributes = self.pages.new_advertiser_page.attributes
        for key, value in attributes.iteritems():
            attributes[key] = long_string
        attributes['email'] = long_string[:244] + '@dataxu.com'
        attributes['primary_domain'] = 'www.yahoo.com'
        attributes['add_on_cost_value'] = '3.3333212'
        attributes['rate_card'] = os.getcwd() + '/data/rate_cards/rate_card_USD.xls'
        self.advertiser_name = long_string
        self.pages.new_advertiser_page.fill_fields(attributes)

    @test_case()
    def add_on_cost_helper(self, page_object, element_list, attribute):
        flag = False
        data = '$3.3333212' if attribute == 'fractional penny' else self.advertiser_name
        for element in element_list:
            if data == page_object.get_content_text(element):
                flag = True
                break
        assert flag is True

    @test_case()
    def validate_fractional_penny_add_on_cost(self):
        self.pages.advertiser_list_page.type_advertiser_name_in_filterbox(self.advertiser_name)
        time.sleep(5)
        self.pages.advertiser_list_page.click_element(self.pages.advertiser_list_page.advertiser_name_link)
        element_list = self.pages.advertiser_details_page.find_elements(self.pages.advertiser_details_page.add_on_cost_rate)
        self.add_on_cost_helper(self.pages.advertiser_details_page, element_list, 'fractional penny')

    @test_case()
    def validate_valid_name_for_add_on_cost(self):
        element_list = self.pages.advertiser_details_page.find_elements(self.pages.advertiser_details_page.add_on_cost_name)
        self.add_on_cost_helper(self.pages.advertiser_details_page, element_list, 'valid name')

    @test_case()
    def validate_add_on_cost_name_with_255_character(self):
        self.validate_valid_name_for_add_on_cost()

    @test_case()
    def validate_valid_value_for_add_on_cost(self):
        element_list = self.pages.advertiser_details_page.find_elements(self.pages.advertiser_details_page.add_on_cost_rate)
        self.add_on_cost_helper(self.pages.advertiser_details_page, element_list, 'fractional penny')

    @test_case()
    def validate_proper_email_id(self):
        message = self.pages.advertiser_list_page.success_message
        self.pages.advertiser_list_page.page_should_contain(message.format(self.advertiser_name))

    @test_case()
    def validate_contact_name_with_255_char(self):
        self.validate_proper_email_id()

    @test_case()
    def validate_cogs_value_less_than_10(self):
        self.assert_data(self.pages.advertiser_details_page, 'cogs_value', '$0.16')

    @test_case()
    def validate_valid_rate_card(self):
        self.validate_proper_email_id()

    @test_case()
    def assert_data(self, page_object, locator, raw_data):
        data = page_object.get_content_text(getattr(page_object, locator)).encode()
        assert data == raw_data, "expected / actual     {0}/{1}".format(raw_data, data)

    @test_case()
    def validate_margin_value_less_than_100(self):
        self.assert_data(self.pages.advertiser_details_page, 'margin_value', '0.155')

    @test_case()
    def validate_same_currency_on_view_page(self):
        self.assert_data(self.pages.advertiser_details_page, 'contracted_currency_on_show_page', 'United States Dollar (USD)')

    @test_case()
    def validate_margin_accept_decimal_numbers(self):
        self.validate_proper_email_id()

    @test_case()
    def validate_show_page_content(self):
        for element in self.pages.advertiser_details_page.show_page_content:
            self.assert_is_element_present(self.pages.advertiser_details_page, element)

    @test_case()
    def validate_details_content(self):
        time.sleep(5)
        for element in self.pages.advertiser_details_page.details_section_content:
            self.assert_is_element_present(self.pages.advertiser_details_page, self.pages.advertiser_details_page.details_section_elements[element].values())

    @test_case()
    def link_navigation_helper(self, text, pause_time):
        self.pages.advertiser_details_page.page_should_contain(text)
        self.pages.advertiser_details_page.go_back()
        time.sleep(pause_time)

    @test_case()
    def validate_link_navigation_on_show_page(self):
        self.pages.advertiser_details_page.go_to_advertiser_list_page()
        time.sleep(10)
        self.assert_is_element_present(self.pages.advertiser_list_page, 'search_box')
        self.pages.advertiser_details_page.go_back()
        time.sleep(5)
        self.pages.advertiser_details_page.go_to_link('Review Blocked Publishers')
        time.sleep(15)
        self.link_navigation_helper('Blocked publisher and site list', 3)
        self.pages.advertiser_details_page.go_to_first_agency_in_list()
        time.sleep(5)
        self.link_navigation_helper('Agency', 3)
        self.pages.advertiser_details_page.go_to_agency_group()
        time.sleep(5)
        self.link_navigation_helper('Agency Group', 3)
        self.pages.advertiser_details_page.click_edit_details()
        time.sleep(5)
        self.pages.advertiser_details_page.page_should_contain('Edit Organization')

    @test_case()
    def validate_edit_page_content(self):
        for element in self.pages.advertiser_edit_page.edit_page_content:
            self.assert_is_element_present(self.pages.advertiser_edit_page, element)

    @test_case()
    def validate_details_content_on_edit_page(self):
        for element in self.pages.advertiser_edit_page.details_section_content:
            self.assert_is_element_present(self.pages.advertiser_edit_page, element)

    @test_case()
    def validate_checked_inventories_on_edit_page(self):
        for inventory in self.dx_constant.inventory_list:
            assert self.pages.advertiser_edit_page.is_element_present([self.pages.advertiser_edit_page.inventory_locator[0], self.pages.advertiser_edit_page.inventory_locator[1].format(inventory)])

    @test_case()
    def validate_insights_checked_on_edit_page(self):
        for element in self.dx_constant.insight_element:
            self.assert_is_selected(self.pages.advertiser_edit_page, self.pages.advertiser_edit_page.insights[element].values())

    @test_case()
    def validate_currency_grayed_out_on_edit_page(self):
        self.assert_is_element_present(self.pages.advertiser_edit_page, 'disabled_currency_drop_down')

    @test_case()
    def get_error_message(self, page_object, index):
        message = page_object.get_content_text(['css selector', '#errorExplanation > ul> li:nth-child({0})'.format(index)]).encode()
        return message

    @test_case()
    def validate_invalid_email_id(self):
        self.pages.advertiser_edit_page.type_email('@dataxu.com')
        self.pages.advertiser_edit_page.upload_rate_card(os.getcwd() + '/data/rate_cards/rate card_CAD.xls')
        self.pages.advertiser_edit_page.click_create_advetiser_button()
        time.sleep(2)
        message = self.get_error_message(self.pages.advertiser_edit_page, 2)
        assert self.pages.advertiser_edit_page.error_message_for_email == message

    @test_case()
    def validate_other_than_contracted_currency_on_edit_page(self):
        message = self.get_error_message(self.pages.advertiser_edit_page, 1)
        assert self.pages.advertiser_edit_page.error_message['rate_card_with_different_currency'] == message

    @test_case()
    def validate_invalid_email_id_2(self):
        self.pages.advertiser_edit_page.type_email('test@')
        self.pages.advertiser_edit_page.click_create_advetiser_button()
        time.sleep(2)
        message = self.get_error_message(self.pages.advertiser_edit_page, 1)
        assert self.pages.advertiser_edit_page.error_message_for_email == message

    @test_case()
    def validate_save_button_functionality_on_edit_page(self):
        self.advertiser_name = 'test_advertiser_' + self.pages.advertiser_edit_page.get_random_digits(10)
        self.pages.advertiser_edit_page.type_organization_name(self.advertiser_name)
        self.pages.advertiser_edit_page.type_email('')
        self.pages.advertiser_edit_page.type_contact_name('')
        self.pages.advertiser_edit_page.click_create_advetiser_button()
        self.pages.advertiser_details_page.page_should_contain(self.pages.advertiser_details_page.success_message.format(self.advertiser_name))
        if self.pages.advertiser_details_page.is_element_present(self.pages.advertiser_details_page.edit_details_button):
            assert self.pages.advertiser_details_page.is_element_present(self.pages.advertiser_details_page.edit_details_button)

    @test_case()
    def validate_cancel_button_functionality_on_edit_page(self):
        self.pages.advertiser_details_page.click_edit_details()
        time.sleep(2)
        advertiser = 'test_advertiser_aurus_dataxu'
        self.pages.advertiser_edit_page.type_organization_name(advertiser)
        self.pages.advertiser_edit_page.click_cancel_button()
        time.sleep(2)
        self.assert_data(self.pages.advertiser_details_page, 'header', 'Advertiser {0}'.format(self.advertiser_name))
        data = self.pages.advertiser_details_page.get_content_text(self.pages.advertiser_details_page.header).encode()
        assert not data == "Advertiser test_advertiser_aurus_dataxu"
        if self.pages.advertiser_details_page.is_element_present(self.pages.advertiser_details_page.edit_details_button):
            self.assert_is_element_present(self.pages.advertiser_details_page, 'edit_details_button')

    @test_case()
    def validate_new_advertiser_button(self):
        if not self.pages.advertiser_list_page.is_element_present(self.pages.advertiser_list_page.new_advertiser): 
            self.open_advertiser_list_page()
        if self.pages.advertiser_list_page.is_element_present(self.pages.advertiser_list_page.new_advertiser):
            self.pages.advertiser_list_page.click_on_new_advrtiser_button()
            time.sleep(10)
        self.assert_is_element_present(self.pages.new_advertiser_page, 'organization_name')
        self.pages.new_advertiser_page.go_back()
        time.sleep(5)

    @test_case()
    def validate_search_icon(self):
        self.pages.advertiser_list_page.type_advertiser_name_in_filterbox(self.advertiser_name)
        time.sleep(3)
        self.assert_is_element_present(self.pages.advertiser_list_page, 'advertiser_name_link')
        self.pages.advertiser_list_page.type_advertiser_name_in_filterbox("Python_Automated_Test_Invalid_Advertiser")
        time.sleep(3)
        self.assert_is_element_present(self.pages.advertiser_list_page, 'advertiser_name_link', criteria=False)

    @test_case()
    def validate_cancel_button_functionality(self):
        self.pages.advertiser_list_page.type_advertiser_name_in_filterbox(self.advertiser_name)
        time.sleep(3)
        self.pages.advertiser_list_page.click_first_delete_icon()
        self.pages.advertiser_list_page.dismiss_alert()
        assert self.pages.advertiser_list_page.is_element_present(['link text', self.advertiser_name])

    @test_case()
    def validate_delete_icon(self):
        self.pages.advertiser_list_page.click_first_delete_icon()
        self.pages.advertiser_list_page.accept_alert()
        time.sleep(10)
        self.pages.advertiser_list_page.page_should_contain(self.pages.advertiser_list_page.delete_message.format(self.advertiser_name))

    @test_case()
    def validate_ok_button_functionality(self):
        self.pages.advertiser_list_page.page_should_contain(self.pages.advertiser_list_page.delete_message.format(self.advertiser_name))

    @test_case()
    def validate_advertiser_name_link_functionality(self):
        if self.pages.advertiser_list_page.is_element_present(self.pages.advertiser_list_page.new_advertiser):
            self.pages.advertiser_list_page.click_first_advertiser()
        self.assert_is_element_present(self.pages.advertiser_details_page, 'edit_details_button')

    @test_case()
    def fill_field_with_digits(self):
        self.open_new_advertiser_page()
        self.pages.new_advertiser_page.select_agency_group('DataXu Managed Services')
        time.sleep(10)
        self.pages.new_advertiser_page.select_agency(2, 'index')
        self.pages.new_advertiser_page.click_inherit_licenses_checkbox()
        self.pages.new_advertiser_page.select_inventories(self.dx_constant.uncheck_inventory_list)
        long_string = self.pages.new_advertiser_page.get_random_characters(240)
        long_number = self.pages.new_advertiser_page.get_random_digits(10)
        self.add_on_cost_value = self.pages.new_advertiser_page.get_random_digits(250) + "3.233"
        attributes = self.pages.new_advertiser_page.attributes
        attributes['organization_name'] = long_string + long_number + "!@#$%"
        attributes['primary_domain'] = 'www.yahoo.com'
        attributes['add_on_cost_name'] = '14526'
        attributes['add_on_cost_value'] = "3.333"
        self.advertiser_name = long_string
        self.pages.new_advertiser_page.fill_fields(attributes)

    @test_case()
    def validate_add_on_cost_name_with_digits(self):
        self.list_page_helper()
        add_on_cost_name_list = self.pages.advertiser_details_page.get_content_text_list(self.pages.advertiser_details_page.add_on_cost_name)
        assert "14526" in add_on_cost_name_list

    @test_case()
    def validate_advertiser_name_with_255_chars(self):
        data = self.pages.advertiser_list_page.get_content_text(self.pages.advertiser_list_page.success_message_locator)
        assert "was successfully created." in data
        self.assert_is_element_present(self.pages.advertiser_list_page, 'new_advertiser')

    @test_case()
    def validate_insights_unchecked_on_edit_page(self):
        self.pages.advertiser_details_page.click_edit_details()
        self.pages.advertiser_edit_page.wait_till_visible(self.pages.advertiser_edit_page.save_advertiser_button, 50)
        for element in self.dx_constant.insight_element:
            self.assert_is_selected(self.pages.advertiser_edit_page, self.pages.advertiser_edit_page.insights[element].values(), criteria=False)

    @test_case()
    def validate_unchecked_inventories_on_edit_page(self):
        for inventory in self.dx_constant.inventory_list:
            self.assert_is_element_present(self.pages.advertiser_edit_page, [self.pages.advertiser_edit_page.inventory_locator[0], self.pages.advertiser_edit_page.inventory_locator[1].format(inventory)])

    @test_case()
    def validate_configure_seat_pop_up(self):
        self.open_new_advertiser_page()
        assert 'Inheriting Seat' in self.pages.new_advertiser_page.get_content_text(self.pages.new_advertiser_page.configure_seats_pop_up['seat_content'].values())
        self.pages.new_advertiser_page.click_seats_edit_icon()
        for element in self.pages.new_advertiser_page.configure_seat_pop_up:
            self.assert_is_element_present(self.pages.new_advertiser_page, self.pages.new_advertiser_page.configure_seats_pop_up[element].values())

    @test_case()
    def edit_configure_seat(self):
        self.pages.new_advertiser_page.click_seats_override_radio_button()
        self.pages.new_advertiser_page.type_seat_name('test')
        self.pages.new_advertiser_page.type_seat_id('123')
        self.pages.new_advertiser_page.click_seats_ok_button()
        assert 'test - 123' in self.pages.new_advertiser_page.get_content_text(self.pages.new_advertiser_page.configure_seats_pop_up['seat_content'].values())

    @test_case()
    def add_on_cost_value_helper(self):
        self.pages.new_advertiser_page.select_agency_group('DataXu Managed Services')
        time.sleep(10)
        self.pages.new_advertiser_page.select_agency(2, 'index')

    @test_case()
    def list_page_helper(self):
        self.pages.advertiser_list_page.type_advertiser_name_in_filterbox(self.advertiser_name)
        time.sleep(3)
        self.pages.advertiser_list_page.click_first_advertiser()

    @test_case()
    def validate_add_on_cost_rate_less_than_100(self):
        self.open_new_advertiser_page()
        self.add_on_cost_value_helper()
        attributes = self.pages.new_advertiser_page.attributes
        attributes['organization_name'] = 'test_advertiser' + self.pages.new_advertiser_page.get_random_digits(10)
        attributes['primary_domain'] = 'www.yahoo.com'
        attributes['add_on_cost_name'] = 'test_add_on_cost'
        attributes['add_on_cost_value'] = "112"
        self.pages.new_advertiser_page.fill_fields(attributes)
        time.sleep(5)
        self.pages.new_advertiser_page.page_should_contain(self.pages.new_advertiser_page.add_on_cost_cpm_more_than_100)
        self.add_on_cost_value_helper()
        self.pages.new_advertiser_page.click_new_add_on_cost_button()
        self.pages.new_advertiser_page.type_add_on_cost_name('test_add_on_cost')
        self.pages.new_advertiser_page.type_add_on_cost_rate('99')
        self.pages.new_advertiser_page.click_seats_edit_icon()
        self.edit_configure_seat()
        self.pages.new_advertiser_page.click_create_advetiser_button()
        self.advertiser_name = attributes['organization_name']
        self.list_page_helper()
        element_list = self.pages.advertiser_details_page.find_elements(self.pages.advertiser_details_page.add_on_cost_rate)
        self.advertiser_name = '$99.00'
        self.add_on_cost_helper(self.pages.advertiser_details_page, element_list, 'add on cost rate')

    @test_case()
    def validate_seat_configuration_on_show_page(self):
        assert 'test - 123' in self.pages.advertiser_details_page.get_content_text(self.pages.advertiser_details_page.seat_content)

    def media_type_helper(self, media_type):
        self.open_new_advertiser_page()
        self.pages.new_advertiser_page.click_inherit_licenses_checkbox()
        if not self.pages.new_advertiser_page.find_element(self.pages.new_advertiser_page.online_media_type_checkbox[media_type].values()).is_selected():
            self.pages.new_advertiser_page.click_media_type_checkbox(media_type)
        self.pages.new_advertiser_page.select_agency_group('DataXu Managed Services')
        time.sleep(10)
        self.pages.new_advertiser_page.select_agency(2, 'index')
        attributes = self.pages.new_advertiser_page.attributes
        attributes['organization_name'] = 'test_advertiser' + self.pages.new_advertiser_page.get_random_digits(10)
        attributes['primary_domain'] = 'www.yahoo.com'
        attributes['add_on_cost_name'] = 'test_add_on_cost'
        attributes['add_on_cost_value'] = "99"
        self.pages.new_advertiser_page.fill_fields(attributes)
        self.advertiser_name = attributes['organization_name']
        self.list_page_helper()
        self.assert_is_element_present(self.pages.advertiser_details_page, 'edit_details_button')
        self.pages.advertiser_details_page.click_edit_details()
        self.assert_is_selected(self.pages.advertiser_edit_page, self.pages.advertiser_edit_page.online_media_type_checkbox[media_type].values())
        self.pages.advertiser_edit_page.click_media_type_checkbox(media_type)
        self.pages.advertiser_edit_page.click_create_advetiser_button()
        time.sleep(3)
        self.pages.advertiser_details_page.click_edit_details()
        self.assert_is_selected(self.pages.advertiser_edit_page, self.pages.advertiser_edit_page.online_media_type_checkbox[media_type].values(), criteria=False)

    @test_case()
    def validate_online_is_checked(self):
        self.media_type_helper("online")

    @test_case()
    def validate_mobile_is_checked(self):
        self.media_type_helper("mobile")

    @test_case()
    def validate_video_is_checked(self):
        self.media_type_helper("video")
