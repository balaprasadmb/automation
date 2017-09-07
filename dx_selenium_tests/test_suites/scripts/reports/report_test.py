import time
import csv
import os
from robot.utils import asserts
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from configs.dx_web_driver import DXWebDriver
from page_object import PageObjects

class ReportTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self, user_details):
        self.pages.sso_login_page.open()
        self.fill_login_details(user_details)
        self.pages.sso_login_page.wait_till_invisible(self.pages.sso_login_page.back_to_legacy_login_link)

    def verify_ui_auto_logout(self):
        print 'Started waiting at %s' % time.ctime()
        time.sleep(2100)            #35 Minutes
        print 'Waited till %s' % time.ctime()
        asserts.assert_true(self.pages.sso_login_page.is_element_present(self.pages.sso_login_page.access_button), 'Should be auto logged out after 35 minutes')

    @test_case()
    def fill_login_details(self, user_details):
        self.pages.sso_login_page.wait_till_visible(self.pages.sso_login_page.access_button)
        self.pages.sso_login_page.type_email(user_details[0])
        self.pages.sso_login_page.type_password(user_details[1])
        self.pages.sso_login_page.submit()

    def verify_dashboard_page(self):
        for content in ['Dashboards', 'Reports', 'Manage']:
            self.pages.search_page.page_should_contain(content)

    @test_case()
    def auth_login(self):                                                        #will be removed
        self.pages.search_page.wait_till_visible(self.pages.search_page.reports_link)
        self.pages.search_page.click_reports_link()
        self.driver.driver.switch_to_window(self.driver.driver.window_handles[1])
        assert 'Sign In with Auth0' == self.driver.driver.title
        user_details = self.dx_constant.user_by_role['sso_enabled_campaign_manager']
        self.pages.sso_login_page.wait_till_visible(self.pages.sso_login_page.access_button)
        self.pages.sso_login_page.type_email(user_details['user_name'])
        self.pages.sso_login_page.type_password(user_details['password'].decode('base64', 'strict'))
        self.pages.sso_login_page.submit()
        self.pages.search_page.wait_till_visible(['id', 'pagesContainer'], 90)

    @test_case()
    def verify_search_page_report_link(self):
        self.driver.driver.switch_to_window(self.driver.driver.window_handles[0])
        self.pages.search_page.wait_till_visible(self.pages.search_page.reports_link)
        self.pages.search_page.click_reports_link()
        time.sleep(5)
        self.driver.driver.switch_to_window(self.driver.driver.window_handles[1])
        asserts.assert_not_equal('Sign In with Auth0', self.driver.driver.title, 'Should show the reports')
        self.pages.search_page.wait_till_visible(['id', 'pagesContainer'], 50)
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
        self.driver.driver.switch_to_window(self.driver.driver.window_handles[1])
        asserts.assert_not_equal('Sign In with Auth0', self.driver.driver.title, 'Should show the reports')
        self.pages.search_page.wait_till_visible(['id', 'pagesContainer'], 50)
        self.verify_dashboard_page()

    @test_case()
    def test_reports_links(self):
        first_row = False
        with open(os.getcwd() + '/users.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            for reader in csvreader:
                if first_row:
                    self.login_as_campaign_manager(reader)
                    self.verify_ui_auto_logout()
                    self.driver.driver.refresh()
                    self.login_as_campaign_manager(reader)
                    self.auth_login()                          #will be removed
                    self.verify_search_page_report_link()
                    self.verify_campaigns_reports_link()
                    self.driver.driver.switch_to_window(self.driver.driver.window_handles[0])
                    if  not self.pages.sso_login_page.is_element_present(self.pages.sso_login_page.access_button):
                        self.pages.search_page.go_to_link('Admin')
                        self.pages.search_page.go_to_link('Logout')
                first_row = True
        csvfile.close()
