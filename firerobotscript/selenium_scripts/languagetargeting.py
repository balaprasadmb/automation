# -*- coding: utf-8 -*-
from campaign_edit import Tests
from selenium.webdriver.support.ui import WebDriverWait
from python.setup import get_advertiser, get_campaign, get_uid
import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium2Library import keywords
from selenium.webdriver.support.ui import Select
import time

def test_1080():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        obj.driver.find_element_by_id("campaign_objective_Distribution").click()
        data = drivers.find_element_by_css_selector("#language_targeting > .section_header.contain_cols9 > h1 > div ~ div").text
        assert data == "Optional, none set"
        obj.driver.find_element_by_css_selector("#language_targeting > .section_header.contain_cols9 > h1 > .section_title.cols4 > span").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1080")
        raise exception

def test_1088():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "target_languages_all", 0)
        data = drivers.find_element_by_css_selector("#target_languages_all").get_attribute("value")
        drivers.find_element_by_css_selector("#mv_sel_target_languages").click()
        obj.select_from_list_by_value(By.ID, "target_languages_selected", data)
        obj.select_from_list_by_index(By.ID, "target_languages_selected", 0)
        drivers.find_element_by_css_selector("#rm_sel_target_languages").click()
        obj.select_from_list_by_index(By.ID, "target_languages_all", 0)
        obj.select_from_list_by_index(By.ID, "target_languages_all", 1)
        drivers.find_element_by_css_selector("#mv_all_sel_target_languages").click()
        obj.select_from_list_by_value(By.ID, "target_languages_selected", data)
        drivers.find_element_by_css_selector("#rm_all_sel_target_languages").click()
        #drivers.find_element_by_css_selector("#rm_all_sel_country_countries").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1088")
        raise exception

def test_1149():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        obj.driver.find_element_by_id("campaign_objective_Distribution").click()
        obj.driver.find_element_by_css_selector("#language_targeting > .section_header.contain_cols9 > h1 > .section_title.cols4 > span").click()
        obj.select_from_list_by_label(By.ID, "target_languages_all", "English")
        data = drivers.find_element_by_css_selector("#target_languages_all").get_attribute("value")
        drivers.find_element_by_css_selector("#mv_sel_target_languages").click()
        obj.driver.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        drivers.find_element_by_link_text(campaign).click()
        drivers.find_element_by_link_text("Edit").click()
        obj.select_from_list_by_label(By.ID, "target_languages_selected", "English")
        drivers.find_element_by_css_selector("#rm_sel_target_languages").click()
        obj.select_from_list_by_label(By.ID, "target_languages_all", "Spanish")
        drivers.find_element_by_css_selector("#mv_sel_target_languages").click()
        obj.driver.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        #drivers.find_element_by_link_text(campaign).click()
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#target_languages_selected"))
        for o in select.options:
            assert o.text != "Spanish "
    except Exception as exception:
        obj.screenshot("DXUITC-1149")
        raise exception

# login("https://stg-ui-app05.sldc.dataxu.net/user_session/new?locale=en", "dx_admin@dataxu.com", "P@22w0rd")
# test_1128()
