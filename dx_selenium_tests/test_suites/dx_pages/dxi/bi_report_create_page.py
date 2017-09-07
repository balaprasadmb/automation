from base.dx import Dx
from selenium.webdriver.common.keys import Keys

class BiReportCreatePage(Dx):

    def click_on_back_to_bi_reports_link(self):
        self.click_element(self.back_to_bi_reports_link)

    def enter_bi_report_name(self, bi_report_name):
        self.clear_and_send_value(bi_report_name, self.bi_report_name_textbox)

    def enter_bi_report_path(self, bi_report_path):
        self.clear_and_send_value(bi_report_path, self.bi_report_path_textbox)

    def enter_bi_report_description(self, bi_report_description):
        self.clear_and_send_value(bi_report_description, self.bi_report_description_textbox)

    def click_on_create_button(self):
        self.click_element(self.bi_create_report_button)

    def click_on_cancel_button(self):
        self.click_element(self.bi_report_cancel_button)

    def select_screenshot(self, file_path):
        self.fill_field(self.bi_report_browse_screenshot, file_path)
