from base.dx import Dx
import time

class NewUser(Dx):

    def enter_user_email_id(self, email_id):
        self.clear_and_send_value(email_id, self.email_text_box)
    
    def select_organization(self, organization, method = 'label'):
        self.select_option(self.organization_dropdown, organization, method)

    def click_on_add_user_role_button(self):
        self.click_element(self.add_user_role_button)
        time.sleep(1)

    def select_organization_to_add_role(self, organization):
        self.select_option(self.get_last_element(self.roles_and_permissions_organization_dropdown), organization)
        time.sleep(2)

    def select_user_role(self, role):
        self.select_option(self.get_last_element(self.roles_and_permissions_role_dropdown), role)

    def click_on_submit_button(self):
        self.click_element(self.submit_button)
