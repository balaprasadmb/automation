# -*- coding: utf-8 -*-
from campaign_edit import Tests
from selenium.webdriver.support.ui import WebDriverWait 
from python.setup import get_advertiser, get_campaign, get_uid
import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium2Library import keywords

def test_85():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "DXAS-BANNER-01")
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys("1.333")
        drivers.find_element_by_id("campaign_submit").click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flight_name")))
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        WebDriverWait(drivers, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_name")))
        data = drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").get_attribute("value")
        assert data == "1.333"
    except Exception as exception:
        obj.screenshot("DXUITC-85")
        raise exception

def test_1377():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        drivers.find_element_by_link_text("View Change History").click()
        data = drivers.find_element_by_css_selector("div[class *='dialog-'][style*='display: block'][role='dialog'] > div.ui-dialog-titlebar ~ div> table > thead > tr > .campaigns_cog_history_date").text
        assert "Date" in data, data
        data = drivers.find_element_by_css_selector("div[class *='dialog-'][style*='display: block'][role='dialog'] > div.ui-dialog-titlebar ~ div> table > thead > tr > .cpm").text
        assert "CPM" in data, data
        data = drivers.find_element_by_css_selector("div[class *='dialog-'][style*='display: block'][role='dialog'] > div.ui-dialog-titlebar ~ div> table > thead > tr > .campaigns_cog_history_billable").text
        assert "Billable" in data, data
        data = drivers.find_element_by_css_selector("div[class *='dialog-'][style*='display: block'][role='dialog'] > div.ui-dialog-titlebar ~ div> table > thead > tr > .campaigns_cog_history_user").text
        assert "User" in data, data
        drivers.find_element_by_css_selector("div[class *='dialog-'][style*='display: block'][role='dialog'] > div.ui-dialog-titlebar > .ui-dialog-titlebar-close").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1377")
        raise exception

def test_1343():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "DXAS-BANNER-01")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']")
        drivers.find_element_by_link_text("View Change History")
        drivers.find_element_by_id("add_new_add_on_cost").click()
        drivers.find_element_by_css_selector(".group.aoc_row + .aoc_row")
    except Exception as exception:
        obj.screenshot("DXUITC-1343")
        raise exception
    
def test_1349():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "DXAS-BANNER-01")
        drivers.find_element_by_link_text("View Change History").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class *='dialog-'][style*='display: block'][role='dialog'] > div.ui-dialog-titlebar > span")))
        assert drivers.find_element_by_css_selector("div[class *='dialog-'][style*='display: block'][role='dialog'] > div.ui-dialog-titlebar > span").text == "Add On Cost History"
        drivers.find_element_by_css_selector("div[class *='dialog-'][style*='display: block'][role='dialog'] > div.ui-dialog-titlebar > .ui-dialog-titlebar-close").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1349")
        raise exception
    
def test_1421():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "DXAS-BANNER-01")
        drivers.find_element_by_css_selector('.remove_add_on_cost').click()
        list = drivers.find_elements_by_css_selector('#add_on_costs_content > .aoc_row')
        assert len(list) == 0
    except Exception as exception:
        obj.screenshot("DXUITC-1421")
        raise exception

def test_1389():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        obj.select_from_list_by_value(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys("7.5")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_fee_type > select", "CPM (USD)")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_is_billable > input ~ input").click()
        drivers.find_element_by_id("campaign_submit").click()
        obj.assert_result("Add on costs name can't be blank")
    except Exception as exception:
        obj.screenshot("DXUITC-1389")
        raise exception

def test_1397():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "Custom...")
        string = "01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").send_keys(string)
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys("7.5")
        drivers.find_element_by_id("campaign_submit").click()
        obj.assert_result("Add on costs name is too long (maximum is 255 characters)")
    except Exception as exception:
        obj.screenshot("DXUITC-1397")
        raise exception

def test_1395():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        drivers.find_element_by_id("campaign_name").clear()
        drivers.find_element_by_id("campaign_name").send_keys(campaign)
        string = "56789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "Custom...")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").clear()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").send_keys(string)
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys("1.333")
        drivers.find_element_by_id("campaign_submit").click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flight_name")))
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        WebDriverWait(drivers, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_name")))
        data = drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").get_attribute("value")
        assert data == string
    except Exception as exception:
        obj.screenshot("DXUITC-1395")
        raise exception

def test_1382():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "Custom...")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").clear()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").send_keys("test")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys("1.333")
        drivers.find_element_by_id("campaign_submit").click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flight_name")))
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        WebDriverWait(drivers, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_name")))
        data = drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").get_attribute("value")
        assert data == "test"
    except Exception as exception:
        obj.screenshot("DXUITC-1382")
        raise exception

def test_1399():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "Custom...")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").clear()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").send_keys("0123456789")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys("1.333")
        drivers.find_element_by_id("campaign_submit").click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flight_name")))
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        WebDriverWait(drivers, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_name")))
        data = drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").get_attribute("value")
        assert data == "0123456789"
    except Exception as exception:
        obj.screenshot("DXUITC-1382")
        raise exception

def test_1410():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "Custom...")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").clear()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").send_keys("test")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").clear()
        drivers.find_element_by_id("campaign_submit").click()
        obj.assert_result("Add on costs value is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-1410")
        raise exception

def test_1412():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        string = "01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "Custom...")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").clear()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").send_keys("test")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys(string)
        drivers.find_element_by_id("campaign_submit").click()
        obj.assert_result("Add on costs value Value must be less than or equal to 100 USD.")
    except Exception as exception:
        obj.screenshot("DXUITC-1412")
        raise exception

def test_1414():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        string = "12345qwe"
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "Custom...")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").clear()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").send_keys("test")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys(string)
        drivers.find_element_by_id("campaign_submit").click()
        obj.assert_result("Add on costs value is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-1414")
        raise exception

def test_1415():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        string = "!@#$"
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "Custom...")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").clear()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").send_keys("test")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys(string)
        drivers.find_element_by_id("campaign_submit").click()
        obj.assert_result("Add on costs value is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-1415")
        raise exception

def test_1417():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "Custom...")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").clear()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_name > li > input[id$='_name_custom']").send_keys("test")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys("-9")
        drivers.find_element_by_id("campaign_submit").click()
        obj.assert_result("Add on costs value must be greater than or equal to 0.0")
    except Exception as exception:
        obj.screenshot("DXUITC-1417")
        raise exception

def test_1400():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "DXAS-BANNER-01")
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys("1.3")
        drivers.find_element_by_id("campaign_submit").click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flight_name")))
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        WebDriverWait(drivers, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_name")))
        data = drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").get_attribute("value")
        assert data == "1.3"
    except Exception as exception:
        obj.screenshot("DXUITC-1400")
        raise exception

def test_1411():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "DXAS-BANNER-01")
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys("101")
        drivers.find_element_by_id("campaign_submit").click()
        obj.assert_result("Add on costs value Value must be less than or equal to 100 USD.")
    except Exception as exception:
        obj.screenshot("DXUITC-1411")
        raise exception

def test_1419():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.addoncost(campaign)
        obj.select_from_list_by_value(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_name > li > select[id$='_name']", "")
        drivers.find_element_by_css_selector("#add_on_costs_content > .aoc_row > .aoc_value > input[type='number']").send_keys("7.5")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#add_on_costs_content > .aoc_row > .aoc_fee_type > select", "CPM (USD)")
    except Exception as exception:
        obj.screenshot("DXUITC-1419")
        raise exception