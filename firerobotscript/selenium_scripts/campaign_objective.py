# -*- coding: utf-8 -*-
from campaign_edit import Tests
from selenium.webdriver.support.ui import WebDriverWait 
from python.setup import get_advertiser, get_campaign, get_uid
import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium2Library import keywords
import time

def test_873():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        obj.select_from_list_by_value(By.ID, "campaign_performance_attribution_type_id", "1")
        obj.select_from_list_by_value(By.ID, "campaign_performance_attribution_type_id", "2")
        obj.select_from_list_by_index(By.CSS_SELECTOR, "select[id$='activity_id']", 1)
        drivers.find_element_by_link_text("Add row")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#first_campaign_activity_subform_fields  > ol > div:nth-child(2) > li > select", "Learning Pixel")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#first_campaign_activity_subform_fields  > ol > div:nth-child(2) > li > select", "Conversion Pixel")
        drivers.find_element_by_css_selector("#first_campaign_activity_subform_fields  > ol > div:nth-child(4) > li > textarea").send_keys("test")
        #obj.select_from_list_by_label(By.CSS_SELECTOR, "#first_campaign_activity_subform_fields  > ol > div:nth-child(6) > div > ol > li > select", "DFA")
        #drivers.find_element_by_css_selector("#first_campaign_activity_subform_fields  > ol > div:nth-child(6) > div ~ div > ol > li > input").send_keys("123456")
    except Exception as exception:
        obj.screenshot("DXUITC-873")
        raise exception

def test_874():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        flight = "test-flight"
        drivers.find_element_by_id("campaign_submit").click()
        obj.flights_details(flight)
        time.sleep(10)
        drivers.find_element_by_css_selector(".save_and_exit").click()
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(1) > .value").text
        assert data == "Maximize Performance & Distribution"
    except Exception as exception:
        obj.screenshot("DXUITC-874")
        raise exception

def test_875():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.ctr(campaign, criteria="valid")
        flight = "test-flight"
        obj.flights_details(flight)
        time.sleep(10)
        drivers.find_element_by_css_selector(".save_and_exit").click()
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(1) > .value").text
        assert data == "Maximize CTR"
    except Exception as exception:
        obj.screenshot("DXUITC-875")
        raise exception

def test_876():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        data = drivers.find_element_by_css_selector("#maximize_performance>strong>label").text
        assert data == "Maximize Performance and Distribution"
        data = drivers.find_element_by_css_selector("#maximize_distribution>strong>label").text
        assert data == "Maximize Distribution"
        data = drivers.find_element_by_css_selector("#maximize_ctr>strong>label").text
        assert data == "Maximize CTR"
    except Exception as exception:
        obj.screenshot("DXUITC-876")
        raise exception

def test_877():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_mobile_campaign()
        data = drivers.find_element_by_css_selector("#maximize_performance>strong>label").text
        assert data == "Maximize Performance and Distribution"
        data = drivers.find_element_by_css_selector("#maximize_distribution>strong>label").text
        assert data == "Maximize Distribution"
        data = drivers.find_element_by_css_selector("#maximize_ctr>strong>label").text
        assert data == "Maximize CTR"
        data = drivers.find_element_by_css_selector("#maximize_completed_views>strong>label").text
        assert data == "Maximize Completed Ad Views"
    except Exception as exception:
        obj.screenshot("DXUITC-877")
        raise exception

def test_878():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_video_campaign()
        data = drivers.find_element_by_css_selector("#maximize_performance>strong>label").text
        assert data == "Maximize Performance and Distribution"
        data = drivers.find_element_by_css_selector("#maximize_distribution>strong>label").text
        assert data == "Maximize Distribution"
        data = drivers.find_element_by_css_selector("#maximize_ctr>strong>label").text
        assert data == "Maximize CTR"
        data = drivers.find_element_by_css_selector("#maximize_completed_views>strong>label").text
        assert data == "Maximize Completed Ad Views"
    except Exception as exception:
        obj.screenshot("DXUITC-878")
        raise exception

def test_879():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_id("campaign_submit").click()
        flight = "test-flight"
        obj.flights_details(flight)
        time.sleep(10)
        drivers.find_element_by_css_selector(".save_and_exit").click()
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(1) > .value").text
        assert data == "Maximize Distribution"
    except Exception as exception:
        obj.screenshot("DXUITC-879")
        raise exception

def test_880():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Completed_Views").click()
        drivers.find_element_by_id("campaign_submit").click()
        flight = "test-flight"
        obj.flights_details(flight)
        time.sleep(10)
        drivers.find_element_by_css_selector(".save_and_exit").click()
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(1) > .value").text
        assert data == "Maximize Completed Ad Views"
    except Exception as exception:
        obj.screenshot("DXUITC-880")
        raise exception