# -*- coding: utf-8 -*-
from campaign_edit import Tests
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from python.setup import get_advertiser, get_campaign, get_uid
import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium2Library import keywords
import time
from selenium.webdriver.common.alert import Alert

def test_467(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        uid = get_uid()
        agency_group = "regress_agency_" + str(uid)
        contact_name = "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567891234567891012"
        drivers.find_element_by_link_text("Admin").click()
        drivers.find_element_by_link_text("Agency Groups").click()
        drivers.find_element_by_link_text("New Agency Group").click()
        obj.agency_group_detail(agency_group, file_path, criteria="valid_email", contact=contact_name)
        obj.assert_result('Organization contact name is too long (maximum is 255 characters)')
    except Exception as exception:
        obj.screenshot("DXUITC-467")
        raise exception

def test_469(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        contact_name = "!@#$!"
        drivers.find_element_by_id("agency_group_rate_card").send_keys(file_path)
        drivers.find_element_by_id("agency_group_organization_attributes_contact_name").clear()
        drivers.find_element_by_id("agency_group_organization_attributes_contact_name").send_keys(contact_name)
        drivers.find_element_by_id("agency_group_submit").click()
        obj.assert_result('Organization contact name cannot contain special characters')
    except Exception as exception:
        obj.screenshot("DXUITC-469")
        raise exception

def test_1301(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        drivers.find_element_by_id("agency_group_rate_card").send_keys(file_path)
        drivers.find_element_by_id("agency_group_organization_attributes_contact_name").clear()
        drivers.find_element_by_id("agency_group_organization_attributes_contact_name").send_keys("<html><body><h1>Test</h1></body></html>")
        drivers.find_element_by_id("agency_group_submit").click()
        obj.assert_result('Organization contact name cannot contain special characters')
    except Exception as exception:
        obj.screenshot("DXUITC-1301")
        raise exception

def test_465(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        contact_name = "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345674125639"
        agency_group = drivers.find_element_by_id("agency_group_name").get_attribute("value")
        drivers.find_element_by_id("agency_group_organization_attributes_contact_name").clear()
        drivers.find_element_by_id("agency_group_organization_attributes_contact_name").send_keys(contact_name)
        drivers.find_element_by_id("agency_group_rate_card").send_keys(file_path)
        drivers.find_element_by_id("agency_group_submit").click()
        obj.assert_result('Agency group "{0}" was successfully created.'.format(agency_group))
    except Exception as exception:
        obj.screenshot("DXUITC-465")
        raise exception

def test_468(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        uid = get_uid()
        agency_group = "regress_agency_" + str(uid)
        drivers.find_element_by_link_text("Admin").click()
        drivers.find_element_by_link_text("Agency Groups").click()
        drivers.find_element_by_link_text("New Agency Group").click()
        obj.agency_group_detail(agency_group, file_path, criteria="255", contact="")
        obj.assert_result('Agency group "{0}" was successfully created.'.format(agency_group))
    except Exception as exception:
        obj.screenshot("DXUITC-468")
        raise exception

def test_481(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        uid = get_uid()
        agency_group = "regress_agency_" + str(uid)
        drivers.find_element_by_link_text("Admin").click()
        drivers.find_element_by_link_text("Agency Groups").click()
        drivers.find_element_by_link_text("New Agency Group").click()
        obj.agency_group_detail(agency_group, file_path, criteria="255", contact="123456")
        obj.assert_result('Agency group "{0}" was successfully created.'.format(agency_group))
    except Exception as exception:
        obj.screenshot("DXUITC-481")
        raise exception