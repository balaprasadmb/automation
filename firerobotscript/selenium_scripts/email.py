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


def test_351(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        uid = get_uid()
        agency_group = "regress_agency_" + str(uid)
        drivers.find_element_by_link_text("Admin").click()
        drivers.find_element_by_link_text("Agency Groups").click()
        drivers.find_element_by_link_text("New Agency Group").click()
        obj.agency_group_detail(agency_group, file_path, criteria="valid_email")
        obj.assert_result('Agency group "{0}" was successfully created.'.format(agency_group))
    except Exception as exception:
        obj.screenshot("DXUITC-351")
        raise exception

def test_354(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        uid = get_uid()
        agency_group = "regress_agency_" + str(uid)
        drivers.find_element_by_link_text("Admin").click()
        drivers.find_element_by_link_text("Agency Groups").click()
        drivers.find_element_by_link_text("New Agency Group").click()
        obj.agency_group_detail(agency_group, file_path, criteria="invalid_email")
        obj.assert_result('Organization email must be in a valid format.')
    except Exception as exception:
        obj.screenshot("DXUITC-354")
        raise exception
    
def test_437(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        email ="01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789@dataxu.com"
        drivers.find_element_by_id("agency_group_organization_attributes_email").clear()
        drivers.find_element_by_id("agency_group_organization_attributes_email").send_keys(email)
        drivers.find_element_by_id("agency_group_submit").click()
        obj.assert_result('Organization email is too long (maximum is 255 characters)')
    except Exception as exception:
        obj.screenshot("DXUITC-437")
        raise exception

def test_455(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        drivers.find_element_by_id("agency_group_organization_attributes_email").clear()
        drivers.find_element_by_id("agency_group_organization_attributes_email").send_keys("@dataxu.com")
        drivers.find_element_by_id("agency_group_submit").click()
        obj.assert_result('Organization email must be in a valid format.')
    except Exception as exception:
        obj.screenshot("DXUITC-455")
        raise exception

def test_457(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        drivers.find_element_by_id("agency_group_organization_attributes_email").clear()
        drivers.find_element_by_id("agency_group_organization_attributes_email").send_keys("test@")
        drivers.find_element_by_id("agency_group_submit").click()
        obj.assert_result('Organization email must be in a valid format.')
    except Exception as exception:
        obj.screenshot("DXUITC-457")
        raise exception

def test_1297(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        drivers.find_element_by_id("agency_group_organization_attributes_email").clear()
        drivers.find_element_by_id("agency_group_organization_attributes_email").send_keys("<html><body><h1>Test</h1></body></html>")
        drivers.find_element_by_id("agency_group_submit").click()
        obj.assert_result('Organization email cannot contain special characters')
        obj.assert_result("Organization email must be in a valid format.")
    except Exception as exception:
        obj.screenshot("DXUITC-1297")
        raise exception

def test_355(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        agency_group = drivers.find_element_by_id("agency_group_name").get_attribute("value")
        drivers.find_element_by_id("agency_group_organization_attributes_email").clear()
        drivers.find_element_by_id("agency_group_rate_card").send_keys(file_path)
        drivers.find_element_by_id("agency_group_submit").click()
        obj.assert_result('Agency group "{0}" was successfully created.'.format(agency_group))
    except Exception as exception:
        obj.screenshot("DXUITC-355")
        raise exception

def test_436(file_path):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        uid = get_uid()
        agency_group = "regress_agency_" + str(uid)
        drivers.find_element_by_link_text("Admin").click()
        drivers.find_element_by_link_text("Agency Groups").click()
        drivers.find_element_by_link_text("New Agency Group").click()
        obj.agency_group_detail(agency_group, file_path, criteria="255")
        obj.assert_result('Agency group "{0}" was successfully created.'.format(agency_group))
    except Exception as exception:
        obj.screenshot("DXUITC-436")
        raise exception
