from base.dx import Dx

class DomainListManagementPage(Dx):
    def click_on_new_list_button(self):
        self.click_element(self.new_list_button)

    def set_domain_list_name(self, domain_list_name):
        self.clear_and_send_value(domain_list_name, self.domain_list_name_textbox)

    def click_on_save_button(self):
        self.click_element(self.domain_list_name_submit_button)

    def click_on_edit_button(self):
        self.click_element(self.edit_button)

    def enter_domain_name_in_domain_text_area(self, domain_name):
        self.fill_field(self.domains_input_text_area, domain_name)

    def click_on_domain_list_submit_button(self):
        self.click_element(self.domain_list_submit_button)

    def click_on_back_button(self):
        self.click_element(self.back_button)
