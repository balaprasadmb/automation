from base.dx import Dx
from selenium.webdriver.common.keys import Keys

class BiReportsPackCreatePage(Dx):

    def click_on_back_to_bi_reports_link(self):
        self.click_element(self.back_to_bi_reports_link)

    def enter_bi_report_pack_name(self, report_pack_name):
        self.clear_and_send_value(report_pack_name, self.bi_report_pack_name_textbox)

    def enter_bi_report_pack_description(self, report_pack_description):
        self.clear_and_send_value(report_pack_description, self.bi_report_pack_description_textbox)

    def click_add_organization_link(self):
        self.click_element(self.add_organization_link)
        self.wait_till_enabled(self.organization_dropdown)

    def select_organization(self, organization_name):
        self.click_element(self.organization_dropdown)
        self.wait_till_enabled(self.organization_dropdown_input)
        self.send_keys(self.organization_dropdown_input, organization_name)
        self.fill_field(self.organization_dropdown_input, Keys.ENTER)

    def click_on_create_pack_button(self):
        self.click_element(self.bi_report_pack_create_button)

    def click_on_cancel_button(self):
        self.click_element(self.bi_report_pack_cancel_button)
