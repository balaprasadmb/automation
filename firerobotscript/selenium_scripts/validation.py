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
from selenium.webdriver.common.keys import Keys


def test_2256():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        media_plan = "test-media-" + str(uid)
        obj.driver.find_element_by_id("drop1").click()
        advertiser = get_advertiser()
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        obj.driver.find_element_by_link_text("New Media Plan").click()
        obj.driver.find_element_by_id("media_plan_name").send_keys(media_plan)
        obj.driver.find_element_by_id("media_plan_project_plan_budget").send_keys("ASD")
        obj.driver.find_element_by_id("media_plan_submit").click()
        time.sleep(2)
        obj.assert_result(" Project plan budget is not a number")
        obj.driver.find_element_by_id("media_plan_project_plan_budget").clear()
        obj.driver.find_element_by_id("media_plan_project_plan_budget").send_keys("@#$#")
        obj.driver.find_element_by_id("media_plan_submit").click()
        time.sleep(2)
        obj.assert_result(" Project plan budget is not a number")
        obj.driver.find_element_by_id("media_plan_project_plan_budget").clear()
        obj.driver.find_element_by_id("media_plan_project_plan_budget").send_keys("AW32")
        obj.driver.find_element_by_id("media_plan_submit").click()
        time.sleep(2)
        obj.assert_result(" Project plan budget is not a number")
        obj.driver.find_element_by_id("media_plan_project_plan_budget").clear()
        obj.driver.find_element_by_id("media_plan_project_plan_budget").send_keys("45")
        obj.driver.find_element_by_id("media_plan_submit").click()
        time.sleep(2)
        obj.assert_result(" Successfully created media plan.")
    except Exception as exception:
        obj.screenshot("DXUITC-2256")
        raise exception

def test_2277():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        media_plan = "test-media-" + str(uid)
        obj.driver.find_element_by_id("drop1").click()
        advertiser = get_advertiser()
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        obj.driver.find_element_by_link_text("New Media Plan").click()
        obj.driver.find_element_by_id("media_plan_name").send_keys(media_plan)
        obj.driver.find_element_by_id("media_plan_project_plan_budget").send_keys("45")
        obj.driver.find_element_by_css_selector(".add").click()
        obj.driver.find_element_by_css_selector("input[id $= '_filter']").send_keys("40")
        obj.driver.find_element_by_css_selector("input[id $='_value']").send_keys("QWe")
        obj.driver.find_element_by_id("media_plan_submit").click()
        time.sleep(2)
        message = drivers.find_element_by_css_selector(".flash.error").text
        assert "Media plan activities value is not a number" in message
        obj.driver.find_element_by_css_selector(".add").click()
        obj.driver.find_element_by_css_selector("input[id $= '_filter']").send_keys("40")
        obj.driver.find_element_by_css_selector("input[id $='_value']").send_keys("@#$")
        obj.driver.find_element_by_id("media_plan_submit").click()
        time.sleep(2)
        message = drivers.find_element_by_css_selector(".flash.error").text
        assert "Media plan activities value is not a number" in message
        obj.driver.find_element_by_css_selector(".add").click()
        obj.driver.find_element_by_css_selector("input[id $= '_filter']").send_keys("40")
        obj.driver.find_element_by_css_selector("input[id $='_value']").send_keys("23SD")
        obj.driver.find_element_by_id("media_plan_submit").click()
        time.sleep(2)
        message = drivers.find_element_by_css_selector(".flash.error").text
        assert "Media plan activities value is not a number" in message
        obj.driver.find_element_by_css_selector(".add").click()
        obj.driver.find_element_by_css_selector("input[id $= '_filter']").send_keys("40")
        obj.driver.find_element_by_css_selector("input[id $='_value']").send_keys("20")
        obj.driver.find_element_by_id("media_plan_submit").click()
        time.sleep(2)
        obj.assert_result("Successfully created media plan.")
    except Exception as exception:
        obj.screenshot("DXUITC-2277")
        raise exception  
    
def test_2278():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        media_plan = "test-media-" + str(uid)
        obj.driver.find_element_by_id("drop1").click()
        advertiser = get_advertiser()
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        obj.driver.find_element_by_link_text("New Media Plan").click()
        obj.driver.find_element_by_id("media_plan_name").send_keys(media_plan)
        obj.driver.find_element_by_id("media_plan_start_at").clear()
        obj.driver.find_element_by_id("media_plan_start_at").send_keys("01/05/2015")
        obj.driver.find_element_by_id("media_plan_end_at").clear()
        obj.driver.find_element_by_id("media_plan_end_at").send_keys("2015/05/01")
        obj.driver.find_element_by_id("media_plan_submit").click()
        msg="Start at must be after or equal to "+ get_todaysdate() +" 00:00:00 -0400"
        obj.driver.find_element_by_id("media_plan_start_at").clear()
        obj.driver.find_element_by_id("media_plan_start_at").send_keys("2015/01/12")
        obj.driver.find_element_by_id("media_plan_submit").click()
        obj.assert_result(msg)
    except Exception as exception:
        obj.screenshot("DXUITC-2278")
        raise exception      
    
def test_2279():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        media_plan = "test-media-" + str(uid)
        obj.driver.find_element_by_id("drop1").click()
        advertiser = get_advertiser()
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        obj.driver.find_element_by_link_text("New Media Plan").click()
        obj.driver.find_element_by_id("media_plan_name").send_keys(media_plan)
        obj.driver.find_element_by_id("media_plan_start_at").clear()
        obj.driver.find_element_by_id("media_plan_start_at").send_keys(obj.one_day())
        obj.driver.find_element_by_id("media_plan_end_at").clear()
        obj.driver.find_element_by_id("media_plan_end_at").send_keys("01/06/2015")
        obj.driver.find_element_by_id("media_plan_project_plan_budget").send_keys("45")
        obj.driver.find_element_by_id("media_plan_submit").click()
        msg="End at must be after or equal to "+ get_todaysdate() +" 00:00:00 -0400"
        obj.driver.find_element_by_id("media_plan_end_at").clear()
        obj.driver.find_element_by_id("media_plan_end_at").send_keys("2015/01/12")
        obj.driver.find_element_by_id("media_plan_submit").click()
        obj.assert_result(msg)
    except Exception as exception:
        obj.screenshot("DXUITC-2279")
        raise exception 
    
def test_4462():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_id("drop1").click()
        advertiser = get_advertiser()
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        obj.driver.find_element_by_link_text("New Media Plan").click()
        obj.driver.find_element_by_id("media_plan_name").send_keys("Test Media")
        obj.driver.find_element_by_id("media_plan_start_at").clear()
        obj.driver.find_element_by_id("media_plan_start_at").send_keys(obj.one_day())
        obj.driver.find_element_by_id("media_plan_end_at").send_keys("04/17/201415")
        obj.driver.find_element_by_id("media_plan_submit").click()
    except Exception as exception:
        obj.screenshot("DXUITC-4462")
        raise exception   
    
# login("https://stg-ui-app05.sldc.dataxu.net/user_session/new?locale=en", "dx_admin@dataxu.com", "P@22w0rd")
# test_2279()               
