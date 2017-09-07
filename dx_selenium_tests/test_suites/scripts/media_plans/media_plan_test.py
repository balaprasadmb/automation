from selenium.webdriver.common.keys import Keys
from dx_test.dx_test import DXTest
from lib.dx_date import DXDate
from lib.gui_tests import test_case

class MediaPlanTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.setup(self.dx_constant.user_by_role['campaign_manager'])

    @test_case()
    def go_to_campaign_list_page(self):
        self.pages.search_page.click_campaign_link()
        self.pages.campaign_list_page.wait_till_visible(self.pages.campaign_list_page.campaign_list_table)
        self.pages.campaign_list_page.click_element(self.pages.campaign_list_page.search_box)
        self.pages.campaign_list_page.select_orgnization(self.dx_constant.advertiser_name)
        self.pages.campaign_list_page.wait_till_visible(self.pages.campaign_list_page.campaign_list_table)

    @test_case()
    def go_to_create_media_plan_page(self):
        self.pages.campaign_list_page.click_new_media()
        self.pages.create_media_plan_page.wait_till_visible(self.pages.create_media_plan_page.submit)

    @test_case()
    def create_media_plan_page_contents(self):
        self.go_to_campaign_list_page()
        self.go_to_create_media_plan_page()
        self.pages.create_media_plan_page.click_add_row()
        for element in ['Last View', 'Last Click']:
            self.pages.create_media_plan_page.select_attribution_model(element)
        for value in ['Percent Of Price', 'Fixed']:
            self.pages.create_media_plan_page.select_value_type(value)
        options = ['Days', 'Hours', 'Minutes']
        for option in options:
            self.pages.create_media_plan_page.select_last_click(option)
        for option in options:
            self.pages.create_media_plan_page.select_last_view(option)
        self.pages.create_media_plan_page.page_should_contain('Reporting and Learning Lookback Windows')
        for element in self.pages.create_media_plan_page.create_media_plan_page_contents:
            assert self.pages.create_media_plan_page.is_element_present(getattr(self.pages.create_media_plan_page, element))
 
    @test_case()
    def fill_media_plan_details(self):
        self.media_plan_name = 'test-media-plan-' + self.pages.create_media_plan_page.get_random_string(6)
        self.pages.create_media_plan_page.type_name(self.media_plan_name)
        self.pages.create_media_plan_page.type_start_date(DXDate().todays_date())
        self.pages.create_media_plan_page.type_budget('5000')
        self.pages.create_media_plan_page.type_value('9')
        self.pages.create_media_plan_page.type_end_date(DXDate().date_after_two_days())
        self.pages.create_media_plan_page.click_submit()
        self.pages.media_plan_show_page.wait_till_visible(self.pages.media_plan_show_page.edit_media_plan_button)
        self.pages.media_plan_show_page.page_should_contain(self.media_plan_name)
        self.pages.media_plan_show_page.click_on_media_plans_and_campaigns_link()
        self.pages.campaign_list_page.wait_till_visible(self.pages.campaign_list_page.campaign_list_table)
        self.pages.campaign_list_page.page_should_contain(self.media_plan_name)

    @test_case()
    def go_to_edit_media_plan(self):
        self.pages.campaign_list_page.filter_campaigns(self.media_plan_name)
        self.pages.campaign_list_page.go_to_link(self.media_plan_name)
        self.pages.media_plan_show_page.wait_till_visible(self.pages.media_plan_show_page.edit_media_plan_button)
        self.pages.media_plan_show_page.click_on_edit_media_plan_button()
        self.pages.edit_media_plan_page.wait_till_visible(self.pages.edit_media_plan_page.submit)
    
    def check_messages(self, key):
        self.pages.edit_media_plan_page.page_should_contain(self.pages.edit_media_plan_page.messages[key])

    @test_case()
    def validate_plan_budget(self):
        self.go_to_edit_media_plan()
        for message in ['strings', 'special_char', 'alphanumeric_value']:
            self.pages.edit_media_plan_page.type_budget(getattr(self.dx_constant, message))
            self.pages.edit_media_plan_page.click_submit()
            self.pages.edit_media_plan_page.wait_till_visible(self.pages.edit_media_plan_page.submit)
            self.check_messages('budget')
        self.pages.edit_media_plan_page.type_budget(self.dx_constant.budget)
        self.pages.edit_media_plan_page.click_submit()
        self.pages.media_plan_show_page.wait_till_visible(self.pages.media_plan_show_page.edit_media_plan_button)
        self.check_messages('update')

    @test_case()
    def validate_activity_value(self):
        self.pages.media_plan_show_page.click_on_edit_media_plan_button()
        self.pages.edit_media_plan_page.wait_till_visible(self.pages.edit_media_plan_page.submit)
        for message in ['strings', 'special_char', 'alphanumeric_value']:
            self.pages.edit_media_plan_page.type_value(self.dx_constant.strings)
            self.pages.edit_media_plan_page.click_submit()
            self.pages.edit_media_plan_page.wait_till_visible(self.pages.edit_media_plan_page.submit)
            self.check_messages('activity_value')
        self.pages.edit_media_plan_page.type_value(self.dx_constant.value)
        self.pages.edit_media_plan_page.click_submit()
        self.pages.media_plan_show_page.wait_till_visible(self.pages.media_plan_show_page.edit_media_plan_button)
        self.check_messages('update')

    @test_case()
    def media_plan_with_currency_euro(self):
        self.go_to_campaign_list_page()
        self.go_to_create_media_plan_page()
        self.pages.create_media_plan_page.click_add_row()
        media_plan_name = 'Media-plan-Euro-' + self.pages.create_media_plan_page.get_random_string(6)
        self.pages.create_media_plan_page.type_name(media_plan_name)
        self.pages.create_media_plan_page.type_start_date(DXDate().todays_date())
        self.pages.create_media_plan_page.type_budget('5000')
        self.pages.create_media_plan_page.type_value('9')
        self.pages.create_media_plan_page.select_currency('Euro (EUR)')
        self.pages.create_media_plan_page.type_end_date(DXDate().date_after_two_days())
        self.pages.create_media_plan_page.click_submit()
        self.pages.media_plan_show_page.wait_till_visible(self.pages.media_plan_show_page.edit_media_plan_button)

    @test_case()
    def verify_media_plan_created(self):
        self.pages.media_plan_show_page.page_should_contain(self.pages.media_plan_show_page.messages['success'])
        self.pages.media_plan_show_page.page_should_contain('Euro (EUR)')
