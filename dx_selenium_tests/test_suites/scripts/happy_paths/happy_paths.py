from dx_test.dx_test import DXTest
from gui_tests import test_case
from campaign_test_helpers.campaign_test_helper import CampaignTestHelper
from common_helpers.common_helpers import CommonHelper
from lib.dx_date import DXDate
from selenium.webdriver.common.keys import Keys
from dx_search_file_path import SearchFilePath
import os
import time

class HappyPaths(DXTest):

    @test_case()
    def login_as_admin(self):
        self.dx_date = DXDate()
        self.common_helper = CommonHelper()
        self.campaign_helper = CampaignTestHelper()
        self.setup()

    def go_to_admin_page(self):
        self.pages.admin_page.open()
        self.pages.admin_page.wait_till_visible(self.pages.admin_page.system_message_table)
        self.pages.admin_page.page_should_contain(self.pages.admin_page.admin_page_title)

    @test_case()
    def functionality_of_edit_my_account_link(self):
        self.pages.admin_page.click_on_edit_my_account_link()
        self.pages.user_edit_page.wait_till_visible(self.pages.user_edit_page.submit_button)
        self.pages.user_edit_page.page_should_contain(self.pages.user_edit_page.user_edit_page_title)

    @test_case()
    def functionality_subscription_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_subscriptions_link()
        self.pages.admin_page.page_should_contain('Subscriptions')
        for page_content in self.pages.admin_page.subscriptions_table_header:
            self.pages.admin_page.page_should_contain(page_content)

    @test_case()
    def functionality_of_report_inbox_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_report_inbox_link()
        for page_content in ['Report Inbox (last 30 days)', 'Custom Query Results:', 'Subscription Results:']:
            self.pages.admin_page.page_should_contain(page_content)

    @test_case()
    def functionality_of_create_new_campaign_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_create_new_campaign_link()
        self.pages.admin_page.page_should_contain('Before creating a new Campaign, please pick an advertiser.')

    @test_case()
    def functionality_of_inventory_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_inventory_link()
        self.verify_guaranteed_inventory_list_page_contents()

    @test_case()
    def verify_creative_list_page_contents(self):
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.asset_list_table)
        for page_content in self.pages.creative_list_page.sections_title:
            self.pages.creative_list_page.page_should_contain(page_content)
        assert self.pages.creative_list_page.is_element_present(self.pages.creative_list_page.new_creative_button)

    @test_case()
    def functionality_of_creatives_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_creative_link()
        self.verify_creative_list_page_contents()

    @test_case()
    def functionality_of_segments_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_segments_link()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        for content in self.pages.audience_segment_list_page.audience_list_page_contents:
            self.pages.audience_segment_list_page.page_should_contain(content)
        for element in self.pages.audience_segment_list_page.audience_list_page_elements:
            assert self.pages.audience_segment_list_page.is_element_present(getattr(self.pages.audience_segment_list_page, element))

    @test_case()
    def functionality_of_users_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_users_link()
        self.pages.user_list_page.wait_till_visible(self.pages.user_list_page.list_pagination_setup)
        assert self.pages.user_list_page.is_element_present(self.pages.user_list_page.new_user_button)

    @test_case()
    def functionality_of_create_new_user_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_create_new_user_link()
        self.pages.new_user_page.wait_till_visible(self.pages.new_user_page.submit_button)
        for page_content in self.pages.new_user_page.sections_title:
            self.pages.new_user_page.page_should_contain(page_content)
        assert self.pages.new_user_page.is_element_present(self.pages.new_user_page.submit_button)

    @test_case()
    def creation_of_new_user(self):
        self.pages.new_user_page.enter_user_email_id(self.pages.new_user_page.get_random_string(5)+'@test.com')
        self.pages.new_user_page.select_organization(self.dx_constant.agency_group_name)
        self.pages.new_user_page.click_on_add_user_role_button()
        self.pages.new_user_page.select_organization_to_add_role(self.dx_constant.agency_group_name)
        self.pages.new_user_page.select_user_role('Campaign Manager')
        self.pages.new_user_page.click_on_submit_button()
        self.pages.user_show_page.wait_till_visible(self.pages.user_show_page.edit_link)
        self.pages.user_show_page.page_should_contain(self.pages.user_show_page.user_creation_success_message)

    @test_case()
    def functionality_of_business_intelligence_reports_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_business_intelligence_reports_link()
        self.pages.bi_reports_list_page.wait_till_visible(self.pages.bi_reports_list_page.bi_reports_list_table)

    @test_case()
    def creation_of_bi_report(self):
        self.pages.bi_reports_list_page.click_on_new_bi_report_button()
        self.pages.bi_report_create_page.wait_till_visible(self.pages.bi_report_create_page.bi_create_report_button)
        self.pages.bi_report_create_page.enter_bi_report_name(self.pages.bi_report_create_page.get_random_string())
        self.pages.bi_report_create_page.enter_bi_report_path(self.pages.bi_report_create_page.get_random_string(5))
        self.pages.bi_report_create_page.enter_bi_report_description(self.pages.bi_report_create_page.get_random_string())
        self.pages.bi_report_create_page.click_on_create_button()
        self.pages.bi_reports_list_page.page_should_contain(self.pages.bi_reports_list_page.report_creation_success_message)

    @test_case()
    def creation_of_bi_report_pack(self):
        self.pages.bi_reports_list_page.click_on_new_bi_report_pack_button()
        self.pages.bi_report_pack_create_page.wait_till_visible(self.pages.bi_report_pack_create_page.add_organization_link)
        self.pages.bi_report_pack_create_page.enter_bi_report_pack_name(self.pages.bi_report_pack_create_page.get_random_string())
        self.pages.bi_report_pack_create_page.enter_bi_report_pack_description('test description')
        self.pages.bi_report_pack_create_page.click_on_create_pack_button()
        self.pages.bi_reports_list_page.page_should_contain(self.pages.bi_reports_list_page.report_Pack_creation_success_message)

    @test_case()
    def functionality_of_edit_icon_for_bi_reports(self):
        self.pages.bi_reports_list_page.click_on_report_edit_icon()
        self.pages.bi_report_pack_create_page.wait_till_visible(self.pages.bi_report_pack_create_page.add_organization_link)
        self.pages.bi_report_pack_create_page.page_should_contain(self.pages.bi_report_pack_create_page.bi_report_pack_edit_page_title)

    @test_case()
    def functionality_of_customer_intelligence_dataset_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_customer_intelligence_dataset_link()
        self.pages.ci_datasets_list_page.wait_till_visible(self.pages.ci_datasets_list_page.ci_datasets_list_table)
        self.pages.ci_datasets_list_page.page_should_contain(self.pages.ci_datasets_list_page.ci_list_page_title)

    @test_case()
    def creation_of_ci_new_dataset(self):
        self.pages.ci_datasets_list_page.click_on_new_dataset_button()
        self.pages.create_new_dataset_page.wait_till_visible(self.pages.create_new_dataset_page.create_dataset_button)
        self.pages.create_new_dataset_page.select_organization(self.dx_constant.agency_group_name+' >> '+self.dx_constant.advertiser_name)
        self.pages.create_new_dataset_page.enter_dataset_name(self.pages.create_new_dataset_page.get_random_string())
        self.pages.create_new_dataset_page.click_on_create_dataset_button()
        self.pages.ci_datasets_list_page.wait_till_visible(self.pages.ci_datasets_list_page.ci_datasets_list_table)
        self.pages.ci_datasets_list_page.page_should_contain(self.pages.ci_datasets_list_page.ci_creation_success_message)

    @test_case()
    def functionality_of_edit_link_for_ci_dataset(self):
        self.pages.ci_datasets_list_page.click_on_gear_icon()
        self.pages.ci_datasets_list_page.click_on_edit_link()
        self.pages.create_new_dataset_page.wait_till_visible(self.pages.create_new_dataset_page.create_dataset_button)
        self.pages.create_new_dataset_page.page_should_contain(self.pages.create_new_dataset_page.ci_edit_page_title)

    @test_case()
    def functionality_of_product_feature_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_product_feature_link()
        self.pages.admin_page.page_should_contain('Manage Access to Product Features')

    @test_case()
    def functionality_of_login_screen_slides_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_login_screen_slides_link()
        self.pages.login_slides_list_page.wait_till_visible(self.pages.login_slides_list_page.new_login_slides_btn)
        self.pages.login_slides_list_page.page_should_contain(self.pages.login_slides_list_page.list_page_title)

    @test_case()
    def creation_of_login_screen_slide(self):
        self.pages.login_slides_list_page.click_new_login_slides_btn()
        self.pages.login_slides_edit_page.wait_till_visible(self.pages.login_slides_edit_page.create_login_slide_btn)
        self.pages.login_slides_edit_page.enter_login_slide_name(self.pages.login_slides_edit_page.get_random_string())
        self.pages.login_slides_edit_page.enter_login_slide_body(self.pages.login_slides_edit_page.get_random_string())
        self.pages.login_slides_edit_page.click_create_login_slide_btn()
        self.pages.login_slides_show_page.wait_till_visible(self.pages.login_slides_show_page.edit_link)
        self.pages.login_slides_show_page.page_should_contain(self.pages.login_slides_show_page.slide_creation_success_message)

    @test_case()
    def functionality_of_login_slides_edit_link(self):
        self.pages.login_slides_show_page.click_edit_link()
        self.pages.login_slides_edit_page.wait_till_visible(self.pages.login_slides_edit_page.create_login_slide_btn)
        self.pages.login_slides_edit_page.page_should_contain(self.pages.login_slides_edit_page.login_slide_edit_page_title)

    @test_case()
    def creation_of_new_system_message(self):
        self.go_to_admin_page()
        self.pages.system_notices_list_page.click_on_new_system_message()
        self.pages.new_system_message_page.wait_till_visible(self.pages.new_system_message_page.save_message)
        self.pages.new_system_message_page.click_on_save_message_button()
        self.pages.system_notices_list_page.page_should_contain(self.pages.system_notices_list_page.new_creation_success_message)

    @test_case()
    def functionality_of_edit_link_for_system_message(self):
        self.pages.system_notices_list_page.click_on_gear_icon()
        self.pages.system_notices_list_page.click_on_edit_link()
        self.pages.edit_system_notices_page.wait_till_visible(self.pages.edit_system_notices_page.save_message_button)
        self.pages.edit_system_notices_page.page_should_contain(self.pages.edit_system_notices_page.system_message_edit_page_title)

    @test_case()
    def functionality_of_delete_link_for_system_message(self):
        self.go_to_admin_page()
        self.pages.system_notices_list_page.click_on_gear_icon()
        self.pages.system_notices_list_page.click_on_delete_link()
        self.pages.system_notices_list_page.accept_alert()
        self.pages.admin_page.wait_till_visible(self.pages.admin_page.system_message_table)
        self.pages.system_notices_list_page.page_should_contain(self.pages.system_notices_list_page.delete_message)

    @test_case()
    def functionality_of_preview_link_for_system_message(self):
        self.pages.system_notices_list_page.click_on_gear_icon()
        self.pages.system_notices_list_page.click_on_preview_link()
        self.pages.system_notices_list_page.is_element_present(self.pages.system_notices_list_page.preview_popup_content)
        self.pages.system_notices_list_page.close_preview_popup()

    @test_case()
    def functionality_of_clone_link_for_system_message(self):
        self.pages.system_notices_list_page.click_on_clone_link()
        self.pages.new_system_message_page.wait_till_visible(self.pages.edit_system_notices_page.save_message_button)
        self.pages.new_system_message_page.page_should_contain(self.pages.new_system_message_page.create_system_message_page_title)

    @test_case()
    def assert_agency_group_list_page(self):
        self.pages.agency_group_list_page.wait_till_visible(self.pages.agency_group_list_page.agency_group_list_table)
        self.pages.agency_group_list_page.page_should_contain(self.pages.agency_group_list_page.agency_group_list_page_title)
        assert self.pages.agency_group_list_page.is_element_present(self.pages.agency_group_list_page.new_agency_group_link)

    @test_case()
    def functionality_of_agency_groups_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_agency_group_link()
        self.assert_agency_group_list_page()

    @test_case()
    def functionality_of_new_agency_group_button(self):
        self.pages.agency_group_list_page.go_to_new_agency()
        self.pages.new_agency_group_page.wait_till_element_clickable(self.pages.new_agency_group_page.submit_button)
        self.pages.new_agency_group_page.page_should_contain(self.pages.new_agency_group_page.create_agency_group_page_title)

    @test_case()
    def creation_of_agency_group(self):
        self.agency_group_name = "Smoke_agency_group_" + self.pages.new_agency_group_page.get_random_string(10)
        self.pages.new_agency_group_page.type_organization_name(self.agency_group_name)
        self.pages.new_agency_group_page.type_email("smoke_test@dataxu.com")
        self.pages.new_agency_group_page.type_contact_name("DataXu")
        self.pages.new_agency_group_page.check_select_all_currencies()
        self.pages.new_agency_group_page.upload_rate_card(os.getcwd() + '/data/rate_cards/rate_card_USD.xls')
        for media in self.dx_constant.media_type:
            self.pages.new_agency_group_page.click_media_type_checkbox(media)
        self.pages.new_agency_group_page.select_all_inventory()
        if self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.dx_technical_exchange):
            self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.dx_technical_exchange).click()
        for insight in self.pages.new_agency_group_page.insight_list:
            self.pages.new_agency_group_page.select_insights(insight)
        self.pages.new_agency_group_page.click_targeting_checkbox()
        self.pages.new_agency_group_page.click_cost_model_type('CPA')
        self.pages.new_agency_group_page.click_create_agency_group_button()
        self.pages.agency_group_details_page.wait_till_visible(self.pages.agency_group_details_page.edit_details)
        self.pages.agency_group_details_page.page_should_contain(self.pages.agency_group_details_page.agency_group_creation_message.format(self.agency_group_name))

    @test_case()
    def functionality_of_agency_group_list_link_from_show_page(self):
        self.pages.agency_group_details_page.go_to_list_page()
        self.assert_agency_group_list_page()

    @test_case()
    def agency_group_edit_icon_functionality(self):
        self.pages.agency_group_list_page.search_agency_group(self.agency_group_name)
        self.pages.agency_group_list_page.click_first_edit_icon()
        self.pages.agency_group_edit_page.wait_till_element_clickable(self.pages.agency_group_edit_page.save_agency)
        self.pages.agency_group_edit_page.page_should_contain(self.pages.agency_group_edit_page.agency_group_edit_page_title)

    @test_case()
    def functionality_of_cancel_button_from_agency_group_page(self):
        self.pages.agency_group_edit_page.click_on_cancel_button()
        self.assert_agency_group_list_page()

    @test_case()
    def functionality_of_agency_group_name_link(self):
        self.pages.agency_group_list_page.search_agency_group(self.agency_group_name)
        self.pages.agency_group_list_page.click_on_first_agency_group_name_link()
        self.pages.agency_group_details_page.wait_till_visible(self.pages.agency_group_details_page.edit_details)
        self.pages.agency_group_details_page.page_should_contain(self.pages.agency_group_details_page.agency_group_show_page_title.format(self.agency_group_name))

    @test_case()
    def assert_agency_list_page(self):
        self.pages.agency_list_page.wait_till_visible(self.pages.agency_list_page.agencies_list_table)
        self.pages.agency_list_page.page_should_contain(self.pages.agency_list_page.agencies_list_page_title)
        assert self.pages.agency_list_page.is_element_present(self.pages.agency_list_page.new_agency_button)

    @test_case()
    def functionality_of_agencies_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_agencies_link()
        self.assert_agency_list_page()

    @test_case()
    def functionality_of_new_agency_button(self):
        self.pages.agency_list_page.click_on_new_agency_button()
        self.pages.new_agency_page.wait_till_visible(self.pages.new_agency_page.agency_group_dropdown)
        self.pages.new_agency_page.select_agency_group(self.agency_group_name)
        self.pages.new_agency_page.wait_till_element_clickable(self.pages.new_agency_page.submit_button)
        self.pages.new_agency_page.page_should_contain(self.pages.new_agency_page.create_agency_page_title)

    @test_case()
    def creation_of_new_agency(self):
        self.agency_name = 'Smoke_Agency_'+self.pages.new_agency_page.get_random_string()
        self.pages.new_agency_page.type_organization_name(self.agency_name)
        self.pages.new_agency_page.click_create_agency_button()
        self.pages.agency_details_page.wait_till_visible(self.pages.agency_details_page.edit_details_button)
        self.pages.agency_details_page.page_should_contain(self.pages.agency_details_page.success_message['organization_name']['create_new_agency'].format(self.agency_name))

    @test_case()
    def functionality_of_agency_list_link_from_show_page(self):
        self.pages.agency_details_page.go_to_agency_list_page()
        self.assert_agency_list_page()

    @test_case()
    def agency_edit_icon_functionality(self):
        self.pages.agency_list_page.search_agency(self.agency_name)
        self.pages.agency_list_page.click_first_edit_icon()
        self.pages.agency_edit_page.wait_till_element_clickable(self.pages.agency_edit_page.submit_button)
        self.pages.agency_edit_page.page_should_contain(self.pages.agency_edit_page.agency_edit_page_title)

    @test_case()
    def functionality_of_cancel_button_from_agency_edit_page(self):
        self.pages.agency_edit_page.click_on_cancel_button()
        self.assert_agency_list_page()

    @test_case()
    def functionality_of_agency_name_link(self):
        self.pages.agency_list_page.click_first_agency()
        self.pages.agency_details_page.wait_till_visible(self.pages.agency_details_page.edit_details_button)
        self.pages.agency_details_page.page_should_contain(self.pages.agency_details_page.agency_show_page_title.format(self.agency_name))

    @test_case()
    def assert_advertiser_list_page(self):
        self.pages.advertiser_list_page.wait_till_visible(self.pages.advertiser_list_page.advertiser_list)
        self.pages.advertiser_list_page.page_should_contain(self.pages.advertiser_list_page.advertiser_list_page_title)
        assert self.pages.advertiser_list_page.is_element_present(self.pages.advertiser_list_page.new_advertiser)

    @test_case()
    def functionality_of_advertisers_link(self):
        self.go_to_admin_page()
        self.pages.admin_page.click_on_advertisers_link()
        self.assert_advertiser_list_page()

    @test_case()
    def functionality_of_new_advertiser_button(self):
        self.pages.advertiser_list_page.click_on_new_advrtiser_button()
        self.pages.new_advertiser_page.wait_till_element_clickable(self.pages.new_advertiser_page.submit_button)
        self.pages.new_advertiser_page.page_should_contain(self.pages.new_advertiser_page.create_advertiser_page_title)

    @test_case()
    def creation_of_new_advertiser(self):
        self.pages.new_advertiser_page.select_agency_group(self.agency_group_name)
        self.pages.new_advertiser_page.wait_till_enabled(self.pages.new_advertiser_page.agency)
        self.pages.new_advertiser_page.select_agency(self.agency_name)
        self.advertiser_name = 'Smoke_test_advertiser'+self.pages.new_advertiser_page.get_random_string(10)
        self.pages.new_advertiser_page.type_organization_name(self.advertiser_name)
        self.pages.new_advertiser_page.type_advertiser_domain('www.smoke.com')
        self.pages.new_advertiser_page.check_select_all_currencies()
        self.pages.new_advertiser_page.click_create_advetiser_button()
        self.assert_advertiser_list_page()
        self.pages.advertiser_list_page.page_should_contain(self.pages.advertiser_list_page.success_message.format(self.advertiser_name))

    @test_case()
    def advertiser_edit_icon_functionality(self):
        self.pages.advertiser_list_page.search_advertiser(self.advertiser_name)
        self.pages.advertiser_list_page.click_first_edit_icon()
        self.pages.advertiser_edit_page.wait_till_visible(self.pages.advertiser_edit_page.save_advertiser_button, 40)
        self.pages.advertiser_edit_page.page_should_contain(self.pages.advertiser_edit_page.advertiser_edit_page_title)

    @test_case()
    def functionality_of_cancel_button_from_advertiser_edit_page(self):
        self.pages.advertiser_edit_page.click_on_cancel_button()
        self.assert_advertiser_list_page()

    @test_case()
    def functionality_of_advertiser_name_link(self):
        self.pages.advertiser_list_page.search_advertiser(self.advertiser_name)
        self.pages.advertiser_list_page.click_first_advertiser()
        self.pages.advertiser_details_page.wait_till_visible(self.pages.advertiser_details_page.edit_details_button)
        self.pages.advertiser_details_page.page_should_contain(self.pages.advertiser_details_page.advertiser_show_page_title.format(self.advertiser_name))

    @test_case()
    def functionality_of_advertiser_list_link_from_advertiser_show_page(self):
        self.pages.advertiser_details_page.go_to_advertiser_list_page()
        self.assert_advertiser_list_page()

    @test_case()
    def functionality_of_advertiser_delete_icon(self):
        self.pages.advertiser_list_page.search_advertiser(self.advertiser_name)
        self.pages.advertiser_list_page.click_first_delete_icon()
        self.pages.advertiser_list_page.accept_alert()
        self.assert_advertiser_list_page()
        self.pages.advertiser_list_page.page_should_contain(self.pages.advertiser_list_page.delete_message.format(self.advertiser_name))

    @test_case()
    def functionality_of_agency_delete_icon(self):
        self.pages.agency_list_page.open()
        self.assert_agency_list_page()
        self.pages.agency_list_page.search_agency(self.agency_name)
        self.pages.agency_list_page.click_first_delete_icon()
        self.pages.agency_list_page.accept_alert()
        self.assert_agency_list_page()
        self.pages.agency_list_page.page_should_contain(self.pages.agency_list_page.delete_success_message.format(self.agency_name))
 
    @test_case()
    def functionality_of_agency_group_delete_icon(self):
        self.pages.agency_group_list_page.open()
        self.assert_agency_group_list_page()
        self.pages.agency_group_list_page.search_agency_group(self.agency_group_name)
        self.pages.agency_group_list_page.click_first_delete_icon()
        self.pages.agency_list_page.accept_alert()
        self.assert_agency_group_list_page()
        self.pages.agency_group_list_page.page_should_contain(self.pages.agency_group_list_page.success_message.format(self.agency_group_name))

    @test_case()
    def login_as_campaign_manager(self):
        self.common_helper.logout_and_login_by_new_user(self.pages.login_page.driver, 'campaign_manager')
        self.pages.admin_page.page_should_contain('dx_campaign@dataxu.com')

    @test_case()
    def verify_guaranteed_inventory_list_page_contents(self):
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.guaranteed_inventory_list_table)
        for page_contents in self.pages.inventory_list_page.guaranteed_inventory_list_page_contents:
            self.pages.inventory_list_page.page_should_contain(page_contents)
        for elements in self.pages.inventory_list_page.guaranteed_inventory_list_page_elements:
            assert self.pages.inventory_list_page.is_element_present(getattr(self.pages.inventory_list_page, elements))

    @test_case()
    def go_to_inventory_list_page_and_verify_contents(self):
        self.pages.search_page.click_inventory_link()
        self.verify_guaranteed_inventory_list_page_contents()

    @test_case()
    def assert_guaranteed_inventory_create_or_edit_page_title(self, page_title):
        self.pages.guaranteed_inventory_edit_page.wait_till_visible(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_save_button)
        self.pages.guaranteed_inventory_edit_page.page_should_contain(getattr(self.pages.guaranteed_inventory_edit_page, page_title))

    @test_case()
    def functionality_of_new_guaranteed_media_button(self):
        self.pages.inventory_list_page.click_on_new_guaranteed_media_button()
        self.assert_guaranteed_inventory_create_or_edit_page_title('guaranteed_inventory_create_page_title')

    @test_case()
    def creation_of_new_guaranteed_media_inventory(self, media_type = 'Online'):
        inventory_name = 'Smoke-GM-inventory-' + self.pages.guaranteed_inventory_edit_page.get_random_string()
        functions_dict = {'enter_guaranteed_inventory_publisher_name': inventory_name, 'enter_guaranteed_inventory_placement_name': inventory_name,
                          'click_on_guaranteed_inventory_available_checkbox': '', 'click_on_guaranteed_inventory_secure_checkbox': '',
                          'select_guaranteed_inventory_media_type': media_type}
        for key, value in functions_dict.iteritems():
            if value:
                getattr(self.pages.guaranteed_inventory_edit_page, key)(value)
            else:
                getattr(self.pages.guaranteed_inventory_edit_page, key)()
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_save_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.guaranteed_inventory_list_table)
        self.pages.inventory_list_page.page_should_contain(self.pages.inventory_list_page.guaranteed_inventory_success_message.format(inventory_name))

    @test_case()
    def functionality_of_guaranteed_inventory_edit_link(self):
        self.pages.inventory_list_page.click_on_guaranteed_inventory_gear_icon()
        self.pages.inventory_list_page.click_on_guaranteed_inventory_edit_link()
        self.assert_guaranteed_inventory_create_or_edit_page_title('guaranteed_inventory_edit_page_title')

    @test_case()
    def functionality_of_cancel_button_from_gm_edit_page(self):
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_cancel_button()
        self.verify_guaranteed_inventory_list_page_contents()

    @test_case()
    def guaranteed_inventory_functionality_of_placement_name_link_helper(self):
        self.pages.guaranteed_inventory_show_page.wait_till_visible(['id', 'details'])
        for page_contents in self.pages.guaranteed_inventory_show_page.guaranteed_inventory_show_page_contents:
            self.pages.guaranteed_inventory_show_page.page_should_contain(page_contents)
        self.pages.guaranteed_inventory_show_page.page_should_not_contain("Price")
        for elements in self.pages.guaranteed_inventory_show_page.guaranteed_inventory_show_page_elements:
            assert self.pages.guaranteed_inventory_show_page.is_element_present(getattr(self.pages.guaranteed_inventory_show_page, elements))

    @test_case()
    def functionality_of_gm_inventory_publisher_or_placement_name_link(self):
        self.pages.inventory_list_page.click_on_guaranteed_inventory_publisher_name_link()
        self.guaranteed_inventory_functionality_of_placement_name_link_helper()
        self.go_to_inventory_list_page_and_verify_contents()
        self.pages.inventory_list_page.click_on_guaranteed_inventory_placement_name_link()
        self.guaranteed_inventory_functionality_of_placement_name_link_helper()

    @test_case()
    def verify_deals_list_page_contents(self):
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.deal_inventory_list_table)
        for page_contents in self.pages.inventory_list_page.deals_inventory_list_page_contents:
            self.pages.inventory_list_page.page_should_contain(page_contents)
        for elements in self.pages.inventory_list_page.deals_inventory_list_page_elements:
            assert self.pages.inventory_list_page.is_element_present(getattr(self.pages.inventory_list_page, elements))

    @test_case()
    def go_to_deals_page_and_verify_contents(self):
        self.go_to_inventory_list_page_and_verify_contents()
        self.pages.inventory_list_page.click_on_deals_tab()
        self.verify_deals_list_page_contents()

    @test_case()
    def assert_deal_create_or_edit_page_title(self, page_title):
        self.pages.deal_inventory_edit_page.wait_till_visible(self.pages.deal_inventory_edit_page.save_deal_button)
        self.pages.deal_inventory_edit_page.page_should_contain(getattr(self.pages.deal_inventory_edit_page, page_title))

    @test_case()
    def functionality_of_new_deal_button(self):
        self.pages.inventory_list_page.click_on_new_deal_button()
        self.assert_deal_create_or_edit_page_title('deal_create_page_title')

    @test_case()
    def creation_of_deal(self):
        deal_name = 'Smoke-deal-'+self.pages.deal_inventory_edit_page.get_random_string(5)
        self.pages.deal_inventory_edit_page.enter_deal_name(deal_name)
        self.pages.deal_inventory_edit_page.select_deal_inventory_exchange('Admeta')
        self.pages.deal_inventory_edit_page.enter_deal_id(self.pages.deal_inventory_edit_page.get_random_string())
        self.pages.deal_inventory_edit_page.select_deal_type(1)
        self.pages.deal_inventory_edit_page.enter_cost_cpm_value(self.dx_constant.deal_cpm)
        self.pages.deal_inventory_edit_page.enter_start_date(self.dx_date.todays_date())
        self.pages.deal_inventory_edit_page.enter_end_date(self.dx_date.last_date_of_current_month())
        self.pages.deal_inventory_edit_page.enter_deal_description(self.dx_constant.deal_description)
        self.pages.deal_inventory_edit_page.enter_deal_permissioned_advertiser_name(self.dx_constant.advertiser_name)
        self.pages.deal_inventory_edit_page.fill_field(self.pages.deal_inventory_edit_page.deal_permissioned_advertiser_name, Keys.ENTER)
        self.pages.deal_inventory_edit_page.click_on_save_deal_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.deal_inventory_list_table)
        self.pages.inventory_list_page.page_should_contain(self.pages.inventory_list_page.deal_success_message.format(deal_name))

    @test_case()
    def functionality_of_deal_edit_link(self):
        self.pages.inventory_list_page.click_on_deal_inventory_gear_icon()
        self.pages.inventory_list_page.click_on_deal_inventory_edit_link()
        self.assert_deal_create_or_edit_page_title('deal_edit_page_title')

    @test_case()
    def functionality_of_cancel_button_from_deal_edit_page(self):
        self.pages.deal_inventory_edit_page.click_on_deal_cancel_button()
        self.verify_deals_list_page_contents()

    @test_case()
    def functionality_of_deal_name_link(self):
        self.pages.inventory_list_page.click_on_deal_name()
        self.pages.deal_inventory_show_page.wait_till_visible(self.pages.deal_inventory_show_page.edit_deal_button)
        for page_content in self.pages.deal_inventory_show_page.deal_show_page_contents:
            self.pages.deal_inventory_show_page.page_should_contain(page_content)

    @test_case()
    def verify_custom_inventory_list_page_contents(self):
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.custom_inventory_table)
        for page_contents in self.pages.inventory_list_page.custom_inventory_list_page_contents:
            self.pages.inventory_list_page.page_should_contain(page_contents)
        for element in self.pages.inventory_list_page.custom_inventory_list_page_elements:
            assert self.pages.inventory_list_page.is_element_present(getattr(self.pages.inventory_list_page, element))

    @test_case()
    def go_to_custom_inventory_page_and_verify_contents(self):
        self.go_to_inventory_list_page_and_verify_contents()
        self.pages.inventory_list_page.click_on_custom_inventory_tab()
        self.verify_custom_inventory_list_page_contents()

    @test_case()
    def assert_custom_inventory_create_or_edit_page_title(self, page_title):
        self.pages.custom_inventory_edit_page.wait_till_visible(self.pages.custom_inventory_edit_page.save_custom_inventory_button)
        self.pages.custom_inventory_edit_page.page_should_contain(getattr(self.pages.custom_inventory_edit_page, page_title))

    @test_case()
    def functionality_of_new_custom_inventory_button(self):
        self.pages.inventory_list_page.click_on_new_custom_inventory_button()
        self.assert_custom_inventory_create_or_edit_page_title('custom_inventory_create_page_title')

    @test_case()
    def creation_of_custom_inventory(self, media_type = 'Online'):
        custom_inventory_name = 'Smoke-custom-inventory-' + self.pages.guaranteed_inventory_edit_page.get_random_string(5)
        functions_dict = {'enter_custom_inventory_publisher_name': custom_inventory_name, 'enter_custom_inventory_placement_name': custom_inventory_name,
                          'click_on_custom_inventory_available_checkbox': '', 'click_on_custom_inventory_secure_checkbox': '',
                          'select_custom_inventory_media_type': media_type}
        for key, value in functions_dict.iteritems():
            if value:
                getattr(self.pages.custom_inventory_edit_page, key)(value)
            else:
                getattr(self.pages.custom_inventory_edit_page, key)()
        self.pages.custom_inventory_edit_page.click_on_save_custom_inventory_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.custom_inventory_table)
        self.pages.inventory_list_page.page_should_contain(self.pages.inventory_list_page.custom_inventory_success_message.format(custom_inventory_name))

    @test_case()
    def functionality_of_custom_inventory_edit_link(self):
        self.pages.inventory_list_page.click_on_custom_inventory_gear_icon()
        self.pages.inventory_list_page.click_on_custom_inventory_edit_link()
        self.assert_custom_inventory_create_or_edit_page_title('custom_inventory_edit_page_title')

    @test_case()
    def functionality_of_cancel_button_from_custom_inventory_edit_page(self):
        self.pages.custom_inventory_edit_page.click_on_custom_inventory_cancel_button()
        self.verify_custom_inventory_list_page_contents()

    @test_case()
    def custom_inventory_functionality_of_placement_name_link_helper(self):
        self.pages.custom_inventory_show_page.wait_till_visible(['id', 'details'])
        for page_contents in self.pages.custom_inventory_show_page.custom_inventory_show_page_contents:
            self.pages.custom_inventory_show_page.page_should_contain(page_contents)
        for element in self.pages.custom_inventory_show_page.custom_inventory_show_page_elements:
            assert self.pages.custom_inventory_show_page.is_element_present(getattr(self.pages.custom_inventory_show_page, element))

    @test_case()
    def functionality_of_custom_inventory_publisher_or_placement_name_link(self):
        self.pages.inventory_list_page.click_on_custom_inventory_publisher_name_link()
        self.custom_inventory_functionality_of_placement_name_link_helper()
        self.pages.custom_inventory_show_page.click_on_custom_inventory_link()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.custom_inventory_table)
        self.pages.inventory_list_page.click_on_custom_inventory_placement_name_link()
        self.guaranteed_inventory_functionality_of_placement_name_link_helper()

    @test_case()
    def verify_activity_list_page_contents(self):
        self.pages.activity_list_page.wait_till_visible(self.pages.activity_list_page.activity_table)
        for page_content in self.pages.activity_list_page.activity_list_page_contents:
            self.pages.activity_list_page.page_should_contain(page_content)
        for element in self.pages.activity_list_page.activity_list_page_elements:
            self.common_helper.assert_is_element_present(self.pages.activity_list_page, getattr(self.pages.activity_list_page, element))

    @test_case()
    def go_to_activity_list_page_and_verify_contents(self):
        self.pages.search_page.click_activity_tab()
        self.verify_activity_list_page_contents()
        self.pages.activity_list_page.click_element(self.pages.activity_list_page.activity_filter_box)

    @test_case()
    def functionality_of_create_activity_button(self):
        self.pages.activity_list_page.click_on_create_new_activity_button()
        self.pages.activity_create_new_page.wait_till_visible(self.pages.activity_create_new_page.create_activity_button)
        self.pages.activity_create_new_page.page_should_contain("Create activity")

    @test_case()
    def creation_of_activity_with_segment_and_audience(self):
        self.pages.activity_create_new_page.enter_activity_name_first('Smoke-activity-'+self.pages.activity_create_new_page.get_random_string(5))
        self.pages.activity_create_new_page.select_activity_type('Expand')
        self.pages.activity_create_new_page.select_tag_server('DFA')
        self.pages.activity_create_new_page.enter_tag_id_first(self.pages.activity_create_new_page.get_random_digits(8))
        self.pages.activity_create_new_page.click_secure_checkbox_first()
        self.pages.activity_create_new_page.click_rmx_checkbox_first()
        self.pages.activity_create_new_page.check_create_segment_checkbox()
        self.pages.activity_create_new_page.enter_activity_segment_name('Smoke-activity-segment-'+self.pages.activity_create_new_page.get_random_string(5))
        self.pages.activity_create_new_page.check_create_audience_checkbox()
        self.pages.activity_create_new_page.enter_audience_name('Smoke-activity-audience-'+self.pages.activity_create_new_page.get_random_string(5))
        self.pages.activity_create_new_page.click_create_activity_button()
        self.verify_activity_list_page_contents()
        self.pages.activity_list_page.page_should_contain(self.pages.activity_list_page.activity_create_success_message)

    @test_case()
    def functionality_of_edit_activity_link(self):
        self.pages.activity_list_page.click_gear_icon()
        self.pages.activity_list_page.click_edit_activity_link()
        self.pages.activity_edit_page.wait_till_visible(self.pages.activity_edit_page.create_activity_button)
        self.pages.activity_edit_page.page_should_contain(self.pages.activity_edit_page.activity_edit_page_title)

    @test_case()
    def functionality_of_activities_link(self, page_object):
        page_object.click_activities_link()
        self.verify_activity_list_page_contents()

    @test_case()
    def functionality_of_activities_link_from_activity_edit_page(self):
        self.functionality_of_activities_link(self.pages.activity_edit_page)

    @test_case()
    def verify_activity_show_page_contents(self):
        self.pages.activity_show_page.wait_till_visible(self.pages.activity_show_page.activity_show_page_locator)
        for page_contents in self.pages.activity_show_page.activity_show_page_contents:
            self.pages.activity_show_page.page_should_contain(page_contents)
        for element in self.pages.activity_show_page.activity_show_page_elements:
            self.common_helper.assert_is_element_present(self.pages.activity_show_page, getattr(self.pages.activity_show_page, element))

    @test_case()
    def functionality_of_view_activity_link(self):
        self.pages.activity_list_page.click_gear_icon()
        self.pages.activity_list_page.click_view_activity_link()
        self.verify_activity_show_page_contents()

    @test_case()
    def functionality_of_activities_link_from_activity_show_page(self):
        self.functionality_of_activities_link(self.pages.activity_show_page)

    @test_case()
    def functionality_of_activity_name_link(self):
        self.pages.activity_list_page.click_activity_name()
        self.verify_activity_show_page_contents()

    @test_case()
    def verify_audience_list_page_contents(self):
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        for content in self.pages.audience_segment_list_page.audience_list_page_contents:
            self.pages.audience_segment_list_page.page_should_contain(content)
        for element in self.pages.audience_segment_list_page.audience_list_page_elements:
            assert self.pages.audience_segment_list_page.is_element_present(getattr(self.pages.audience_segment_list_page, element))

    @test_case()
    def go_to_audience_list_page_and_verify_contents(self):
        self.pages.search_page.click_audience_link()
        self.verify_audience_list_page_contents()
        self.pages.audience_segment_list_page.click_element(self.pages.audience_segment_list_page.audience_search_text_box)

    @test_case()
    def functionality_of_create_new_audience_button(self):
        self.pages.audience_segment_list_page.click_on_create_new_audience_button()
        self.pages.audience_create_page.wait_till_visible(self.pages.audience_create_page.segment_table)
        self.pages.audience_create_page.page_should_contain(self.pages.audience_create_page.audience_create_page_title)

    @test_case()
    def creation_of_audience(self):
        audience_name = 'Smoke-test-audience-'+self.pages.audience_create_page.get_random_string(5)
        self.pages.audience_create_page.select_first_audience_marketplace_from_audience_marketplace_table()
        self.pages.audience_create_page.click_use_advance_mode_checkbox()
        self.pages.audience_create_page.click_and_button()
        self.pages.audience_create_page.click_or_button()
        self.pages.audience_create_page.enter_audience_name(audience_name)
        self.pages.audience_create_page.click_create_audience_button()
        self.pages.audience_show_page.wait_till_visible(self.pages.audience_show_page.audience_detail_section)
        self.pages.audience_show_page.page_should_contain(self.pages.audience_show_page.creation_sucess_message.format(audience_name))

    @test_case()
    def functionality_of_view_all_link_from_audience_show_page(self):
        self.pages.audience_show_page.click_view_all_link()
        self.verify_audience_list_page_contents()

    @test_case()
    def functionality_of_audience_edit_icon(self):
        first_audience_name = self.pages.audience_segment_list_page.get_first_element_from_list("first_audience_name")
        self.pages.audience_segment_list_page.click_first_edit_icon()
        self.pages.audience_create_page.wait_till_visible(self.pages.audience_create_page.create_audience_button)
        self.pages.audience_create_page.page_should_contain(self.pages.audience_create_page.audience_edit_page_title.format(first_audience_name))

    @test_case()
    def functionality_of_cancel_button_from_audience_edit_page(self):
        self.pages.audience_create_page.click_cancel_button()
        self.verify_audience_list_page_contents()

    @test_case()
    def functionality_of_audience_name_link(self):
        first_audience_name = self.pages.audience_segment_list_page.get_first_element_from_list("first_audience_name")
        self.pages.audience_segment_list_page.click_first_audience_name_link()
        self.pages.audience_show_page.wait_till_visible(self.pages.audience_show_page.audience_detail_section)
        self.pages.audience_show_page.page_should_contain(self.pages.audience_show_page.audience_show_page_title.format(first_audience_name))
        self.functionality_of_view_all_link_from_audience_show_page()

    @test_case()
    def verify_segment_list_page_contents(self):
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.segment_table)
        self.pages.audience_segment_list_page.select_option_from_segment_filter_dropdown("View All")
        for content in self.pages.audience_segment_list_page.segment_list_page_contents:
            self.pages.audience_segment_list_page.page_should_contain(content)
        for element in self.pages.audience_segment_list_page.segment_list_page_elements:
            assert self.pages.audience_segment_list_page.is_element_present(getattr(self.pages.audience_segment_list_page, element))
        self.pages.audience_segment_list_page.check_dropdown_options(self.pages.audience_segment_list_page.segment_filter_dropdown_options,
                                                       self.pages.audience_segment_list_page.segment_filter_dropdown)

    @test_case()
    def go_to_segment_list_page_and_verify_contents(self):
        self.pages.search_page.click_audience_link()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.audience_table)
        self.pages.audience_segment_list_page.click_segment_tab()
        self.verify_segment_list_page_contents()

    @test_case()
    def functionality_of_create_first_party_segment_button(self):
        self.pages.audience_segment_list_page.click_on_create_first_party_segment_button()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.segment_create_page_title)

    @test_case()
    def creation_of_segment(self):
        segment_name = 'Smoke-test-segment-'+self.pages.segment_create_page.get_random_string(5)
        self.pages.segment_create_page.enter_segment_name(segment_name)
        self.pages.segment_create_page.click_on_create_segment_button()
        self.pages.segment_show_page.wait_till_visible(self.pages.segment_show_page.add_pixel_activity_button)
        self.pages.segment_show_page.page_should_contain(self.pages.segment_show_page.segment_creation_success_message.format(segment_name))

    @test_case()
    def functionality_of_view_all_from_segment_show_page(self):
        self.pages.segment_show_page.click_on_view_all_link()
        self.verify_audience_list_page_contents()

    @test_case()
    def go_to_segment_list_page_and_set_view_all(self):
        self.pages.audience_segment_list_page.click_segment_tab()
        self.pages.audience_segment_list_page.wait_till_visible(self.pages.audience_segment_list_page.segment_table)
        self.pages.audience_segment_list_page.select_option_from_segment_filter_dropdown("View All")

    @test_case()
    def functionality_of_segment_edit_link(self):
        self.go_to_segment_list_page_and_set_view_all()
        self.pages.audience_segment_list_page.click_first_segment_gear_icon()
        self.pages.audience_segment_list_page.click_first_segment_edit_link()
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        self.pages.segment_create_page.page_should_contain(self.pages.segment_create_page.segment_edit_page_title)

    @test_case()
    def functionality_of_view_all_from_segment_edit_page(self):
        self.pages.segment_create_page.click_view_all_link()
        self.verify_audience_list_page_contents()

    @test_case()
    def verify_segment_show_page_contents(self):
        self.pages.segment_show_page.wait_till_visible(self.pages.segment_show_page.add_pixel_activity_button)
        for content in self.pages.segment_show_page.segment_show_page_contents:
            self.pages.segment_show_page.page_should_contain(content)
        for element in self.pages.segment_show_page.segment_show_page_elements:
            assert self.pages.segment_show_page.is_element_present(getattr(self.pages.segment_show_page, element))

    @test_case()
    def functionality_of_segment_view_link(self):
        self.go_to_segment_list_page_and_set_view_all()
        self.pages.audience_segment_list_page.click_first_segment_gear_icon()
        self.pages.audience_segment_list_page.click_first_segment_view_link()
        self.verify_segment_show_page_contents()

    @test_case()
    def functionality_of_segment_name_link(self):
        self.functionality_of_view_all_from_segment_show_page()
        self.go_to_segment_list_page_and_set_view_all()
        self.pages.audience_segment_list_page.click_on_first_segment_name()
        self.verify_segment_show_page_contents()

    @test_case()
    def go_to_creative_list_page_and_verify_contents(self):
        self.pages.search_page.click_creative_link()
        self.verify_creative_list_page_contents()
        self.pages.creative_list_page.click_element(self.pages.creative_list_page.filters)

    @test_case()
    def functionality_of_new_creatives_button(self):
        self.pages.creative_list_page.click_new_creatives()
        self.pages.bulk_edit_creative_page.wait_for_creative_forms()
        self.pages.bulk_edit_creative_page.page_should_contain(self.pages.bulk_edit_creative_page.creatives_bulk_edit_page_title)
        assert self.pages.bulk_edit_creative_page.is_element_present(self.pages.bulk_edit_creative_page.detailed_edit_link)

    @test_case()
    def functionality_of_detailed_edit_link(self):
        self.pages.bulk_edit_creative_page.go_to_link('Detailed Edit')
        self.pages.detailed_edit_creatives.wait_for_detailed_form()
        self.pages.detailed_edit_creatives.page_should_contain('Creatives List')

    @test_case()
    def functionality_of_bulk_upload_creatives_button(self):
        self.pages.detailed_edit_creatives.click_on_bulk_upload_creative_button()
        self.pages.detailed_edit_creatives.accept_alert()
        self.pages.bulk_upload_new_creative.wait_till_visible(self.pages.bulk_upload_new_creative.creative_attributes_section)
        self.pages.bulk_upload_new_creative.page_should_contain(self.pages.bulk_upload_new_creative.creative_bulk_upload_page_title)

    @test_case()
    def creation_of_creative_by_uploading(self):
        self.pages.bulk_upload_new_creative.select_is_flash(self.dx_constant.select_value_false)
        self.pages.bulk_upload_new_creative.input_concept('Creative_Concept')
        time.sleep(1)
        creative_file_path = SearchFilePath('mock_creative_data.xls', os.path.abspath(os.path.dirname(__file__) + '/../../../data/')).file_name
        self.pages.bulk_upload_new_creative.click_upload(creative_file_path)
        self.pages.bulk_upload_new_creative.click_submit()
        self.pages.detailed_edit_creatives.wait_till_visible(self.pages.detailed_edit_creatives.creative_form)
        self.pages.detailed_edit_creatives.click_detailed_edit()
        self.pages.detailed_edit_creatives.wait_for_detailed_form()
        self.pages.detailed_edit_creatives.input_first_creative_name('Smoke-test-creative-'+self.pages.detailed_edit_creatives.get_random_string(5))
        self.pages.detailed_edit_creatives.fill_field(self.pages.detailed_edit_creatives.first_creative_name, Keys.TAB)
        self.pages.detailed_edit_creatives.save_creative()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.creative_table)
        self.pages.creative_list_page.page_should_contain(self.pages.creative_list_page.creative_success_message)

    @test_case()
    def functionality_of_creative_name_link(self):
        self.pages.creative_list_page.click_first_creative()
        self.pages.creative_show_page.wait_till_visible(self.pages.creative_show_page.ad_tag_snippet_section)
        for element in self.pages.creative_show_page.creative_show_page_elements:
            assert self.pages.creative_show_page.is_element_present(getattr(self.pages.creative_show_page, element))

    @test_case()
    def functionality_of_creatives_for_advertiser_link(self):
        self.pages.creative_show_page.click_on_creatives_for_advertiser_link()
        self.verify_creative_list_page_contents()

    @test_case()
    def functionality_of_creative_edit_link(self):
        self.pages.creative_list_page.click_on_first_creative_gear_icon()
        self.pages.creative_list_page.click_on_first_creative_edit_link()
        self.pages.creative_edit_page.wait_till_visible(self.pages.creative_edit_page.submit_button)
        self.pages.creative_edit_page.page_should_contain(self.pages.creative_edit_page.creative_edit_page_title)

    @test_case()
    def functionality_of_back_to_creative_list_link(self):
        self.pages.creative_edit_page.click_creative_list_link()
        self.verify_creative_list_page_contents()

    @test_case()
    def functionality_of_new_assets_button(self):
        self.pages.creative_list_page.click_on_new_assets_button()
        self.pages.upload_assets_page.wait_till_visible(self.pages.upload_assets_page.upload_assets_button)
        self.pages.upload_assets_page.page_should_contain(self.pages.upload_assets_page.upload_asset_page_title)

    @test_case()
    def upload_asset_file(self, generate_creative_checkbox='Unchecked'):
        asset_file_path = SearchFilePath('jpeg_asset.jpeg', os.path.abspath(os.path.dirname(__file__) + '/../../../data/')).file_name
        self.pages.upload_assets_page.select_asset_file(asset_file_path)
        if generate_creative_checkbox == 'Checked':
            self.pages.upload_assets_page.click_generate_creatives_checkbox()
        self.pages.upload_assets_page.click_upload_assets_button()

    @test_case()
    def creation_of_asset(self):
        self.upload_asset_file()
        self.verify_creative_list_page_contents()
        self.pages.creative_list_page.page_should_contain(self.pages.creative_list_page.asset_success_message)

    @test_case()
    def functionality_of_delete_asset_button(self):
        self.pages.creative_list_page.click_first_asset_checkbox()
        self.pages.creative_list_page.click_delete_asset_button()
        self.pages.creative_list_page.accept_alert()
        time.sleep(2)
        self.verify_creative_list_page_contents()
        self.pages.creative_list_page.page_should_contain(self.pages.creative_list_page.asset_delete_message)        

    @test_case()
    def generating_creative_from_asset(self):
        self.functionality_of_new_assets_button()
        self.upload_asset_file('Checked')
        self.pages.generate_creative_page.wait_till_visible(self.pages.generate_creative_page.ok_button)
        self.pages.generate_creative_page.page_should_contain(self.pages.generate_creative_page.generate_creative_message)
        self.pages.generate_creative_page.enter_creative_name('Smoke-test-asset-'+self.pages.generate_creative_page.get_random_string(5))
        self.pages.generate_creative_page.click_ok_button()
        self.pages.detailed_edit_creatives.wait_for_detailed_form()
        self.pages.detailed_edit_creatives.save_creative()
        self.verify_creative_list_page_contents()
        self.pages.creative_list_page.page_should_contain(self.pages.creative_list_page.creative_success_message)

    @test_case()
    def functionality_of_asset_edit_link(self):
        self.pages.creative_list_page.click_first_asset_gear_icon()
        self.pages.creative_list_page.click_first_asset_edit_link()
        self.pages.asset_edit_page.wait_till_visible(self.pages.asset_edit_page.asset_save_button)
        self.pages.asset_edit_page.page_should_contain(self.pages.asset_edit_page.asset_edit_page_title)

    @test_case()
    def verify_campaign_list_page_contents(self):
        self.pages.campaign_list_page.wait_till_visible(self.pages.campaign_list_page.campaign_list_table)
        self.pages.campaign_list_page.click_element(self.pages.campaign_list_page.search_box)
        for element in self.pages.campaign_list_page.campaign_list_page_element:
            assert self.pages.campaign_list_page.is_element_present(getattr(self.pages.campaign_list_page, element))

    @test_case()
    def go_to_campaign_list_page_and_verify_contents(self):
        self.pages.search_page.click_campaign_link()
        self.verify_campaign_list_page_contents()

    @test_case()
    def functionality_of_new_media_plan_button(self):
        self.pages.campaign_list_page.click_new_media()
        self.pages.create_media_plan_page.wait_till_visible(self.pages.create_media_plan_page.submit)
        self.pages.create_media_plan_page.page_should_contain(self.pages.create_media_plan_page.create_media_plan_title)

    @test_case()
    def creation_of_new_media_plan(self):
        self.pages.create_media_plan_page.type_name('Smoke-test-media-plan-'+self.pages.create_media_plan_page.get_random_string(5))
        self.pages.create_media_plan_page.type_budget('50')
        self.pages.create_media_plan_page.click_add_row()
        self.pages.create_media_plan_page.type_activity_filter('15454545')
        self.pages.create_media_plan_page.type_value('6')
        self.pages.create_media_plan_page.click_submit()
        self.pages.create_media_plan_page.page_should_contain(self.pages.create_media_plan_page.messages['success'])

    @test_case()
    def functionality_of_media_plans_and_campaigns_link(self):
        self.pages.create_media_plan_page.go_to_link('Media Plans & Campaigns')
        self.verify_campaign_list_page_contents()

    @test_case()
    def functionality_of_new_campaign_button(self, channel_type = "Online"):
        self.pages.campaign_list_page.click_new_campaign()
        self.pages.new_campaign_pop_up.wait_till_visible(self.pages.new_campaign_pop_up.advertiser)
        self.pages.new_campaign_pop_up.type_advertiser(self.dx_constant.advertiser_name)
        for element in self.pages.new_campaign_pop_up.create_campaign_popup_elements:
            assert self.pages.new_campaign_pop_up.is_element_present(getattr(self.pages.new_campaign_pop_up, element))
        self.pages.new_campaign_pop_up.page_should_contain(self.pages.new_campaign_pop_up.create_campaign_popup_title)
        self.pages.new_campaign_pop_up.select_campaign_channel(channel_type)
        self.pages.new_campaign_pop_up.submit()
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.create_campaign_page_title)

    @test_case()
    def creation_of_campaign(self):
        self.campaign_name = "Smoke-test-campaign-" + self.pages.create_campaign_page.get_random_string(5)
        self.pages.create_campaign_page.type_campaign_name(self.campaign_name)
        self.pages.create_campaign_page.enter_start_date(self.dx_date.date_after_two_days())
        self.pages.create_campaign_page.enter_cpa_goal(self.dx_constant.new_campaign_cpa)
        self.pages.create_campaign_page.enter_budget(self.dx_constant.new_campaign_budget)
        self.pages.create_campaign_page.enter_cpm(self.dx_constant.new_campaign_cpm)
        self.pages.create_campaign_page.click_campaign_objective_distribution()
        self.pages.create_campaign_page.enter_end_date(self.dx_date.last_date_of_current_month())
        self.pages.create_campaign_page.click_element(self.pages.create_campaign_page.campaign_name)
        self.pages.create_campaign_page.wait_till_element_clickable(self.pages.create_campaign_page.create_campaign_button)
        self.pages.create_campaign_page.submit()
        if self.pages.create_campaign_page.is_element_present(self.pages.create_campaign_page.create_campaign_button):
            self.pages.create_campaign_page.submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row)
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.fbs_page_title)

    @test_case()
    def creation_of_flight(self):
        self.flight_name = 'Smoke-test-flight-' + self.pages.fbs_page.get_random_string(5)
        self.pages.fbs_page.fill_description(self.flight_name)
        self.pages.fbs_page.type_bid_enter(self.dx_constant.flight_bid)
        self.pages.fbs_page.type_budget_enter(self.dx_constant.flight_budget)
        time.sleep(1)
        self.pages.fbs_page.click_on_save_continue()
        self.pages.create_flight_page.wait_for_flight_details()
        self.pages.create_flight_page.page_should_contain(self.pages.create_flight_page.flight_detailed_edit_page_title.format(self.flight_name))

    @test_case()
    def verify_campaign_show_page(self):
        self.pages.campaign_show_page.wait_for_loading()
        self.pages.campaign_show_page.page_should_contain(self.pages.campaign_show_page.campaign_show_page_title.format(self.campaign_name))

    @test_case()
    def functionality_of_flight_save_and_exit_button(self):
        self.pages.create_flight_page.click_save_exit()
        self.verify_campaign_show_page()

    @test_case()
    def functionality_of_campaign_edit_link(self):
        self.pages.campaign_show_page.edit()
        self.pages.create_campaign_page.wait_till_visible(self.pages.create_campaign_page.create_campaign_button, 40)
        self.pages.create_campaign_page.page_should_contain(self.pages.create_campaign_page.campaign_edit_page_title)

    @test_case()
    def functionality_of_update_campaign_button(self):
        self.pages.create_campaign_page.enter_budget('1250')
        self.pages.create_campaign_page.submit()
        self.verify_campaign_show_page()

    @test_case()
    def functionality_of_flight_name_link(self):
        self.pages.campaign_show_page.go_to_link(self.flight_name)
        self.pages.flight_show_page.wait_for_flight_basics()
        for element in self.pages.flight_show_page.flight_show_page_element:
            assert self.pages.flight_show_page.is_element_present(getattr(self.pages.flight_show_page, element))

    @test_case()
    def functionality_of_view_campaign_link(self):
        self.pages.flight_show_page.view_all_campaigns()
        self.verify_campaign_show_page()

    @test_case()
    def functionality_of_flight_edit_icon(self):
        self.pages.campaign_show_page.click_first_flight_edit_icon()
        self.pages.create_flight_page.wait_for_flight_details()
        assert self.pages.create_flight_page.is_element_present(self.pages.create_flight_page.save_and_exit)
        self.pages.create_flight_page.click_on_campaign_name_link()
        self.verify_campaign_show_page()

    @test_case()
    def functionality_of_bulk_upload_flights_button(self):
        self.pages.campaign_show_page.bulk_upload_flights()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.upload_flight_sections, 60)
        self.pages.upload_flights_page.page_should_contain(self.pages.upload_flights_page.flight_upload_page_title)

    @test_case()
    def creation_of_flights_by_uploading(self):
        self.common_helper.process_flight_file_with_name_and_date('test_valid_flights', 'Online')
        self.pages.upload_flights_page.select_file(os.path.dirname(__file__)+ '/../../../data/flights_upload/test_valid_flights.csv')
        self.pages.upload_flights_page.click_upload_file()
        self.pages.upload_flights_page.wait_till_visible(self.pages.upload_flights_page.flight_submit, 120)
        self.pages.upload_flights_page.click_flights_submit()
        self.pages.fbs_page.wait_till_visible(self.pages.fbs_page.flights_row, 180)
        self.pages.fbs_page.page_should_contain(self.pages.fbs_page.flight_upload_success_message)
        self.pages.fbs_page.click_on_save_exit()
        self.verify_campaign_show_page()
