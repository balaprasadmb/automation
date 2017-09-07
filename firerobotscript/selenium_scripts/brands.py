# -*- encoding: utf-8 -*-
from campaign_edit import Tests#,login 
from python.setup import get_uid,get_advertiser
from selenium.webdriver.support import expected_conditions as EC
import driver
import time

def test_1164():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.assert_result("Brand Safety")
        obj.assert_result("Defaults to Level 2")
        obj.enable_hidden("brand_safety")
        EC.element_to_be_selected(drivers.find_element_by_id("campaign_brand_safety_level_2"))
        obj.assert_result("Level One")
        obj.assert_result("Reach")
        obj.assert_result("Media Cost")
        obj.assert_result("Risk")
        obj.assert_result("Run your ads using the filtering provided by our exchange partners to get the greatest reach at low cost.  All exchanges provide some basic site categorization and filtering.")
        obj.assert_result("Level Two")
        obj.assert_result("Automatically exclude potentially offensive sites using")
        obj.assert_result("IAB quality guidelines")
        obj.assert_result(". This may include some uncategorized / unknown sites.")
        obj.assert_result("View or customize categories...")
        obj.assert_result("Level Three")
        obj.assert_result("Run only on sites which have been classified according to")
        obj.assert_result("IAB quality guidelines,")
        obj.assert_result(". This will exclude all uncategorized or potentially offensive sites.")
        obj.assert_result("View or customize categories...")
        obj.assert_result("Level Four")
        obj.assert_result("Upload a custom whitelist of sites for your campaign. Depending on your list, your reach and cost of media may be affected.")
    except Exception as exception:
        obj.screenshot("DXUITC-1164")
        raise exception

def test_1344():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.brands(campaign, "default")
        time.sleep(5)
        obj.assert_result('Flight budget and schedule setup')
        obj.edit_campaign(campaign)
        time.sleep(5)
        obj.assert_result("Brand Safety")
        obj.assert_result("Level Two")
    except Exception as exception:
        obj.screenshot("DXUITC-1344")
        raise exception

def test_1346():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.brands(campaign, "level1")
        time.sleep(5)
        obj.assert_result('Flight budget and schedule setup')
        obj.edit_campaign(campaign)
        time.sleep(5)
        obj.assert_result("Brand Safety")
        obj.assert_result("Level One")
    except Exception as exception:
        obj.screenshot("DXUITC-1346")
        raise exception

def test_1375():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.brands(campaign, "level3")
        time.sleep(5)
        obj.assert_result('Flight budget and schedule setup')
        obj.edit_campaign(campaign)
        time.sleep(5)
        obj.assert_result("Brand Safety")
        obj.assert_result("Level Three")
    except Exception as exception:
        obj.screenshot("DXUITC-1375")
        raise exception

def test_1376():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.brands(campaign, "level4")
        time.sleep(5)
        obj.assert_result('White list domains can\'t be blank')
    except Exception as exception:
        obj.screenshot("DXUITC-1376")
        raise exception

def test_1449():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.brands(campaign, "whitelist")
        time.sleep(5)
        obj.assert_result('White list domains can\'t be blank')
    except Exception as exception:
        obj.screenshot("DXUITC-1449")
        raise exception
