from selenium.webdriver.common.by import By
from base.dx import Dx

class CreateNewDatasetPage(Dx):

    def select_organization(self, organization_name):
        self.select_option(self.organization_dropdown, organization_name)

    def enter_dataset_name(self, dataset_name):
        self.clear_and_send_value(dataset_name, self.dataset_name_textbox)

    def click_on_create_dataset_button(self):
        self.click_element(self.create_dataset_button)
