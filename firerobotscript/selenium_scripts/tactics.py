# -*- coding: utf-8 -*-
from campaign_edit import Tests 
from python.setup import get_uid,get_advertiser
import driver
from selenium.webdriver.support.ui import Select
import time

def test_966():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.assert_result("Tactics")
        obj.assert_result("Optional, one \"Default\" tactic")
    except Exception as exception:
        obj.screenshot("DXUITC-966")
        raise exception

def test_979():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.enable_hidden("tactics")
        obj.assert_result("Tactic name")
        obj.assert_result("Budget")
        obj.assert_result("Impression Cap")
        obj.assert_result("Add a Tactic")
        drivers.find_element_by_id("add_new_tactic").click()
        obj.assert_result("Delete")
    except Exception as exception:
        obj.screenshot("DXUITC-979")
        raise exception

def test_984():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)        
        obj.assert_result("Retargeting")
        obj.assert_result("Optimized")
        obj.assert_result("GeoTargeting")
        obj.assert_result("Channel")
        obj.assert_result("Custom...")
    except Exception as exception:
        obj.screenshot("DXUITC-984")
        raise exception

def test_987():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "custom field appear")
    except Exception as exception:
        obj.screenshot("DXUITC-987")
        raise exception

def test_995():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "blank")
        obj.assert_result("Tactics name can't be blank")
    except Exception as exception:
        obj.screenshot("DXUITC-995")
        raise exception

def test_1067():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "overflow")
        obj.assert_result("Tactics name is too long (maximum is 255 characters)")
    except Exception as exception:
        obj.screenshot("DXUITC-1067")
        raise exception

def test_996():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "valid")
        obj.assert_result("Flight budget and schedule setup")
    except Exception as exception:
        obj.screenshot("DXUITC-996")
        raise exception

def test_1068():
    try:
        time.sleep(10)
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "characters")
        obj.assert_result('Flight budget and schedule setup')
    except Exception as exception:
        obj.screenshot("DXUITC-1068")
        raise exception

def test_1071():
    try:
        time.sleep(10)
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "numbers")
        obj.assert_result('Flight budget and schedule setup')
    except Exception as exception:
        obj.screenshot("DXUITC-1071")
        raise exception

def test_1073():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "special chars")
        #obj.assert_result("The basic campaign information for {0} » {1} was created successfully.".format(get_advertiser(), campaign))
        obj.assert_result('Flight budget and schedule setup')
    except Exception as exception:
        obj.screenshot("DXUITC-1073")
        raise exception

def test_1004():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        select = Select(drivers.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
        select.select_by_visible_text("Custom...")
        obj.assert_result("Custom...")
        drivers.find_element_by_id("add_new_tactic").click()
        obj.assert_result("Retargeting")
        drivers.find_element_by_id("add_new_tactic").click()
        obj.assert_result("Optimized")
        drivers.find_element_by_id("add_new_tactic").click()
        obj.assert_result("GeoTargeting")
        drivers.find_element_by_id("add_new_tactic").click()
        obj.assert_result("Channel")
        drivers.find_element_by_id("add_new_tactic").click()
        obj.assert_result("Custom...")
    except Exception as exception:
        obj.screenshot("DXUITC-1004")
        raise exception

def test_1017():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign)
        obj.assert_result('Flight budget and schedule setup')
        obj.assert_result('Default')
    except Exception as exception:
        obj.screenshot("DXUITC-1017")
        raise exception

def test_1052():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "Retargeting")
        time.sleep(10)
        obj.assert_result('Flight budget and schedule setup')
        obj.assert_result('Default')
        obj.assert_result('Retargeting')
    except Exception as exception:
        obj.screenshot("DXUITC-1052")
        raise exception

def test_1054():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "Optimized")
        time.sleep(10)
        obj.assert_result('Flight budget and schedule setup')
        obj.assert_result('Optimized')
    except Exception as exception:
        obj.screenshot("DXUITC-1054")
        raise exception

def test_1056():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "Channel")
        time.sleep(10)
        obj.assert_result('Flight budget and schedule setup')
        obj.assert_result('Channel')
    except Exception as exception:
        obj.screenshot("DXUITC-1056")
        raise exception

def test_1057():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        tactic=obj.tactics(campaign, "Custom...")
        time.sleep(10)
        obj.assert_result('Flight budget and schedule setup')
        obj.assert_result('Default')
        obj.assert_result(tactic)
    except Exception as exception:
        obj.screenshot("DXUITC-1057")
        raise exception

def test_1075():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "valid budget")
        time.sleep(10)
        obj.assert_result('Flight budget and schedule setup')
    except Exception as exception:
        obj.screenshot("DXUITC-1075")
        raise exception

def test_1076():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid() 
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "invalid budget")
        obj.assert_result("Tactics budget is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-1076")
        raise exception

def test_1078():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "valid impression")
        time.sleep(10)
        obj.assert_result('Flight budget and schedule setup')
    except Exception as exception:
        obj.screenshot("DXUITC-1078")
        raise exception

def test_1079():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid() 
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "invalid impression")
        obj.assert_result("Tactics impression cap is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-1079")
        raise exception

def test_1084():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("tactics")
        drivers.find_element_by_id("add_new_tactic").click()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.tactics(campaign, "Retargeting")
        time.sleep(10)
        obj.assert_result('Flight budget and schedule setup')
        obj.assert_result('Default')
        obj.assert_result('Retargeting')
        obj.edit_campaign(campaign)
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(10)
        #drivers.find_element_by_css_selector("#tactics_content>div:nth-child(3)>input").click()
        drivers.find_element_by_id("add_new_tactic").click()
        select = Select(drivers.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
        select.select_by_visible_text("Optimized")
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(10)
        obj.assert_result('Campaign \''+campaign+'\' was successfully updated.')
    except Exception as exception:
        obj.screenshot("DXUITC-1084")
        raise exception