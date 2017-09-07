from selenium.webdriver.common.by import By
from base.dx import Dx

class CiDatasetsListPage(Dx):

    def click_on_new_dataset_button(self):
        self.click_element(self.new_dataset_button)

    def click_on_gear_icon(self):
        self.click_element(self.first_gear_icon)

    def click_on_edit_link(self):
        self.click_element(self.edit_link)

