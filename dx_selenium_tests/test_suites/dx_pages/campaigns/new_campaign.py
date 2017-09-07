from base.dx import Dx
from selenium.webdriver.common.keys import Keys
from configs.dx_constant import DXConstant
from selenium.webdriver import ActionChains
import time

class NewCampaign(Dx):
    def click_new_campaign_link(self):
        self.click_element(self.new_campaign_link)

    def type_advertiser(self, advertiser):
        self.wait_till_visible(self.advertiser)
        self.generate_and_accept_javascript_alert()
        self.clear_and_send_value(advertiser, self.advertiser)
        self.generate_and_accept_javascript_alert()
        self.fill_field(self.advertiser, Keys.TAB)
        self.wait_till_visible(self.campaign_channel)
        self.wait_till_element_clickable(self.popup_create_campaign_button)

    def submit(self):
        self.submit_form(self.online_campaign_submit)

    def select_campaign_currency(self, value):
        self.wait_till_visible(self.campaign_currency)
        self.select_option(self.campaign_currency, value)

    def select_campaign_channel(self , value):
        self.wait_till_visible(self.campaign_channel)
        self.select_option(self.campaign_channel, value)

    def select_campaign_inventory(self, value):
        self.select_option(self.inventory_type, value)

    def check_channel_visible(self):
        return True if self.find_element(self.campaign_channel).is_displayed() else False

    def close(self):
        self.click_element(self.close_popup)

    def new_campaign_body_click(self):
        self.click_element(self.new_online_campaign_body_link)

    def clear_advertiser(self):
        self.clear(self.advertiser)
