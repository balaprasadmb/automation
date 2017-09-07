from dx_test.dx_test import DXTest
from lib.gui_tests import test_case

class OrganizationAdministratorTest(DXTest):

    def login_as_organization_administrator(self):
        self.setup(self.dx_constant.user_by_role['organization_administrator'])

    @test_case()
    def permitted_to_edit_my_account(self):
        self.pages.admin_page.open()
        self.pages.admin_page.click_on_edit_my_account_link()
        self.pages.user_edit_page.page_should_contain(self.pages.user_edit_page.user_edit_page_title)

    def create_new_user(self, user_role = 'campaign_manager'):
        self.pages.new_user_page.open()
        self.pages.new_user_page.wait_till_visible(self.pages.new_user_page.add_user_role_button)
        email_id = 'test_' + self.pages.new_user_page.get_random_string(5) + '@dataxu.com'
        self.pages.new_user_page.enter_user_email_id(email_id)
        self.pages.new_user_page.select_organization(self.pages.new_user_page.organization)
        self.pages.new_user_page.click_on_add_user_role_button()
        self.pages.new_user_page.select_organization_to_add_role(self.pages.new_user_page.organization)
        self.pages.new_user_page.select_user_role(self.pages.new_user_page.roles[user_role])
        self.pages.new_user_page.click_on_submit_button()
        self.pages.user_show_page.page_should_contain(self.pages.user_show_page.user_creation_success_message)

    @test_case()
    def create_user_campaign_manager(self):
        self.create_new_user()

    @test_case()
    def create_user_inventory_manager(self):
        self.create_new_user('inventory_manager')

    @test_case()
    def create_user_planner(self):
        self.create_new_user('planner')

    @test_case()
    def create_user_read_only(self):
        self.create_new_user('read_only_user')

    @test_case()
    def create_user_report(self):
        self.create_new_user('report_user')

    @test_case()
    def create_user_support(self):
        self.create_new_user('support_user')

    @test_case()
    def create_user_user_administrator(self):
        self.create_new_user('user_administrator')

    @test_case()
    def not_permitted_to_create_campaign(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_create_campaign)

    @test_case()
    def not_permitted_to_create_reports(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_create_reports)

    @test_case()
    def not_permitted_to_create_creative(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_create_creative)

    @test_case()
    def not_permitted_to_activity(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_activity)
        self.pages.admin_page.link_not_exists(self.pages.admin_page.activity_tab)

    @test_case()
    def not_permitted_to_inventory(self):
        self.pages.admin_page.page_should_not_contain(self.pages.admin_page.permitted_to_inventory)
        self.pages.admin_page.link_not_exists(self.pages.admin_page.inventory_tab)

    @test_case()
    def permitted_to_product_feature(self):
        self.pages.admin_page.page_should_contain(self.pages.admin_page.permitted_to_product_feature)
        self.pages.admin_page.click_on_product_feature_link()
        self.pages.admin_page.wait_till_visible(self.pages.admin_page.product_feature_list_table)
        self.pages.admin_page.page_should_contain('Manage Access to Product Features')
