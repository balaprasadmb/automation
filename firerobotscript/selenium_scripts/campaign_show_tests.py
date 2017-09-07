# -*- encoding: utf-8 -*-
from campaign_edit import Tests#, login
from python.setup import get_uid,get_campaign,get_advertiser,get_flight
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import driver
import time

def test_4764():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        drivers.find_element_by_id("drop1").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".add.button.new_campaign_top")))
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        time.sleep(5)
        obj.edit_campaign(get_campaign())
        time.sleep(2)
        drivers.find_element_by_css_selector("tbody#tactic_flight_body>tr:nth-child(2)>td:nth-child(8)>a").click()
        obj.assert_result("Confirm Creative Assignments")
        drivers.find_element_by_link_text("Add Creatives").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ui-dialog.ui-widget.ui-widget-content.ui-corner-all.modal-dialog")))
        drivers.find_element_by_css_selector("div#available_creatives>div>div>div.dataTables_scrollBody>table>tbody>tr:nth-child(1)>td:nth-child(1)>input").click()
        drivers.find_element_by_css_selector("div#available_creatives>div>div>div.dataTables_scrollBody>table>tbody>tr:nth-child(2)>td:nth-child(1)>input").click()
        drivers.find_element_by_link_text('Assign Creatives').click()
        obj.assert_result("Confirm Creative Assignments")
        time.sleep(5)
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"table.available_creatives.dataTable>tbody>tr:nth-child(1)>td:nth-child(8)>img")))
        drivers.find_element_by_css_selector("table.available_creatives.dataTable>tbody>tr:nth-child(1)>td:nth-child(8)>img").click()
        obj.assert_result("Confirm Creative Assignments")
    except Exception as exception:
        obj.screenshot("DXUITC-4764")
        raise exception
    
    

def test_41_8079():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".add.button.new_campaign_top")))
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        time.sleep(5)
        obj.edit_campaign(get_campaign())
        time.sleep(2)
        drivers.find_element_by_link_text('Smart Assign Creatives').click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ui-dialog.ui-widget.ui-widget-content.ui-corner-all.modal-dialog")))
        obj.assert_result('Smart Assign Creatives')
        obj.assert_result('Status')
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    except Exception as exception:
        obj.screenshot("DXUITC-41-8079")
        raise exception

def test_859():
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
        obj.assert_result("Campaign Whitelist")
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    except Exception as exception:
        obj.screenshot("DXUITC-858")
        raise exception

def test_858():
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
        obj.assert_result("Campaign Blacklist")
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    except Exception as exception:
        obj.screenshot("DXUITC-859")
        raise exception

def test_4755():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        time.sleep(5)
        obj.edit_campaign(get_campaign())
        time.sleep(2)
        drivers.find_element_by_css_selector("tbody#tactic_flight_body>tr:nth-child(2)>td:nth-child(8)>a").click()
        obj.assert_result("Processing...")
    except Exception as exception:
        obj.screenshot("DXUITC-4755")
        raise exception

def test_4749_4785():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        time.sleep(5)
        obj.edit_campaign(get_campaign())
        time.sleep(2)
        drivers.find_element_by_css_selector("tbody#tactic_flight_body>tr:nth-child(2)>td:nth-child(8)>a").click()
        obj.assert_result("Confirm Creative Assignments")
        drivers.find_element_by_link_text("Add Creatives").click()
        WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ui-dialog.ui-widget.ui-widget-content.ui-corner-all.modal-dialog")))
        obj.assert_result("Available Creatives")
        obj.assert_result("Name")
        obj.assert_result("Size")
        obj.assert_result("APX")
        obj.assert_result("RMX")
        obj.assert_result("Start/End")
        obj.assert_result("Status")
        drivers.find_element_by_css_selector("div.dataTables_scroll>div>div>table>thead>tr>th>input").click()
        drivers.find_element_by_css_selector("div.ui-dialog>div:nth-child(2)>div:nth-child(2)>#assign_selected_creatives").click()
        WebDriverWait(drivers,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".overlay>span")))
        drivers.find_element_by_css_selector("#flight_submit[value$='Exit']").click()
        obj.assert_result("Flight \""+get_flight()+"\" creative assignments have been successfully updated.")
    except Exception as exception:
        obj.screenshot("DXUITC-4749-4785")
        raise exception

def test_4766():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".add.button.new_campaign_top")))
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        time.sleep(5)
        obj.edit_campaign(get_campaign())
        time.sleep(2)
        drivers.find_element_by_css_selector("tbody#tactic_flight_body>tr:nth-child(2)>td:nth-child(8)>a").click()
        obj.assert_result("Confirm Creative Assignments")
        search=str(drivers.find_element_by_css_selector("td.names>a").get_attribute('innerHTML'))
        search_text=search.replace('<wbr>', '')
        drivers.find_element_by_css_selector("input.search").send_keys(search_text)
        expected=drivers.find_element_by_css_selector("td.names>a").get_attribute('innerHTML')
        expected_text=search.replace('<wbr>', '')
        if search_text!=expected_text:
            raise AssertionError
    except Exception as exception:
        obj.screenshot("DXUITC-4766")
        raise exception

def test_4768():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        time.sleep(5)
        obj.edit_campaign(get_campaign())
        time.sleep(1)
        drivers.find_element_by_css_selector("tbody#tactic_flight_body>tr:nth-child(2)>td:nth-child(8)>a").click()
        obj.assert_result("Confirm Creative Assignments")
        search_text=drivers.find_element_by_css_selector("td.names>a").get_attribute('innerHTML')
        drivers.find_element_by_css_selector("input.search").send_keys(search_text)
        obj.assert_result("Processing...")
    except Exception as exception:
        obj.screenshot("DXUITC-4768")
        raise exception

def test_4770():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        time.sleep(5)
        obj.edit_campaign(get_campaign())
        time.sleep(2)
        drivers.find_element_by_css_selector("tbody#tactic_flight_body>tr:nth-child(2)>td:nth-child(8)>a").click()
        obj.assert_result("Confirm Creative Assignments")
        drivers.find_element_by_link_text("Add Creatives").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ui-dialog.ui-widget.ui-widget-content.ui-corner-all.modal-dialog")))
        search=str(drivers.find_element_by_css_selector("div#available_creatives>div>div>div.dataTables_scrollBody>table>tbody>tr:nth-child(1)>td:nth-child(2)>a").get_attribute('innerHTML'))
        search_text=search.replace('<wbr>', '')
        drivers.find_element_by_css_selector("#DataTables_Table_1_filter>label>input").send_keys(search_text)
        expected=str(drivers.find_element_by_css_selector("div#available_creatives>div>div>div.dataTables_scrollBody>table>tbody>tr:nth-child(1)>td:nth-child(2)>a").get_attribute('innerHTML'))
        expected_text=expected.replace('<wbr>', '')
        if search_text!=expected_text:
            raise AssertionError
    except Exception as exception:
        obj.screenshot("DXUITC-4770")
        raise exception
    drivers.refresh()

def test_4783():
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers) 
        drivers.find_element_by_id("drop1").click()
        drivers.find_element_by_css_selector(".chzn-single").click()
        drivers.find_element_by_css_selector("div.chzn-search>input").send_keys(get_advertiser(),Keys.ENTER)
        time.sleep(5)
        obj.edit_campaign(get_campaign())
        time.sleep(2)
        drivers.find_element_by_css_selector("tbody#tactic_flight_body>tr:nth-child(2)>td:nth-child(8)>a").click()
        obj.assert_result("Confirm Creative Assignments")
        drivers.find_element_by_link_text("Add Creatives").click()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ui-dialog.ui-widget.ui-widget-content.ui-corner-all.modal-dialog")))
        drivers.find_element_by_css_selector("#DataTables_Table_1_filter>label>input").send_keys('@$&%&^*')
        obj.assert_result("Showing 0 to 0 of 0 entries")
        obj.assert_result("No data available in table")
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    except Exception as exception:
        obj.screenshot("DXUITC-4770")
        drivers.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
        raise exception
