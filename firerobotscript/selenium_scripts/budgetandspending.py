# -*- coding: utf-8 -*-
from campaign_edit import Tests
from selenium.webdriver.support.ui import WebDriverWait 
from python.setup import get_uid, get_advertiser
import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

def test_887():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        select = Select(drivers.find_element(By.ID,"campaign_campaign_cost_model_type_id"))
        option = select.first_selected_option
        value  = option.get_attribute('value')
        assert value == "2"
        drivers.find_element_by_id("campaign_cog_attributes_cpa_goal")
        drivers.find_element_by_id("campaign_cog_attributes_insertion_order_budget")
        drivers.find_element_by_id("campaign_cog_attributes_cpm")
        drivers.find_element_by_id("campaign_cog_attributes_cogs")
        drivers.find_element_by_id("campaign_cog_attributes_margin")
    except Exception as exception:
        obj.screenshot("DXUITC-887")
        raise exception

def test_888():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        select = Select(drivers.find_element(By.ID,"campaign_campaign_cost_model_type_id"))
        option = select.first_selected_option
        value  = option.get_attribute('value')
        assert value == "2"
        select.select_by_visible_text("CPA")
    except Exception as exception:
        obj.screenshot("DXUITC-888")
        raise exception
    
def test_889():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        select = Select(drivers.find_element(By.ID,"campaign_campaign_cost_model_type_id"))
        obj.assert_result("CPA ($)")
        obj.assert_result("Budget ($)")
        obj.assert_result("CPM ($)")
        obj.assert_result("COGS ($)")
    except Exception as exception:
        obj.screenshot("DXUITC-888")
        raise exception
    
def test_890():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.budgetandspending(campaign, "empty")
        obj.assert_result("Cog cpa goal is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-890")
        raise exception

def test_891():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.budgetandspending(campaign, "InvalidCPA")
        obj.assert_result("Cog cpa goal must be less than or equal to 10000")
        #obj.budgetandspending(campaign, "ValidCPA")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("10000")
        obj.driver.find_element_by_id("campaign_submit").click()  
        time.sleep(05)
        #WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input.ember-view.ember-text-field.flight_name.text")))
        #obj.assert_result("The basic campaign information for {0} » {1} was created successfully.".format(advertiser, campaign))
        obj.assert_result("Flight budget and schedule setup")
    except Exception as exception:
        obj.screenshot("DXUITC-891")
        raise exception
    
def test_892():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        #WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_campaign_cost_model_type_id")))
        obj.budgetandspending(campaign, "InvalidBudget ($)")
        obj.assert_result("IO Budget must be less than or equal to 500,000")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").send_keys("0")
        obj.driver.find_element_by_id("campaign_submit").click()
        #obj.assert_result("The basic campaign information for {0} » {1} was created successfully.".format(advertiser, campaign))
        time.sleep(05)
        obj.assert_result("Flight budget and schedule setup")
    except Exception as exception:
        obj.screenshot("DXUITC-892")
        raise exception  

def test_893():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_campaign_cost_model_type_id")))
        obj.budgetandspending(campaign, "BlankBudget ($)")
        obj.assert_result("IO Budget is not a number")  
    except Exception as exception:
        obj.screenshot("DXUITC-893")
        raise exception 
        
def test_894():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_campaign_cost_model_type_id")))
        obj.budgetandspending(campaign, "BlankCPM ($)")
        obj.assert_result("Cog cpm is not a number")   
    except Exception as exception:
        obj.screenshot("DXUITC-894")
        raise exception 
    
def test_895():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        #WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_campaign_cost_model_type_id")))
        obj.budgetandspending(campaign, "InvalidCPM")
        obj.assert_result("Cog cpm must be less than or equal to 100")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("0")
        obj.driver.find_element_by_id("campaign_submit").click() 
        obj.assert_result("Cog cpm must be greater than or equal to 0.01")  
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("30")
        obj.driver.find_element_by_id("campaign_submit").click()
        time.sleep(05)
        #obj.assert_result("The basic campaign information for {0} » {1} was created successfully.".format(advertiser, campaign))
        obj.assert_result("Flight budget and schedule setup")   
    except Exception as exception:
        obj.screenshot("DXUITC-895")
        raise exception  
    
def test_896():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.budgetandspending(campaign, "BlankCOGS")
        time.sleep(2)
        obj.assert_result("Cog cogs is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-896")
        raise exception 
    
def test_898():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cogs").send_keys("05")
        obj.driver.find_element_by_id("campaign_submit").click()
        time.sleep(05)
        #WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input.ember-view.ember-text-field.flight_name.text")))
        #obj.assert_result("The basic campaign information for {0} » {1} was created successfully.".format(advertiser, campaign))
        obj.assert_result("Flight budget and schedule setup")
    except Exception as exception:
        obj.screenshot("DXUITC-898")
        raise exception  
       
def test_899():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_campaign_cost_model_type_id")))
        obj.budgetandspending(campaign, "BlankMargin")
        obj.assert_result("Cog margin is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-899")
        raise exception  
    
def test_900():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_campaign_cost_model_type_id")))
        obj.budgetandspending(campaign, "InvalidMargin")
        obj.assert_result("Cog margin must be less than 100")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_margin").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_margin").send_keys("30")
        obj.driver.find_element_by_id("campaign_submit").click()
        time.sleep(05)
        obj.assert_result("Flight budget and schedule setup")
    except Exception as exception:
        obj.screenshot("DXUITC-900")
        raise exception 
    
def test_924():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#campaign_campaign_cost_model_type_id")))
        obj.budgetandspending(campaign, "CPAcharacter")
        obj.assert_result("Cog cpa goal is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-924")
        raise exception  
    
def test_926():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.budgetandspending(campaign, "CPAcharacter")
        obj.assert_result("Cog cpa goal is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-926")
        raise exception  
    
def test_929():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("10")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").send_keys("ABC")
        obj.driver.find_element_by_id("campaign_submit").click()
        obj.assert_result("IO Budget is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-929")
        raise exception                                      
    
def test_930():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").send_keys("10")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cogs").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cogs").send_keys("ASD")
        obj.driver.find_element_by_id("campaign_submit").click()
        obj.assert_result("Cog cogs is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-930")
        raise exception 
    
def test_935():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cogs").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cogs").send_keys("10")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("@#$")
        obj.driver.find_element_by_id("campaign_submit").click()
        obj.assert_result(" Cog cpa goal is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-935")
        raise exception 
    
def test_936():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("5")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").send_keys("@#$")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("5")
        obj.driver.find_element_by_id("campaign_submit").click()
        obj.assert_result(" IO Budget is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-936")
        raise exception 
    
def test_937():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").send_keys("10")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("@#$")
        obj.driver.find_element_by_id("campaign_submit").click()
        obj.assert_result(" Cog cpm is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-937")
        raise exception  
    
def test_938():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("5")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cogs").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cogs").send_keys("#$%")
        obj.driver.find_element_by_id("campaign_submit").click()
        obj.assert_result(" Cog cogs is not a number")
    except Exception as exception:
        obj.screenshot("DXUITC-938")
        raise exception 

def test_1192():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        #remove
        obj.new_online_campaign()
        advertiser = get_advertiser()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.driver.find_element_by_css_selector("#campaign_name").clear()
        obj.driver.find_element_by_css_selector("#campaign_name").send_keys(campaign)
        #remove
        obj.driver.find_element_by_id("campaign_start_date").send_keys(obj.start_date())
        obj.driver.find_element_by_id("campaign_end_date").send_keys(obj.end_date())
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("5")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").send_keys("5")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("5")
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cogs").clear()
        obj.driver.find_element_by_css_selector("#campaign_cog_attributes_cogs").send_keys("5")
        obj.driver.find_element_by_id("campaign_objective_Distribution").click()
        obj.driver.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        drivers.find_element_by_link_text(campaign).click()
        WebDriverWait(drivers, 05).until(EC.visibility_of_element_located((By.LINK_TEXT, "Export Flights")))
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        data = drivers.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").get_attribute("value")
        assert data == "5.00"
        data = drivers.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").get_attribute("value")
        assert data == "5.00"
    except Exception as exception:
        obj.screenshot("DXUITC-1192")
        raise exception  
    
def test_1475():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.driver.find_element_by_link_text("Review COGS Margin history").click()
        data = drivers.find_element_by_css_selector("#ui-dialog-title-cog_margin_history").text
        assert data == "COG and Margin History" 
        obj.driver.find_element_by_css_selector("#ui-dialog-title-cog_margin_history ~ a").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1475")
        raise exception       
