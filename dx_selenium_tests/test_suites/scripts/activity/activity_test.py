#coding: utf-8
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from selenium.webdriver.common.keys import Keys
from common_helpers.common_helpers import CommonHelper

class ActivityTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.common_helper = CommonHelper()
        self.setup(self.dx_constant.user_by_role['campaign_manager'])

    @test_case()
    def click_on_activity_tab(self):
        self.pages.search_page.click_activity_tab()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)

    @test_case()
    def functionality_of_advertiser_dropdown(self):
        self.click_on_activity_tab()
        actual_advertiser_name = self.dx_constant.advertiser_name
        self.pages.activity_list_page.select_organization(actual_advertiser_name)
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        expected_advertiser_name = self.pages.activity_list_page.get_innerhtml_text("seleceted_organization_name")
        assert actual_advertiser_name in expected_advertiser_name

    @test_case()
    def activity_list_page_contents(self):
        for page_content in self.pages.activity_list_page.activity_list_page_contents:
            self.pages.activity_list_page.page_should_contain(page_content)
        for element in self.pages.activity_list_page.activity_list_page_elements:
            assert self.pages.activity_list_page.is_element_present(getattr(self.pages.activity_list_page, element))

    @test_case()
    def check_all_checkboxes_are_checked(self, criteria=True):
        elements = [self.pages.activity_list_page.header_master_checkbox, self.pages.activity_list_page.first_activity_checkbox,
                    self.pages.activity_list_page.footer_master_checkbox]
        for element in elements:
            self.common_helper.assert_is_selected(self.pages.activity_list_page, element, criteria)

    @test_case()
    def functionality_of_master_checkbox(self):
        for checkbox in ['click_activity_header_master_checkbox', 'click_activity_footer_master_checkbox']:
            getattr(self.pages.activity_list_page, checkbox)()
            self.check_all_checkboxes_are_checked()
            getattr(self.pages.activity_list_page, checkbox)()
            self.check_all_checkboxes_are_checked(criteria=False)

    @test_case()
    def gear_icon_contents(self):
        self.pages.activity_list_page.click_gear_icon()
        for elements in self.pages.activity_list_page.activity_gear_icon_elements:
            assert self.pages.activity_list_page.is_element_present(getattr(self.pages.activity_list_page, elements))

    @test_case()
    def functionality_of_activity_name(self):
        expected_activity_name = self.pages.activity_list_page.get_innerhtml_text("first_activity_name")
        self.pages.activity_list_page.click_activity_name()
        self.pages.activity_show_page.wait_till_visible(self.pages.activity_show_page.activity_show_page_locator)
        actual_activity_name = self.pages.activity_show_page.get_activity_name()
        assert actual_activity_name in expected_activity_name

    @test_case()
    def activity_show_page_contents(self):
        for page_contents in self.pages.activity_show_page.activity_show_page_contents:
            self.pages.activity_show_page.page_should_contain(page_contents)
        for element in self.pages.activity_show_page.activity_show_page_elements:
            assert self.pages.activity_show_page.is_element_present(getattr(self.pages.activity_show_page, element))

    @test_case()
    def functionality_of_edit_link_from_show_page(self):
        self.pages.activity_show_page.click_edit_link()
        self.pages.activity_edit_page.wait_till_visible(self.pages.activity_edit_page.create_activity_button)
        self.pages.activity_edit_page.page_should_contain("Edit activity")

    @test_case()
    def existing_activity_edit_page_contents(self):
        for element in self.pages.activity_edit_page.activity_edit_page_elements:
            assert self.pages.activity_edit_page.is_element_present(getattr(self.pages.activity_edit_page, element))
        for element in self.pages.activity_edit_page.unavailable_elements:
            assert not self.pages.activity_edit_page.is_element_present(getattr(self.pages.activity_edit_page, element))

    @test_case()
    def functionality_of_cancel_button_from_edit_page(self):
        self.pages.activity_edit_page.click_cancel_button()
        self.pages.activity_show_page.wait_till_visible(self.pages.activity_show_page.activity_show_page_locator)
        self.activity_show_page_contents()

    @test_case()
    def functionality_of_activities_link_from_show_page(self):
        self.pages.activity_show_page.click_activities_link()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        self.activity_list_page_contents()

    @test_case()
    def functionality_of_view_activity_link_from_gear_icon(self):
        expected_activity_name = self.pages.activity_list_page.get_innerhtml_text("first_activity_name")
        self.pages.activity_list_page.click_gear_icon()
        self.pages.activity_list_page.click_view_activity_link()
        self.pages.activity_show_page.wait_till_visible(self.pages.activity_show_page.activity_show_page_locator)
        actual_activity_name = self.pages.activity_show_page.get_activity_name()
        assert actual_activity_name in expected_activity_name
        self.functionality_of_activities_link_from_show_page()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        self.activity_list_page_contents()

    @test_case()
    def functionality_of_edit_link_from_gear_icon(self):
        self.pages.activity_list_page.click_gear_icon()
        self.pages.activity_list_page.click_edit_activity_link()
        self.pages.activity_edit_page.wait_till_visible(self.pages.activity_edit_page.create_activity_button)
        assert self.pages.activity_edit_page.is_element_present(self.pages.activity_edit_page.create_activity_button)
        self.pages.activity_edit_page.click_activities_link()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        self.activity_list_page_contents()

    @test_case()
    def functionality_of_new_activity_button(self):
        self.pages.activity_list_page.click_on_create_new_activity_button()
        self.pages.activity_create_new_page.wait_till_visible(self.pages.activity_create_new_page.create_activity_button)
        self.pages.activity_create_new_page.page_should_contain("Create activity")

    @test_case()
    def new_activity_edit_page_contents_for_permission_user(self):
        for element in self.pages.activity_create_new_page.activity_create_new_page_elements:
            assert self.pages.activity_create_new_page.is_element_present(getattr(self.pages.activity_create_new_page, element))

    @test_case()
    def activity_type_dropdown_options(self):
        elements = self.pages.activity_create_new_page.find_elements(self.pages.activity_create_new_page.activity_type_dropdown_option)
        actual_option_text = []
        for element in elements:
            actual_option_text.append(element.get_attribute('innerHTML'))
        for option in actual_option_text:
            assert option in self.pages.activity_create_new_page.expected_activity_type_options

    @test_case()
    def functionality_of_add_pixel_button(self):
        self.pages.activity_create_new_page.click_add_pixel_button()
        for element in self.pages.activity_create_new_page.activity_second_row_elements:
            assert self.pages.activity_create_new_page.is_element_present(getattr(self.pages.activity_create_new_page, element))

    @test_case()
    def functionality_of_remove_button(self):
        self.pages.activity_create_new_page.click_remove_button()
        for element in self.pages.activity_create_new_page.activity_second_row_elements:
            assert not self.pages.activity_create_new_page.is_element_present(getattr(self.pages.activity_create_new_page, element))

    @test_case()
    def set_activity_name_and_save(self, activity_name):
        self.pages.activity_create_new_page.enter_activity_name_first(activity_name)
        self.pages.activity_create_new_page.click_create_activity_button()
        self.pages.activity_create_new_page.wait_till_visible(self.pages.activity_create_new_page.create_activity_button)

    @test_case()
    def activity_with_blank_name(self):
        self.set_activity_name_and_save('')
        self.pages.activity_create_new_page.page_should_contain("Activity name can't be blank")

    @test_case()
    def activity_name_with_script_tag(self):
        self.set_activity_name_and_save(self.dx_constant.html_tag)
        self.pages.activity_create_new_page.page_should_contain("Activity name is invalid")

    @test_case()
    def activity_name_with_more_than_255_char(self):
        self.set_activity_name_and_save(self.pages.activity_create_new_page.get_random_string(256))
        self.pages.activity_create_new_page.page_should_contain("Activity name is too long (maximum is 255 characters)")

    @test_case()
    def functionality_of_cancel_button_from_create_activity_page(self):
        self.pages.activity_create_new_page.click_cancel_button()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        self.activity_list_page_contents()

    @test_case()
    def valid_activity_name(self, activity_name):
        self.pages.activity_list_page.click_on_create_new_activity_button()
        self.pages.activity_create_new_page.wait_till_element_clickable(self.pages.activity_create_new_page.create_activity_button)
        self.pages.activity_create_new_page.enter_activity_name_first(activity_name)
        self.pages.activity_create_new_page.click_create_activity_button()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        self.pages.activity_list_page.page_should_contain("Activity successfully created:")

    @test_case()
    def activity_name_with_255_chars_and_search_functionality(self):
        activity_name = self.pages.activity_list_page.get_random_string(255)
        self.valid_activity_name(activity_name)
        self.activity_search_functionality(activity_name)

    @test_case()
    def update_activity_with_name(self, activity_name):
        self.functionality_of_edit_link_from_show_page()
        self.pages.activity_edit_page.enter_activity_name(activity_name)
        self.pages.activity_edit_page.click_create_activity_button()
        self.pages.activity_show_page.wait_till_visible(self.pages.activity_show_page.activity_show_page_locator)
        self.pages.activity_show_page.page_should_contain(self.pages.activity_show_page.update_success_message.format(activity_name))

    @test_case()
    def activity_name_with_special_chars(self):
        self.update_activity_with_name("!@#$%" + self.pages.activity_create_new_page.get_random_string(10))

    @test_case()
    def activity_name_with_alphanumeric_chars(self):
        self.update_activity_with_name(self.pages.activity_list_page.get_random_string())

    @test_case()
    def activity_search_functionality(self, activity_name):
        expected_activity_name = activity_name
        self.pages.activity_list_page.search_activity(activity_name)
        self.pages.activity_list_page.click_activity_name()
        self.pages.activity_show_page.wait_till_visible(self.pages.activity_show_page.activity_show_page_locator)
        actual_activity_name = self.pages.activity_show_page.get_activity_name()
        assert actual_activity_name in expected_activity_name
        
    @test_case()
    def fill_up_activity_fields(self, activity_type, is_secure=False):
        self.click_on_activity_tab()
        self.functionality_of_advertiser_dropdown()
        self.functionality_of_new_activity_button()
        activity_name = self.pages.activity_create_new_page.get_random_string()
        self.pages.activity_create_new_page.enter_activity_name_first(activity_name)
        self.pages.activity_create_new_page.select_activity_type(activity_type)
        self.pages.activity_create_new_page.select_tag_server("DFA")
        self.pages.activity_create_new_page.enter_tag_id_first(self.pages.activity_create_new_page.get_random_digits(8))
        if is_secure:
            self.pages.activity_create_new_page.click_secure_checkbox_first()
        self.pages.activity_create_new_page.click_rmx_checkbox_first()
        self.pages.activity_create_new_page.click_create_activity_button()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        self.pages.activity_list_page.page_should_contain("Activity successfully created:")
        return activity_name

    @test_case()
    def creation_of_new_activity_with_secure(self):
        activity_name = self.fill_up_activity_fields("Marketing", True)
        self.activity_search_functionality(activity_name)
        pixel_tag_value = self.pages.activity_show_page.get_pixel_tag_value()
        for content in ['img', 'https']:
            assert content in pixel_tag_value

    @test_case()
    def creation_of_new_activity_with_non_secure(self):
        activity_name = self.fill_up_activity_fields("Product")
        self.activity_search_functionality(activity_name)
        pixel_tag_value = self.pages.activity_show_page.get_pixel_tag_value()
        for content in ['img', 'http']:
            assert content in pixel_tag_value
        for content in ['https']:
            assert content not in pixel_tag_value

    @test_case()
    def creation_of_activity_with_segment_and_audience(self):
        self.click_on_activity_tab()
        self.functionality_of_advertiser_dropdown()
        self.functionality_of_new_activity_button()
        self.pages.activity_create_new_page.enter_activity_name_first(self.pages.activity_create_new_page.get_random_string())
        self.pages.activity_create_new_page.select_activity_type("Homepage")
        self.pages.activity_create_new_page.select_tag_server("DFA")
        self.pages.activity_create_new_page.enter_tag_id_first(self.pages.activity_create_new_page.get_random_digits(8))
        self.pages.activity_create_new_page.click_secure_checkbox_first()
        self.pages.activity_create_new_page.click_rmx_checkbox_first()
        segment_audience_name = "segment_audience-"+self.pages.activity_create_new_page.get_random_string()
        self.pages.activity_create_new_page.check_create_segment_checkbox()
        self.pages.activity_create_new_page.enter_activity_segment_name(segment_audience_name)
        self.pages.activity_create_new_page.check_create_audience_checkbox()
        self.pages.activity_create_new_page.enter_audience_name(segment_audience_name)
        self.pages.activity_create_new_page.click_create_activity_button()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        self.pages.activity_list_page.page_should_contain("Activity successfully created:")

    @test_case()
    def functionality_of_share_button(self):
        expected_shared_staus = "With Others"
        self.pages.activity_list_page.select_first_activity_checkbox()
        self.pages.activity_list_page.click_share_activities_button()
        for element in self.pages.activity_list_page.activity_share_popup_element:
            assert self.pages.activity_list_page.is_element_present(getattr(self.pages.activity_list_page, element))
        self.pages.activity_list_page.select_sharing_organization()
        self.pages.activity_list_page.click_share_button_from_popup()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        actual_shared_status = self.pages.activity_list_page.get_innerhtml_text("shared_status")
        assert expected_shared_staus in actual_shared_status

    @test_case()
    def functionality_of_display_check_activities_button(self):
        self.pages.activity_list_page.select_first_activity_checkbox()
        self.pages.activity_list_page.click_display_checked_activities_button()
        assert self.pages.activity_list_page.find_element(self.pages.activity_list_page.display_activities_popup).is_displayed()
        self.pages.activity_list_page.click_display_activities_close_btn()
        assert not self.pages.activity_list_page.find_element(self.pages.activity_list_page.display_activities_popup).is_displayed()

    @test_case()
    def updating_existing_activity(self):
        self.pages.activity_list_page.click_gear_icon()
        self.pages.activity_list_page.click_edit_activity_link()
        self.pages.activity_edit_page.wait_till_element_clickable(self.pages.activity_edit_page.create_activity_button)
        activity_name = self.pages.activity_edit_page.get_random_string()
        self.pages.activity_edit_page.enter_activity_name(activity_name)
        self.pages.activity_edit_page.select_activity_type("Expand")
        self.pages.activity_edit_page.select_tag_server("DFA")
        self.pages.activity_edit_page.enter_tag_id(self.pages.activity_create_new_page.get_random_digits(8))
        self.pages.activity_edit_page.click_secure_checkbox()
        self.pages.activity_edit_page.click_rmx_checkbox()
        self.pages.activity_edit_page.click_create_activity_button()
        self.pages.activity_show_page.wait_till_visible(self.pages.activity_show_page.activity_show_page_locator)
        self.pages.activity_show_page.page_should_contain(self.pages.activity_show_page.update_success_message.format(activity_name))
        
    @test_case()
    def creation_of_multiple_activities(self):
        self.click_on_activity_tab()
        self.functionality_of_advertiser_dropdown()
        self.functionality_of_new_activity_button()
        self.pages.activity_create_new_page.enter_activity_name_first(self.pages.activity_create_new_page.get_random_string())
        self.pages.activity_create_new_page.click_add_pixel_button()
        self.pages.activity_create_new_page.enter_activity_name_second(self.pages.activity_create_new_page.get_random_string())
        self.pages.activity_create_new_page.click_create_activity_button()
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        self.pages.activity_list_page.page_should_contain("2 Activities successfully created:")

    @test_case()
    def activity_list_page_contents_without_permissions(self):
        self.common_helper.logout_and_login_by_new_user(self.pages.login_page.driver, 'campaign_manager_one_view')
        self.click_on_activity_tab()
        self.pages.activity_list_page.select_organization(self.dx_constant.advertiser_name)
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        for page_content in self.pages.activity_list_page.activity_list_page_contents:
            self.pages.activity_list_page.page_should_contain(page_content)
        for element in self.pages.activity_list_page.activity_list_page_elements_without_permission:
            assert self.pages.activity_list_page.is_element_present(getattr(self.pages.activity_list_page, element))
        assert not self.pages.activity_list_page.is_element_present(self.pages.activity_list_page.share_activities_button)

    @test_case()
    def new_activity_edit_page_contents_without_permissions(self):
        self.pages.activity_list_page.click_on_create_new_activity_button()
        self.pages.activity_create_new_page.wait_till_element_clickable(self.pages.activity_create_new_page.create_activity_button)
        for element in self.pages.activity_create_new_page.create_new_page_elements_without_permissions:
            assert self.pages.activity_create_new_page.is_element_present(getattr(self.pages.activity_create_new_page, element))
        for element in self.pages.activity_create_new_page.unavilable_create_new_page_elements_without_permissions:
            assert not self.pages.activity_create_new_page.is_element_present(getattr(self.pages.activity_create_new_page, element))
