from base.dx import Dx

class CreativeShowPage(Dx):

    def click_on_edit_link(self):
        self.click_element(self.edit_link)

    def click_on_delete_link(self):
        self.click_element(self.delete_link)

    def click_on_creatives_for_advertiser_link(self):
        self.click_element(self.creatives_for_advertiser_link)

    def click_on_all_creatives_link(self):
        self.click_element(self.all_creatives_link)
