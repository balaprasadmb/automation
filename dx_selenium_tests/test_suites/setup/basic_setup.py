# -*- coding: utf-8 -*-
import os
import time
from lib.dx_date import DXDate
from selenium.webdriver.common.keys import Keys
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from manage_organizations import ManageOrganizations
from dx_search_file_path import SearchFilePath

class EnvironmentSetup(DXTest):

    @test_case()
    def login_as_dx_manager(self):
        self.manage_organization = ManageOrganizations()
        self.agency_group_success_message = self.pages.new_agency_group_page.success_message['organization_name']
        self.agency_success_message = self.pages.new_agency_page.success_message['organization_name']
        self.advertiser_id_map = {}
        self.login_as_user()

    @test_case()
    def setup_organizations(self):
        self.pages.new_agency_group_page.open()
        self.pages.new_agency_group_page.wait_till_visible(self.pages.new_agency_group_page.agency_group_name)
        self.agency_group_name = "regression_agency_group_" + self.pages.new_agency_group_page.get_random_string(8)
        self.pages.new_agency_group_page.type_organization_name(self.agency_group_name)
        self.pages.new_agency_group_page.type_email("regression@dataxu.com")
        self.pages.new_agency_group_page.type_contact_name("DataXu")
        self.pages.new_agency_group_page.check_select_all_currencies()
        self.pages.new_agency_group_page.upload_rate_card(os.getcwd() + '/data/rate_cards/rate_card_USD.xls')
        for media in ["Online", "Mobile", "Video"]:
            self.pages.new_agency_group_page.click_media_type_checkbox(media)
        self.pages.new_agency_group_page.select_all_inventory()
        if self.pages.new_agency_group_page.is_element_present(self.pages.new_agency_group_page.dx_technical_exchange):
            self.pages.new_agency_group_page.find_element(self.pages.new_agency_group_page.dx_technical_exchange).click()
        insight_list = self.pages.new_agency_group_page.insight_list
        for insight in insight_list:
            self.pages.new_agency_group_page.select_insights(insight)
        self.pages.new_agency_group_page.click_targeting_checkbox()
        self.pages.new_agency_group_page.click_cost_model_type('CPA')
        self.pages.new_agency_group_page.click_create_agency_group_button()
        self.pages.new_agency_group_page.check_success_message(
        	self.agency_group_success_message['create_new_agency_group'].format(self.agency_group_name))
        self.manage_organization.override_agency_group(self.agency_group_name)
        self.pages.agency_group_details_page.wait_till_visible(self.pages.agency_group_details_page.add_agency)
        self.pages.agency_group_details_page.click_add_agency()
        self.pages.new_agency_page.wait_till_visible(self.pages.new_agency_page.submit_button)
        self.agency_name = "regression_agency_" + self.pages.new_agency_page.get_random_string(8)
        self.pages.new_agency_page.type_organization_name(self.agency_name)
        self.pages.new_agency_page.click_create_agency_button()
        self.pages.new_agency_page.check_success_message(
        	self.agency_success_message['create_new_agency'].format(self.agency_name))
        self.manage_organization.override_agency(self.agency_name)
        self.pages.agency_details_page.wait_till_visible(self.pages.agency_details_page.add_advertiser_button)
        self.pages.agency_details_page.add_new_advertiser()
        self.pages.new_advertiser_page.wait_till_visible(self.pages.new_advertiser_page.organization_name)
        self.advertiser_name = "regression_advertiser_" + self.pages.new_advertiser_page.get_random_string(8)
        self.pages.new_advertiser_page.type_organization_name(self.advertiser_name)
        self.pages.new_advertiser_page.type_advertiser_domain('www.dataxu.com')
        self.pages.new_advertiser_page.check_limit_one_impression_per_page_view()
        self.pages.new_advertiser_page.click_on_oba_checkbox()
        self.pages.new_advertiser_page.click_on_oba_popup_accept_button()
        self.pages.new_advertiser_page.click_create_advetiser_button()
        message = self.pages.advertiser_list_page.success_message
        self.pages.advertiser_list_page.page_should_contain(message.format(self.advertiser_name))
        self.manage_organization.override_advertiser(self.advertiser_name)
        self.pages.advertiser_list_page.type_advertiser_name_in_filterbox(self.advertiser_name)
        time.sleep(2)
        url = self.pages.advertiser_list_page.find_element(self.pages.advertiser_list_page.advertiser_name_link).get_attribute('href')
        self.advertiser_id_map[self.advertiser_name] = url.split('?')[0].split('/')[-1]

    def is_user_exist(self, user_id):
        self.pages.user_list_page.open()
        self.pages.user_list_page.wait_till_visible(self.pages.user_list_page.list_pagination_setup)
        self.pages.user_list_page.filter_user(user_id)
        if self.pages.user_list_page.is_element_present(self.pages.user_list_page.first_user_email):
            searched_user = self.pages.user_list_page.get_attribute_value(self.pages.user_list_page.first_user_email)
            assert user_id in searched_user
            return 'user_exist'
        else:
            return 'user_not_exist'

    @test_case()
    def select_organization_and_roles_for_users(self, page_object, org_for_role, user_role):
        page_object.select_organization(self.agency_group_name)
        for role in user_role:
            page_object.click_on_add_user_role_button()
            page_object.select_organization_to_add_role(org_for_role)
            page_object.select_user_role(role)
        page_object.click_on_submit_button()
        self.pages.user_show_page.wait_till_visible(self.pages.user_show_page.edit_link)

    @test_case()
    def user_setup(self, email_id, org_for_role, user_role):
        user_id = email_id['user_name'].split('@')[0]
        user_status = self.is_user_exist(user_id)
        if user_status == 'user_exist':
            self.pages.user_list_page.click_on_edit_icon()
            self.pages.user_edit_page.wait_till_visible(self.pages.user_edit_page.roles_and_permissions_remove_button)
            for element in self.pages.user_edit_page.find_elements(self.pages.user_edit_page.roles_and_permissions_remove_button):
                element.click()
                time.sleep(1)
            self.select_organization_and_roles_for_users(self.pages.user_edit_page, org_for_role, user_role)
            self.pages.user_show_page.page_should_contain(self.pages.user_show_page.user_update_message)
        else:
            self.pages.new_user_page.open()
            self.pages.new_user_page.wait_till_visible(self.pages.new_user_page.submit_button)
            self.pages.new_user_page.enter_user_email_id(email_id['user_name'])
            self.select_organization_and_roles_for_users(self.pages.new_user_page, org_for_role, user_role)
            self.pages.user_show_page.page_should_contain(self.pages.user_show_page.user_creation_success_message)

    @test_case()
    def setup_of_agency_group_system_organization_admin(self):
        self.user_setup(self.dx_constant.user_by_role['system_level_organization_administrator_two'], 'System', ['Organization Administrator'])

    @test_case()
    def setup_of_agency_system_organization_admin(self):
        self.user_setup(self.dx_constant.user_by_role['system_level_organization_administrator_one'], 'System', ['Organization Administrator'])

    @test_case()
    def setup_of_advertiser_system_organization_admin(self):
        self.user_setup(self.dx_constant.user_by_role['system_level_organization_administrator_three'], 'System', ['Organization Administrator'])

    @test_case()
    def setup_of_system_level_organization_admin(self):
        self.user_setup(self.dx_constant.user_by_role['organization_administrator'], 'System', ['Organization Administrator'])

    @test_case()
    def setup_of_oneview_system_organization_admin(self):
        self.user_setup(self.dx_constant.user_by_role['sys_admin_one_view'], 'System', ['Organization Administrator'])

    @test_case()
    def setup_of_oneview_campaign_manager(self):
        self.user_setup(self.dx_constant.user_by_role['campaign_manager_one_view'], self.agency_group_name, ['Campaign Manager'])

    @test_case()
    def setup_of_non_domain_campaign_manager(self):
        self.user_setup(self.dx_constant.user_by_role['non_dataxu_domain_campaign_user'], self.agency_group_name, ['Campaign Manager'])

    @test_case()
    def setup_of_inventory_manager(self):
        self.user_setup(self.dx_constant.user_by_role['inventory_manager'], self.agency_group_name, ['Inventory Manager'])

    @test_case()
    def setup_of_campaign_and_inventory_manager(self):
        self.user_setup(self.dx_constant.user_by_role['campaign_manager'], self.agency_group_name, ['Campaign Manager', 'Inventory Manager'])

    @test_case()
    def apply_product_features_to_user(self, selected_product_features, user_list):
        self.pages.product_feature_list_page.open()
        self.pages.product_feature_list_page.wait_till_visible(self.pages.product_feature_list_page.product_feature_list_table)
        for product_feature in selected_product_features:
            self.pages.product_feature_list_page.search_product_feature(product_feature)
            self.pages.product_feature_list_page.click_on_first_edit_link()
            self.pages.product_feature_edit_page.wait_till_visible(self.pages.product_feature_edit_page.user_selection_box)
            selected_users_list = self.pages.product_feature_edit_page.get_selected_users_list()
            for user in user_list:
                if user not in selected_users_list:
                    self.pages.product_feature_edit_page.add_user_in_user_selection_box(user)
                    updated_selected_users_list = self.pages.product_feature_edit_page.get_selected_users_list()
                    assert user in updated_selected_users_list
                else:
                    assert user in selected_users_list
            self.pages.product_feature_edit_page.click_on_update_product_feature_button()
            self.pages.product_feature_list_page.wait_till_visible(self.pages.product_feature_list_page.product_feature_list_table)
            self.pages.product_feature_list_page.page_should_contain(self.pages.product_feature_list_page.update_success_message.format(product_feature))

    @test_case()
    def apply_product_features_to_dx_campaign(self):
        selected_product_features = self.dx_constant.product_features
        self.apply_product_features_to_user(selected_product_features, ['dx_campaign@dataxu.com'])

    @test_case()
    def apply_product_features_to_dx_inventory(self):
        selected_product_features = ['Guaranteed Media']
        self.apply_product_features_to_user(selected_product_features, ['dx_inventory@dataxu.com'])

    @test_case()
    def apply_product_features_to_system_admin_users(self):
        selected_product_features = ['Inheritable Add On Costs']
        self.sys_admin_user_list = ['dx_agency_group_admin@dataxu.com', 'dx_agency_admin@dataxu.com', 'dx_advertiser_admin@dataxu.com', 'dx_organization_admin@dataxu.com', 'dx_oneview_admin@dataxu.com']
        self.apply_product_features_to_user(selected_product_features, self.sys_admin_user_list)

    @test_case()
    def apply_legacy_campaign_types_product_feature_to_all_users(self):
        selected_product_features = ['Legacy Campaign Types']
        user_list = ['dx_campaign@dataxu.com', 'dx_oneview_campaign@dataxu.com', 'dx_non@domain.com'] + self.sys_admin_user_list
        self.apply_product_features_to_user(selected_product_features, user_list)

    @test_case()
    def setup_creative(self):
        self.pages.bulk_upload_new_creative._open('advertisers/%s/creatives' % self.advertiser_id_map[self.advertiser_name])
        self.pages.bulk_upload_new_creative.wait_till_visible(self.pages.bulk_upload_new_creative.creative_attributes_section)
        self.pages.bulk_upload_new_creative.select_is_flash(self.dx_constant.select_value_false)
        self.pages.bulk_upload_new_creative.input_concept('Creative_Concept')
        time.sleep(1)
        mock_creative_data_filepath = '/../../data/bulk_upload_creative_files/mock_creative_data.xls'
        self.pages.bulk_upload_new_creative.click_upload(os.path.abspath(os.path.dirname(__file__) + mock_creative_data_filepath))
        self.pages.bulk_upload_new_creative.click_submit()
        self.pages.detailed_edit_creatives.wait_till_visible(self.pages.detailed_edit_creatives.creative_form)
        self.pages.detailed_edit_creatives.click_detailed_edit()
        time.sleep(2)
        self.pages.detailed_edit_creatives.save_creative()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.creative_table)
        self.pages.detailed_edit_creatives.page_should_contain('Creatives successfully saved. Creative Registration status may take up to 48 hours to update.')

    @test_case()
    def setup_asset(self):
        self.pages.upload_assets_page._open('advertisers/%s/assets/batch_upload' % self.advertiser_id_map[self.advertiser_name])
        self.pages.upload_assets_page.wait_till_visible(self.pages.upload_assets_page.more_assets_button)
        asset_file_path = SearchFilePath('jpeg_asset.jpeg', os.path.abspath(os.path.dirname(__file__) + '/../../data/')).file_name
        self.pages.upload_assets_page.select_asset_file(asset_file_path)
        self.pages.upload_assets_page.click_upload_assets_button()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.asset_list_table)
        self.pages.creative_list_page.page_should_contain(self.pages.creative_list_page.asset_success_message)

    @test_case()
    def setup_segment(self):
        self.pages.segment_create_page._open('advertisers/%s/first_party_segments/new' % self.advertiser_id_map[self.advertiser_name])
        self.pages.segment_create_page.wait_till_visible(self.pages.segment_create_page.create_segment_button)
        segment_name = self.dx_constant.segment_name + self.pages.segment_create_page.get_random_string(8)
        self.pages.segment_create_page.enter_segment_name(segment_name)
        self.pages.segment_create_page.click_on_create_segment_button()
        self.pages.segment_create_page.page_should_contain("Successfully created segment '{0}'.".format(segment_name))
 
    @test_case()
    def setup_audience(self):
        self.pages.audience_create_page._open('advertisers/%s/composite_segments/new' % self.advertiser_id_map[self.advertiser_name])
        self.pages.audience_create_page.wait_till_visible(self.pages.audience_create_page.segment_table)
        self.pages.audience_create_page.select_first_segment_from_segment_table()
        self.pages.audience_create_page.click_use_advance_mode_checkbox()
        self.pages.audience_create_page.click_and_button()
        audience_name = self.dx_constant.audience_name + self.pages.audience_create_page.get_random_string(8)
        self.pages.audience_create_page.enter_audience_name(audience_name)
        self.pages.audience_create_page.click_create_audience_button()
        self.pages.audience_segment_list_page.page_should_contain("Successfully created segment '{0}'.".format(audience_name))

    @test_case()
    def setup_activity(self):
        self.pages.activity_create_new_page._open('advertisers/%s/activities/new' % self.advertiser_id_map[self.advertiser_name])
        self.pages.activity_create_new_page.wait_till_visible(self.pages.activity_create_new_page.create_activity_button)
        self.pages.activity_create_new_page.enter_activity_name_first(self.dx_constant.activity_name + self.pages.activity_create_new_page.get_random_string(8))
        self.pages.activity_create_new_page.click_create_activity_button()
        self.pages.activity_create_new_page.page_should_contain("Activity successfully created:")

    @test_case()
    def setup_guaranteed_media_inventory(self):
        self.pages.guaranteed_inventory_edit_page._open('advertisers/%s/inventory_sources/new' % self.advertiser_id_map[self.advertiser_name])
        self.pages.guaranteed_inventory_edit_page.wait_till_visible(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_save_button)
        guaranteed_inventory_name = 'test-guaranteed-inventory-' + self.pages.custom_inventory_edit_page.get_random_string(8)
        self.pages.guaranteed_inventory_edit_page.enter_guaranteed_inventory_publisher_name(guaranteed_inventory_name)
        self.pages.guaranteed_inventory_edit_page.enter_guaranteed_inventory_placement_name(guaranteed_inventory_name)
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_available_checkbox()
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_save_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.guaranteed_inventory_list_table, 40)
        self.pages.inventory_list_page.page_should_contain(self.pages.inventory_list_page.guaranteed_inventory_success_message.format(guaranteed_inventory_name))

    @test_case()
    def setup_deal(self):
        self.pages.deal_inventory_edit_page._open('deal_inventories/new?locale=en')
        self.pages.deal_inventory_edit_page.wait_till_visible(self.pages.deal_inventory_edit_page.save_deal_button)
        deal_name = self.dx_constant.deal_name + self.pages.deal_inventory_edit_page.get_random_string(8)
        self.pages.deal_inventory_edit_page.enter_deal_name(deal_name)
        self.pages.deal_inventory_edit_page.select_deal_inventory_exchange('Admeta')
        self.pages.deal_inventory_edit_page.enter_deal_id(self.pages.deal_inventory_edit_page.get_random_string(8))
        self.pages.deal_inventory_edit_page.select_deal_type(1)
        self.pages.deal_inventory_edit_page.enter_cost_cpm_value('8')
        self.pages.deal_inventory_edit_page.enter_start_date(DXDate().todays_date())
        self.pages.deal_inventory_edit_page.enter_deal_description('test deal description')
        self.pages.deal_inventory_edit_page.enter_deal_permissioned_advertiser_name(self.advertiser_name)
        self.pages.deal_inventory_edit_page.fill_field(self.pages.deal_inventory_edit_page.deal_permissioned_advertiser_name, Keys.ENTER)
        self.pages.deal_inventory_edit_page.enter_end_date(DXDate().last_date_of_current_month())
        self.pages.deal_inventory_edit_page.click_on_save_deal_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.deal_inventory_list_table, 120)
        self.pages.inventory_list_page.page_should_contain(self.pages.inventory_list_page.deal_success_message.format(deal_name))

    @test_case()
    def setup_custom_inventory(self):
        self.pages.custom_inventory_edit_page._open('custom_inventories/new?locale=en')
        self.pages.custom_inventory_edit_page.wait_till_visible(self.pages.custom_inventory_edit_page.save_custom_inventory_button)
        custom_inventory_name = 'test-custom-inventory-' + self.pages.custom_inventory_edit_page.get_random_string(8)
        self.pages.custom_inventory_edit_page.enter_custom_inventory_publisher_name(custom_inventory_name)
        self.pages.custom_inventory_edit_page.enter_custom_inventory_placement_name(custom_inventory_name)
        self.pages.custom_inventory_edit_page.click_on_custom_inventory_available_checkbox()
        self.pages.custom_inventory_edit_page.click_on_save_custom_inventory_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.custom_inventory_table, 40)
        self.pages.inventory_list_page.page_should_contain(self.pages.inventory_list_page.custom_inventory_success_message.format(custom_inventory_name))

    @test_case()
    def setup_system_message(self):
        self.pages.advertiser_list_page._open('/system_notices/new?locale=en')
        self.pages.new_system_message_page.wait_till_visible(self.pages.new_system_message_page.save_message)
        self.pages.new_system_message_page.select_status_from_dropdown('Running')
        self.pages.new_system_message_page.click_on_save_message_button()
        self.pages.new_system_message_page.page_should_contain('Successfully Created System Message')
