from lib.gui_tests import test_case
from dx_test.dx_test import DXTest
from common_helpers.common_helpers import CommonHelper
import time
import os

class BiReportTest(DXTest):

    @test_case()
    def login_as_dx_admin(self):
        self.common_helper = CommonHelper()
        self.setup()

    @test_case()
    def functionality_of_business_intelligence_reports_link(self):
        self.pages.admin_page.click_on_business_intelligence_reports_link()
        self.pages.bi_reports_list_page.wait_till_visible(self.pages.bi_reports_list_page.bi_reports_list_table)
        for content in self.pages.bi_reports_list_page.bi_report_list_page_contents:
            self.pages.bi_reports_list_page.page_should_contain(content)
        for element in self.pages.bi_reports_list_page.bi_report_list_page_elements:
            self.common_helper.assert_is_element_present(self.pages.bi_reports_list_page, getattr(self.pages.bi_reports_list_page, element))

    @test_case()
    def functionality_of_new_bi_report_button(self):
        self.pages.bi_reports_list_page.click_on_new_bi_report_button()
        self.pages.bi_report_create_page.wait_till_visible(self.pages.bi_report_create_page.bi_create_report_button)
        self.pages.bi_report_create_page.page_should_contain(self.pages.bi_report_create_page.bi_report_create_page_title)

    @test_case()
    def assert_for_bi_reports_list_page(self):
        self.pages.bi_reports_list_page.wait_till_visible(self.pages.bi_reports_list_page.bi_reports_list_table)
        assert self.pages.bi_reports_list_page.is_element_present(self.pages.bi_reports_list_page.new_bi_report_button)

    @test_case()
    def functionality_of_back_to_bi_reports_link(self, page_object):
        page_object.click_on_back_to_bi_reports_link()
        self.assert_for_bi_reports_list_page()

    @test_case()
    def functionality_of_cancel_button(self, page_object):
        page_object.click_on_cancel_button()
        self.assert_for_bi_reports_list_page()

    @test_case()
    def functionality_of_back_link_from_bi_report_create_page(self):
        self.functionality_of_back_to_bi_reports_link(self.pages.bi_report_create_page)

    @test_case()
    def functionality_of_cancel_button_from_bi_report_create_page(self):
        self.functionality_of_new_bi_report_button()
        self.functionality_of_cancel_button(self.pages.bi_report_create_page)

    @test_case()
    def set_fields_for_bi_report_create_page_click_create_button(self, bi_report_name, bi_report_path):
        self.pages.bi_report_create_page.enter_bi_report_name(bi_report_name)
        self.pages.bi_report_create_page.enter_bi_report_path(bi_report_path)
        self.pages.bi_report_create_page.enter_bi_report_description(self.pages.bi_report_create_page.get_random_string())
        self.pages.bi_report_create_page.click_on_create_button()

    @test_case()
    def assert_report_or_pack_creation_message(self, sucess_message):
        self.pages.bi_reports_list_page.wait_till_visible(self.pages.bi_reports_list_page.bi_reports_list_table)
        self.pages.bi_reports_list_page.page_should_contain(sucess_message)

    @test_case()
    def creation_of_bi_report_with_blank_path_field(self):
        self.functionality_of_new_bi_report_button()
        self.bi_report_name = self.pages.bi_report_create_page.get_random_string()
        self.set_fields_for_bi_report_create_page_click_create_button(self.bi_report_name, '')
        self.pages.bi_report_create_page.wait_till_visible(self.pages.bi_report_create_page.bi_create_report_button)
        self.pages.bi_report_create_page.page_should_contain(self.pages.bi_report_create_page.blank_report_path_error)

    @test_case()
    def creation_of_bi_report_with_valid_fields(self):
        self.bi_report_path = self.pages.bi_report_create_page.get_random_string(5)
        self.set_fields_for_bi_report_create_page_click_create_button(self.bi_report_name, self.bi_report_path)
        self.assert_report_or_pack_creation_message(self.pages.bi_reports_list_page.report_creation_success_message)

    @test_case()
    def creation_of_bi_report_with_screenshot(self, screenshot_name):
        self.functionality_of_new_bi_report_button()
        bi_report_name = self.pages.bi_report_create_page.get_random_string()
        bi_report_path = self.pages.bi_report_create_page.get_random_string(5)
        self.pages.bi_report_create_page.select_screenshot(os.path.dirname(__file__)+ '/../../../data/bi_report_images/'+screenshot_name)
        self.set_fields_for_bi_report_create_page_click_create_button(bi_report_name, bi_report_path)
        self.assert_report_or_pack_creation_message(self.pages.bi_reports_list_page.report_creation_success_message)

    @test_case()
    def creation_of_bi_report_with_png_image(self):
        self.creation_of_bi_report_with_screenshot('png_bi_report.png')

    @test_case()
    def creation_of_bi_report_with_jpg_image(self):
        self.creation_of_bi_report_with_screenshot('jpg_bi_report.jpg')

    @test_case()
    def creation_of_bi_report_with_duplicate_name(self):
        self.functionality_of_new_bi_report_button()
        bi_report_path = self.pages.bi_report_create_page.get_random_string(5)
        self.set_fields_for_bi_report_create_page_click_create_button(self.bi_report_name, bi_report_path)
        self.pages.bi_report_create_page.wait_till_visible(self.pages.bi_report_create_page.bi_create_report_button)
        self.pages.bi_report_create_page.page_should_contain(self.pages.bi_report_create_page.duplicate_report_name_error)

    @test_case()
    def creation_of_bi_report_with_duplicate_path(self):
        bi_report_name = self.pages.bi_report_create_page.get_random_string()
        self.set_fields_for_bi_report_create_page_click_create_button(bi_report_name, self.bi_report_path)
        self.pages.bi_report_create_page.wait_till_visible(self.pages.bi_report_create_page.bi_create_report_button)
        self.pages.bi_report_create_page.page_should_contain(self.pages.bi_report_create_page.duplicate_report_path_error)
        self.functionality_of_back_link_from_bi_report_create_page()

    @test_case()
    def delete_report_functionality(self):
        innerhtml_text = self.pages.bi_reports_list_page.get_innerhtml_text('first_report_name')
        report_pack_name = innerhtml_text.split('<br>')
        self.pages.bi_reports_list_page.click_on_first_report_delete_button()
        self.pages.bi_reports_list_page.dismiss_alert()
        self.pages.bi_reports_list_page.page_should_contain(report_pack_name[0])
        self.pages.bi_reports_list_page.click_on_first_report_delete_button()
        self.pages.bi_reports_list_page.accept_alert()
        self.pages.bi_reports_list_page.page_should_not_contain(report_pack_name[0])
    
    @test_case()
    def functionality_of_new_bi_report_pack_button(self):
        self.pages.bi_reports_list_page.click_on_new_bi_report_pack_button()
        self.pages.bi_report_pack_create_page.wait_till_visible(self.pages.bi_report_pack_create_page.add_organization_link)
        self.pages.bi_report_pack_create_page.page_should_contain(self.pages.bi_report_pack_create_page.bi_report_pack_create_page_title)

    @test_case()
    def functionality_of_back_link_from_bi_report_pack_create_page(self):
        self.functionality_of_back_to_bi_reports_link(self.pages.bi_report_pack_create_page)

    @test_case()
    def functionality_of_cancel_button_from_bi_report_pack_create_page(self):
        self.functionality_of_new_bi_report_pack_button()
        self.functionality_of_cancel_button(self.pages.bi_report_pack_create_page)

    @test_case()
    def set_required_fields_for_bi_report_pack_create_page_click_create_button(self, report_pack_name, organization_name=None):
        self.functionality_of_new_bi_report_pack_button()
        if organization_name:
            time.sleep(3)
            self.pages.bi_report_pack_create_page.wait_till_element_clickable(self.pages.bi_report_pack_create_page.add_organization_link)
            self.pages.bi_report_pack_create_page.click_add_organization_link()
            self.pages.bi_report_pack_create_page.select_organization(organization_name)
        self.pages.bi_report_pack_create_page.enter_bi_report_pack_name(report_pack_name)
        self.pages.bi_report_pack_create_page.enter_bi_report_pack_description('test description')
        self.pages.bi_report_pack_create_page.click_on_create_pack_button()

    @test_case()
    def creation_of_bi_report_pack_with_no_organization(self):
        self.bi_report_pack_name = self.pages.bi_report_pack_create_page.get_random_string()
        self.set_required_fields_for_bi_report_pack_create_page_click_create_button(self.bi_report_pack_name)
        self.assert_report_or_pack_creation_message(self.pages.bi_reports_list_page.report_Pack_creation_success_message)

    @test_case()
    def creation_of_bi_report_pack_with_organization(self):
        bi_report_pack_name01 = self.pages.bi_report_pack_create_page.get_random_string()
        self.set_required_fields_for_bi_report_pack_create_page_click_create_button(bi_report_pack_name01, self.dx_constant.agency_group_name)
        self.assert_report_or_pack_creation_message(self.pages.bi_reports_list_page.report_Pack_creation_success_message)

    @test_case()
    def creation_of_bi_report_pack_with_duplicate_name(self):
        self.set_required_fields_for_bi_report_pack_create_page_click_create_button(self.bi_report_pack_name)
        self.pages.bi_report_pack_create_page.wait_till_visible(self.pages.bi_report_pack_create_page.bi_report_pack_create_button)
        self.pages.bi_report_create_page.page_should_contain(self.pages.bi_report_pack_create_page.duplicate_report_pack_name_error)
