from base.dx import Dx
from selenium.webdriver.common.keys import Keys
import time

class AudiencesListPage(Dx):

    def select_orgnization(self, advertiser_name):
        self.click_element(self.organization_dropdown)
        self.send_keys(self.organization_dropdown_input, advertiser_name)
        self.fill_field(self.organization_dropdown_input, Keys.ENTER)

    def click_on_create_new_audience_button(self):
        self.click_element(self.create_new_audience_button)

    def click_first_audience_name_link(self):
        self.click_element(self.first_audience_name)

    def get_first_element_from_list(self, locator, attribute='innerHTML'):
        innerhtml_text = str(self.find_element(getattr(self, locator)).get_attribute(attribute))
        return innerhtml_text.replace('<wbr>', '')

    def get_selected_advertiser_name(self):
        return str(self.find_element(self.selected_advertiser_name).get_attribute('innerHTML'))

    def click_first_edit_icon(self):
        self.click_element(self.first_audience_edit_icon)

    def check_hide_audiences_checkbox(self):
        self.click_element(self.hide_audiences_checkbox)
        time.sleep(4)

    def search_helper(self, search_string, search_what):
        configuration = { 'segment': self.segment_search_text_box, 'audience':self.audience_search_text_box }
        self.clear_and_send_value(search_string, configuration[search_what])
        self.fill_field(configuration[search_what], Keys.ENTER)
        time.sleep(3)

    def search_audience(self, search_string):
        self.search_helper(search_string, 'audience')

    def click_segment_tab(self):
        self.click_element(self.segment_tab)

    def select_option_from_segment_filter_dropdown(self, option):
        self.select_option(self.segment_filter_dropdown, option)
        time.sleep(3)

    def click_on_create_first_party_segment_button(self):
        self.click_element(self.create_first_party_segment_button)

    def click_on_first_segment_name(self):
        self.click_element(self.first_segment_name)

    def click_first_segment_gear_icon(self):
        self.click_element(self.first_segment_gear_icon)

    def click_first_segment_edit_link(self):
        self.click_element(self.first_segment_edit_link)

    def click_first_segment_view_link(self):
        self.click_element(self.first_segment_view_link)

    def search_segment(self, search_string):
        self.search_helper(search_string, 'segment')
