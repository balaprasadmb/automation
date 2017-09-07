# -*- coding: utf-8 -*-
from campaign_edit import Tests
from selenium.webdriver.support.ui import WebDriverWait 
from python.setup import get_advertiser, get_campaign, get_uid
import driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium2Library import keywords
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

def test_1866():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.ctr(campaign, "Negative value")
        obj.assert_result("Goal ctr must be greater than or equal to 0")
    except Exception as exception:
        obj.screenshot("DXUITC-1866")
        raise exception
    
def test_1864():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.ctr(campaign, "Special Character")
        obj.assert_result("Goal ctr is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-1864")
        raise exception
    
def test_1869():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.ctr(campaign,"greater value than 100")
        obj.assert_result("Goal ctr must be less than or equal to 100")
    except Exception as exception:
        obj.screenshot("DXUITC-1869")
        raise exception
    
def test_1859():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.ctr(campaign,"empty")
        obj.assert_result(" Goal ctr is required to Maximize CTR")
    except Exception as exception:
        obj.screenshot("DXUITC-1859")
        raise exception
    
def test_1823():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.ctr(campaign,"contents")
    except Exception as exception:
        obj.screenshot("DXUITC-1823")
        raise exception    
    
def test_1855():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.ctr(campaign,"valid")
        #obj.assert_result(" Flight budget and schedule setup")
        #WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flight_name")))
        time.sleep(5)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        data = drivers.find_element_by_id("campaign_goal_ctr").get_attribute("value")
        assert data == "20.0"
    except Exception as exception:
        obj.screenshot("DXUITC-1855")
        raise exception
     
