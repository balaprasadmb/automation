from base.dx import Dx
import time

class BiReportListPage(Dx):

    def click_on_new_bi_report_button(self):
        self.click_element(self.new_bi_report_button)

    def click_on_new_bi_report_pack_button(self):
        self.click_element(self.new_bi_report_pack_button)
        time.sleep(4)

    def click_on_first_report_delete_button(self):
        self.click_element(self.first_report_delete_button)

    def click_on_report_edit_icon(self):
        self.click_element(self.first_report_edit_icon)

    def get_innerhtml_text(self, locator, attribute = 'innerHTML'):
        return str(self.find_element(getattr(self, locator)).get_attribute(attribute))
