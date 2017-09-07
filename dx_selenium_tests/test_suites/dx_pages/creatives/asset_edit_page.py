from base.dx import Dx

class AssetEditPage(Dx):

    def click_asset_save_button(self):
        self.click_element(self.asset_save_button)
