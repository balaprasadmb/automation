# -*- coding: utf-8 -*-
from campaign_edit import Tests#,login 
from python.setup import get_uid,get_advertiser
import driver
import time

def test_1751():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        drivers.find_element_by_id("campaign_objective_Performance").click()
        obj.assert_result("Attribution Model")
        obj.assert_result("Last Click")
        obj.assert_result("Last View")
        obj.assert_result("Activity Pixel")
        obj.assert_result("Pixel Type")
        obj.assert_result("Learning Pixel")
        obj.assert_result("Conversion Pixel")
        obj.assert_result("Filters")
        obj.assert_result("3rd Party Tag Server")
        obj.assert_result("DFA")
        obj.assert_result("Delete")
        obj.assert_result("Add row")
    except Exception as exception:
        obj.screenshot("DXUITC-1751")
        raise exception

def test_1756():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.performance(campaign)
        obj.assert_result("Flight budget and schedule setup")
        obj.edit_campaign(campaign)
        time.sleep(10)
        obj.assert_result("Maximize Performance & Distribution")
    except Exception as exception:
        obj.screenshot("DXUITC-1756")
        raise exception
    
def test_1760():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.performance(campaign,"Invalid Tag Id")
        obj.assert_result("Campaign activities activity third party server id external must be all digits")
    except Exception as exception:
        obj.screenshot("DXUITC-1760")
        raise exception

def test_1772():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.performance(campaign,"Blank Tag Id")
        obj.assert_result("Campaign activities activity third party server id external can't be blank")
    except Exception as exception:
        obj.screenshot("DXUITC-1772")
        raise exception

def test_1774():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.performance(campaign,"Invalid Tag Id")
        obj.assert_result("Campaign activities activity third party server id external must be all digits")
    except Exception as exception:
        obj.screenshot("DXUITC-1774")
        raise exception

def test_1779():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.performance(campaign,"Small Tag Id")
        obj.assert_result("Campaign activities activity third party server id external is too short (minimum is 6 characters)")
    except Exception as exception:
        obj.screenshot("DXUITC-1779")
        raise exception

def test_1790():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.performance(campaign,"Negative Tag Id")
        obj.assert_result("Campaign activities activity third party server id external must be all digits")
    except Exception as exception:
        obj.screenshot("DXUITC-1790")
        raise exception

def test_1814():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.performance(campaign,"Negative Activity")
        obj.assert_result("Campaign activities user value must be greater than or equal to 0")
    except Exception as exception:
        obj.screenshot("DXUITC-1814")
        raise exception

def test_1817():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.performance(campaign,"Activity Limit")
        obj.assert_result("Flight budget and schedule setup")
    except Exception as exception:
        obj.screenshot("DXUITC-1817")
        raise exception

def test_1804():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.performance(campaign,"Tag Id limit")
        obj.assert_result("Flight budget and schedule setup")
    except Exception as exception:
        obj.screenshot("DXUITC-1804")
        raise exception

def test_1820():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.performance(campaign,"Tag Id limit")
        obj.assert_result("Flight budget and schedule setup")
    except Exception as exception:
        obj.screenshot("DXUITC-1820")
        raise exception

#login("https://stg-ui-app05.sldc.dataxu.net/user_session/new?locale=en", "dx_admin@dataxu.com", "P@22w0rd")
#test_1751()
#test_1756()
#test_1760()