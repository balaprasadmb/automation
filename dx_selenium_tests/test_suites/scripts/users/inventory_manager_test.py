from dx_test.dx_test import DXTest
from lib.gui_tests import test_case

class InventoryManagerTest(DXTest):

    @test_case()
    def login_as_inventory_manager(self):
        self.setup(self.dx_constant.user_by_role['inventory_manager'])

    @test_case()
    def verify_admin_page_contents_for_inventory_manager(self):
       for content in self.pages.admin_page.admin_page_contents_by_role['inventory_manager'].values():
            self.pages.admin_page.page_should_contain(content)

    @test_case()
    def not_permitted_to_create_campaign(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_create_campaign)

    @test_case()
    def not_permitted_to_create_creative(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_create_creative)

    @test_case()
    def not_permitted_to_create_user(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_create_user)

    @test_case()
    def not_permitted_to_create_reports(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_create_reports)

    @test_case()
    def not_permitted_to_product_feature(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_product_feature)

    @test_case()
    def not_permitted_to_login_slide(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_login_slide)

    @test_case()
    def not_permitted_to_audience(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_audience)
        self.pages.admin_page.link_not_exists(self.pages.admin_page.audience_tab)

    @test_case()
    def not_permitted_to_activity(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_activity)
        self.pages.admin_page.link_not_exists(self.pages.admin_page.activity_tab)

    @test_case()
    def permitted_to_inventory(self):
        self.pages.admin_page.page_should_contain(self.pages.admin_page.permitted_to_inventory)
        self.pages.admin_page.link_exists(self.pages.admin_page.inventory_tab)

    @test_case()
    def permitted_to_edit_my_account(self):
        self.pages.admin_page.click_on_edit_my_account_link()
        self.pages.user_edit_page.page_should_contain(self.pages.user_edit_page.user_edit_page_title)
