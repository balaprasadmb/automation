from selenium.webdriver.common.keys import Keys
from base.dx import Dx

class ActivityEditPage(Dx):
    
    def enter_activity_name(self, activity_name):
        self.clear_and_send_value(activity_name, self.activity_name)

    def select_helper(self, name, type):
        configuration = {'activity': [self.activity_type_dropdown, self.activity_type_textbox],
                         'tag_server': [self.tag_server_dropdown, self.tag_server_textbox]}
        self.click_element(configuration[type][0])
        self.clear_and_send_value(name, configuration[type][1])
        self.fill_field(configuration[type][1], Keys.TAB)

    def select_activity_type(self, activity_type):
        self.select_helper(activity_type, 'activity')

    def select_tag_server(self, tag_server_name):
        self.select_helper(tag_server_name, 'tag_server')

    def enter_tag_id(self, tag_id):
        self.fill_field(self.tag_id, tag_id)

    def click_secure_checkbox(self):
        self.click_element(self.secure_checkbox)

    def click_rmx_checkbox(self):
        self.click_element(self.rmx_checkbox)

    def click_create_activity_button(self):
        self.click_element(self.create_activity_button)
        
    def click_cancel_button(self):
        self.click_element(self.cancel_button)

    def check_enable_sharing_checkbox(self):
        self.click_element(self.enable_sharing_checkbox)

    def click_activities_link(self):
        self.click_element(self.activities_link)

    def get_activity_name(self):
        return str(self.find_element(self.activity_name).get_attribute('value'))
