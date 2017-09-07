from dx_test.dx_test import DXTest
from lib.dx_date import DXDate
from lib.gui_tests import test_case
import time

class SystemNoticesTest(DXTest):

    @test_case()
    def login_as_dx_admin(self):
        self.setup()

    @test_case()
    def go_to_admin_page(self):
        self.pages.admin_page.open()
        self.pages.admin_page.wait_till_visible(self.pages.admin_page.system_message_table)

    @test_case()
    def validate_system_notices_page_content(self):
        for content in self.pages.system_notices_list_page.system_message_list_contents.values():
            self.pages.system_notices_list_page.page_should_contain(content)

    @test_case()
    def functionality_of_new_system_message(self):
        self.pages.system_notices_list_page.click_on_new_system_message()
        self.pages.edit_system_notices_page.page_should_contain("Create System Message")

    @test_case()
    def check_gear_icon_list(self):
        self.go_to_admin_page()
        self.pages.system_notices_list_page.click_on_gear_icon()
        element_list = self.pages.system_notices_list_page.gear_icon_system_message
        for element in element_list:
            assert self.pages.system_notices_list_page.is_element_present(["link text", element])

    @test_case()
    def check_functionality_name_link(self):
        self.pages.system_notices_list_page.click_on_first_system_message_name()
        self.pages.edit_system_notices_page.wait_till_visible(self.pages.edit_system_notices_page.cancel_button)
        self.pages.edit_system_notices_page.page_should_contain("View System Message")

    @test_case()
    def check_functionality_of_edit_link(self):
        self.pages.system_notices_list_page.click_on_edit_link()
        self.pages.system_notices_list_page.page_should_contain("Edit System Message")

    @test_case()
    def check_functionality_of_preview_link(self):
        self.go_to_admin_page()
        self.pages.system_notices_list_page.click_on_gear_icon()
        self.pages.system_notices_list_page.click_on_preview_link()
        self.pages.system_notices_list_page.is_element_present(self.pages.system_notices_list_page.preview_popup_content)
        self.pages.system_notices_list_page.close_preview_popup()

    @test_case()
    def check_functionality_of_delete_link(self):
        self.pages.system_notices_list_page.click_on_delete_link()
        self.pages.system_notices_list_page.dismiss_alert()
        self.pages.system_notices_list_page.page_should_not_contain(self.pages.system_notices_list_page.delete_message)
        self.pages.system_notices_list_page.click_on_delete_link()
        self.pages.system_notices_list_page.accept_alert()
        self.pages.system_notices_list_page.page_should_contain(self.pages.system_notices_list_page.delete_message)

    @test_case()
    def check_functionality_of_clone_link(self):
        self.pages.system_notices_list_page.click_on_gear_icon()
        self.pages.system_notices_list_page.click_on_clone_link()
        self.pages.edit_system_notices_page.wait_till_visible(self.pages.edit_system_notices_page.save_message_button)
        self.pages.edit_system_notices_page.page_should_contain("Create System Message")

    @test_case()
    def check_functionality_of_edit_button_from_show_page(self):
        self.go_to_admin_page()
        self.check_functionality_name_link()
        self.pages.edit_system_notices_page.click_on_edit_button()
        self.pages.edit_system_notices_page.wait_till_visible(self.pages.edit_system_notices_page.save_message_button)
        self.pages.edit_system_notices_page.page_should_contain("Edit System Message")

    @test_case()
    def check_functionality_of_cancel_button_from_show_page(self):
        self.go_to_admin_page()
        self.check_functionality_name_link()
        self.pages.edit_system_notices_page.click_on_cancel_button()
        self.pages.admin_page.wait_till_visible(self.pages.admin_page.system_message_table)
        self.pages.system_notices_list_page.page_should_contain("Administration")

    @test_case()
    def check_content_of_new_message_page(self):
        self.pages.system_notices_list_page.click_on_new_system_message()
        self.pages.new_system_message_page.wait_till_visible(self.pages.new_system_message_page.save_message)
        for content in self.pages.new_system_message_page.create_system_message_content:
            self.pages.new_system_message_page.page_should_contain(content)
        new_system_message_content = ['cancel', 'save_message', 'add_external_link']
        for button_name in new_system_message_content:
            assert self.pages.new_system_message_page.is_element_present(getattr(self.pages.new_system_message_page, button_name))

    @test_case()
    def check_functionality_of_status_on_new_message_page(self):
        self.go_to_admin_page()
        self.pages.system_notices_list_page.click_on_new_system_message()
        self.pages.new_system_message_page.fill_title_textbox("test")
        for option in ['Draft', 'Paused', 'Running']:                       
            self.pages.new_system_message_page.select_status_from_dropdown(option)
            self.pages.new_system_message_page.click_on_save_message_button()
            self.pages.system_notices_list_page.click_on_new_system_message()

    @test_case()
    def check_functionality_of_message_text_box(self):
        self.go_to_admin_page()
        self.pages.system_notices_list_page.click_on_new_system_message()
        for message in ['alphanumeric_value', 'special_char', 'strings']:
            self.pages.new_system_message_page.type_message_in_message_body(getattr(self.dx_constant, message))
        self.pages.new_system_message_page.click_on_save_message_button()       

    @test_case()
    def check_functionality_of_importance_drop_down(self):
        self.pages.system_notices_list_page.click_on_admin_link()        
        status='Draft'
        for importance in ['High', 'Normal']:
            self.pages.new_system_message_page.fill_system_message_page("test1", status, importance)
        self.pages.system_notices_list_page.click_on_new_system_message() 

    @test_case()
    def check_functionality_of_ui_content(self):
        self.pages.system_notices_list_page.click_on_admin_link()
        self.pages.new_system_message_page.fill_system_message_page("check external url")

    @test_case()
    def check_functionality_of_cancel_button(self):
        self.pages.system_notices_list_page.click_on_admin_link()
        self.pages.system_notices_list_page.click_on_new_system_message()
        self.pages.new_system_message_page.fill_title_textbox("check cancel button")
        self.pages.new_system_message_page.click_on_cancel_button()
        self.pages.system_notices_list_page.page_should_contain('Administration')

    @test_case()
    def check_functionality_of_dismiss_all_button(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_display_message_link()
        self.pages.admin_page.wait_till_visible(self.pages.admin_page.dismiss_all_notices_button)
        self.pages.admin_page.click_dismiss_all_notices_button()
        assert not self.pages.admin_page.find_element(self.pages.admin_page.display_message_link).is_displayed()
