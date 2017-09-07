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
import os

def test_5172():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        widget = drivers.find_element_by_css_selector("#geo_targeting")
        hover = ActionChains(drivers).move_to_element(widget)
        hover.perform()
        hover = ActionChains(drivers).move_to_element(widget).click()
        hover.perform()
        obj.select_from_list_by_label(By.ID, "geo_target_type", "Target GeoFenced regions")
        obj.driver.find_element_by_id("geohash_groups_all")
        obj.driver.find_element_by_id("geohash_groups_selected")
    except Exception as exception:
        obj.screenshot("DXUITC-5172")
        raise exception
    
def test_5173():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        widget = drivers.find_element_by_css_selector("#geo_targeting")
        hover = ActionChains(drivers).move_to_element(widget)
        hover.perform()
        hover = ActionChains(drivers).move_to_element(widget).click()
        hover.perform()
        obj.select_from_list_by_label(By.ID, "geo_target_type", "Target GeoFenced regions")
        obj.driver.find_element_by_id("geohash_group_file").send_keys(os.path.dirname(__file__)+'/uploads/exports_3.csv')
        obj.driver.find_element_by_css_selector("#geohash_group_name").send_keys("01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789")
        obj.driver.find_element_by_id("campaign_geohash_submit").click()  
        time.sleep(2)
        obj.assert_result("Failure to upload GeoFence groups. Name is too long (maximum is 255 characters)")  
    except Exception as exception:
        obj.screenshot("DXUITC-5173")
        raise exception
    
def test_5174():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        widget = drivers.find_element_by_css_selector("#geo_targeting")
        hover = ActionChains(drivers).move_to_element(widget)
        hover.perform()
        hover = ActionChains(drivers).move_to_element(widget).click()
        hover.perform()
        obj.select_from_list_by_label(By.ID, "geo_target_type", "Target GeoFenced regions")
        obj.driver.find_element_by_id("geohash_group_file").send_keys(os.path.dirname(__file__)+'/uploads/exports_3.csv')
        obj.driver.find_element_by_css_selector("#geohash_group_name").send_keys("valid test")
        obj.driver.find_element_by_id("campaign_geohash_submit").click()  
        select = Select(drivers.find_element_by_css_selector("#geohash_groups_selected"))
        for o in select.options:
            assert o.text != "valid test " 
    except Exception as exception:        
        obj.screenshot("DXUITC-5174")
        raise exception  
    
def test_5175():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        widget = drivers.find_element_by_css_selector("#geo_targeting")
        hover = ActionChains(drivers).move_to_element(widget)
        hover.perform()
        hover = ActionChains(drivers).move_to_element(widget).click()
        hover.perform()
        obj.select_from_list_by_label(By.ID, "geo_target_type", "Target GeoFenced regions")
        obj.driver.find_element_by_id("geohash_group_file").send_keys(os.path.dirname(__file__)+'/uploads/exports_3.csv')
        obj.driver.find_element_by_css_selector("#geohash_group_name").send_keys("AS234")
        obj.driver.find_element_by_id("campaign_geohash_submit").click()  
        select = Select(drivers.find_element_by_css_selector("#geohash_groups_selected"))
        for o in select.options:
            assert o.text != "AS234 " 
    except Exception as exception:
        obj.screenshot("DXUITC-5175")
        raise exception

def test_5176():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        widget = drivers.find_element_by_css_selector("#geo_targeting")
        hover = ActionChains(drivers).move_to_element(widget)
        hover.perform()
        hover = ActionChains(drivers).move_to_element(widget).click()
        hover.perform()
        obj.select_from_list_by_label(By.ID, "geo_target_type", "Target GeoFenced regions")
        obj.driver.find_element_by_id("geohash_group_file").send_keys(os.path.dirname(__file__)+'/uploads/seleniumpython.xls')
        obj.driver.find_element_by_css_selector("#geohash_group_name").send_keys("AS234")
        obj.driver.find_element_by_id("campaign_geohash_submit").click()  
        time.sleep(2)
        message = drivers.find_element_by_css_selector(".upload_error_message").text
        assert message == "Failure to upload GeoFence groups. Unrecognized file type. Expected a CSV file."
    except Exception as exception:
        obj.screenshot("DXUITC-5176")
        raise exception            
    
# login("https://stg-ui-app05.sldc.dataxu.net/user_session/new?locale=en", "dx_admin@dataxu.com", "P@22w0rd")
# test_5176()    