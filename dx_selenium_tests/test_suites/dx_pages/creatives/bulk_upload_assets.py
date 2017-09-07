from base.dx import Dx
import time

class BulkUploadAssets(Dx):

    def select_asset_file(self, file_path):
        element = self.get_last_element(self.browse_asset_file_button)
        self.upload_file(file_path, element)

    def click_more_assets_button(self):
        self.click_element(self.more_assets_button)
        time.sleep(1)

    def click_upload_assets_button(self):
        self.click_element(self.upload_assets_button)

    def click_generate_creatives_checkbox(self):
        self.click_element(self.generate_creatives_checkbox)
    
    def click_use_creatives_instead_link(self):
        self.click_element(self.use_creatives_instead_link)
