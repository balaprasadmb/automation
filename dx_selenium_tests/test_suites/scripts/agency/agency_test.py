# -*- coding: utf-8 -*-
import os
import time

from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from common_helpers.common_helpers import CommonHelper


class AgencyTest(DXTest):
    
    @test_case()
    def login_as_agency_manager(self):
        self.common_helper = CommonHelper()
        self.setup(self.dx_constant.user_by_role['system_level_organization_administrator_one'])

    @test_case()
    def assert_is_element_present(self, page_object, loc, criteria=True):
        self.common_helper.assert_is_element_present(page_object, loc, criteria)

    @test_case()
    def assert_is_selected(self, page_object, loc, criteria=True):
        self.common_helper.assert_is_selected(page_object, loc, criteria)

    def open_new_agency_page(self):
        self.pages.new_agency_page.open()

    def open_new_agency_list_page(self):
        self.pages.agency_list_page.open()

    @test_case()
    def validate_list_page_contents(self):
        self.open_new_agency_list_page()
        self.pages.agency_list_page.page_should_contain('Agencies')
        for element in ['new_agency_button', 'search_filter_agency',
                        'edit_icon', 'delete_icon', 'agency_name_locator',
                        'agency_name_sort', 'agency_contact_sort', 'agency_email_sort',
                        'agency_group_sort']:
            assert self.pages.agency_list_page.is_element_present(getattr(self.pages.agency_list_page, element))

    @test_case()
    def validate_new_agency_button(self):
        self.pages.agency_list_page.click_on_new_agency_button()
        time.sleep(10)
        self.pages.agency_list_page.select_agency_group('2', 'index')
        self.assert_is_element_present(self.pages.new_agency_page, 'agency_name')
        self.pages.new_agency_page.go_back()
        time.sleep(10)

    @test_case()
    def validate_edit_icon_functionality(self):
        self.pages.agency_list_page.click_first_edit_icon()
        time.sleep(10)
        self.assert_is_element_present(self.pages.new_agency_page, 'agency_name')
        self.pages.agency_list_page.go_back()

    @test_case()
    def validate_cancel_on_delete(self):
        time.sleep(10)
        self.pages.agency_list_page.click_first_delete_icon()
        self.pages.agency_list_page.dismiss_alert()
        self.assert_is_element_present(self.pages.agency_list_page, 'new_agency_button')

    @test_case()
    def validate_delete_functionality(self):
        self.open_new_agency_list_page()
        self.pages.agency_list_page.filter_agency_name_in_filterbox(self.agency_name)
        time.sleep(10)
        self.pages.agency_list_page.click_first_delete_icon()
        self.pages.agency_list_page.accept_alert()
        time.sleep(10)
        message = self.pages.agency_list_page.get_content_text(self.pages.agency_list_page.success_message_locator).encode()
        assert self.pages.agency_list_page.delete_success_message in message

    @test_case()
    def validate_search_box_functionality(self):
        self.pages.agency_list_page.filter_agency_name_in_filterbox('aawdadwedwe')
        self.pages.agency_list_page.page_should_contain(self.pages.agency_list_page.invalid_search_message)

    def sort(self, data, data_after_sort):
        try:
            assert data == data_after_sort, '{0}/{1}'.format(data, data_after_sort)
        except:
            assert data != data_after_sort, '{0}/{1}'.format(data, data_after_sort)

    @test_case()
    def validate_sort_functionality(self):
        data = self.pages.agency_list_page.get_content_text(self.pages.agency_list_page.agency_name_locator).encode()
        self.pages.agency_list_page.click_element(self.pages.agency_list_page.agency_name_sort)
        data_after_sort = self.pages.agency_list_page.get_content_text(self.pages.agency_list_page.agency_name_locator).encode()
        if data[0].isdigit():
            self.sort(data, data_after_sort)
        else:
            assert data != data_after_sort, '{0}/{1}'.format(data, data_after_sort)
        data = self.pages.agency_list_page.get_content_text(self.pages.agency_list_page.agency_name_locator).encode()
        self.pages.agency_list_page.click_element(self.pages.agency_list_page.agency_name_sort)
        data_after_sort = self.pages.agency_list_page.get_content_text(self.pages.agency_list_page.agency_name_locator).encode()
        assert data != data_after_sort, '{0}/{1}'.format(data, data_after_sort)

    @test_case()
    def validate_agency_name_functionality(self):
        self.pages.agency_list_page.page_refresh()
        self.pages.agency_list_page.click_element(self.pages.agency_list_page.agency_name_locator)
        time.sleep(10)
        self.assert_is_element_present(self.pages.agency_list_page, 'new_agency_button', criteria=False)
        self.pages.agency_list_page.go_back()

    @test_case()
    def validate_presence_of_new_inventories(self):
        self.pages.agency_list_page.click_on_new_agency_button()
        time.sleep(2)
        self.pages.agency_list_page.select_agency_group('2', 'index')
        inventory_list = self.pages.new_agency_page.get_content_text_list(self.pages.new_agency_page.agency_invenotry_supplier_label)
        for inventory in self.dx_constant.new_inventory_list:
            assert inventory in inventory_list, '{0} inventory is not available'.format(inventory)

    @test_case()
    def validate_contracted_currency_grayed_out(self):
        self.assert_is_element_present(self.pages.new_agency_page, 'currency')

    @test_case()
    def validate_select_all_checkbox(self):
        self.pages.new_agency_page.open()
        attribute_dict = self.pages.new_agency_page.attributes
        new_value = self.pages.new_agency_page.get_random_string(10)
        for key, value in attribute_dict.iteritems():
                attribute_dict[key] = new_value
        attribute_dict['organization_name'] = '{0}'.format(new_value)
        self.agency_name = attribute_dict['organization_name']
        attribute_dict['email'] = ''
        attribute_dict['contact_name'] = ''
        attribute_dict['add_on_cost_value'] = '0'
        attribute_dict['rate_card'] = os.getcwd() + '/data/rate_cards/rate_card_USD.xls'
        self.pages.new_agency_page.fill_fields(attribute_dict)
        self.open_new_agency_list_page()
        self.pages.agency_list_page.click_on_new_agency_button()
        time.sleep(10)
        self.pages.agency_list_page.select_agency_group(self.dx_constant.agency_group_name, 'label')
        self.assert_is_selected(self.pages.new_agency_page, 'euro_currency_checkbox')
        self.pages.new_agency_page.check_select_all_currencies()
        self.assert_is_selected(self.pages.new_agency_page, 'euro_currency_checkbox', criteria=False)

    @test_case()
    def validate_individual_checkbox(self):
        self.pages.new_agency_page.check_select_all_currencies()
        self.assert_is_selected(self.pages.new_agency_page, 'select_all_currency')
        self.pages.new_agency_page.check_select_all_currencies()
        self.assert_is_selected(self.pages.new_agency_page, 'select_all_currency', criteria=False)
        self.pages.new_agency_page.click_inherit_licenses_checkbox()
        self.assert_is_selected(self.pages.new_agency_page, 'inherit_licensing_checkbox', criteria=False)
        self.pages.new_agency_page.select_all_inventory()
        self.assert_is_selected(self.pages.new_agency_page, 'select_all_inventories')
        self.pages.new_agency_page.select_all_inventory()
        self.assert_is_selected(self.pages.new_agency_page, 'select_all_inventories', criteria=False)
        self.pages.new_agency_page.click_inherit_licenses_checkbox()
        self.assert_is_selected(self.pages.new_agency_page, 'inherit_licensing_checkbox')

    def check_data(self, page_object, element_name, editable=False):
        element_locator = {'cogs': 'cogs_inherited_value_textbox', 'margin': 'margin_inherited_value_textbox'}
        checkbox_locator = {'cogs': 'cogs_inherited_value_checkbox', 'margin': 'margin_inherited_value_checkbox'}
        data = page_object.get_content_value(getattr(page_object, element_locator[element_name]))
        if editable:
            assert data == '', data
            self.assert_is_selected(page_object, checkbox_locator[element_name], criteria=False)
        else:
            assert data != '', data
            self.assert_is_selected(page_object, checkbox_locator[element_name])

    @test_case()
    def validate_cogs_value_inherited(self):
        self.open_new_agency_page()
        self.check_data(self.pages.new_agency_page, 'cogs')

    @test_case()
    def validate_margin_value_inherited(self):
        self.check_data(self.pages.new_agency_page, 'margin')

    @test_case()
    def validate_margin_checkbox_editable(self):
        self.pages.new_agency_page.click_margin_inherited_value_checkbox()
        self.check_data(self.pages.new_agency_page, 'margin', editable=True)

    @test_case()
    def validate_cogs_checkbox_editable(self):
        self.pages.new_agency_page.click_cogs_inherited_value_checkbox()
        self.check_data(self.pages.new_agency_page, 'cogs', editable=True)

    @test_case()
    def validate_cogs_currency(self):
        data = self.pages.new_agency_page.get_content_text(self.pages.new_agency_page.cogs_currency)
        assert data == 'USD', data

    @test_case()
    def validate_blank_organization_name(self):
        self.pages.new_agency_page.click_create_agency_button()
        self.pages.new_agency_page.page_should_contain(self.pages.new_agency_page.blank_message['organization_name'])

    def invalid_email(self, email):
        self.pages.new_agency_page.type_email(email)
        self.pages.new_agency_page.click_create_agency_button()
        assert self.pages.new_agency_page.error_message['invalid_email'] == self.pages.new_agency_page.get_content_text(['css selector', self.pages.new_agency_page.error_message_locator.format(2)]).encode()

    @test_case()
    def validate_invalid_email_id_with_sign(self):
        self.invalid_email('@dataxu.com')

    @test_case()
    def validate_invalid_email_id_with_suffix_sign(self):
        self.invalid_email('test@')

    @test_case()
    def check_contents_of_show_page(self):
        self.open_new_agency_list_page()
        self.pages.agency_list_page.go_to_link(self.dx_constant.agency_name)
        time.sleep(5)
        for element in ['agency_list_page_link', 'add_advertiser_button', 'edit_details_button',
                        'details_section', 'currencies_section', 'settings_section',
                        'add_on_cost_section', 'rate_card_section', 'licenses_section', 'private_inventory_section', 'seats_section']:
            self.assert_is_element_present(self.pages.agency_details_page, element)

    @test_case()
    def verify_details_section(self):
        data_list = ['Organization Type', 'Organization Name', 'Email', 'Agency Group', 'Advertisers']
        for key, value in self.pages.agency_details_page.details_section_elements.iteritems():
            if type(value) is not str:
                assert self.pages.agency_details_page.get_content_text(value.values()) in data_list

    def link_navigation_helper(self, page_object, validation_string):
        page_object.page_should_contain(validation_string)
        page_object.go_back()

    @test_case()
    def verify_link_navigation(self):
        if not self.pages.agency_details_page.is_element_present(self.pages.agency_details_page.advertiser_list):
            self.pages.agency_details_page.add_new_advertiser()
            time.sleep(60)
            advertiser_name = "advertiser_{0}".format(self.pages.new_advertiser_page.get_random_string(10))
            self.pages.new_advertiser_page.type_organization_name(advertiser_name)
            self.pages.new_advertiser_page.type_advertiser_domain('www.example.com')
            self.pages.new_advertiser_page.click_create_advetiser_button()
            for i in range(1, 3):
                self.pages.new_advertiser_page.go_back()
                time.sleep(3)
                self.pages.agency_details_page.page_refresh()
        for key, value in {'Agencies': 'go_to_agency_list_page', 'Create New Organization': 'add_new_advertiser',
                           'Advertiser domain': 'go_to_first_advertiser_in_list', 'Agency Group': 'go_to_agency_group',
                           'Edit Organization': 'click_edit_details'}.iteritems():
            getattr(self.pages.agency_details_page, value)()
            time.sleep(10)
            self.pages.agency_details_page.page_should_contain(key)
            self.pages.agency_details_page.go_back()

    @test_case()
    def contents_of_agency_edit_page(self):
        self.pages.agency_details_page.click_edit_details()
        time.sleep(5)
        for element in ['details_section', 'currency_section', 'default_settings_section',
                        'add_on_cost_section', 'rate_card_section', 'configure_licensing_section',
                        'configure_seat_section', 'submit_button', 'cancel_button']:
            self.assert_is_element_present(self.pages.agency_edit_page, element)

    @test_case()
    def contents_of_details_section_on_edit_page(self):
        for element in ['agency_name', 'email', 'contact_name', 'agency_group', 'organization_type']:
            self.assert_is_element_present(self.pages.agency_edit_page, element)

    @test_case()
    def save_button_functionality_on_edit_page(self):
        self.agency_name = self.pages.agency_edit_page.get_content_value(self.pages.agency_edit_page.agency_name)
        agency = self.pages.agency_edit_page.get_random_string(10)
        self.pages.agency_edit_page.type_organization_name(agency)
        self.pages.agency_edit_page.click_create_agency_button()
        time.sleep(2)
        message = self.pages.agency_edit_page.success_message['edit_agency']
        self.pages.agency_details_page.page_should_contain(message.format(agency))

    @test_case()
    def cancel_button_functionality_on_edit_page(self):
        self.pages.agency_details_page.click_edit_details()
        time.sleep(2)
        self.pages.agency_edit_page.click_cancel_button()
        time.sleep(2)
        self.assert_is_element_present(self.pages.agency_details_page, 'add_advertiser_button')
        self.pages.agency_details_page.click_edit_details()
        self.pages.agency_edit_page.type_organization_name(self.agency_name)
        self.pages.agency_edit_page.click_create_agency_button()
        message = self.pages.agency_edit_page.success_message['edit_agency']
        self.pages.agency_edit_page.page_should_contain(message.format(self.agency_name))

    @test_case()
    def add_on_cost_for_permission_user(self):
        self.open_new_agency_page()
        for element in ['name', 'cpm', 'billable', 'channel']:
            self.assert_is_element_present(self.pages.new_agency_page, self.pages.new_agency_page.add_on_cost_section_headers[element].values())
        self.assert_is_element_present(self.pages.new_agency_page, 'new_add_on_cost')
        self.pages.new_agency_page.click_new_add_on_cost_button()
        for element in ['add_on_cost_name', 'add_on_cost_value', 'add_on_cost_billable_checkbox', 'add_on_cost_channel', 'remove_add_on_cost']:
            self.assert_is_element_present(self.pages.new_agency_page, element)

    @test_case()
    def validate_channel_dropdown_guaranteed_media_permission(self):
        self.pages.new_agency_page.check_dropdown_options(self.dx_constant.add_on_cost_channel_options, self.pages.new_agency_page.add_on_cost_channel)

    @test_case()
    def validate_currency_for_add_on_cost_CPM_field(self):
        currency_code = self.pages.new_agency_page.get_content_value(self.pages.new_agency_page.selected_currency)
        self.pages.new_agency_page.click_new_add_on_cost_button()
        self.pages.new_agency_page.select_add_on_cost_fee_type('CPM ({0})'.format(self.dx_constant.agency_group_currency_code.keys()[self.dx_constant.agency_group_currency_code.values().index(currency_code)]))
        self.assert_is_element_present(self.pages.new_agency_page, 'organization_type')

    @test_case()
    def add_on_cost_delete_functionality(self):
        self.element_count = len(self.pages.new_agency_page.find_elements(self.pages.new_agency_page.add_on_cost_name))
        self.pages.new_agency_page.remove_add_on_cost_functionality()
        count = len(self.pages.new_agency_page.find_elements(self.pages.new_agency_page.add_on_cost_name))
        assert  count < self.element_count

    @test_case()
    def validate_cogs_value_more_than_10(self):
        self.pages.new_agency_page.click_cogs_inherited_value_checkbox()
        self.pages.new_agency_page.click_margin_inherited_value_checkbox()
        self.pages.new_agency_page.type_cogs_value('11')
        self.pages.new_agency_page.type_margin_value('101')
        self.pages.new_agency_page.click_create_agency_button()
        self.pages.new_agency_page.page_should_contain(self.pages.new_agency_page.error_message['cogs_more_than_10'].format('11'))

    @test_case()
    def validate_margin_value_more_than_100(self):
        self.pages.new_agency_page.page_should_contain(self.pages.new_agency_page.error_message['margin_more_than_100'])

    @test_case()
    def validate_margin_negative_value(self):
        self.pages.new_agency_page.type_margin_value('-1')
        self.pages.new_agency_page.click_create_agency_button()
        self.pages.new_agency_page.page_should_contain(self.pages.new_agency_page.negative_value['margin_negative'])

    @test_case()
    def validate_margin_alphanumeric_value(self):
        self.pages.new_agency_page.type_margin_value('asd21')
        self.pages.new_agency_page.click_create_agency_button()
        self.pages.new_agency_page.page_should_contain(self.pages.new_agency_page.error_message['margin_alphanumeric'])

    @test_case()
    def validate_grayed_out_fields(self):
        self.assert_is_selected(self.pages.new_agency_page, 'inherit_licensing_checkbox')
        self.pages.new_agency_page.check_select_all_currencies()
        for element in ['online_disabled_checkbox' , 'disabled_select_all_inventory_checkbox']:
            self.assert_is_element_present(self.pages.new_agency_page, element)
                                                      
    @test_case()
    def validate_inherit_value_checkbox_functionality(self):
        self.pages.new_agency_page.click_inherit_licenses_checkbox()
        self.assert_is_selected(self.pages.new_agency_page, 'inherit_licensing_checkbox', criteria=False)
        for element in ['online_disabled_checkbox' , 'disabled_select_all_inventory_checkbox']:
            self.assert_is_element_present(self.pages.new_agency_page, element, criteria=False)

    @test_case()
    def validate_media_types(self):
        self.open_new_agency_page()
        self.pages.new_agency_page.click_inherit_licenses_checkbox()
        for media_type in ['online', 'mobile', 'video']:
            self.assert_is_element_present(self.pages.new_agency_page, self.pages.new_agency_page.online_media_type_checkbox[media_type].values())

    @test_case()
    def validate_available_inventory_supplier(self):
        element_list = self.pages.new_agency_page.find_elements(self.pages.new_agency_page.agency_invenotry_supplier_label)
        for element in element_list:
            assert self.pages.new_agency_page.get_content_text(element) in self.dx_constant.invenotry_supplier_label_list

    @test_case()
    def validate_available_insights(self):
        self.pages.new_agency_page.click_inherit_licenses_checkbox()
        for insight in ['frequency', 'consideration', 'retargeting', 'index']:
            self.assert_is_element_present(self.pages.new_agency_page, self.pages.new_agency_page.insights[insight].values())

    def fill_fields_with_255_char(self):
        attribute_dict = self.pages.new_agency_page.attributes
        new_value = self.pages.new_agency_page.get_random_string(255)
        self.agency_name = new_value
        for key, value in attribute_dict.iteritems():
                attribute_dict[key] = new_value
        attribute_dict['email'] = new_value[:244] + '@dataxu.com'
        attribute_dict['add_on_cost_name'] = self.pages.new_agency_page.get_random_digits(255)
        attribute_dict['add_on_cost_value'] = '100'
        self.pages.new_agency_page.click_cogs_inherited_value_checkbox()
        self.pages.new_agency_page.click_margin_inherited_value_checkbox()
        self.pages.new_agency_page.type_cogs_value('9')
        self.pages.new_agency_page.type_margin_value('99')
        self.pages.new_agency_page.click_inherit_licenses_checkbox()
        for element in ['Online', 'Mobile', 'Video']:
            if not self.pages.new_agency_page.find_element(self.pages.new_agency_page.online_media_type_checkbox[element.lower()].values()).is_selected(): 
                self.pages.new_agency_page.click_media_type_checkbox(element)
        self.pages.new_agency_page.select_all_inventory()
        if self.pages.new_agency_page.is_element_present(self.pages.new_agency_page.dx_technical_exchange):
            self.pages.new_agency_page.find_element(self.pages.new_agency_page.dx_technical_exchange).click()
        insight_dict = {
            'Frequency Impact Report': 'frequency',
            'Consideration Period Report': 'consideration',
            'Retargeting Effectiveness Report': 'retargeting',
            'Index of Best Metrocodes': 'index'
        }
        for key,value in insight_dict.iteritems():
            if not self.pages.new_agency_page.find_element(self.pages.new_agency_page.insights[insight_dict[key]].values()).is_selected():
                self.pages.new_agency_page.select_insights(key)
        self.pages.new_agency_page.fill_fields(attribute_dict)
        self.success_message = self.pages.new_agency_page.success_message['organization_name']

    @test_case()
    def validate_add_on_cost_name_with_255_char(self):
        self.pages.new_agency_page.check_success_message(self.success_message['create_new_agency'].format(self.agency_name))

    def validate_with_255_char(self):
        self.pages.new_agency_page.check_success_message(self.success_message['create_new_agency'].format(self.agency_name))

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
        self.pages.new_agency_page.page_should_contain('United States Dollar (USD)')

    @test_case()
    def validate_cogs_value_less_than_10(self):
        data = self.pages.agency_details_page.get_content_text(self.pages.agency_details_page.cogs_value)
        assert data == '$9.00', data

    @test_case()
    def validate_margin_value_less_than_100(self):
        data = self.pages.agency_details_page.get_content_text(self.pages.agency_details_page.margin_value)
        assert data == '99.0', data

    @test_case()
    def validate_online_checked_on_edit_page(self):
        self.pages.agency_details_page.click_edit_details()
        self.assert_is_selected(self.pages.agency_edit_page, self.pages.agency_edit_page.online_media_type_checkbox['online'].values())

    @test_case()
    def validate_mobile_checked_on_edit_page(self):
        self.assert_is_selected(self.pages.agency_edit_page, self.pages.agency_edit_page.online_media_type_checkbox['mobile'].values())

    @test_case()
    def validate_video_checked_on_edit_page(self):
        self.assert_is_selected(self.pages.agency_edit_page, self.pages.agency_edit_page.online_media_type_checkbox['video'].values())

    @test_case()
    def validate_insights_checked_on_edit_page(self):
        for element in ['frequency', 'consideration', 'retargeting', 'index']:
            self.assert_is_selected(self.pages.agency_edit_page, self.pages.agency_edit_page.insights[element].values())

    @test_case()
    def validate_checked_inventories_on_edit_page(self):
        for inventory in self.dx_constant.inventory_list:
            self.assert_is_element_present(self.pages.agency_edit_page, [self.pages.agency_edit_page.invetory_locator[0], self.pages.agency_edit_page.invetory_locator[1].format(inventory)])

    def fill_fields_with_valid_values(self):
        self.open_new_agency_page()
        attribute_dict = self.pages.new_agency_page.attributes
        new_value = self.pages.new_agency_page.get_random_string(10)
        self.agency_name = "test_agency_" + new_value
        attribute_dict['organization_name'] = self.agency_name
        attribute_dict['contact_name'] = '102348'
        attribute_dict['rate_card'] = ''
        attribute_dict['email'] = 'cdeokar@dataxu.com'
        attribute_dict['add_on_cost_name'] = "test_aoc" + new_value
        self.add_on_cost_names = attribute_dict['add_on_cost_name']
        attribute_dict['add_on_cost_value'] = '3.333621'
        self.pages.new_agency_page.click_cogs_inherited_value_checkbox()
        self.pages.new_agency_page.type_cogs_value('0.155')
        self.pages.new_agency_page.click_inherit_licenses_checkbox()
        for element in ['Online', 'Mobile', 'Video']:
            if self.pages.new_agency_page.find_element(self.pages.new_agency_page.online_media_type_checkbox[element.lower()].values()).is_selected(): 
                self.pages.new_agency_page.click_media_type_checkbox(element)
        insight_dict = {
            'Frequency Impact Report': 'frequency',
            'Consideration Period Report': 'consideration',
            'Retargeting Effectiveness Report': 'retargeting',
            'Index of Best Metrocodes': 'index'
        }
        for key,value in insight_dict.iteritems():
            if self.pages.new_agency_page.find_element(self.pages.new_agency_page.insights[insight_dict[key]].values()).is_selected():
                self.pages.new_agency_page.select_insights(key)
        for inventory in self.dx_constant.uncheck_inventory_list:
            if self.pages.new_agency_page.find_element(['css selector', self.pages.new_agency_page.inventory_select.format(inventory)]).is_selected():
                self.pages.new_agency_page.select_inventories(inventory)
        self.pages.new_agency_page.fill_fields(attribute_dict)

    @test_case()
    def validate_fractional_penny_add_on_cost(self):
        element_list = self.pages.agency_details_page.find_elements(self.pages.agency_details_page.add_on_cost_rate)
        flag = False
        for element in element_list:
            if '$3.333621' == self.pages.agency_details_page.get_content_text(element):
                flag = True
                break
        assert flag is True

    @test_case()
    def validate_add_on_cost_name(self):
        element_list = self.pages.agency_details_page.find_elements(self.pages.agency_details_page.add_on_cost_name)
        flag = False
        for element in element_list:
            if self.add_on_cost_names == self.pages.agency_details_page.get_content_text(element):
                flag = True
                break
        assert flag is True

    @test_case()
    def validate_proper_email_id(self):
        self.validate_add_on_cost_name_with_255_char()

    @test_case()
    def validate_contact_with_digits(self):
        self.validate_with_255_char()

    @test_case()
    def validate_cogs_value_as_decimal(self):
        data = self.pages.agency_details_page.get_content_text(self.pages.agency_details_page.cogs_value)
        assert data == '$0.16', data

    @test_case()
    def validate_agency_creates_without_rate_card(self):
        self.validate_with_255_char()

    @test_case()
    def validate_online_unchecked_on_edit_page(self):
        self.pages.agency_details_page.click_edit_details()
        self.assert_is_selected(self.pages.agency_edit_page, self.pages.agency_edit_page.online_media_type_checkbox['online'].values(), criteria=False)

    @test_case()
    def validate_mobile_unchecked_on_edit_page(self):
        self.assert_is_selected(self.pages.agency_edit_page, self.pages.agency_edit_page.online_media_type_checkbox['mobile'].values(), criteria=False)

    @test_case()
    def validate_video_unchecked_on_edit_page(self):
        self.assert_is_selected(self.pages.agency_edit_page, self.pages.agency_edit_page.online_media_type_checkbox['video'].values(), criteria=False)

    @test_case()
    def validate_insights_unchecked_on_edit_page(self):
        for element in ['frequency', 'consideration', 'retargeting', 'index']:
            self.assert_is_selected(self.pages.agency_edit_page, self.pages.agency_edit_page.insights[element].values(), criteria=False)

    @test_case()
    def validate_unchecked_inventories_on_edit_page(self):
        for inventory in self.dx_constant.inventory_list:
            self.assert_is_element_present(self.pages.agency_edit_page, [self.pages.agency_edit_page.invetory_locator[0], self.pages.agency_edit_page.invetory_locator[1].format(inventory)])

    @test_case()
    def validate_grayed_out_field_on_new_agency_page(self):
        self.open_new_agency_page()
        time.sleep(5)
        for element in ['organization_type', 'agency_group_disabled']:
            self.assert_is_element_present(self.pages.new_agency_page, element)

    @test_case()
    def validate_configure_seat_pop_up(self):
        assert 'Inheriting Seat' in self.pages.new_agency_page.get_content_text(self.pages.new_agency_page.configure_seats_pop_up['seat_content'].values())
        self.pages.new_agency_page.click_seats_edit_icon()
        for element in ['inherit_checkbox', 'override_checkbox', 'ok_button', 'cancel_button']:
            self.assert_is_element_present(self.pages.new_agency_page, self.pages.new_agency_page.configure_seats_pop_up[element].values())

    @test_case()
    def edit_configure_seat(self):
        self.pages.new_agency_page.click_seats_override_radio_button()
        self.pages.new_agency_page.type_seat_name('test')
        self.pages.new_agency_page.type_seat_id('123')
        self.pages.new_agency_page.click_seats_ok_button()
        assert 'test - 123' in self.pages.new_agency_page.get_content_text(self.pages.new_agency_page.configure_seats_pop_up['seat_content'].values())

    @test_case()
    def validate_seat_configuration_on_show_page(self):
        self.agency_name = 'seat_edited_agency_{0}'.format(self.pages.new_agency_page.get_random_string(11)) 
        self.pages.new_agency_page.type_organization_name(self.agency_name)
        self.pages.new_agency_page.click_create_agency_button()
        self.validate_add_on_cost_name_with_255_char()
        assert 'test - 123' in self.pages.agency_details_page.get_content_text(self.pages.agency_details_page.seat_content)

    @test_case()
    def validate_agency_with_blank_email(self):
        self.validate_with_255_char()

    @test_case()
    def validate_agency_with_blank_contact_name(self):
        self.validate_with_255_char()

    def get_error_message_list(self, page_object):
        element_list = page_object.find_elements(['css selector', page_object.error_message_locator])
        message_list = []
        for element in element_list:
            message_list.append(page_object.get_content_text(element))
        return message_list

    def validate_with_blank(self):
        self.open_new_agency_page()
        self.pages.new_agency_page.type_organization_name(self.agency_name)
        self.pages.new_agency_page.type_email('@dataxu.com')
        self.pages.new_agency_page.upload_rate_card(os.getcwd() + '/data/rate_cards/rate_card_BRL.xls')
        self.pages.new_agency_page.click_new_add_on_cost_button()
        self.pages.new_agency_page.click_create_agency_button()
        self.message_list = self.get_error_message_list(self.pages.new_agency_page)

    def validate_message(self, message):
        assert message in self.message_list

    @test_case()
    def validate_duplicate_name(self):
        self.validate_message(self.pages.new_agency_page.duplicate_agency_error_message)

    @test_case()
    def validate_blank_add_on_cost_name(self):
        self.validate_message(self.pages.new_agency_page.blank_add_on_cost_name)

    @test_case()
    def validate_blank_add_on_cost_value(self):
        self.validate_message(self.pages.new_agency_page.blank_add_on_cost_value)

    @test_case()
    def validate_email_with_invalid_value(self):
        self.validate_message(self.pages.new_agency_page.invalid_email_message)

    @test_case()
    def validate_agency_with_other_currency_rate_card(self):
        self.validate_message(self.pages.new_agency_page.upload_other_currency_rate_card)

    def fill_fields_with_260_char(self):
        attribute_dict = self.pages.new_agency_page.attributes
        new_value = self.pages.new_agency_page.get_random_digits(260)
        self.add_on_cost_value = new_value
        for key, value in attribute_dict.iteritems():
                attribute_dict[key] = new_value
        attribute_dict['add_on_cost_value'] = '101'
        attribute_dict['rate_card'] = os.getcwd() + '/lib/dx_date.py'
        self.pages.new_agency_page.fill_fields(attribute_dict)

    @test_case()
    def validate_add_on_cost_name_with_260_char(self):
        self.message_list = self.get_error_message_list(self.pages.new_agency_page)
        self.validate_message(self.pages.new_agency_page.add_on_cost_name_more_than_255)

    @test_case()
    def validate_add_on_cost_cpm_value_more_than_100(self):
        self.validate_message(self.pages.new_agency_page.add_on_cost_more_than_hundred)

    @test_case()
    def validate_organization_name_with_260_char(self):
        self.validate_message(self.pages.new_agency_page.agency_name_more_than_255)

    @test_case()
    def validate_email_with_260_char(self):
        self.validate_message(self.pages.new_agency_page.email_more_than_255)

    @test_case()
    def validate_contact_name_with_260_char(self):
        self.validate_message(self.pages.new_agency_page.email_more_than_255)

    @test_case()
    def validate_rate_card_with_invalid_file(self):
        self.validate_message(self.pages.new_agency_page.invalid_rate_card)

    def fill_fields_with_special_char(self):
        self.pages.new_agency_page.type_organization_name('!@#$%^%')
        self.pages.new_agency_page.type_email('test@')
        self.pages.new_agency_page.type_contact_name('!@#$%^%')
        self.pages.new_agency_page.click_margin_inherited_value_checkbox()
        self.pages.new_agency_page.click_cogs_inherited_value_checkbox()
        self.pages.new_agency_page.type_margin_value('!@#$%^%')
        self.pages.new_agency_page.click_create_agency_button()
        self.message_list = self.get_error_message_list(self.pages.new_agency_page)

    @test_case()
    def validate_organization_name_with_special_char(self):
        self.validate_message(self.pages.new_agency_page.organization_name_with_special_char)

    @test_case()
    def validate_email_id_with_wrong_data(self):
        self.validate_message(self.pages.new_agency_page.invalid_email_message)

    @test_case()
    def validate_contact_name_with_special_char(self):
        self.validate_message(self.pages.new_agency_page.contact_name_with_special_character)

    @test_case()
    def validate_margin_with_special_char(self):
        self.validate_message(self.pages.new_agency_page.margin_with_special_char)

    @test_case()
    def fill_fields_with_html_tag(self):
        data = self.dx_constant.html_tag
        self.pages.new_agency_page.type_organization_name(data)
        self.pages.new_agency_page.type_email(data)
        self.pages.new_agency_page.type_contact_name(data)
        self.pages.new_agency_page.click_create_agency_button()
        self.message_list = self.get_error_message_list(self.pages.new_agency_page)

    @test_case()
    def validate_organization_name_with_html_tag(self):
        self.validate_message(self.pages.new_agency_page.organization_name_with_html_tag)

    @test_case()
    def validate_email_with_html_tag(self):
        self.validate_message(self.pages.new_agency_page.email_with_html_tag)

    @test_case()
    def validate_contact_name_with_html_tag(self):
        self.validate_message(self.pages.new_agency_page.contact_name_with_html_tag)

    @test_case()
    def validate_contacted_currency_grayed_out_on_edit_page(self):
        self.open_new_agency_list_page()
        self.pages.agency_list_page.click_first_edit_icon()
        time.sleep(5)
        self.assert_is_element_present(self.pages.agency_edit_page, 'disabled_currency_drop_down')

    @test_case()
    def validate_other_than_contracted_currency_not_accepted(self):
        self.pages.agency_edit_page.upload_rate_card(os.getcwd() + '/data/rate_cards/rate_card_PLN.xls')
        self.pages.agency_edit_page.click_create_agency_button()
        self.message_list = self.get_error_message_list(self.pages.agency_edit_page)
        counter = -1
        for message in self.message_list:
            counter = message.find(self.pages.agency_edit_page.error_message_currency_other_than_contracted)
            if counter >= 0:
                break
        assert counter >= 0, "Given message don't found in message list"
