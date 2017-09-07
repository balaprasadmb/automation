from lib.gui_tests import test_case
from dx_test.dx_test import DXTest
import time

class LoginSlidesTest(DXTest):

    @test_case()
    def login_as_dx_admin(self):
        self.setup()

    @test_case()
    def availability_and_functionality_of_login_screen_slides_link(self):
        self.pages.admin_page.click_login_screen_slides_link()
        self.pages.login_slides_list_page.wait_till_visible(self.pages.login_slides_list_page.login_screen_slides_list_table)
        self.pages.login_slides_list_page.page_should_contain(self.pages.login_slides_list_page.list_page_title)

    @test_case()
    def login_screen_slides_list_page_contents(self):
        for page_contents in self.pages.login_slides_list_page.login_slides_list_page_contents:
            self.pages.login_slides_list_page.page_should_contain(page_contents)
        assert self.pages.login_slides_list_page.is_element_present(self.pages.login_slides_list_page.new_login_slides_btn)

    @test_case()
    def login_screen_slides_create_page_contents(self):
        self.pages.login_slides_list_page.click_new_login_slides_btn()
        self.pages.login_slides_edit_page.wait_till_visible(self.pages.login_slides_edit_page.create_login_slide_btn)
        self.pages.login_slides_edit_page.page_should_contain(self.pages.login_slides_edit_page.login_slide_create_page_title)
        for elements in self.pages.login_slides_edit_page.login_slides_edit_page_elements:
            assert self.pages.login_slides_edit_page.is_element_present(getattr(self.pages.login_slides_edit_page, elements))

    @test_case()
    def creation_of_new_login_screen_slide(self):
        login_slide_name = 'login-screen-name-' + self.pages.login_slides_edit_page.get_random_string(6)
        self.pages.login_slides_edit_page.enter_login_slide_name(login_slide_name)
        self.pages.login_slides_edit_page.enter_login_slide_body('login-slide-body-' + self.pages.login_slides_edit_page.get_random_string())
        self.pages.login_slides_edit_page.click_create_login_slide_btn()
        self.pages.login_slides_show_page.wait_till_visible(self.pages.login_slides_show_page.edit_link)
        self.pages.login_slides_show_page.page_should_contain(self.pages.login_slides_show_page.slide_creation_success_message)
        self.pages.login_slides_show_page.page_should_contain(login_slide_name)

    @test_case()
    def login_screen_slides_show_page_contents_and_links_functionality(self):
        self.pages.login_slides_show_page.click_back_link()
        self.pages.login_slides_list_page.wait_till_visible(self.pages.login_slides_list_page.new_login_slides_btn)
        self.pages.login_slides_list_page.click_first_login_slide_name()
        self.pages.login_slides_show_page.wait_till_visible(self.pages.login_slides_show_page.edit_link)
        self.pages.login_slides_show_page.click_edit_link()
        self.pages.login_slides_edit_page.wait_till_visible(self.pages.login_slides_edit_page.create_login_slide_btn)

    @test_case()
    def updating_existing_login_screen_slide(self):
        login_slide_name = 'login-screen-name-' + self.pages.login_slides_edit_page.get_random_string(6)
        self.pages.login_slides_edit_page.enter_login_slide_name(login_slide_name)
        self.pages.login_slides_edit_page.click_create_login_slide_btn()
        self.pages.login_slides_show_page.wait_till_visible(self.pages.login_slides_show_page.edit_link)
        self.pages.login_slides_show_page.page_should_contain(self.pages.login_slides_show_page.slide_update_success_message)
        self.pages.login_slides_show_page.page_should_contain(login_slide_name)

    @test_case()
    def login_screen_slide_with_cancel(self):
        self.pages.login_slides_list_page._open('/login_screen_slides?locale=en')
        self.pages.login_slides_list_page.wait_till_visible(self.pages.login_slides_list_page.login_screen_slides_list_table)
        self.login_slide_name = self.pages.login_slides_list_page.get_first_login_screen_slide_name()
        self.pages.login_slides_list_page.click_gear_icon()
        self.pages.login_slides_list_page.click_delete_link()
        self.pages.login_slides_list_page.dismiss_alert()
        self.pages.login_slides_list_page.page_should_contain(self.login_slide_name)

    @test_case()
    def login_screen_slide_with_ok(self):
        self.pages.login_slides_list_page.click_delete_link()
        self.pages.login_slides_list_page.accept_alert()
        self.pages.login_slides_list_page.wait_till_visible(self.pages.login_slides_list_page.new_login_slides_btn)
        self.pages.login_slides_list_page.page_should_not_contain(self.login_slide_name)
