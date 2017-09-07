# -*- coding: utf-8 -*-
from campaign_edit import Tests
from selenium.webdriver.support.ui import WebDriverWait 
from python.setup import get_advertiser, get_campaign, get_uid, get_todaysdate
import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium2Library import keywords
from selenium.webdriver.support.ui import Select
import time

def test_4617():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.driver.find_element_by_css_selector(".bulk_pixel_assignment_dialog.lnkbtn.add")
    except Exception as exception:
        obj.screenshot("DXUITC-4617")
        raise exception
    
def test_4618():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector(".bulk_pixel_assignment_dialog.lnkbtn.add").click()
        obj.driver.find_element_by_css_selector("#ui-dialog-title-bulk_pixel_assignment")
        obj.driver.find_element_by_css_selector("#value")
        obj.driver.find_element_by_css_selector("#filter")
        obj.driver.find_element_by_css_selector(".ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only.ui-button-disabled.ui-state-disabled")
    except Exception as exception:
        obj.screenshot("DXUITC-4618")
        raise exception
 
def test_4619():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector(".bulk_pixel_assignment_dialog.lnkbtn.add").click()
        obj.driver.find_element_by_css_selector("#value")
        obj.driver.find_element_by_css_selector("#filter")
        obj.driver.find_element_by_css_selector("#bulk_available_activities>option").click()
        obj.driver.find_element_by_css_selector("#value").click()
        opt_list = ["Learning Pixel", "Conversion Pixel"]
        select = Select(drivers.find_element_by_css_selector("#value"))
        for opt in select.options:
            assert opt.text in opt_list
    except Exception as exception:
        obj.screenshot("DXUITC-4619")
        raise exception 
    
def test_4620():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector(".bulk_pixel_assignment_dialog.lnkbtn.add").click()
        obj.driver.find_element_by_css_selector("#value")
        obj.driver.find_element_by_css_selector("#filter")
        obj.driver.find_element_by_css_selector("#bulk_available_activities>option").click()
        obj.driver.find_element_by_css_selector("#value").click()
        obj.select_from_list_by_label(By.ID, "value", "Learning Pixel")
        assert obj.is_element_present(By.CSS_SELECTOR, "div[class='user_value'][style='display: block;'] >input[id='user_value']") is False,"Text box not present"
    except Exception as exception:
        obj.screenshot("DXUITC-4620")
        raise exception         
    
def test_4621():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label(By.ID, "value", "Conversion Pixel")
        obj.driver.find_element_by_css_selector("#user_value")
        obj.driver.find_element_by_css_selector("#ui-dialog-title-bulk_pixel_assignment ~a").click()
    except Exception as exception:
        obj.screenshot("DXUITC-4621")
        raise exception 
    
def test_4622():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        obj.driver.find_element_by_css_selector(".bulk_pixel_assignment_dialog.lnkbtn.add").click()
        obj.driver.find_element_by_css_selector("#bulk_available_activities>option").click()
        obj.driver.find_element_by_css_selector("body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.modal-dialog.ui-draggable.ui-resizable > .ui-dialog-buttonpane > button > span").click()
        obj.driver.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#campaign_campaign_activities_attributes_0_value"))
        for o in select.options:
            assert o.text != "Learning Pixel "
    except Exception as exception:
        obj.screenshot("DXUITC-4622")
        raise exception  
    
def test_4623():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        obj.driver.find_element_by_css_selector(".bulk_pixel_assignment_dialog.lnkbtn.add").click()
        obj.driver.find_element_by_css_selector("#bulk_available_activities>option").click()
        obj.select_from_list_by_label(By.ID, "value", "Conversion Pixel")
        obj.driver.find_element_by_css_selector("body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.modal-dialog.ui-draggable.ui-resizable > .ui-dialog-buttonpane > button > span").click()
        obj.driver.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        drivers.find_element_by_link_text(campaign).click()
        time.sleep(2)
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#campaign_campaign_activities_attributes_0_value"))
        for o in select.options:
            assert o.text != "Conversion Pixel "
    except Exception as exception:
        obj.screenshot("DXUITC-4623")
        raise exception
    
def test_4624():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector(".bulk_pixel_assignment_dialog.lnkbtn.add").click()
        obj.driver.find_element_by_id("bulk_available_search").send_keys("regression-activity") 
    except Exception as exception:
        obj.screenshot("DXUITC-4624")
        raise exception
    
def test_4625():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector(".bulk_pixel_assignment_dialog.lnkbtn.add").click()
        obj.driver.find_element_by_css_selector("#ui-dialog-title-bulk_pixel_assignment ~a").click() 
    except Exception as exception:
        obj.screenshot("DXUITC-4625")
        raise exception    
    
def test_4626():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        obj.driver.find_element_by_css_selector(".bulk_pixel_assignment_dialog.lnkbtn.add").click()
        obj.driver.find_element_by_css_selector("#value")
        obj.driver.find_element_by_css_selector("#filter")
        obj.driver.find_element_by_css_selector("#bulk_available_activities>option").click()
        obj.select_from_list_by_label(By.ID, "value", "Conversion Pixel")
        obj.driver.find_element_by_id("user_value").send_keys("ASD")
        obj.driver.find_element_by_css_selector("body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.modal-dialog.ui-draggable.ui-resizable > .ui-dialog-buttonpane > button > span").click()
        obj.driver.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        data = str(drivers.find_element_by_css_selector("input[id $= '_user_value']").get_attribute("placeholder"))
        assert data == "0.0"
    except Exception as exception:
        obj.screenshot("DXUITC-4626")
        raise exception 
    
def test_4627():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        obj.driver.find_element_by_css_selector(".bulk_pixel_assignment_dialog.lnkbtn.add").click()
        obj.driver.find_element_by_css_selector("#value")
        obj.driver.find_element_by_css_selector("#filter")
        obj.driver.find_element_by_css_selector("#bulk_available_activities>option").click()
        obj.select_from_list_by_label(By.ID, "value", "Conversion Pixel")
        obj.driver.find_element_by_id("user_value").send_keys("@#$")
        obj.driver.find_element_by_css_selector("body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.modal-dialog.ui-draggable.ui-resizable > .ui-dialog-buttonpane > button > span").click()
        obj.driver.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        data = str(drivers.find_element_by_css_selector("input[id $= '_user_value']").get_attribute("placeholder"))
        assert data == "0.0"
    except Exception as exception:
        obj.screenshot("DXUITC-4627")
        raise exception           
  
