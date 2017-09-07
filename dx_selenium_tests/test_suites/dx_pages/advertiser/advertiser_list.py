from base.dx import Dx
from selenium.webdriver.common.keys import Keys
import time

class AdvertiserListPage(Dx):
    def click_on_new_advrtiser_button(self):
        self.click_element(self.new_advertiser)
        
    def type_advertiser_name_in_filterbox(self, advertiser_name):
        self.clear_and_send_value(advertiser_name, self.search_box)    
        
    def click_edit_icon(self, advertiser_name):
        edit_icon_loc = "a[title='Edit'][href*='{0}']".format(self.get_id_from_link(advertiser_name))
        self.click_element(edit_icon_loc)

    def click_delete_icon(self, advertiser_name):
        edit_icon_loc = "a[title='Delete'][href*='{0}']".format(self.get_id_from_link(advertiser_name))
        self.click_element(edit_icon_loc)

    def click_first_edit_icon(self):
        self.click_element(self.edit_icon)

    def click_first_delete_icon(self):
        self.click_element(self.delete_icon)

    def click_first_advertiser(self):
        self.click_element(self.advertiser_name_link)

    def search_advertiser(self, advertiser_name):
        self.clear_and_send_value(advertiser_name, self.search_box)
        self.fill_field(self.search_box, Keys.TAB)
        time.sleep(3)
