# -*- coding: utf-8 -*-
import os
import time
from lib.dx_date import DXDate
from selenium.webdriver.common.keys import Keys
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from manage_organizations import ManageOrganizations
from dx_search_file_path import SearchFilePath

class UpdateDxConstantFile(DXTest):

    def login_as_dx_manager(self):
        self.manage_organization = ManageOrganizations()
        self.login_as_user()

    def update_organizations(self):
        self.login_as_dx_manager()
        self.pages.user_list_page.open()
        user = self.dx_constant.user_by_role['campaign_manager']['user_name']
        self.pages.user_list_page.filter_user(user.split('@')[0])
        self.pages.user_list_page.go_to_link(user)
        self.pages.user_show_page.wait_till_visible(self.pages.user_show_page.first_assigned_organization_under_roles)
        agency_group = self.pages.user_show_page.get_content_text(self.pages.user_show_page.first_assigned_organization_under_roles)
        self.manage_organization.override_agency_group(agency_group.strip())
        self.pages.agency_group_list_page.open()
        self.pages.agency_group_list_page.go_to_agency_group(agency_group.strip())
        self.pages.agency_group_details_page.wait_till_visible(self.pages.agency_group_details_page.add_agency)
        agency_name = self.pages.agency_group_details_page.get_content_text([self.pages.agency_group_details_page.find_agency_name[0],
                                                               self.pages.agency_group_details_page.find_agency_name[1] % 'regression_agency_'])
        self.manage_organization.override_agency(agency_name.strip())
        self.pages.agency_group_details_page.go_to_link(agency_name)
        self.pages.agency_details_page.wait_till_visible(self.pages.agency_details_page.edit_details_button)
        advertiser_name = self.pages.agency_details_page.get_content_text([self.pages.agency_details_page.get_advertiser_name_from_link[0],
                                                               self.pages.agency_details_page.get_advertiser_name_from_link[1] % 'regression_advertiser_'])
        self.manage_organization.override_advertiser(advertiser_name)
        print "Organization Updated Successfully..."

if __name__ == '__main__':
    update_file = UpdateDxConstantFile()
    update_file.update_organizations()
