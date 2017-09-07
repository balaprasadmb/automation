from campaign_edit import Tests#,login
from python.setup import get_uid,get_campaign,get_advertiser,get_flight
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import driver

def test_1500():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".add.button.new_campaign_top")))
        advertiser = get_advertiser()
        drivers.find_element_by_link_text("New Campaign").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#ui-dialog-title-dataxu_dialog")))
        WebDriverWait(drivers, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#advertiser")))
        drivers.find_element_by_id("advertiser").send_keys(advertiser)
        obj.assert_result("Online")
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1500")
        raise exception

def test_1502():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".add.button.new_campaign_top")))
        advertiser = get_advertiser()
        drivers.find_element_by_link_text("New Campaign").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#ui-dialog-title-dataxu_dialog")))
        WebDriverWait(drivers, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#advertiser")))
        drivers.find_element_by_id("advertiser").send_keys(advertiser)
        obj.assert_result("Mobile")
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1500")
        raise exception

def test_1504():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".add.button.new_campaign_top")))
        advertiser = get_advertiser()
        drivers.find_element_by_link_text("New Campaign").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#ui-dialog-title-dataxu_dialog")))
        WebDriverWait(drivers, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#advertiser")))
        drivers.find_element_by_id("advertiser").send_keys(advertiser)
        obj.assert_result("Video")
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1500")
        raise exception

def test_1506():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".add.button.new_campaign_top")))
        advertiser = get_advertiser()
        drivers.find_element_by_link_text("New Campaign").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#ui-dialog-title-dataxu_dialog")))
        WebDriverWait(drivers, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#advertiser")))
        drivers.find_element_by_id("advertiser").send_keys(advertiser)
        obj.assert_result("Online")
        obj.assert_result("Mobile")
        obj.assert_result("Video")
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1500")
        raise exception

# login("https://stg-ui-app10.sldc.dataxu.net/user_session/new?locale=en", "dx_admin@dataxu.com", "P@22w0rd")
# test_1500()
# test_1502()
# test_1504()
# test_1506()