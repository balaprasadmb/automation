from base.dx import Dx
from selenium.webdriver.common.keys import Keys
import time

class ProductFeatureEditPage(Dx):
    def add_user_in_user_selection_box(self, user_id):
        self.click_element(self.user_selection_box)
        self.send_keys(self.user_selection_box, user_id)
        time.sleep(1)
        self.send_keys(self.user_selection_box, Keys.ENTER)

    def click_on_update_product_feature_button(self):
        self.click_element(self.update_product_feature_button)

    def get_selected_users_list(self):
        selected_users_list = []
        selected_users_elements = self.find_elements(self.selected_users)
        for element in selected_users_elements:
            selected_users_list.append(str(element.get_attribute('innerHTML')))
        return selected_users_list
