# -*- coding: utf-8 -*-
from campaign_edit import Tests
from selenium.webdriver.support.ui import WebDriverWait 
from python.setup import get_advertiser, get_campaign, get_uid
import driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium2Library import keywords

def test_1543():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_details(campaign, "Blank start date")
        obj.assert_result("Start date can't be blank")
    except Exception as exception:
        obj.screenshot("DXUITC-1543")
        raise exception
   
def test_4461():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        drivers.find_element_by_css_selector("#campaign_start_date ~ .ui-datepicker-trigger").click()
        obj.wait_until(By.CSS_SELECTOR,"#ui-datepicker-div")
        assert obj.is_element_present(By.CSS_SELECTOR,"#ui-datepicker-div") is True, "Datepicker doesn't open"
        drivers.find_element_by_css_selector("#campaign_start_date ~ .ui-datepicker-trigger").click()
        time.sleep(5)
        drivers.find_element_by_css_selector("#campaign_start_date ~ .ui-datepicker-trigger").click()
        WebDriverWait(drivers, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#ui-datepicker-div")), "Datepicker is still visible")
    except Exception as exception:
        obj.screenshot("DXUITC-4461")
        raise exception
    
def test_1540():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        drivers.find_element_by_css_selector("#campaign_start_date ~ .ui-datepicker-trigger").click()
        obj.wait_until(By.CSS_SELECTOR,"#ui-datepicker-div")
        assert obj.is_element_present(By.CSS_SELECTOR,"#ui-datepicker-div") is True
    except Exception as exception:
        obj.screenshot("DXUITC-1540")
        raise exception    
        
def test_1528_1533():
    try:
        
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        #self.new_video_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        flight = "test-flight" + str(uid)
        obj.campaign_details(campaign, "Valid")
        obj.flights_details(flight, criteria="Exit")
        obj.wait_until(By.LINK_TEXT, "Export Flights")
        obj.assert_result("Campaign: {0}".format(campaign))
        obj.assert_result("{0} to {1}".format(obj.start_date(), obj.end_date()))
    except Exception as exception:
        obj.screenshot("DXUITC-1528_1533")
        raise exception
        
def test_1535():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        #obj.switch_to_view(view="Classic")
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        flight = "test-flight" + str(uid)
        obj.campaign_details(campaign, "Past Start Date")
        obj.flights_details(flight, criteria="Exit")
        obj.wait_until(By.LINK_TEXT, "Export Flights")
        obj.assert_result("Campaign: {0}".format(campaign))
    except Exception as exception:
        obj.screenshot("DXUITC-1535")
        raise exception

def test_1537():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_details(campaign, "Start date ahead")
        obj.assert_result("End date cannot have an end date prior to the start date")
    except Exception as exception:
        obj.screenshot("DXUITC-1537")
        raise exception
        
def test_1609():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        #obj.switch_to_view(view="Classic")
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_details(campaign, "Special character")
        #USER CANT SAVE DATE WITH SPECIAL CHARCTER
        obj.assert_result("End date cannot have an end date prior to the start date")
    except Exception as exception:
        obj.screenshot("DXUITC-1609")
        raise exception
     
#login("https://stg-ui-app05.sldc.dataxu.net/user_session/new?locale=en", "dx_admin@dataxu.com", "P@22w0rd")
#test_4461()