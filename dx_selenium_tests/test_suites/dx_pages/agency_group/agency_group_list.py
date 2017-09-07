from selenium.webdriver.common.by import By
from base.dx import Dx
from selenium.webdriver.common.keys import Keys
import time

class AgencyGroupList(Dx):
    def go_to_new_agency(self):
        self.click_element(self.new_agency_group_link)

    def go_to_agency_group(self, agency_group):
        self.click_element((By.LINK_TEXT, agency_group))

    def click_edit_icon_with_agency_name(self, agency_group):
        self.click_element("a[title='Edit'][href*='{0}']".format(self.get_id_from_link(agency_group)))

    def click_delete_icon_with_agency_name(self, agency_group):
        self.click_element("a[title='Delete'][href*='{0}']".format(self.get_id_from_link(agency_group)))

    def click_first_edit_icon(self):
        self.click_element(self.edit_icon)

    def click_first_delete_icon(self):
        self.click_element(self.delete_icon)

    def search_agency_group(self, agency_group_name):
        self.clear_and_send_value(agency_group_name, self.search_box)
        self.fill_field(self.search_box, Keys.TAB)
        time.sleep(2)

    def click_on_first_agency_group_name_link(self):
        self.click_element(self.agency_group_name_locator)
