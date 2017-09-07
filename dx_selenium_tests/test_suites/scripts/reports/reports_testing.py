import time
import csv
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from configs.dx_web_driver import DXWebDriver
from page_object import PageObjects

class ReportTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.pages.sso_login_page.open()
        self.fill_login_details()
        self.pages.sso_login_page.wait_till_invisible(self.pages.sso_login_page.back_to_legacy_login_link)

    def fill_login_details(self, is_sso=True):
        self.pages.sso_login_page.wait_till_visible(self.pages.sso_login_page.access_button)
        user_details = self.dx_constant.user_by_role['sso_enabled_campaign_manager']
        self.pages.sso_login_page.type_email(user_details['user_name'])
        if is_sso:
            self.pages.sso_login_page.type_password(self.dx_constant.password.decode('base64', 'strict'))
        else:
            print user_details['password'].decode('base64', 'strict')
            self.pages.sso_login_page.type_password(user_details['password'].decode('base64', 'strict'))
        self.pages.sso_login_page.submit()

    def verify_dashboard_page(self):
        for content in ['Dashboards', 'Reports', 'Manage']:
            self.pages.search_page.page_should_contain(content)

    @test_case()
    def verify_search_page_report_link(self):
        self.pages.search_page.wait_till_visible(self.pages.search_page.reports_link)
        current_tab = self.driver.driver.current_window_handle
        self.pages.search_page.click_reports_link()
        time.sleep(5)
        self.driver.driver.switch_to_window(self.driver.driver.window_handles[1])
        assert 'Sign In with Auth0' == self.driver.driver.title
        self.fill_login_details(False)
        self.pages.search_page.wait_till_visible(['id', 'pagesContainer'], 35)
        self.verify_dashboard_page()
        self.driver.driver.close()
        self.driver.driver.switch_to_window(self.driver.driver.window_handles[0])
        self.pages.search_page.click_reports_link()
        self.driver.driver.switch_to_window(self.driver.driver.window_handles[1])
        assert 'Sign In with Auth0' != self.driver.driver.title
        self.pages.search_page.wait_till_visible(['id', 'pagesContainer'])
        self.verify_dashboard_page()
        self.driver.driver.close()

    @test_case()
    def verify_campaigns_reports_link(self):
        self.driver.driver.switch_to_window(self.driver.driver.window_handles[0])
        self.pages.search_page.go_to_link('Admin')
        self.pages.search_page.switch_to_view()
        self.pages.search_page.click_campaign_link()
        self.pages.campaign_list_page.wait_till_visible(self.pages.campaign_list_page.campaign_list_table)
        self.pages.campaign_list_page.click_element(self.pages.campaign_list_page.search_box)
        self.pages.campaign_list_page.wait_till_element_clickable(self.pages.campaign_list_page.new_campaign_button)
        self.pages.campaign_list_page.click_campaign_link()
        self.pages.campaign_show_page.wait_till_visible(self.pages.campaign_show_page.tactic_flight_table)
        self.pages.campaign_show_page.reports()
        self.pages.search_page.wait_till_visible(['id', 'pagesContainer'], 50)
        self.verify_dashboard_page()

    def verify_search_page_report_link2(self):
        """Working of search page report link"""
        try:
            self.driver.search.search_page.wait_till_visible(['id', 'drop2'])
            current_tab = self.driver.selenium_driver.current_window_handle
            self.driver.search.search_page.find_element(['id', 'drop2']).click()
            time.sleep(5)
            self.driver.selenium_driver.switch_to_window(self.driver.selenium_driver.window_handles[1])
            asserts.assert_not_equal('Sign In with Auth0', self.driver.selenium_driver.title, 'Should show the reports')
            self.driver.search.search_page.wait_till_visible(['id', 'pagesContainer'], 50)
            self.verify_dashboard_page()
            self.driver.selenium_driver.close()
            print("Verified Search Page Report Link")
        except Exception as e:
            print dir(e)
            print e
            self.driver.selenium_driver.get_screenshot_as_file(os.path.dirname(__file__) + '/../../test-robot-results/search_page_report_link' + time.ctime() + '.png')

    def verify_campaigns_reports_link2(self):
        """Working of campaign report link"""
        try:
            self.driver.selenium_driver.switch_to_window(self.driver.selenium_driver.window_handles[0])
            self.driver.search.search_page.go_to_link('Admin')
            self.driver.search.search_page.switch_to_view()
            self.driver.campaign.go_to_campaign_list_page()
            self.driver.campaign.campaign_list_page.wait_till_visible(self.driver.campaign.campaign_list_page.campaign_media_plan_list_table)
            self.driver.campaign.campaign_list_page.click_first_campaign_name_link()
            self.driver.campaign.campaign_show_page.wait_till_visible(self.driver.campaign.campaign_show_page.tactic_flight_table)
            self.driver.campaign.campaign_show_page.reports()
            self.driver.selenium_driver.switch_to_window(self.driver.selenium_driver.window_handles[1])
            asserts.assert_not_equal('Sign In with Auth0', self.driver.selenium_driver.title, 'Should show the reports for campaigns')
            self.driver.search.search_page.wait_till_visible(['id', 'pagesContainer'], 50)
            self.verify_dashboard_page()
            self.driver.selenium_driver.close()
            print("Verified Campaigns Report Link")
        except Exception as e:
            print e
            self.driver.selenium_driver.get_screenshot_as_file(os.path.dirname(__file__) + '/../../test-robot-results/campaign_report_link' + time.ctime() + '.png')

    @test_case()
    def report_test(self):
        user_list = []
        with open(os.getcwd() + '/users.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            for reader in csvreader:
                user_list.append(reader)
        csvfile.close()
        print user_list
#         for users_details in user_list:
            
