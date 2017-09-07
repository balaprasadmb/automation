# -*- encoding: utf-8 -*-
from campaign_edit import Tests
from python.setup import get_uid, get_advertiser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import driver
import time
import os

def test_1378():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("blacklist")
        EC.element_to_be_selected(drivers.find_element_by_id("domain_list"))
        obj.assert_result("campaign_black_list_domains_file")
        obj.assert_result("icon-information")
        obj.assert_result("campaign_black_list_domain")
    except Exception as exception:
        obj.screenshot("DXUITC-1378")
        raise exception

def test_1379():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("blacklist")
        obj.assert_result("campaign_white_list_domains_file")
        obj.assert_result("icon-information")
        obj.assert_result("campaign_white_list_domains")
    except Exception as exception:
        obj.screenshot("DXUITC-1379")
        raise exception

def test_1460():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("blacklist")
        obj.assert_result("The blacklist and whitelist apply to all campaign flights by default.")
        obj.assert_result("You can edit both lists on a per-flight basis later.")
    except Exception as exception:
        obj.screenshot("DXUITC-1460")
        raise exception

def test_1461():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        widget=drivers.find_element_by_css_selector("#whitelist>div>h1>div>div")
        hover=ActionChains(drivers)
        hover.move_to_element(widget)
        hover.perform()
        obj.assert_result("The blacklist and whitelist apply to all campaign flights by default.")
        obj.assert_result("You can edit both lists on a per-flight basis later.")
    except Exception as exception:
        obj.screenshot("DXUITC-1461")
        raise exception

def test_1381():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        if EC.visibility_of_element_located(drivers.find_element_by_id("whitelist"))==False:
            raise Exception
        drivers.find_element_by_id("campaign_brand_safety_level_1").click()
        if EC.invisibility_of_element_located(drivers.find_element_by_id("whitelist"))==False:
            raise Exception
        drivers.find_element_by_id("campaign_brand_safety_level_2").click()
        if EC.invisibility_of_element_located(drivers.find_element_by_id("whitelist"))==False:
            raise Exception
        drivers.find_element_by_id("campaign_brand_safety_level_3").click()
        if EC.invisibility_of_element_located(drivers.find_element_by_id("whitelist"))==False:
            raise Exception
    except Exception as exception:
        obj.screenshot("DXUITC-1381")
        raise exception

def test_1391():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "whitelist present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        drivers.find_element_by_css_selector("div.divider>div:nth-child(3)>p:nth-child(3)>a").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ui-dialog.ui-widget.ui-widget-content.ui-corner-all.dialog-500")))
        time.sleep(5)
        obj.assert_result("www.foobar.com")
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1391")
        raise exception

def test_1416():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "blacklist present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        drivers.find_element_by_css_selector("div.divider>div:nth-child(3)>p:nth-child(2)>a").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ui-dialog.ui-widget.ui-widget-content.ui-corner-all.dialog-500")))
        time.sleep(5)
        obj.assert_result("www.foobar.com")
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    except Exception as exception:
        obj.screenshot("DXUITC-1416")
        raise exception

def test_1384_1430():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "exported blacklist present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","exports_3.csv")
    except Exception as exception:
        obj.screenshot("DXUITC-1384-1430")
        raise exception

def test_1418_1453():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "exported whitelist present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","exports_3.csv")
    except Exception as exception:
        obj.screenshot("DXUITC-1418-1453")
        raise exception

def test_1423():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "blacklist blank")
        obj.assert_result("Black list domains can't be blank")
    except Exception as exception:
        obj.screenshot("DXUITC-1423")
        raise exception

def test_1448():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "whitelist blank")
        obj.assert_result("White list domains can't be blank")
    except Exception as exception:
        obj.screenshot("DXUITC-1448")
        raise exception

def test_1424():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "blacklist blank csv")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(5)
        obj.assert_result("0 domains")
    except Exception as exception:
        obj.screenshot("DXUITC-1424")
        raise exception

def test_1429():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "txt blacklist present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","domain_txt.txt")
    except Exception as exception:
        obj.screenshot("DXUITC-1429")
        raise exception

def test_1452():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "txt whitelist present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","domain_txt.txt")
    except Exception as exception:
        obj.screenshot("DXUITC-1452")
        raise exception

def test_1431():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "xls blacklist present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","domain_xls.xls")
    except Exception as exception:
        obj.screenshot("DXUITC-1431")
        raise exception

def test_1454():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "xls whitelist present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","domain_xls.xls")
    except Exception as exception:
        obj.screenshot("DXUITC-1454")
        raise exception

def test_1432():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "xlsx blacklist present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","domain_xlsx.xlsx")
    except Exception as exception:
        obj.screenshot("DXUITC-1431")
        raise exception

def test_1455():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "xlsx whitelist present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","domain_xlsx.xlsx")
    except Exception as exception:
        obj.screenshot("DXUITC-1454")
        raise exception

def test_1474():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "both list present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","domain_xlsx.xlsx")
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","domain_xlsx_black.xlsx")
    except Exception as exception:
        obj.screenshot("DXUITC-1474")
        raise exception

def test_1476():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "both list present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","domain_xlsx.xlsx")
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","domain_xlsx_black.xlsx")
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        drivers.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx_15.xlsx')
        drivers.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx_15.xlsx')
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        obj.assert_result("Campaign \'" + campaign + "\' was successfully updated.")
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","domain_xlsx_15.xlsx")
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","domain_xlsx_15.xlsx")
    except Exception as exception:
        obj.screenshot("DXUITC-1476")
        raise exception

def test_1477():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "updated list present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","domain_xlsx_15.xlsx")
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","domain_xlsx_15.xlsx")
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        drivers.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx.xlsx')
        drivers.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx_black.xlsx')
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        obj.assert_result("Campaign \'" + campaign + "\' was successfully updated.")
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","domain_xlsx.xlsx")
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","domain_xlsx_black.xlsx")
    except Exception as exception:
        obj.screenshot("DXUITC-1477")
        raise exception

def test_4942():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "default")
        time.sleep(5)
        obj.assert_result('Flight budget and schedule setup')
        obj.edit_campaign(campaign)
        time.sleep(5)
        obj.assert_result("Brand Safety")
        obj.assert_result("Level Two")
    except Exception as exception:
        obj.screenshot("DXUITC-4942")
        raise exception

def test_5013():
    try:
        drivers = driver.getOrCreateWebdriver() 
        obj = Tests(drivers)
        obj.new_online_campaign()
        obj.enable_hidden("brand_safety")
        drivers.find_element_by_id("campaign_brand_safety_level_4").click()
        obj.enable_hidden("whitelist")
        obj.enable_hidden("blacklist")
        uid = get_uid()
        campaign = "test-campaign-" + str(uid)
        obj.black_white_list(campaign, "both list present")
        time.sleep(5)
        obj.edit_campaign(campaign)
        time.sleep(2)
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","domain_xlsx.xlsx")
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","domain_xlsx_black.xlsx")
        drivers.find_element_by_link_text("Edit").click()
        time.sleep(5)
        drivers.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx_15.xlsx')
        drivers.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx_15.xlsx')
        drivers.find_element_by_id("campaign_submit").click()
        time.sleep(5)
        obj.assert_result("Campaign \'" + campaign + "\' was successfully updated.")
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(3)>a","domain_xlsx_15.xlsx")
        obj.verify_uploads("div.divider>div:nth-child(3)>p:nth-child(2)>a","domain_xlsx_15.xlsx")
    except Exception as exception:
        obj.screenshot("DXUITC-5013")
        raise exception
