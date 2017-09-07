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

def test_1090():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        widget = drivers.find_element_by_css_selector("#geo_targeting")
        hover = ActionChains(drivers).move_to_element(widget)
        hover.perform()
        hover = ActionChains(drivers).move_to_element(widget).click()
        hover.perform()
        data = drivers.find_element_by_css_selector("#geo_target_type").get_attribute("value")
        assert data == "tbc", data
        drivers.find_element_by_css_selector("#country__available_search")
        drivers.find_element_by_css_selector("#country_countries_all")
        drivers.find_element_by_css_selector("#country_countries_selected")
    except Exception as exception:
        obj.screenshot("DXUITC-1090")
        raise exception

def test_1095():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        data = drivers.find_element_by_css_selector("#geo_target_type").get_attribute("value")
        assert data == "tbc", data
        obj.select_from_list_by_index(By.ID, "country_countries_all", 0)
        data = drivers.find_element_by_css_selector("#country_countries_all").get_attribute("value")
        drivers.find_element_by_css_selector("#mv_sel_country_countries").click()
        obj.select_from_list_by_value(By.ID, "country_countries_selected", data)
        obj.select_from_list_by_index(By.ID, "country_countries_selected", 0)
        drivers.find_element_by_css_selector("#rm_all_sel_country_countries").click()
        obj.select_from_list_by_index(By.ID, "country_countries_all", 0)
        obj.select_from_list_by_index(By.ID, "country_countries_all", 1)
        drivers.find_element_by_css_selector("#mv_all_sel_country_countries").click()
        obj.select_from_list_by_value(By.ID, "country_countries_selected", data)
        drivers.find_element_by_css_selector("#rm_sel_country_countries").click()
        drivers.find_element_by_css_selector("#rm_all_sel_country_countries").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1095")
        raise exception

def test_1101():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        obj.new_online_campaign()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(3)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#country_countries_selected"))
        for o in select.options:
            assert o.text != "United States "
    except Exception as exception:
        obj.screenshot("DXUITC-1101")
        raise exception

def test_1105():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        obj.new_online_campaign()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.ID, "country_countries_selected", "United States")
        drivers.find_element_by_id("rm_sel_country_countries").click()
        obj.select_from_list_by_label(By.ID, "country_countries_all", "Brazil")
        drivers.find_element_by_id("mv_sel_country_countries").click()
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(3)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#country_countries_selected"))
        for o in select.options:
            assert o.text != "Brazil "
    except Exception as exception:
        obj.screenshot("DXUITC-1105")
        raise exception
    
def test_1107():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        obj.new_online_campaign()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.ID, "country_countries_selected", "United States")
        drivers.find_element_by_id("rm_sel_country_countries").click()
        obj.select_from_list_by_label(By.ID, "country_countries_all", "Canada")
        drivers.find_element_by_id("mv_sel_country_countries").click()
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(3)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#country_countries_selected"))
        for o in select.options:
            assert o.text != "Canada "
    except Exception as exception:
        obj.screenshot("DXUITC-1107")
        raise exception 
    
def test_1108():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        obj.new_online_campaign()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.ID, "country_countries_selected", "United States")
        drivers.find_element_by_id("rm_sel_country_countries").click()
        obj.select_from_list_by_label(By.ID, "country_countries_all", "France")
        drivers.find_element_by_id("mv_sel_country_countries").click()
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(3)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#country_countries_selected"))
        for o in select.options:
            assert o.text != "France "
    except Exception as exception:
        obj.screenshot("DXUITC-1108")
        raise exception   
    
    
def test_1111():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        obj.new_online_campaign()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.ID, "country_countries_selected", "United States")
        drivers.find_element_by_id("rm_sel_country_countries").click()
        obj.select_from_list_by_label(By.ID, "country_countries_all", "Germany")
        drivers.find_element_by_id("mv_sel_country_countries").click()
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(3)
        drivers.find_element_by_link_text(campaign).click()
        time.sleep(3)
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#country_countries_selected"))
        for o in select.options:
            assert o.text != "Germany "
    except Exception as exception:
        obj.screenshot("DXUITC-1111")
        raise exception 
    
def test_1116():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        obj.new_online_campaign()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.ID, "country_countries_selected", "United States")
        drivers.find_element_by_id("rm_sel_country_countries").click()
        obj.select_from_list_by_label(By.ID, "country_countries_all", "Great Britain")
        drivers.find_element_by_id("mv_sel_country_countries").click()
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(3)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#country_countries_selected"))
        for o in select.options:
            assert o.text != "Great Britain "
    except Exception as exception:
        obj.screenshot("DXUITC-1116")
        raise exception   
    
def test_1117():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        obj.new_online_campaign()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.ID, "country_countries_selected", "United States")
        drivers.find_element_by_id("rm_sel_country_countries").click()
        obj.select_from_list_by_label(By.ID, "country_countries_all", "Ireland")
        drivers.find_element_by_id("mv_sel_country_countries").click()
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(3)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#country_countries_selected"))
        for o in select.options:
            assert o.text != "Ireland "
    except Exception as exception:
        obj.screenshot("DXUITC-1117")
        raise exception    

def test_1118():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        obj.new_online_campaign()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.ID, "country_countries_selected", "United States")
        drivers.find_element_by_id("rm_sel_country_countries").click()
        obj.select_from_list_by_label(By.ID, "country_countries_all", "Ireland")
        drivers.find_element_by_id("mv_sel_country_countries").click()
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(3)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#country_countries_selected"))
        for o in select.options:
            assert o.text != "Ireland "
    except Exception as exception:
        obj.screenshot("DXUITC-1118")
        raise exception    

def test_1124():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        obj.new_online_campaign()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.ID, "country_countries_selected", "United States")
        drivers.find_element_by_id("rm_sel_country_countries").click()
        obj.select_from_list_by_label(By.ID, "country_countries_all", "Poland")
        drivers.find_element_by_id("mv_sel_country_countries").click()
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(3)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#country_countries_selected"))
        for o in select.options:
            assert o.text != "Poland "
    except Exception as exception:
        obj.screenshot("DXUITC-1124")
        raise exception  
    
def test_1127():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        uid = get_uid()
        obj.new_online_campaign()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_info(campaign)
        drivers.find_element_by_id("campaign_objective_Distribution").click()
        obj.select_from_list_by_label(By.ID, "country_countries_selected", "United States")
        drivers.find_element_by_id("rm_sel_country_countries").click()
        obj.select_from_list_by_label(By.ID, "country_countries_all", "Spain")
        drivers.find_element_by_id("mv_sel_country_countries").click()
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(3)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        select = Select(drivers.find_element_by_css_selector("#country_countries_selected"))
        for o in select.options:
            assert o.text != "Spain "
    except Exception as exception:
        obj.screenshot("DXUITC-1127")
        raise exception  

def test_1150():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        drivers.find_element_by_id("country__available_search").send_keys("Canada")
        obj.select_from_list_by_label(By.ID, "country_countries_all", "Canada")
        drivers.find_element_by_id("country__available_search").send_keys("invalid")
        data = drivers.find_element_by_css_selector("#country_countries_all").get_attribute("value")
        assert data ==""
    except Exception as exception:
        obj.screenshot("DXUITC-1150")
        raise exception

def test_1134():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        drivers.find_element_by_id("campaign_geo_target_country_id")
        drivers.find_element_by_id("campaign_geo_target_area_type")
        drivers.find_element_by_css_selector("#campaign_regions_input > div.cols3 > span > .dualselect_available_search")
        drivers.find_element_by_css_selector("#campaign_regions_input > div.dualselect_available >select")
        drivers.find_element_by_css_selector("#campaign_regions_input > div.dualselect_applied >select")
    except Exception as exception:
        obj.screenshot("DXUITC-1134")
        raise exception

def test_1140():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "United States")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "New York")
    except Exception as exception:
        obj.screenshot("DXUITC-1140")
        raise exception

def test_1165():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Brazil")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "Acre")
    except Exception as exception:
        obj.screenshot("DXUITC-1165")
        raise exception

def test_1169():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Canada")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "Alberta")
    except Exception as exception:
        obj.screenshot("DXUITC-1169")
        raise exception

def test_1172():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "France")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "Alsace")
    except Exception as exception:
        obj.screenshot("DXUITC-1172")
        raise exception

def test_1173():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Germany")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "Bayern")
    except Exception as exception:
        obj.screenshot("DXUITC-1173")
        raise exception

def test_1174():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Great Britain")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "Angus")
    except Exception as exception:
        obj.screenshot("DXUITC-1174")
        raise exception

def test_1175():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Ireland")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "Cavan")
    except Exception as exception:
        obj.screenshot("DXUITC-1175")
        raise exception

def test_1176():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Italy")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "Abruzzi")
    except Exception as exception:
        obj.screenshot("DXUITC-1176")
        raise exception

def test_1177():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Poland")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "Slaskie")
    except Exception as exception:
        obj.screenshot("DXUITC-1177")
        raise exception

def test_1179():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_index(By.ID, "geo_target_type", 2)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Spain")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "Aragon")
    except Exception as exception:
        obj.screenshot("DXUITC-1179")
        raise exception

def test_1182():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "United States")
        drivers.find_element_by_css_selector("#campaign_regions_input > div.cols3 > span > .dualselect_available_search").send_keys("New York")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_regions_input > div.dualselect_available >select", "New York")
        drivers.find_element_by_css_selector("#campaign_regions_input > div.cols3 > span > .dualselect_available_search").clear()
        drivers.find_element_by_css_selector("#campaign_regions_input > div.cols3 > span > .dualselect_available_search").send_keys("invalid")
        data = drivers.find_element_by_css_selector("#campaign_regions_input > div.dualselect_available >select").get_attribute("value")
        assert data == ""
    except Exception as exception:
        obj.screenshot("DXUITC-1182")
        raise exception

def test_1296():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label(By.ID, "campaign_geo_target_area_type", "Metrocodes")
        drivers.find_element_by_css_selector("#campaign_dmas_input > div.cols3 > span.search_controls > .dualselect_available_search")
        drivers.find_element_by_css_selector("#campaign_dmas_input > div.dualselect_available >select")
        drivers.find_element_by_css_selector("#campaign_dmas_input > div.dualselect_applied >select")
    except Exception as exception:
        obj.screenshot("DXUITC-1296")
        raise exception

def test_1299():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label(By.ID, "campaign_geo_target_area_type", "Metrocodes")
        drivers.find_element_by_css_selector("#campaign_dmas_input > div.cols3 > span.search_controls > .dualselect_available_search")
        drivers.find_element_by_css_selector("#campaign_dmas_input > div.dualselect_available >select")
        obj.select_from_list_by_label(By.CSS_SELECTOR, "#campaign_dmas_input > div.dualselect_available >select", "501 New York NY")
    except Exception as exception:
        obj.screenshot("DXUITC-1299")
        raise exception

def test_1313():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Brazil")
        select = Select(drivers.find_element_by_css_selector("#campaign_geo_target_area_type"))
        for o in select.options:
            assert o.text != "Metrocodes", "Brazil doesn't contain Metrocode option but it contains. "
    except Exception as exception:
        obj.screenshot("DXUITC-1313")
        raise exception

def test_1315():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Canada")
        select = Select(drivers.find_element_by_css_selector("#campaign_geo_target_area_type"))
        for o in select.options:
            assert o.text != "Metrocodes", "Canada doesn't contain Metrocode option but it contains. "
    except Exception as exception:
        obj.screenshot("DXUITC-1315")
        raise exception

def test_1316():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "France")
        select = Select(drivers.find_element_by_css_selector("#campaign_geo_target_area_type"))
        for o in select.options:
            assert o.text != "Metrocodes", "France doesn't contain Metrocode option but it contains. "
    except Exception as exception:
        obj.screenshot("DXUITC-1316")
        raise exception

def test_1317():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Germany")
        select = Select(drivers.find_element_by_css_selector("#campaign_geo_target_area_type"))
        for o in select.options:
            assert o.text != "Metrocodes", "Germany doesn't contain Metrocode option but it contains. "
    except Exception as exception:
        obj.screenshot("DXUITC-1317")
        raise exception

def test_1318():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Great Britain")
        select = Select(drivers.find_element_by_css_selector("#campaign_geo_target_area_type"))
        for o in select.options:
            assert o.text != "Metrocodes", "Great Britain doesn't contain Metrocode option but it contains. "
    except Exception as exception:
        obj.screenshot("DXUITC-1318")
        raise exception

def test_1319():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Ireland")
        select = Select(drivers.find_element_by_css_selector("#campaign_geo_target_area_type"))
        for o in select.options:
            assert o.text != "Metrocodes", "Ireland doesn't contain Metrocode option but it contains. "
    except Exception as exception:
        obj.screenshot("DXUITC-1319")
        raise exception

def test_1320():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Italy")
        select = Select(drivers.find_element_by_css_selector("#campaign_geo_target_area_type"))
        for o in select.options:
            assert o.text != "Metrocodes", "Italy doesn't contain Metrocode option but it contains. "
    except Exception as exception:
        obj.screenshot("DXUITC-1320")
        raise exception

def test_1321():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Poland")
        select = Select(drivers.find_element_by_css_selector("#campaign_geo_target_area_type"))
        for o in select.options:
            assert o.text != "Metrocodes", "Poland doesn't contain Metrocode option but it contains. "
    except Exception as exception:
        obj.screenshot("DXUITC-1321")
        raise exception

def test_1322():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "Spain")
        select = Select(drivers.find_element_by_css_selector("#campaign_geo_target_area_type"))
        for o in select.options:
            assert o.text != "Metrocodes", "Spain doesn't contain Metrocode option but it contains. "
    except Exception as exception:
        obj.screenshot("DXUITC-1322")
        raise exception

def test_1258():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.select_from_list_by_label( By.ID, "campaign_geo_target_country_id", "United States")
        obj.select_from_list_by_label(By.ID, "campaign_geo_target_area_type", "Postal Codes")
        drivers.find_element_by_css_selector("#campaign_postal_code_groups_input > div.cols3 > span.search_controls > .dualselect_available_search")
        drivers.find_element_by_css_selector("#campaign_postal_code_groups_input > div.dualselect_available >select")
        drivers.find_element_by_css_selector("#campaign_postal_code_groups_input > div.dualselect_applied >select")
        drivers.find_element_by_css_selector(".file_label")
        drivers.find_element_by_css_selector("#postal_code_group_name")
        drivers.find_element_by_css_selector(".postal_code_group_upload_submit")
    except Exception as exception:
        obj.screenshot("DXUITC-1258")
        raise exception
