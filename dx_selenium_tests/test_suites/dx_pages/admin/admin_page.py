from selenium.webdriver.common.by import By
from base.dx import Dx
from configs.dx_constant import DXConstant
import time

class AdminPage(Dx):

    def click_on_dataxu_logo(self):
        self.click_element(self.dataxu_logo)

    def click_on_admin_link(self):
        self.click_element(self.admin_link)

    def click_on_edit_my_account_link(self):
        self.click_element(self.edit_my_account_link)

    def click_on_subscriptions_link(self):
        self.click_element(self.subscriptions_link)

    def click_on_report_inbox_link(self):
        self.click_element(self.report_inbox_link)

    def click_on_create_new_campaign_link(self):
        self.click_element(self.create_new_campaign_link)

    def click_on_inventory_link(self):
        self.click_element(self.inventory_link)

    def click_on_creative_link(self):
        self.click_element(self.creative_link)

    def click_on_segments_link(self):
        self.click_element(self.segments_link)

    def click_on_users_link(self):
        self.click_element(self.users_link)

    def click_on_create_new_user_link(self):
        self.click_element(self.create_new_user_link)

    def click_on_customer_intelligence_dataset_link(self):
        self.click_element(self.customer_intelligence_dataset_link)

    def click_on_product_feature_link(self):
        self.click_element(self.product_feature_link)

    def click_login_screen_slides_link(self):
        self.click_element(self.login_screen_slides_link)

    def click_on_ad_server_tag_versions_link(self):
        self.click_element(self.ad_server_tag_versions_link)

    def close_system_message(self):
        self.click_element(self.system_message_close)
        time.sleep(2)

    def click_display_message_link(self):
        self.click_element(self.display_message_link)
        time.sleep(1)

    def click_dismiss_all_notices_button(self):
        self.click_element(self.dismiss_all_notices_button)
        time.sleep(2)

    def click_on_agency_group_link(self):
        self.click_element(self.agency_group_link)

    def click_on_agencies_link(self):
        self.click_element(self.agencies_link)

    def click_on_advertisers_link(self):
        self.click_element(self.advertiser_link)

    def click_on_business_intelligence_reports_link(self):
        self.click_element(self.business_intelligence_reports_link)
