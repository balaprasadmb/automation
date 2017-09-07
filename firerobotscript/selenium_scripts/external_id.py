# -*- coding: utf-8 -*-
from campaign_edit import Tests
from python.setup import get_advertiser, get_campaign, get_uid
import driver
from selenium.webdriver.common.by import By

import time

def test_978():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        drivers.find_element_by_css_selector("#external_ids>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "RMX")
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "DFA")
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "Atlas")
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "BlueKai")
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "WURFL")
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "MediaMind")
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "Facebook")
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "Facebook Campaign")
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "Facebook Page Post Ad")
        drivers.find_element_by_id("campaign_external_ids_attributes_new_external_id_external_id").send_keys("14")
        drivers.find_element_by_css_selector(".remove_external_id")
    except Exception as exception:
        obj.screenshot("DXUITC-978")
        raise exception

def test_1006():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "RMX")
        drivers.find_element_by_id("campaign_submit").click()
        obj.flights_details("test-flight", criteria="Exit")
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols1").text
        assert data == "RMX"
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols2").text
        assert data == "14"
    except Exception as exception:
        obj.screenshot("DXUITC-1006")
        raise exception

def test_1018():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#external_ids>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "Atlas")
        drivers.find_element_by_id("campaign_external_ids_attributes_new_external_id_external_id").send_keys("14")
        drivers.find_element_by_id("campaign_submit").click()
        obj.flights_details("test-flight", criteria="Exit")
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols1").text
        assert data == "Atlas"
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols2").text
        assert data == "14"
    except Exception as exception:
        obj.screenshot("DXUITC-1018")
        raise exception

def test_1020():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#external_ids>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "WURFL")
        drivers.find_element_by_id("campaign_external_ids_attributes_new_external_id_external_id").send_keys("14")
        drivers.find_element_by_id("campaign_submit").click()
        obj.flights_details("test-flight", criteria="Exit")
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols1").text
        assert data == "WURFL"
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols2").text
        assert data == "14"
    except Exception as exception:
        obj.screenshot("DXUITC-1020")
        raise exception

def test_1023():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#external_ids>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "BlueKai")
        drivers.find_element_by_id("campaign_external_ids_attributes_new_external_id_external_id").send_keys("14")
        drivers.find_element_by_id("campaign_submit").click()
        obj.flights_details("test-flight", criteria="Exit")
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols1").text
        assert data == "BlueKai"
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols2").text
        assert data == "14"
    except Exception as exception:
        obj.screenshot("DXUITC-1023")
        raise exception

def test_1024():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#external_ids>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "MediaMind")
        drivers.find_element_by_id("campaign_external_ids_attributes_new_external_id_external_id").send_keys("14")
        drivers.find_element_by_id("campaign_submit").click()
        obj.flights_details("test-flight", criteria="Exit")
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols1").text
        assert data == "MediaMind"
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols2").text
        assert data == "14"
    except Exception as exception:
        obj.screenshot("DXUITC-1024")
        raise exception

def test_1025():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#external_ids>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "Facebook")
        drivers.find_element_by_id("campaign_external_ids_attributes_new_external_id_external_id").send_keys("14")
        drivers.find_element_by_id("campaign_submit").click()
        obj.flights_details("test-flight", criteria="Exit")
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols1").text
        assert data == "Facebook"
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols2").text
        assert data == "14"
    except Exception as exception:
        obj.screenshot("DXUITC-1025")
        raise exception

def test_1026():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#external_ids>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "Facebook Campaign")
        drivers.find_element_by_id("campaign_external_ids_attributes_new_external_id_external_id").send_keys("14")
        drivers.find_element_by_id("campaign_submit").click()
        obj.flights_details("test-flight", criteria="Exit")
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols1").text
        assert data == "Facebook Campaign"
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols2").text
        assert data == "14"
    except Exception as exception:
        obj.screenshot("DXUITC-1026")
        raise exception

def test_1028():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#external_ids>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "Facebook Page Post Ad")
        drivers.find_element_by_id("campaign_external_ids_attributes_new_external_id_external_id").send_keys("14")
        drivers.find_element_by_id("campaign_submit").click()
        obj.flights_details("test-flight", criteria="Exit")
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols1").text
        assert data == "Facebook Page Post Ad"
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols2").text
        assert data == "14"
    except Exception as exception:
        obj.screenshot("DXUITC-1028")
        raise exception

def test_1029():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#external_ids>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "RMX")
        drivers.find_element_by_id("campaign_submit").click()
        obj.flights_details("test-flight", criteria="Exit")
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols1").text
        assert data == "RMX"
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols2").text
        assert data == ""
    except Exception as exception:
        obj.screenshot("DXUITC-1029")
        raise exception

def test_1066():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        drivers.find_element_by_link_text("Edit").click()
        obj.select_from_list_by_label(By.CSS_SELECTOR, "select[id$='_source']", "Atlas")
        drivers.find_element_by_css_selector("input[name$='[external_id]']").send_keys("15")
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols1").text
        assert data == "Atlas"
        data = drivers.find_element_by_css_selector("#container3 > .push_group.divider > div:nth-child(5) > .cols2").text
        assert data == "15"
    except Exception as exception:
        obj.screenshot("DXUITC-1066")
        raise exception

def test_1069():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#external_ids>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "RMX")
        drivers.find_element_by_css_selector(".remove_external_id").click()
        list = drivers.find_elements_by_css_selector("#campaign_external_ids_attributes_new_external_id_source")
        assert len(list) == 0
    except Exception as exception:
        obj.screenshot("DXUITC-1069")
        raise exception

def test_1072():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        drivers.find_element_by_id("new_external_id").click()
        obj.select_from_list_by_label(By.ID, "campaign_external_ids_attributes_new_external_id_source", "RMX")
        list = drivers.find_elements_by_css_selector("#campaign_external_ids_attributes_new_external_id_source")
        assert len(list) > 0
    except Exception as exception:
        obj.screenshot("DXUITC-1072")
        raise exception
