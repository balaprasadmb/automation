from dx_test.dx_test import DXTest
from lib.gui_tests import test_case

class UserTest(DXTest):

    @test_case()
    def login_as_admin(self):
        self.setup()

    @test_case()
    def functionality_of_users_link(self):
        self.pages.admin_page.click_on_users_link()
        self.pages.user_list_page.wait_till_visible(self.pages.user_list_page.list_pagination_setup)
        assert self.pages.user_list_page.is_element_present(self.pages.user_list_page.new_user_button)
    
    @test_case()
    def user_list_table_column_name(self):
        for content in self.pages.user_list_page.user_list_page_contents:
            self.pages.user_list_page.page_should_contain(content)

    @test_case()
    def functionality_of_new_user_button_and_verify_contents(self):
        self.pages.user_list_page.click_on_new_user_button()
        self.pages.new_user_page.wait_till_visible(self.pages.new_user_page.add_user_role_button)
        for page_content in self.pages.new_user_page.sections_title:
            self.pages.new_user_page.page_should_contain(page_content)
        assert self.pages.new_user_page.is_element_present(self.pages.new_user_page.submit_button)
