from base.dx import Dx
from selenium.webdriver.common.keys import Keys
import time

class CreativeAssignDashboardPage(Dx):

    def click_on_first_flight_checkbox(self):
        self.click_element(self.first_flight_checkbox)

    def search_creative(self, creative_name):
        self.send_keys(self.creative_filter_box, creative_name)
        self.fill_field(self.creative_filter_box, Keys.ENTER)
        self.wait_till_enabled(self.first_creative_add_button)

    def click_on_blacklist_inherit_slider(self):
        self.click_element(self.blacklist_inherit_slider)
        time.sleep(2)

    def click_on_creatives_available_button(self):
        self.click_element(self.creatives_available_button)
        time.sleep(3)

    def click_on_first_creative_add_button(self):
        self.click_element(self.first_creative_add_button)
        time.sleep(2)

    def close_flash_message_div(self):
        self.click_element(self.message_div_close_button)

    def click_on_domains_available_button(self):
        self.click_element(self.domains_available_button)
        time.sleep(2)

    def click_on_create_domains_list_link(self):
        self.click_element(self.create_domains_list_link)

    def click_on_edit_flight_button(self):
        self.click_element(self.edit_flight_button)

    def click_on_first_blacklist_domainlist_name(self):
        self.click_element(self.blacklist_domain_list_name_row)
