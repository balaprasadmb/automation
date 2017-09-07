# -*- coding: utf-8 -*-
import os
import time

from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from lib.custom_exception import CustomException


class AgencyGroupTest(DXTest):
    organization_name = None
    add_on_cost_value = None
    element_count = None

    @test_case()
    def login_as_agency_group_manager(self):
        self.success_message = self.pages.new_agency_group_page.success_message['organization_name']
        self.locator = self.pages.new_agency_group_page.green_tick
        self.setup(self.dx_constant.user_by_role['system_level_organization_administrator_two'])

    @test_case()
    def open_new_agency_group_page(self):
        self.pages.new_agency_group_page.open()

    @test_case()
    def fill_all_fields(self, new_agency_group, attributes_dictionary):
        self.pages.new_agency_group_page.fill_fields(attributes_dictionary)

    @test_case()
    def fill_fields_with_blank_data(self):
        self.open_new_agency_group_page()
        blank_dict = getattr(self.pages.new_agency_group_page, 'attributes')
        for key in blank_dict.keys():
            blank_dict[key] = ''
        self.fill_all_fields(self.pages.new_agency_group_page, blank_dict)

    @test_case()
    def validate_blank_scenario(self, element_name):
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.blank_message[element_name])

    @test_case()
    def validate_blank_organization_name(self):
        self.validate_blank_scenario('organization_name')

    @test_case()
    def validate_blank_rate_card_path(self):
        self.validate_blank_scenario('rate_card')

    @test_case()
    def validate_blank_add_on_cost_name(self):
        self.validate_blank_scenario('add_on_cost_name')

    @test_case()
    def validate_blank_add_on_cost_cpm_value(self):
        self.validate_blank_scenario('add_on_cost_value')

    @test_case()
    def fill_fields_with_html_tag(self):
        attribute_dict = self.pages.new_agency_group_page.attributes
        for key, value in attribute_dict.iteritems():
            attribute_dict[key] = self.dx_constant.html_tag
        attribute_dict['rate_card'] = os.getcwd() + '/lib/dx_date.py'
        attribute_dict['add_on_cost_value'] = '-1'
        self.fill_all_fields(self.pages.new_agency_group_page, attribute_dict)

    @test_case()
    def validate_rate_card_with_invalid_file(self):
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.error_message['rate_card_invalid_file'])

    def validate_html_tag(self, element_name):
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.html_tag[element_name])

    @test_case()
    def validate_organization_with_html_tag(self):
        self.validate_html_tag('organization_name')

    @test_case()
    def validate_email_with_html_tag(self):
        self.validate_html_tag('email')

    @test_case()
    def validate_contact_name_with_html_tag(self):
        self.validate_html_tag('contact_name')

    def fill_fields_with_special_char(self):
        self.open_new_agency_group_page()
        attribute_dict = self.pages.new_agency_group_page.attributes
        for key, value in attribute_dict.iteritems():
                attribute_dict[key] = self.dx_constant.special_char
        attribute_dict['add_on_cost_value'] = '100'
        attribute_dict['rate_card'] = os.getcwd() + '/data/rate_cards/rate card_CAD.xls'
        self.pages.new_agency_group_page.click_cogs_inherited_value_checkbox()
        self.pages.new_agency_group_page.click_margin_inherited_value_checkbox()
        self.pages.new_agency_group_page.type_cogs_value(self.dx_constant.special_char)
        self.pages.new_agency_group_page.type_margin_value(self.dx_constant.special_char)
        self.fill_all_fields(self.pages.new_agency_group_page, attribute_dict)

    def validate_with_special_char(self, element_name):
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.special_character_message[element_name])

    @test_case()
    def validate_cogs_with_special_char(self):
        self.validate_with_special_char('cogs_special_char')

    @test_case()
    def validate_margin_with_special_char(self):
        self.validate_with_special_char('margin_special_char')

    @test_case()
    def validate_contact_name_with_special_char(self):
        self.validate_with_special_char('contact_name')

    @test_case()
    def validate_add_on_cost_cpm_negative_value(self):
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.negative_value['add_on_cost_value'])

    @test_case()
    def validate_rate_card_with_different_currency(self):
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.different_currency['rate_card'])

    def fill_fields_with_260_char(self):
        self.open_new_agency_group_page()
        attribute_dict = self.pages.new_agency_group_page.attributes
        new_value = self.pages.new_agency_group_page.get_random_digits(260)
        for key, value in attribute_dict.iteritems():
                attribute_dict[key] = new_value
        attribute_dict['rate_card'] = os.getcwd() + '/data/rate_cards/rate_card_USD.xls'
        attribute_dict['add_on_cost_value'] = 101
        self.fill_all_fields(self.pages.new_agency_group_page, attribute_dict)

    def validate_with_long_char(self, element_name):
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.long_char[element_name])

    @test_case()
    def validate_add_on_cost_name_with_260_char(self):
        self.validate_with_long_char('add_on_cost_name')

    @test_case()
    def validate_add_on_cost_cpm_value_with_260_char(self):
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.long_char['add_on_cost_value'].format(str(101)))

    @test_case()
    def validate_organization_with_260_char(self):
        self.validate_with_long_char('organization_name')

    @test_case()
    def validate_email_with_260_char(self):
        self.validate_with_long_char('email')

    @test_case()
    def validate_contact_with_260_char(self):
        self.validate_with_long_char('contact_name')

    def fill_fields_with_255_char(self):
        self.open_new_agency_group_page()
        attribute_dict = self.pages.new_agency_group_page.attributes
        new_value = self.pages.new_agency_group_page.get_random_string(255)
        self.organization_name = new_value
        for key, value in attribute_dict.iteritems():
                attribute_dict[key] = new_value
        attribute_dict['email'] = new_value[:244] + '@dataxu.com'
        attribute_dict['add_on_cost_name'] = self.pages.new_agency_group_page.get_random_digits(255)
        attribute_dict['add_on_cost_value'] = '100'
        attribute_dict['rate_card'] = os.getcwd() + '/data/rate_cards/rate_card_USD.xls'
        self.pages.new_agency_group_page.click_cogs_inherited_value_checkbox()
        self.pages.new_agency_group_page.click_margin_inherited_value_checkbox()
        self.pages.new_agency_group_page.type_cogs_value('9')
        self.pages.new_agency_group_page.type_margin_value('99')
        self.fill_all_fields(self.pages.new_agency_group_page, attribute_dict)

    @test_case()
    def validate_add_on_cost_name_with_255_char(self):
        self.pages.new_agency_group_page.check_success_message(self.success_message['create_new_agency_group'].format(self.organization_name))

    def validate_with_255_char(self):
        self.pages.new_agency_group_page.check_success_message(self.success_message['create_new_agency_group'].format(self.organization_name))

    @test_case()
    def validate_organization_name_with_255_char(self):
        self.validate_with_255_char()

    @test_case()
    def validate_add_on_cost_name_accepts_digit(self):
        self.validate_with_255_char()

    @test_case()
    def validate_email_with_255_char(self):
        self.validate_with_255_char()

    @test_case()
    def validate_contact_name_with_255_char(self):
        self.validate_with_255_char()

    @test_case()
    def validate_add_on_cost_cpm_value_with_100(self):
        self.validate_with_255_char()

    @test_case()
    def validate_rate_card_with_valid_file(self):
        self.validate_with_255_char()

    @test_case()
    def validate_same_currency_on_view_page(self):
        self.pages.new_agency_group_page.page_should_contain('United States Dollar (USD)')

    @test_case()
    def validate_cogs_value_less_than_10(self):
        data = self.pages.agency_group_details_page.get_content_text(self.pages.agency_group_details_page.cogs_value)
        assert data == '$9.00', data

    @test_case()
    def validate_margin_value_less_than_100(self):
        data = self.pages.agency_group_details_page.get_content_text(self.pages.agency_group_details_page.margin_value)
        assert data == '99.0', data

    @test_case()
    def validate_cogs_value_inherited(self):
        self.open_new_agency_group_page()
        data = self.pages.new_agency_group_page.get_content_value(self.pages.new_agency_group_page.cogs_inherited_value_textbox)
        assert data != '', data
        assert self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.cogs_inherited_value_checkbox).is_selected()

    @test_case()
    def validate_individual_checkbox_functionality(self):
        self.pages.new_agency_group_page.check_select_all_currencies()
        assert self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.select_all_currency).is_selected()
        self.pages.new_agency_group_page.check_select_all_currencies()
        assert not self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.select_all_currency).is_selected()
        self.pages.new_agency_group_page.click_inherit_licenses_checkbox()
        assert not self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.inherit_licensing_checkbox).is_selected()
        self.pages.new_agency_group_page.select_all_inventory()
        assert self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.select_all_inventories).is_selected()
        self.pages.new_agency_group_page.select_all_inventory()
        assert not self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.select_all_inventories).is_selected()
        self.pages.new_agency_group_page.click_inherit_licenses_checkbox()
        assert self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.inherit_licensing_checkbox).is_selected()

    @test_case()
    def validate_page_title(self):
        self.pages.new_agency_group_page.page_should_contain('Create New Organization')

    @test_case()
    def validate_add_on_cost_value_with_respect_to_currency(self):
        self.pages.new_agency_group_page.select_currency_from_listbox('Euro (EUR)')
        option_list = ['CPM (EUR)']
        self.pages.new_agency_group_page.check_dropdown_options(option_list, self.pages.new_agency_group_page.add_on_cost_fee_type)
        self.pages.new_agency_group_page.select_currency_from_listbox('United States Dollar (USD)')

    @test_case()
    def validate_media_types(self):
        self.pages.new_agency_group_page.click_inherit_licenses_checkbox()
        for media_type in ['online', 'mobile', 'video']:
            assert self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.online_media_type_checkbox[media_type].values())

    @test_case()
    def validate_available_inventory_supplier(self):
        self.pages.new_agency_group_page.click_inherit_licenses_checkbox()
        element_list = self.pages.new_agency_group_page.find_elements(self.pages.new_agency_group_page.agency_group_invenotry_supplier_label)
        for element in element_list:
            assert self.pages.new_agency_group_page.get_content_text(element) in self.dx_constant.invenotry_supplier_label_list

    @test_case()
    def validate_available_insights(self):
        self.pages.new_agency_group_page.click_inherit_licenses_checkbox()
        for insight in ['frequency', 'consideration', 'retargeting', 'index']:
            assert self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.insights[insight].values())

    @test_case()
    def validate_presence_of_new_inventories(self):
        inventory_list = self.pages.new_agency_group_page.get_content_text_list(self.pages.new_agency_group_page.agency_group_invenotry_supplier_label)
        for inventory in self.dx_constant.new_inventory_list:
            assert inventory in inventory_list, '{0} inventory is not available'.format(inventory)

    @test_case()
    def validate_configure_seat_pop_up(self):
        assert 'Inheriting Seat' in self.pages.new_agency_group_page.get_content_text(self.pages.new_agency_group_page.configure_seats_pop_up['seat_content'].values())
        self.pages.new_agency_group_page.click_seats_edit_icon()
        for element in ['inherit_checkbox', 'override_checkbox', 'ok_button', 'cancel_button']:
            assert self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.configure_seats_pop_up[element].values())

    @test_case()
    def edit_configure_seat(self):
        self.pages.new_agency_group_page.click_seats_override_radio_button()
        self.pages.new_agency_group_page.type_seat_name('test')
        self.pages.new_agency_group_page.type_seat_id('123')
        self.pages.new_agency_group_page.click_seats_ok_button()
        assert 'test - 123' in self.pages.new_agency_group_page.get_content_text(self.pages.new_agency_group_page.configure_seats_pop_up['seat_content'].values())

    @test_case()
    def validate_organization_type_grayed_out(self):
        assert self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.organization_type)

    @test_case()
    def validate_add_on_cost_section_permission_user(self):
        for element in ['name', 'cpm', 'billable', 'channel']:
            assert self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.add_on_cost_section_headers[element].values())
        assert self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.new_add_on_cost)
        self.pages.new_agency_group_page.click_new_add_on_cost_button()
        for element in ['add_on_cost_name', 'add_on_cost_value', 'add_on_cost_billable_checkbox', 'add_on_cost_channel', 'remove_add_on_cost']:
            assert self.pages.new_agency_group_page.is_element_present(getattr(self.pages.new_agency_group_page, element))

    @test_case()
    def validate_channel_dropdown_guaranteed_media_permission(self):
        self.pages.new_agency_group_page.check_dropdown_options(self.dx_constant.add_on_cost_channel_options, self.pages.new_agency_group_page.add_on_cost_channel)

    @test_case()
    def validate_currency_for_add_on_cost_CPM_field(self):
        self.pages.new_agency_group_page.click_new_add_on_cost_button()
        self.pages.new_agency_group_page.select_add_on_cost_fee_type('CPM (USD)')
        self.element_count = len(self.pages.new_agency_group_page.find_elements(self.pages.new_agency_group_page.add_on_cost_name))
        assert self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.organization_type)

    @test_case()
    def add_on_cost_delete_functionality(self):
        self.pages.new_agency_group_page.remove_add_on_cost_functionality()
        count = len(self.pages.new_agency_group_page.find_elements(self.pages.new_agency_group_page.add_on_cost_name))
        assert  count < self.element_count

    @test_case()
    def validate_margin_value_inherited(self):
        data = self.pages.new_agency_group_page.get_content_value(self.pages.new_agency_group_page.margin_inherited_value_textbox)
        assert data != '', data
        assert self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.margin_inherited_value_checkbox).is_selected()

    @test_case()
    def validate_cogs_checkbox_editable(self):
        self.pages.new_agency_group_page.click_cogs_inherited_value_checkbox()
        data = self.pages.new_agency_group_page.get_content_value(self.pages.new_agency_group_page.cogs_inherited_value_textbox)
        assert data == '', data

    @test_case()
    def validate_margin_checkbox_editable(self):
        self.pages.new_agency_group_page.click_margin_inherited_value_checkbox()
        data = self.pages.new_agency_group_page.get_content_value(self.pages.new_agency_group_page.margin_inherited_value_textbox)
        assert data == '', data

    @test_case()
    def validate_cogs_value_more_than_10(self):
        self.pages.new_agency_group_page.type_cogs_value('11')
        self.pages.new_agency_group_page.type_margin_value('101')
        self.pages.new_agency_group_page.click_create_agency_group_button()
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.error_message['cogs_more_than_10'].format('11'))

    @test_case()
    def validate_margin_value_more_than_100(self):
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.error_message['margin_more_than_100'])

    @test_case()
    def validate_margin_negative_value(self):
        self.pages.new_agency_group_page.type_margin_value('-1')
        self.pages.new_agency_group_page.click_create_agency_group_button()
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.negative_value['margin_negative'])

    @test_case()
    def validate_margin_alphanumeric_value(self):
        self.pages.new_agency_group_page.type_margin_value('sfv45')
        self.pages.new_agency_group_page.click_create_agency_group_button()
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.error_message['margin_alphanumeric'])

    @test_case()
    def validate_cogs_currency(self):
        data = self.pages.new_agency_group_page.get_content_text(self.pages.new_agency_group_page.cogs_currency)
        assert data == 'USD', data

    @test_case()
    def validate_show_page_content(self):
        for element in ['agency_group_list_page', 'add_agency',
                        'edit_details', 'details_div', 'currency_div',
                        'settings_div', 'seats_div' , 'add_on_cost_div',
                        'rate_card_div', 'licenses_div', 'inventories_div']:
            assert self.pages.agency_group_details_page.is_element_present(getattr(self.pages.agency_group_details_page, element))

    @test_case()
    def validate_details_content(self):
        for text in ['Organization Type', 'Organization Name', 'Email', 'Agencies']:
            self.pages.new_agency_group_page.page_should_contain(text)

    @test_case()
    def validate_link_navigation_on_show_page(self):
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            self.pages.agency_group_details_page.go_to_list_page()
            assert self.pages.agency_group_list_page.is_element_present(self.pages.agency_group_list_page.new_agency_group_link)
        if self.pages.agency_group_list_page.is_element_present(self.pages.agency_group_list_page.new_agency_group_link):
            self.pages.agency_group_list_page.go_back()
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            self.pages.agency_group_details_page.click_add_agency()
            time.sleep(15)
        if self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.organization_type):
            self.pages.new_agency_group_page.page_should_contain('Create New Organization')
            self.pages.new_agency_group_page.go_back()
            time.sleep(3)
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            self.pages.agency_group_details_page.click_edit_details()
            time.sleep(10)
        if self.pages.agency_group_edit_page.is_element_present(self.pages.agency_group_edit_page.agency_group_name):
            self.pages.agency_group_edit_page.page_should_contain('Edit Organization')
        else:
            raise CustomException('Stuck on different page')

    @test_case()
    def validate_edit_page_content(self):
        self.open_agency_group_list_page()
        if self.pages.agency_group_list_page.is_element_present(self.pages.agency_group_list_page.new_agency_group_link):
            self.pages.agency_group_list_page.click_first_edit_icon()
            time.sleep(30)
        if self.pages.agency_group_edit_page.is_element_present(self.pages.agency_group_edit_page.agency_group_name):
            for element in ['organization_details', 'currency', 'configure_default',
                            'add_on_cost_section', 'rate_card', 'licenses',
                            'seats',  'save_agency', 'cancel_button']:
                assert self.pages.agency_group_edit_page.is_element_present(getattr(self.pages.agency_group_edit_page, element))
        else:
            raise CustomException('Stuck on different page')

    @test_case()
    def validate_details_content_on_edit_page(self):
        for element in ['organization_type', 'agency_group_name', 'email', 'contact_name']:
            assert self.pages.agency_group_edit_page.is_element_present(getattr(self.pages.agency_group_edit_page, element))

    @test_case()
    def validate_cancel_button_functionality(self):
        if self.pages.agency_group_edit_page.is_element_present(self.pages.agency_group_edit_page.agency_group_name):
            self.pages.agency_group_edit_page.type_email('abc@dataxu.com')
            self.pages.agency_group_edit_page.click_cancel_button()
        if self.pages.agency_group_list_page.is_element_present(self.pages.agency_group_list_page.new_agency_group_link):
            self.pages.agency_group_list_page.click_element(self.pages.agency_group_list_page.agency_group_name_locator)
            time.sleep(2)
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            assert self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency)
        else:
            raise CustomException('Stuck on different page')

    @test_case()
    def validate_save_button_functionality(self):
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            self.pages.agency_group_details_page.click_edit_details()
        if self.pages.agency_group_edit_page.is_element_present(self.pages.agency_group_edit_page.agency_group_name):
            self.pages.agency_group_edit_page.type_add_on_cost_rate('3.3333')
            orgnization = self.pages.agency_group_edit_page.get_content_value(self.pages.agency_group_edit_page.agency_group_name)
            self.pages.agency_group_edit_page.click_create_agency_group_button()
            self.pages.agency_group_edit_page.accept_add_on_cost_pop_up()
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            self.pages.agency_group_details_page.page_should_contain(self.pages.agency_group_details_page.success_message.format(orgnization))
        else:
            raise CustomException('Stuck on different page')

    @test_case()
    def validate_fractional_penny_add_on_cost(self):
        element_list = self.pages.agency_group_details_page.find_elements(self.pages.agency_group_details_page.add_on_cost_rate)
        flag = False
        for element in element_list:
            if '$3.3333' == self.pages.agency_group_details_page.get_content_text(element):
                flag = True
        assert flag is True

    @test_case()
    def fill_fields_with_valid_data(self):
        self.open_new_agency_group_page()
        attribute_dict = self.pages.new_agency_group_page.attributes
        attribute_dict['organization_name'] = '{0}'.format(self.pages.new_agency_group_page.get_random_characters(5))
        attribute_dict['email'] = 'sample@dataxu.com'
        attribute_dict['contact_name'] = '123456'
        attribute_dict['add_on_cost_name'] = 'test_aoc_{0}'.format(self.pages.new_agency_group_page.get_random_string(5))
        attribute_dict['add_on_cost_value'] = '1.34'
        attribute_dict['rate_card'] = os.getcwd() + '/data/rate_cards/rate_card_USD.xls'
        self.organization_name = attribute_dict['organization_name']
        self.fill_all_fields(self.pages.new_agency_group_page, attribute_dict)

    @test_case()
    def validate_valid_name_for_add_on_cost(self):
        self.pages.new_agency_group_page.check_success_message(self.success_message['create_new_agency_group'].format(self.organization_name))

    def validte_with_valid_value(self):
        self.pages.new_agency_group_page.check_success_message(self.success_message['create_new_agency_group'].format(self.organization_name))

    @test_case()
    def validate_valid_value_for_add_on_cost_cpm(self):
        self.validte_with_valid_value()

    @test_case()
    def validate_proper_email_id(self):
        self.validte_with_valid_value()

    @test_case()
    def validate_organization_name_accepts_255_characters(self):
        self.validte_with_valid_value()

    @test_case()
    def validate_contact_name_accepts_digits(self):
        self.validte_with_valid_value()

    @test_case()
    def validate_currency_field_grayed_out_on_edit_page(self):
        self.pages.agency_group_details_page.click_edit_details()
        assert self.pages.agency_group_edit_page.is_element_present(self.pages.agency_group_edit_page.greyed_out_currency_list_box)

    @test_case()
    def validate_other_than_contracted_currency_on_edit_page(self):
        self.pages.agency_group_edit_page.upload_rate_card(os.getcwd() + '/data/rate_cards/rate card_CAD.xls')
        self.pages.agency_group_edit_page.click_create_agency_group_button()
        time.sleep(2)
        message = self.pages.agency_group_edit_page.get_content_text(['css selector', '#errorExplanation > ul> li:nth-child(1)']).encode()
        assert self.pages.agency_group_edit_page.error_message['rate_card_with_different_currency'] == message

    @test_case()
    def validate_organization_duplicate_name(self):
        self.open_new_agency_group_page()
        self.pages.new_agency_group_page.type_organization_name(self.organization_name)
        self.pages.new_agency_group_page.type_email('add!@#@dataxu.com')
        self.pages.new_agency_group_page.click_create_agency_group_button()
        time.sleep(2)
        message = self.pages.new_agency_group_page.get_content_text(['css selector', self.pages.new_agency_group_page.error_message_locator.format(4)]).encode()
        assert self.pages.new_agency_group_page.error_message['duplicate_organization_name'].format(self.organization_name) == message

    @test_case()
    def validate_invalid_email_id(self):
        assert self.pages.new_agency_group_page.error_message['invalid_email'] == self.pages.new_agency_group_page.get_content_text(
                                                                            ['css selector', self.pages.new_agency_group_page.error_message_locator.format(3)]).encode()

    def invalid_email(self, email):
        self.pages.new_agency_group_page.type_email(email)
        self.pages.new_agency_group_page.click_create_agency_group_button()
        assert self.pages.new_agency_group_page.error_message['invalid_email'] == self.pages.new_agency_group_page.get_content_text(
                                                                            ['css selector', self.pages.new_agency_group_page.error_message_locator.format(2)]).encode()

    @test_case()
    def validate_invalid_email_id_with_sign(self):
        self.invalid_email('@dataxu.com')

    @test_case()
    def validate_invalid_email_id_with_suffix_sign(self):
        self.invalid_email('test@')

    @test_case()
    def validate_select_all_currency_checkbox(self):
        self.pages.new_agency_group_page.check_select_all_currencies()
        assert self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.euro_currency_checkbox).is_selected()
        self.pages.new_agency_group_page.check_select_all_currencies()
        assert not self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.euro_currency_checkbox).is_selected()

    @test_case()
    def validate_individual_selection_of_currency(self):
        self.pages.new_agency_group_page.select_currency_from_listbox('Euro (EUR)')
        assert self.pages.new_agency_group_page.get_content_value(self.pages.new_agency_group_page.currency) == '3'
        self.pages.new_agency_group_page.select_currency_from_listbox('United States Dollar (USD)')
        assert self.pages.new_agency_group_page.get_content_value(self.pages.new_agency_group_page.currency) == '1'

    @test_case()
    def validate_grayed_out_fields(self):
        assert self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.inherit_licensing_checkbox).is_selected()
        self.pages.new_agency_group_page.check_select_all_currencies()
        assert self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.online_disabled_checkbox)
        assert self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.disabled_select_all_inventory_checkbox)

    def fill_details_with_blank_email(self):
        self.open_new_agency_group_page()
        attribute_dict = self.pages.new_agency_group_page.attributes
        new_value = self.pages.new_agency_group_page.get_random_string(10) + self.pages.new_agency_group_page.get_random_digits(10)
        self.organization_name = new_value
        for key, value in attribute_dict.iteritems():
                attribute_dict[key] = new_value
        attribute_dict['email'] = ''
        attribute_dict['contact_name'] = ''
        attribute_dict['add_on_cost_value'] = '0'
        attribute_dict['rate_card'] = os.getcwd() + '/data/rate_cards/rate_card_USD.xls'
        self.pages.new_agency_group_page.click_cogs_inherited_value_checkbox()
        self.pages.new_agency_group_page.click_margin_inherited_value_checkbox()
        self.pages.new_agency_group_page.type_cogs_value('0.155')
        self.pages.new_agency_group_page.type_margin_value('0.155')
        self.pages.new_agency_group_page.click_inherit_licenses_checkbox()
        self.pages.new_agency_group_page.click_media_type_checkbox()
        self.pages.new_agency_group_page.click_media_type_checkbox('video')
        self.pages.new_agency_group_page.select_inventories(self.dx_constant.inventory_list)
        insight_list = self.pages.new_agency_group_page.insight_list
        for insight in insight_list:
            self.pages.new_agency_group_page.select_insights(insight)
        self.fill_all_fields(self.pages.new_agency_group_page, attribute_dict)
        self.success_message = self.pages.new_agency_group_page.success_message['organization_name']

    @test_case()
    def validate_blank_email_accepted(self):
        self.pages.new_agency_group_page.check_success_message(self.success_message['create_new_agency_group'].format(self.organization_name))

    @test_case()
    def validate_blank_contact_name_accepted(self):
        self.pages.new_agency_group_page.check_success_message(self.success_message['create_new_agency_group'].format(self.organization_name))

    @test_case()
    def validate_cogs_value_as_decimal(self):
        data = self.pages.agency_group_details_page.get_content_text(self.pages.agency_group_details_page.cogs_value)
        assert data == '$0.16', data

    @test_case()
    def validate_margin_value_as_decimal(self):
        data = self.pages.agency_group_details_page.get_content_text(self.pages.agency_group_details_page.margin_value)
        assert data == '0.155', data

    @test_case()
    def validate_online_checked_on_edit_page(self):
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            self.pages.agency_group_details_page.click_edit_details()
        if self.pages.agency_group_edit_page.is_element_present(self.pages.agency_group_edit_page.agency_group_name):
            assert self.pages.agency_group_edit_page.find_element(self.pages.agency_group_edit_page.online_media_type_checkbox['online'].values()).is_selected()

    @test_case()
    def validate_mobile_checked_on_edit_page(self):
        assert self.pages.agency_group_edit_page.find_element(self.pages.agency_group_edit_page.online_media_type_checkbox['mobile'].values()).is_selected()

    @test_case()
    def validate_video_checked_on_edit_page(self):
        assert self.pages.agency_group_edit_page.find_element(self.pages.agency_group_edit_page.online_media_type_checkbox['video'].values()).is_selected()

    @test_case()
    def validate_insights_checked_on_edit_page(self):
        for element in ['frequency', 'consideration', 'retargeting', 'index']:
            assert self.pages.agency_group_edit_page.find_element(self.pages.agency_group_edit_page.insights[element].values()).is_selected()

    @test_case()
    def validate_checked_inventories_on_edit_page(self):
        for inventory in self.dx_constant.inventory_list:
            assert self.pages.agency_group_edit_page.is_element_present([self.pages.agency_group_edit_page.invetory_locator[0], self.pages.agency_group_edit_page.invetory_locator[1].format(inventory)])

    def fill_organization_name_with_special_characters(self):
        self.open_new_agency_group_page()
        attribute_dict = self.pages.new_agency_group_page.attributes
        new_value = self.pages.new_agency_group_page.get_random_string(10)
        for key, value in attribute_dict.iteritems():
                attribute_dict[key] = new_value
        attribute_dict['organization_name'] = '{0}_!@#$%'.format(new_value)
        self.organization_name = attribute_dict['organization_name']
        attribute_dict['email'] = ''
        attribute_dict['contact_name'] = ''
        attribute_dict['add_on_cost_value'] = '0'
        attribute_dict['rate_card'] = os.getcwd() + '/data/rate_cards/rate_card_USD.xls'
        self.pages.new_agency_group_page.click_inherit_licenses_checkbox()
        self.pages.new_agency_group_page.click_media_type_checkbox('online')
        self.pages.new_agency_group_page.select_inventories(self.dx_constant.uncheck_inventory_list)
        self.fill_all_fields(self.pages.new_agency_group_page, attribute_dict)
        self.success_message = self.pages.new_agency_group_page.success_message['organization_name']

    @test_case()
    def validate_agency_name_with_special_char(self):
        self.pages.new_agency_group_page.check_success_message(self.success_message['create_new_agency_group'].format(self.organization_name))

    @test_case()
    def validate_online_unchecked_on_edit_page(self):
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            self.pages.agency_group_details_page.click_edit_details()
        if self.pages.agency_group_edit_page.is_element_present(self.pages.agency_group_edit_page.agency_group_name):
            assert not self.pages.agency_group_edit_page.find_element(self.pages.agency_group_edit_page.online_media_type_checkbox['online'].values()).is_selected()

    @test_case()
    def validate_mobile_unchecked_on_edit_page(self):
        assert not self.pages.agency_group_edit_page.find_element(self.pages.agency_group_edit_page.online_media_type_checkbox['mobile'].values()).is_selected()

    @test_case()
    def validate_video_unchecked_on_edit_page(self):
        assert not self.pages.agency_group_edit_page.find_element(self.pages.agency_group_edit_page.online_media_type_checkbox['video'].values()).is_selected()

    @test_case()
    def validate_insights_unchecked_on_edit_page(self):
        for element in ['frequency', 'consideration', 'retargeting', 'index']:
            assert not self.pages.agency_group_edit_page.find_element(self.pages.agency_group_edit_page.insights[element].values()).is_selected()

    @test_case()
    def validate_unchecked_inventories_on_edit_page(self):
        for inventory in self.dx_constant.inventory_list:
            assert self.pages.agency_group_edit_page.is_element_present([self.pages.agency_group_edit_page.invetory_locator[0],
                                                                   self.pages.agency_group_edit_page.invetory_locator[1].format(inventory)])

    def open_agency_group_list_page(self):
        self.pages.agency_group_list_page.open()

    @test_case()
    def validate_list_page_contents(self):
        self.open_agency_group_list_page()
        assert 'Agency Groups' == self.pages.agency_group_list_page.get_content_text(self.pages.agency_group_list_page.page_header)

    @test_case()
    def validate_new_agency_group_button(self):
        if self.pages.agency_group_list_page.is_element_present(self.pages.agency_group_list_page.new_agency_group_link):
            self.pages.agency_group_list_page.go_to_new_agency()
            time.sleep(15)
        if self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.agency_group_name):
            result = self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.currency)
            assert result == True, result
            self.pages.new_agency_group_page.go_back()
        else:
            raise CustomException('Stuck on different page')

    @test_case()
    def validate_edit_icon(self):
        self.open_agency_group_list_page()
        if self.pages.agency_group_list_page.is_element_present(self.pages.agency_group_list_page.new_agency_group_link):
            self.pages.agency_group_list_page.click_first_edit_icon()
            time.sleep(10)
        if self.pages.agency_group_edit_page.is_element_present(self.pages.agency_group_edit_page.agency_group_name):
            result = self.pages.agency_group_edit_page.is_element_present(self.pages.agency_group_edit_page.select_all_currency)
            assert result == True, result
        self.pages.agency_group_list_page.go_back()

    @test_case()
    def validate_delete_icon(self):
        self.open_agency_group_list_page()
        self.pages.agency_group_list_page.search_agency_group(self.organization_name)
        self.pages.agency_group_list_page.click_first_delete_icon()
        self.pages.agency_group_list_page.accept_alert()
        time.sleep(3)
        message = self.pages.agency_group_list_page.get_content_text(self.pages.agency_group_list_page.success_message_locator).encode()
        assert message == self.pages.agency_group_list_page.success_message.format(self.organization_name), self.pages.agency_group_list_page.success_message.format(self.organization_name)

    @test_case()
    def validate_ok_button_functionality(self):
        message = self.pages.agency_group_list_page.get_content_text(self.pages.agency_group_list_page.success_message_locator).encode()
        assert message == self.pages.agency_group_list_page.success_message.format(self.organization_name), self.pages.agency_group_list_page.success_message.format(self.organization_name)

    @test_case()
    def validate_cancel_button_functionality_on_list_page(self):
        time.sleep(3)
        self.pages.agency_group_list_page.click_first_delete_icon()
        self.pages.agency_group_list_page.dismiss_alert()

    @test_case()
    def validate_search_box(self):
        self.pages.agency_group_list_page.search_agency_group(self.organization_name)
        self.pages.agency_group_list_page.page_should_contain(self.pages.agency_group_list_page.invalid_search_message)

    def sort(self, data, data_after_sort):
        try:
            data == data_after_sort, '{0}/{1}'.format(data, data_after_sort)
        except:
            assert data != data_after_sort, '{0}/{1}'.format(data, data_after_sort)

    @test_case()
    def validate_sort_functionality(self):
        data = self.pages.agency_group_list_page.get_content_text(self.pages.agency_group_list_page.agency_group_name_locator).encode()
        self.pages.agency_group_list_page.click_element(self.pages.agency_group_list_page.sort_button_locator)
        data_after_sort = self.pages.agency_group_list_page.get_content_text(self.pages.agency_group_list_page.agency_group_name_locator).encode()
        if data[0].isdigit():
            self.sort(data, data_after_sort)
        else:
            assert data != data_after_sort, '{0}/{1}'.format(data, data_after_sort)
        data = self.pages.agency_group_list_page.get_content_text(self.pages.agency_group_list_page.agency_group_name_locator).encode()
        self.pages.agency_group_list_page.click_element(self.pages.agency_group_list_page.sort_button_locator)
        data_after_sort = self.pages.agency_group_list_page.get_content_text(self.pages.agency_group_list_page.agency_group_name_locator).encode()
        assert data != data_after_sort, '{0}/{1}'.format(data, data_after_sort)

    @test_case()
    def validate_agency_group_name_link(self):
        self.pages.agency_group_list_page.click_element(self.pages.agency_group_list_page.agency_group_name_locator)
        time.sleep(3)
        assert not self.pages.agency_group_list_page.is_element_present(self.pages.agency_group_list_page.new_agency_group_link)
        self.pages.agency_group_list_page.go_back()

    @test_case()
    def validate_seat_configuration_on_show_page(self):
        self.open_new_agency_group_page()
        self.organization_name = 'seat_edited_agency_{0}'.format(self.pages.new_agency_group_page.get_random_string(11))
        self.pages.new_agency_group_page.type_organization_name(self.organization_name)
        self.pages.new_agency_group_page.upload_rate_card(os.getcwd() + '/data/rate_cards/rate_card_USD.xls')
        assert 'Inheriting Seat' in self.pages.new_agency_group_page.get_content_text(self.pages.new_agency_group_page.configure_seats_pop_up['seat_content'].values())
        self.pages.new_agency_group_page.click_seats_edit_icon()
        self.pages.new_agency_group_page.click_seats_override_radio_button()
        self.pages.new_agency_group_page.type_seat_name('test')
        self.pages.new_agency_group_page.type_seat_id('123')
        self.pages.new_agency_group_page.click_seats_ok_button()
        assert 'test - 123' in self.pages.new_agency_group_page.get_content_text(self.pages.new_agency_group_page.configure_seats_pop_up['seat_content'].values())
        self.pages.new_agency_group_page.click_create_agency_group_button()
        self.pages.new_agency_group_page.check_success_message(self.success_message['create_new_agency_group'].format(self.organization_name))
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            assert 'test - 123' in self.pages.agency_group_details_page.get_content_text(self.pages.agency_group_details_page.seat_content)

    def validate_availabel_currency(self, currency):
        currency_dict = {'USD': 'United States Dollar (USD)', 'GBP': 'British Pound (GBP)', 'EUR': 'Euro (EUR)' , 'CAD': 'Canadian Dollar (CAD)', 'BRL': 'Brazilian Real (BRL)', 'PLN': 'Polish Złoty (PLN)'}
        currency_code = {'USD': '1', 'GBP': '2', 'EUR': '3', 'CAD': '4', 'BRL': '5', 'PLN': '6'}
        self.open_new_agency_group_page()
        time.sleep(10)
        self.pages.new_agency_group_page.select_currency_from_listbox(currency_dict[currency].decode('utf-8'))
        time.sleep(2)
        new_locator = [self.locator[0], self.locator[1].format(currency_code[currency])]
        assert self.pages.new_agency_group_page.is_element_present(new_locator)

    @test_case()
    def validate_currency(self, currency):
        currency_dict = {'USD': 'United States Dollar (USD)', 'GBP': 'British Pound (GBP)', 'EUR': 'Euro (EUR)' , 'CAD': 'Canadian Dollar (CAD)', 'BRL': 'Brazilian Real (BRL)', 'PLN': 'Polish Złoty (PLN)'}
        rate_card_path = {'USD': '/data/rate_cards/rate_card_USD.xls', 'GBP': '/data/rate_cards/rate_card_UK_GBP.xls', 'EUR': '/data/rate_cards/Rate card_EUR.xls', 'CAD': '/data/rate_cards/rate card_CAD.xls', 'BRL': '/data/rate_cards/rate_card_BRL.xls', 'PLN': '/data/rate_cards/rate_card_PLN.xls'}
        self.organization_name = 'seat_edited_agency_group_{0}'.format(self.pages.new_agency_group_page.get_random_string(11))
        if self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.organization_type):
            self.pages.new_agency_group_page.type_organization_name(self.organization_name)
            self.pages.new_agency_group_page.upload_rate_card(os.getcwd() + rate_card_path[currency])
            self.pages.new_agency_group_page.check_select_all_currencies()
            self.pages.new_agency_group_page.click_create_agency_group_button()
            self.pages.new_agency_group_page.check_success_message(self.success_message['create_new_agency_group'].format(self.organization_name))
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            assert currency_dict[currency].decode('utf-8') == self.pages.agency_group_details_page.get_content_text(self.pages.agency_group_details_page.contracted_currency)

    def validate_currency_for_cogs(self, currency):
        if self.pages.agency_group_details_page.is_element_present(self.pages.agency_group_details_page.add_agency):
            self.pages.agency_group_details_page.click_edit_details()
        if self.pages.agency_group_edit_page.is_element_present(self.pages.agency_group_edit_page.agency_group_name):
            data = self.pages.agency_group_edit_page.get_content_text(self.pages.agency_group_edit_page.cogs_currency)
            assert data == currency, data
            self.pages.agency_group_edit_page.select_add_on_cost_fee_type('CPM ({0})'.format(currency))

    @test_case()
    def validate_available_currencies_usd(self):
        self.validate_availabel_currency('USD')

    @test_case()
    def validate_usd_currency(self):
        self.validate_currency('USD')

    @test_case()
    def validate_available_currency_on_show_page(self):
        currency_list = self.pages.agency_group_details_page.get_content_text_list(self.pages.agency_group_details_page.available_currency_list_locator)
        for currency in currency_list:
            assert currency in self.pages.agency_group_details_page.currency_list

    @test_case()
    def validate_updating_currency(self):
        currency_list = self.pages.agency_group_details_page.get_content_text_list(self.pages.agency_group_details_page.available_currency_list_locator)
        for currency in currency_list:
            assert currency in self.pages.agency_group_details_page.currency_list

    @test_case()
    def validate_contracted_usd_currency_for_cogs(self):
        self.validate_currency_for_cogs('USD')

    @test_case()
    def validate_available_currencies_gbp(self):
        self.validate_availabel_currency('GBP')

    @test_case()
    def validate_gbp_currency(self):
        self.validate_currency('GBP')

    @test_case()
    def validate_contracted_gbp_currency_for_cogs(self):
        self.validate_currency_for_cogs('GBP')

    @test_case()
    def validate_available_currencies_eur(self):
        self.validate_availabel_currency('EUR')

    @test_case()
    def validate_eur_currency(self):
        self.validate_currency('EUR')

    @test_case()
    def validate_contracted_eur_currency_for_cogs(self):
        self.validate_currency_for_cogs('EUR')

    @test_case()
    def validate_available_currencies_cad(self):
        self.validate_availabel_currency('CAD')

    @test_case()
    def validate_cad_currency(self):
        self.validate_currency('CAD')

    @test_case()
    def validate_contracted_cad_currency_for_cogs(self):
        self.validate_currency_for_cogs('CAD')

    @test_case()
    def validate_available_currencies_brl(self):
        self.validate_availabel_currency('BRL')

    @test_case()
    def validate_brl_currency(self):
        self.validate_currency('BRL')

    @test_case()
    def validate_contracted_brl_currency_for_cogs(self):
        self.validate_currency_for_cogs('BRL')

    @test_case()
    def validate_available_currencies_pln(self):
        self.validate_availabel_currency('PLN')

    @test_case()
    def validate_pln_currency(self):
        self.validate_currency('PLN')

    @test_case()
    def validate_contracted_pln_currency_for_cogs(self):
        self.validate_currency_for_cogs('PLN')
