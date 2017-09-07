from base.dx import Dx

class ActivityShowPage(Dx):
    def click_activities_link(self):
        self.click_element(self.activities_link)

    def click_edit_link(self):
        self.click_element(self.edit_link)

    def get_activity_name(self):
        return str(self.find_element(self.activity_name_title).get_attribute('innerHTML')).strip('.')
    
    def get_pixel_tag_value(self):
        return str(self.find_element(self.pixel_tag).get_attribute('innerHTML'))
