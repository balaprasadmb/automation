from base.dx import Dx

class SsoLoginPage(Dx):

    def click_on_back_to_legacy_login_link(self):
        self.click_element(self.back_to_legacy_login_link)

    def type_email(self, email):
        self.fill_field(self.email, email)

    def type_password(self, password):
        self.fill_field(self.password, password)

    def submit(self):
        self.click_element(self.access_button)
