from selenium.webdriver.common.keys import Keys
from base.dx import Dx
import time

class CreativeList(Dx):

    def select_advertiser(self, advertiser):
        self.click_element(self.advertiser_click)
        for value in [ advertiser, Keys.ENTER ]:
            self.fill_field(self.advertiser_input, value)

    def search_creative(self, creative_name):
        self.send_keys(self.filters, creative_name)
        self.fill_field(self.filters, Keys.ENTER)

    def wait_for_spinner(self):
        self.wait_till_visible(self.creative_tag_spinner)
        self.wait_till_invisible(self.creative_tag_spinner)

    def click_new_creatives(self):
        self.click_element(self.new_creative_button)

    def click_select_all(self):
        self.click_element(self.select_all)

    def click_first_checkbox(self):
        self.click_element(self.first_creative_checkbox)

    def click_first_creative(self):
        self.click_element(self.first_creative_link)

    def click_on_first_creative_gear_icon(self):
        self.click_element(self.first_creative_gear_icon)

    def click_on_first_creative_edit_link(self):
        self.click_element(self.first_creative_edit_link)

    def click_get_rmx_id(self):
        self.click_element(self.get_rmx_id)

    def close_rmx_id_popup(self):
        self.click_element(self.close_rmx_ids_popup)

    def wait_for_creatives_list(self):
        self.wait_till_visible(self.creatives_view, 30)

    def get_first_creative(self):
        creative = str(self.find_element(self.first_creative_link).get_attribute('innerHTML')).replace('<wbr>', '')
        return creative.strip()

    def click_on_new_assets_button(self):
        self.click_element(self.new_assets_button)

    def click_first_asset_checkbox(self):
        self.click_element(self.first_asset_checkbox)

    def click_delete_asset_button(self):
        self.click_element(self.delete_asset_button)

    def click_first_asset_gear_icon(self):
        self.click_element(self.first_asset_gear_icon)

    def click_first_asset_edit_link(self):
        self.click_element(self.first_asset_edit_link)

    def search_asset(self, asset_name):
        for element in [asset_name, Keys.ENTER]:
            self.fill_field(self.asset_filter_textbox, element)
        time.sleep(3)
