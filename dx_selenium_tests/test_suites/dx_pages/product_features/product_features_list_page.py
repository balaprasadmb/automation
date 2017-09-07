from base.dx import Dx
from selenium.webdriver.common.keys import Keys
import time

class ProductFeaturesListPage(Dx):
    def search_product_feature(self, search_string):
        for element in [ search_string, Keys.ENTER ]:
            self.fill_field(self.filter_text_box, element)
        time.sleep(2)

    def click_on_first_edit_link(self):
        self.click_element(self.first_edit_link)
