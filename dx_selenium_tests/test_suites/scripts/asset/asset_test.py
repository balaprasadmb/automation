#coding: utf-8
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from selenium.webdriver.common.keys import Keys
from common_helpers.common_helpers import CommonHelper
from dx_search_file_path import SearchFilePath
import os

class AssetTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.setup(self.dx_constant.user_by_role['campaign_manager'])

    @test_case()
    def go_to_creative_list_page(self):
        self.pages.search_page.click_creative_link()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.asset_list_table)
        self.pages.creative_list_page.click_element(self.pages.creative_list_page.filters)

    @test_case()
    def verify_asset_list_page_contents(self):
        self.go_to_creative_list_page()
        for element in self.pages.creative_list_page.asset_list_page_elements:
            assert self.pages.creative_list_page.is_element_present(getattr(self.pages.creative_list_page, element)), '{0} missing from asset list page'.format(element)

    @test_case()
    def functionality_of_new_assets_button(self):
        self.pages.creative_list_page.click_on_new_assets_button()
        self.pages.upload_assets_page.wait_till_visible(self.pages.upload_assets_page.upload_assets_button)
        self.pages.upload_assets_page.page_should_contain(self.pages.upload_assets_page.upload_asset_page_title)

    @test_case()
    def verify_accepted_asset_file_formats(self):
        for content in self.pages.upload_assets_page.accepted_file_formats_list:
            self.pages.upload_assets_page.page_should_contain(content)

    @test_case()
    def functionality_of_use_creatives_instead_link(self):
        self.pages.upload_assets_page.click_use_creatives_instead_link()
        self.pages.bulk_upload_new_creative.wait_till_visible(self.pages.bulk_upload_new_creative.creative_attributes_section)
        self.pages.bulk_upload_new_creative.page_should_contain(self.pages.bulk_upload_new_creative.creative_bulk_upload_page_title)

    @test_case()
    def verify_accepted_creative_file_formats(self):
        for content in self.pages.bulk_upload_new_creative.accepted_file_formats_list:
            self.pages.bulk_upload_new_creative.page_should_contain(content)

    @test_case()
    def creation_of_assets(self, assets_file_list):
        self.pages.creative_list_page.click_on_new_assets_button()
        self.pages.upload_assets_page.wait_till_visible(self.pages.upload_assets_page.upload_assets_button)
        counter = 1
        for asset_file in assets_file_list:
            asset_file_path = SearchFilePath(asset_file, os.path.abspath(os.path.dirname(__file__) + '/../../../data/')).file_name
            self.pages.upload_assets_page.select_asset_file(asset_file_path)
            if counter < len(assets_file_list):
                self.pages.upload_assets_page.click_more_assets_button()
            counter += 1
        self.pages.upload_assets_page.click_upload_assets_button()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.asset_list_table)
        self.pages.creative_list_page.page_should_contain(self.pages.creative_list_page.asset_success_message)

    @test_case()
    def create_assets_from_jpeg_png_gif_avi_files(self):
        self.go_to_creative_list_page()
        assets_file_list = ['jpeg_asset.jpeg', 'png_asset.png', 'gif_asset.gif', 'avi_asset.avi']
        self.creation_of_assets(assets_file_list)

    @test_case()
    def create_assets_from_webm_f4v_flv_mov_files(self):
        self.go_to_creative_list_page()
        assets_file_list = ['webm_asset.webm', 'f4v_asset.f4v', 'flv_asset.flv', 'mov_asset.mov']
        self.creation_of_assets(assets_file_list)

    @test_case()
    def create_assets_from_mp4_wmv_swf_3gp_files(self):
        self.go_to_creative_list_page()
        assets_file_list = ['mp4_asset.mp4', 'wmv_asset.wmv', 'swf_asset.swf', '3gp_asset.3gp']
        self.creation_of_assets(assets_file_list)
