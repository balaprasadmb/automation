from campaign_edit import Tests
from selenium.webdriver.support.ui import WebDriverWait 
from python.setup import get_uid
import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def test_1559():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        drivers.find_element_by_css_selector("#campaign_end_date ~ .ui-datepicker-trigger").click()
        obj.wait_until(By.CSS_SELECTOR,"#ui-datepicker-div")
        assert obj.is_element_present(By.CSS_SELECTOR,"#ui-datepicker-div") is True
    except Exception as exception:
        obj.screenshot("DXUITC-1559")
        raise exception

def test_1560_1561():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        flight = "test-flight" + str(uid)
        obj.campaign_details(campaign, "Valid")
        obj.flights_details(flight, criteria="Exit")
        obj.wait_until(By.LINK_TEXT, "Export Flights")
        time.sleep(5)
        obj.assert_result("Campaign: {0}".format(campaign))
        obj.assert_result("{0} to {1}".format(obj.start_date(), obj.end_date()))
    except Exception as exception:
        obj.screenshot("DXUITC-1560_1561")
        raise exception

def test_1562():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        flight = "test-flight" + str(uid)
        obj.campaign_details(campaign, "Past End Date")
        obj.assert_result("End date cannot have an end date prior to the start date")
    except Exception as exception:
        obj.screenshot("DXUITC-1562")
        raise exception

def test_1563():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_details(campaign, "End date prior")
        obj.assert_result("End date cannot have an end date prior to the start date")
    except Exception as exception:
        obj.screenshot("DXUITC-1563")
        raise exception

def test_1564():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.campaign_details(campaign, "Blank end date")
        obj.assert_result("End date can't be blank")
    except Exception as exception:
        obj.screenshot("DXUITC-1564")
        raise exception
         