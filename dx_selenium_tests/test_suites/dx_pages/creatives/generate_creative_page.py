from base.dx import Dx

class GenerateCreativePage(Dx):
    
    def enter_creative_name(self, asset_creative_name):
        self.clear_and_send_value(asset_creative_name, self.creative_name_text_box)

    def click_ok_button(self):
        self.click_element(self.ok_button)
