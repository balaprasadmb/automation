import os
import csv
import time
import random, string
from lib.dx_date import DXDate
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from dx_test_helper.dx_test_helper import DXTestHelper
from configs.dx_constant import DXConstant
from advertiser_list import AdvertiserListPage
from advertiser_details import AdvertiserDetailsPage
from edit_advertiser import EditAdvertiser
from new_advertiser import NewAdvertiser
from agencies.agencies_list_page import AgenciesListPage
from agencies.agency_details import AgencyDetailsPage
from agencies.agency_edit import AgencyEdit
from agencies.new_agency import NewAgency
from new_advertiser import NewAdvertiser
from activity_list_page import ActivityListPage
from activity_create_new_page import ActivityCreateNewPage
from activity_edit_page import ActivityEditPage
from activity_show_page import ActivityShowPage
from page_object import PageObjects

class CommonHelper():

    def validate_result(self, result, criteria):
        expected_result = False if criteria == False else True
        assert result == expected_result, result

    def assert_is_element_present(self, page_object, loc, criteria=True):
        if type(loc) == list:
            actual_result = page_object.is_element_present(loc)
        else:
            actual_result = page_object.is_element_present(getattr(page_object, loc))
        self.validate_result(actual_result, criteria)

    def assert_is_selected(self, page_object, loc, criteria=True):
        if type(loc) == list:
            actual_result = page_object.find_element(loc).is_selected()
        else:
            actual_result = page_object.find_element(getattr(page_object, loc)).is_selected()
        self.validate_result(actual_result, criteria)

    def validate_add_on_cost(self, page_object, loc, add_on_cost_name, method='text'):
        flag = False
        if type(loc) == list:
            element_list = page_object.find_elements(loc)
        else:
            element_list = page_object.find_elements(getattr(page_object, loc))
        for element in element_list:
            if method == 'value':
                if add_on_cost_name == page_object.get_content_value(element):
                    flag = True
                    break
            else:
                if add_on_cost_name == page_object.get_content_text(element):
                    flag = True
                    break
        assert flag is True

    def read_csv_file(self, file_name):
        datalist = []
        with open(os.path.dirname(__file__)+ '/../../../../data/flights_upload/' + file_name + '.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            for reader in csvreader:
                datalist.append(reader)
            csvfile.close()
        return datalist

    def write_csv_file(self, file_name, data):
        csvfile = open(os.path.dirname(__file__)+ '/../../../../data/flights_upload/' + file_name + '.csv', 'wb')
        csvfile.write(data)
        csvfile.close()

    def process_flight_file_with_name_and_date(self, file_name, campaign_type, flight_payload='', advertiser_level = None):
        datalist = self.read_csv_file(file_name)
        data = ''
        for line in datalist[1:]:
            if line[0] != '':
                if campaign_type == 'Online' or campaign_type == 'Mobile':
                    line[0] = 'test-flight-' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) + flight_payload
                    line[7] = DXDate().date_after_two_days()
                    line[8] = DXDate().last_date_of_current_month()
                if campaign_type == 'Video' or campaign_type == 'Omni-Channel':
                    line[0] = 'test-flight-' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) + flight_payload
                    line[8] = DXDate().date_after_two_days()
                    line[9] = DXDate().last_date_of_current_month()
                if advertiser_level:
                    line[0] = campaign.campaign_attributes['campaign_name']
                    line[1] = 'test-flight-' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) + flight_payload
                    line[8] = campaign.campaign_attributes['start_date']
                    line[9] = campaign.campaign_attributes['end_date']
            data += '\n' + ",".join(line)
        self.write_csv_file(file_name, ",".join(datalist[0]) + data)

    def process_flight_file_with_domains(self, file_name, campaign_type, whitelist_name, blacklist_name):
        self.process_flight_file_with_name_and_date(file_name, campaign_type)
        datalist = self.read_csv_file(file_name)
        data = ''
        for line in datalist[1:]:
            if line[0] != '':
                if campaign_type == 'Online' or campaign_type == 'Mobile':
                    line[20] = whitelist_name
                    line[21] = blacklist_name
                if campaign_type == 'Video':
                    line[21] = whitelist_name
                    line[22] = blacklist_name
                if campaign_type == 'Omni-Channel':
                    line[22] = whitelist_name
                    line[23] = blacklist_name
            data += '\n' + ",".join(line)
        self.write_csv_file(file_name, ",".join(datalist[0]) + data)

    def get_flights_name_from_file(self, flight_speadsheet):
        flight_names = []
        with open(os.path.dirname(__file__)+ '/../../../../data/flights_upload/' + flight_speadsheet + '.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            first = False
            for reader in csvreader:
                if first:
                    flight_names.append(reader[0])
                first = True
            csvfile.close()
        return flight_names

    def logout_and_login_by_new_user(self, driver, role):
        self.pages = PageObjects(driver)
        self.pages.admin_page.click_on_dataxu_logo()
        self.pages.search_page.wait_till_visible(self.pages.search_page.search_box)
        self.pages.admin_page.go_to_link('Logout')
        time.sleep(6)
        if self.pages.sso_login_page.is_element_present(self.pages.sso_login_page.back_to_legacy_login_link):
            self.pages.sso_login_page.go_to_link('Back to legacy login')
        self.pages.login_page.wait_till_visible(self.pages.login_page.login_submit, 15)
        self.pages.login_page.type_email(DXConstant().user_by_role[role]['user_name'])
        self.pages.login_page.type_password((DXConstant().user_by_role[role]['user_password']).decode('base64', 'strict'))
        self.pages.login_page.submit()
        if self.pages.admin_page.is_element_present(self.pages.admin_page.system_message_popup):
            self.pages.admin_page.close_system_message()
