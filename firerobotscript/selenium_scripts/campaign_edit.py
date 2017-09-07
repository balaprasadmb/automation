# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
#from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import WebDriverWait 
from python.setup import get_advertiser, get_campaign
from datetime import timedelta
from datetime import datetime
import driver
import time
import os
import csv
import xlrd

class Tests(object):
    def __init__(self, new_driver):
        self.driver = new_driver
    
    def switch_to_view(self, view="Dashboard"):
        self.driver.find_element_by_link_text("Admin").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Agency Groups")))
        if view == "Dashboard":
            self.driver.find_element_by_link_text("Switch to Campaign Dashboard").click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Switch to Classic Campaign View")))
        if view == "Classic":
            self.driver.find_element_by_link_text("Switch to Classic Campaign View").click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Switch to Campaign Dashboard")))


    def close_message_popup(self):
        if self.is_element_present(By.CSS_SELECTOR, ".ui-dialog"):
            self.driver.find_element_by_css_selector(".ui-dialog").click()
            self.driver.find_element_by_css_selector(".ui-icon-closethick").click()

    def send_values(self, method, locator, value):
            element = self.driver.find_element(method, locator)
            element.clear()
            element.send_keys(value)
        
    def start_date(self):
        return ((datetime.today()+timedelta(days=2)).strftime('%m/%d/%Y'))
    
    def end_date(self):
        return ((datetime.today()+timedelta(days=28)).strftime('%m/%d/%Y'))
    
    def past_start_date(self):
        return ((datetime.today()+timedelta(days=-3)).strftime('%m/%d/%Y'))
    
    def past_end_date(self):
        return ((datetime.today()+timedelta(days=-2)).strftime('%m/%d/%Y'))
    
    def one_day(self):
        return ((datetime.today().strftime('%m/%d/%Y')))
    
    def new_online_campaign(self):
        self.driver.find_element_by_id("drop1").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".add.button.new_campaign_top")))
        advertiser = get_advertiser()
        self.driver.find_element_by_link_text("New Campaign").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#ui-dialog-title-dataxu_dialog")))
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#advertiser")))
        self.driver.find_element_by_id("advertiser").send_keys(advertiser)
        self.driver.find_element_by_id("campaign_submit").submit()
        
    def new_video_campaign(self):
        self.driver.find_element_by_id("drop1").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".add.button.new_campaign_top")))
        advertiser = get_advertiser()
        self.driver.find_element_by_link_text("New Campaign").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#ui-dialog-title-dataxu_dialog")))
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#advertiser")))
        self.driver.find_element_by_id("advertiser").send_keys(advertiser)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, advertiser)))
        self.driver.find_element_by_link_text(advertiser).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "pick_media_type")))
        self.select_from_list_by_label(By.ID, "pick_media_type", "Video")
        self.driver.find_element_by_id("campaign_submit").submit()

    def new_mobile_campaign(self):
        self.driver.find_element_by_id("drop1").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".add.button.new_campaign_top")))
        advertiser = get_advertiser()
        self.driver.find_element_by_link_text("New Campaign").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#ui-dialog-title-dataxu_dialog")))
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#advertiser")))
        self.driver.find_element_by_id("advertiser").send_keys(advertiser)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, advertiser)))
        self.driver.find_element_by_link_text(advertiser).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "pick_media_type")))
        self.select_from_list_by_label(By.ID, "pick_media_type", "Mobile")
        self.driver.find_element_by_id("campaign_submit").submit()

    def campaign_details(self, campaign, criteria = None):
        #need to change only date
        self.driver.find_element_by_id("campaign_name").send_keys(campaign)
        if criteria is None:
            self.driver.find_element_by_id("campaign_start_date").clear()
            self.driver.find_element_by_id("campaign_end_date").clear()
        if criteria == "Valid":
            self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
            self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        if criteria == "Past Start Date":
            self.driver.find_element_by_id("campaign_start_date").send_keys(self.past_start_date())
            self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        if criteria == "Start date ahead":
            self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
            self.driver.find_element_by_id("campaign_end_date").send_keys(self.past_end_date())
        if criteria == "Special character":
            self.driver.find_element_by_id("campaign_start_date").send_keys("!@#$%")
            self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        if criteria == "Blank start date":
            self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date()) 
        if criteria == "Past End Date":
            self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
            self.driver.find_element_by_id("campaign_end_date").send_keys(self.past_end_date())
        if criteria == "End date prior":    
            self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
            self.driver.find_element_by_id("campaign_end_date").send_keys(self.past_end_date())
        if criteria == "Blank end date":
            self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())       
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").send_keys("10")
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").send_keys("5000")
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").send_keys("10")
        self.driver.find_element_by_id("campaign_objective_Distribution").click()
        self.driver.find_element_by_id("campaign_submit").click()
        
    def flights_details(self, flight, criteria = None):
        WebDriverWait(self.driver, 10).until(EC.visibility_of, "Flight budget and schedule setup")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input.ember-view.ember-text-field.flight_name.text")))
        self.driver.find_element_by_css_selector("input.ember-view.ember-text-field.flight_name.text").send_keys(flight)
        self.driver.find_element_by_css_selector("div.cols1.flight-field-bid>div.numeric>input.ember-text-field").send_keys("3.00")
        self.driver.find_element_by_css_selector("input.ember-view.ember-text-field.day_cap").send_keys("10.00")
        element = self.driver.find_element_by_css_selector(".io_budget > input")
        element.clear()
        element.send_keys("1000")
        element.click()
        self.driver.execute_script("document.querySelector('input.ember-view.ember-text-field.day_cap').focus();")
        time.sleep(5)
        widget = self.driver.find_element_by_css_selector("input.ember-view.ember-text-field.percent")
        hover = ActionChains(self.driver).move_to_element(widget)
        hover.perform()
        hover = ActionChains(self.driver).move_to_element(widget).click()
        hover.perform()
        if criteria is None:
            self.driver.find_element_by_css_selector("button.ember-view.ember-button.primary.save-and-continue").click()
        if criteria == "Exit":
            self.driver.find_element_by_css_selector("button.ember-view.ember-button.primary.save-and-exit").click()
            
    def ctr(self, campaign, criteria = None):
        self.driver.find_element_by_id("campaign_name").send_keys(campaign)
        self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
        self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").send_keys("10")
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").send_keys("5000")
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").send_keys("10")
        self.driver.find_element_by_id("campaign_objective_CTR").click()
        if criteria == "Negative value":
            self.driver.find_element_by_css_selector("#campaign_goal_ctr").send_keys("-50")
        if criteria == "Special Character":
            self.driver.find_element_by_css_selector("#campaign_goal_ctr").send_keys("@#$%")
        if criteria == "greater value than 100":
            self.driver.find_element_by_css_selector("#campaign_goal_ctr").send_keys("200")
        if criteria == "empty":
            self.driver.find_element_by_css_selector("#campaign_goal_ctr").clear()
        if criteria == "valid":
            self.driver.find_element_by_css_selector("#campaign_goal_ctr").send_keys("20")
        if criteria == "contents":
            self.driver.find_element_by_css_selector("#campaign_goal_ctr")
            self.assert_result("Maximize your click through rate and creative selection based on DataXu click tracking and optimization.")
            self.assert_result("Goal CTR")
            self.assert_result(":")
            self.assert_result("%")        
        self.driver.find_element_by_id("campaign_submit").click()    
        
    def addoncost(self, campaign, criteria=None):
        self.driver.find_element_by_id("campaign_name").send_keys(campaign)
        self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
        self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").send_keys("10")
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").send_keys("5000")
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").send_keys("10")
        self.driver.find_element_by_id("campaign_objective_Distribution").click()
        self.driver.find_element_by_css_selector("#add_on_costs>div.section_header.contain_cols9>h1>div.section_title.cols4").click()
        self.driver.find_element_by_id("add_new_add_on_cost").click()

    def campaign_info(self, campaign):
        self.driver.find_element_by_id("campaign_name").send_keys(campaign)
        self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
        self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").send_keys("10")
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").send_keys("5000")
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").send_keys("10")

    def budgetandspending(self, campaign, criteria = None):
        self.driver.find_element_by_id("campaign_name").send_keys(campaign)
        self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
        self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        if criteria == "InvalidCPA":
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").clear()
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("10001")
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").send_keys("100") 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("30") 
        if criteria == "empty":
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").clear()
        if criteria == "InvalidBudget ($)": 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").clear()
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").clear()
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("10") 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").send_keys("9000001")
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("10")
        if criteria == "BlankBudget ($)": 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("10") 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").clear()
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("10")   
        if criteria == "BlankCPM ($)": 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("10") 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").send_keys("100") 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").clear()
        if criteria == "InvalidCPM":
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("101") 
        if criteria == "BlankCOGS": 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("10") 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_insertion_order_budget").send_keys("100") 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("30") 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cogs").clear()
        if criteria == "BlankMargin": 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_margin").clear()  
        if criteria == "InvalidMargin": 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpm").send_keys("30")
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_margin").clear() 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_margin").send_keys("101") 
        if criteria == "CPAcharacter": 
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").clear()
            self.driver.find_element_by_css_selector("#campaign_cog_attributes_cpa_goal").send_keys("ABC")              
        self.driver.find_element_by_id("campaign_objective_Distribution").click()
        self.driver.find_element_by_id("campaign_submit").click()

    def performance(self,campaign,criteria=None):
        self.driver.find_element_by_id("campaign_name").send_keys(campaign)
        self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
        self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").send_keys("10")
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").send_keys("5000")
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").send_keys("10")
        self.driver.find_element_by_id("campaign_objective_Performance").click()
        activity = Select(self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_id"))
        activity.select_by_index(1)
        pixel = Select(self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_value"))
        pixel.select_by_visible_text("Learning Pixel")
        self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_filter").clear()
        if criteria=='Valid Tag Id':
            select = Select(self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_source"))
            select.select_by_visible_text("DFA")
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_external_id").clear()
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_external_id").send_keys("1a2b3c")
        if criteria=='Invalid Tag Id':
            select = Select(self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_source"))
            select.select_by_visible_text("DFA")
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_external_id").clear()
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_external_id").send_keys("1a2b3c")
        if criteria=='Small Tag Id':
            select = Select(self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_source"))
            select.select_by_visible_text("DFA")
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_external_id").clear()
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_external_id").send_keys("1903")
        if criteria=='Negative Tag Id':
            select = Select(self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_source"))
            select.select_by_visible_text("DFA")
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_external_id").clear()
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_external_id").send_keys("-190339")
        if criteria=='Blank Tag Id':
            select = Select(self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_source"))
            select.select_by_visible_text("DFA")
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_activity_attributes_third_party_server_id_attributes_external_id").clear()
        if criteria=='Negative Activity':
            pixel = Select(self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_value"))
            pixel.select_by_visible_text("Conversion Pixel")
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_user_value").clear()
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_user_value").send_keys("-190339")
        if criteria=='Activity Limit':
            pixel = Select(self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_value"))
            pixel.select_by_visible_text("Conversion Pixel")
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_user_value").clear()
            self.driver.find_element_by_id("campaign_campaign_activities_attributes_0_user_value").send_keys("11000")
        self.driver.find_element_by_id("campaign_submit").click()
    
    def edit_campaign(self,campaign):
        self.driver.find_element_by_link_text(campaign).click()
        time.sleep(10)        
    
    def enable_hidden(self,hidden):
        self.driver.find_element_by_css_selector("#%s>div>h1>div>span"%(hidden)).click()
    
    def tactics(self,campaign=None,criteria=None):
        self.driver.find_element_by_id("campaign_name").send_keys(campaign)
        self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
        self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").send_keys("10")
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").send_keys("5000")
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").send_keys("10")
        self.driver.find_element_by_id("campaign_objective_Distribution").click()
        if criteria=="custom field appear":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            widget= self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input")
        if criteria=="blank":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
        if criteria=="overflow":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            input_str=""
            for i in range(1,65):
                input_str+="1903"
            self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input").send_keys(input_str)
        if criteria=="valid":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            input_str=""
            for i in range(1,48):
                input_str+="datax"
            input_str+="_"+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input").send_keys(input_str)
        if criteria=="characters":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input").send_keys("tactics_139_"+datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        if criteria=="numbers":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input").send_keys("190391_"+datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        if criteria=="special chars":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input").send_keys("!@#$%&_"+datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        if criteria=="Retargeting":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Retargeting")
        if criteria=="Optimized":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Optimized")
        if criteria=="Channel":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Channel")
        if criteria=="Custom...":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            tactic="tactics_"+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input").send_keys(tactic)
            self.driver.find_element_by_id("campaign_submit").click()
            return tactic
        if criteria=="valid budget":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            tactic="tactics_1_"+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input").send_keys(tactic)
            self.driver.find_element_by_css_selector("#tactics_groups > div > div:nth-child(2) > input").send_keys(3000)
        if criteria=="invalid budget":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            tactic="tactics_2_"+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input").send_keys(tactic)
            self.driver.find_element_by_css_selector("#tactics_groups > div > div:nth-child(2) > input").send_keys("bpdsdns")
        if criteria=="valid impression":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            tactic="tactics_3_"+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input").send_keys(tactic)
            self.driver.find_element_by_css_selector("#tactics_groups > div > div:nth-child(3) > input").send_keys(3000)
        if criteria=="invalid impression":
            select = Select(self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>select"))
            select.select_by_visible_text("Custom...")
            tactic="tactics_4_"+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.find_element_by_css_selector("#campaign_tactics_attributes_new_tactic_name_input>input").send_keys(tactic)
            self.driver.find_element_by_css_selector("#tactics_groups > div > div:nth-child(3) > input").send_keys("bpdsdns")
        self.driver.find_element_by_id("campaign_submit").click()
    
    def brands(self,campaign=None,criteria=None):
        self.driver.find_element_by_id("campaign_name").send_keys(campaign)
        self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
        self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").send_keys("10")
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").send_keys("5000")
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").send_keys("10")
        self.driver.find_element_by_id("campaign_objective_Distribution").click()
        if criteria =="default":
            EC.element_to_be_selected(self.driver.find_element_by_id("campaign_brand_safety_level_2"))
        if criteria =="level1":
            self.driver.find_element_by_id("campaign_brand_safety_level_1").click()
        if criteria =="level3":
            self.driver.find_element_by_id("campaign_brand_safety_level_3").click()
        if criteria =="level4":
            self.driver.find_element_by_id("campaign_brand_safety_level_4").click()
        if criteria =="whitelist":
            self.driver.find_element_by_id("campaign_brand_safety_level_4").click()
            self.enable_hidden("whitelist")
            self.driver.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/blank.csv')
        self.driver.find_element_by_id("campaign_submit").click()

    def black_white_list(self,campaign=None,criteria=None):
        self.driver.find_element_by_id("campaign_name").send_keys(campaign)
        self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
        self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").send_keys("10")
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").send_keys("5000")
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").send_keys("10")
        self.driver.find_element_by_id("campaign_objective_Distribution").click()
        if criteria =="whitelist present":
            self.driver.find_element_by_id("campaign_white_list_domains").send_keys("www.foobar.com")
        if criteria =="blacklist present":
            self.driver.find_element_by_id("campaign_black_list_domains").send_keys("www.foobar.com")
        if criteria =="exported blacklist present":
            self.driver.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/exports_3.csv')
        if criteria =="exported whitelist present":
            self.driver.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/exports_3.csv')
        if criteria =="blacklist blank":
            self.driver.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/blank.txt')
        if criteria =="whitelist blank":
            self.driver.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/blank.txt')
        if criteria =="blacklist blank csv":
            self.driver.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/blank.csv')
        if criteria =="txt blacklist present":
            self.driver.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_txt.txt')
        if criteria =="txt whitelist present":
            self.driver.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_txt.txt')
        if criteria =="xls blacklist present":
            self.driver.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xls.xls')
        if criteria =="xls whitelist present":
            self.driver.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xls.xls')
        if criteria =="xlsx blacklist present":
            self.driver.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx.xlsx')
        if criteria =="xlsx whitelist present":
            self.driver.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx.xlsx')
        if criteria =="both list present":
            self.driver.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx.xlsx')
            self.driver.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx_black.xlsx')
        if criteria =="updated list present":
            self.driver.find_element_by_id("campaign_white_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx_15.xlsx')
            self.driver.find_element_by_id("campaign_black_list_domains_file").send_keys(os.path.dirname(__file__)+'/uploads/domain_xlsx_15.xlsx')
        self.driver.find_element_by_id("campaign_submit").click()
    
    def verify_uploads(self,locator,list_file):
        splits=list_file.split('.')
        filetype=splits[1]
        self.driver.find_element_by_css_selector(locator).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ui-dialog.ui-widget.ui-widget-content.ui-corner-all.dialog-500")))
        time.sleep(5)
        if filetype=="csv" or filetype=="txt":
            with open(os.path.dirname(__file__)+'/uploads/'+list_file, 'rb') as csvfile:
                csvreader=csv.reader(csvfile)
                for r in csvreader:
                    self.assert_result(r[0])
        elif filetype=="xls" or filetype=="xlsx":
            with xlrd.open_workbook(os.path.dirname(__file__)+'/uploads/'+list_file) as book:
                sheet=book.sheet_by_index(0)
                for row in range(sheet.nrows):
                    self.assert_result(sheet.cell(row,0).value)
        self.driver.find_element_by_css_selector(".ui-icon.ui-icon-closethick").click()
    
    def campaign_show(self,campaign=None,criteria=None):
        self.driver.find_element_by_id("campaign_name").send_keys(campaign)
        self.driver.find_element_by_id("campaign_start_date").send_keys(self.start_date())
        self.driver.find_element_by_id("campaign_end_date").send_keys(self.end_date())
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpa_goal").send_keys("10")
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_insertion_order_budget").send_keys("5000")
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").clear()
        self.driver.find_element_by_id("campaign_cog_attributes_cpm").send_keys("10")
        self.driver.find_element_by_id("campaign_objective_Distribution").click()
        if criteria =="whitelist present":
            self.driver.find_element_by_id("campaign_white_list_domains").send_keys("www.foobar.com")
        if criteria =="blacklist present":
            self.driver.find_element_by_id("campaign_black_list_domains").send_keys("www.foobar.com")
        self.driver.find_element_by_id("campaign_submit").click()
            
    def assert_result(self, strings):
        page_source = self.driver.page_source
        assert strings in page_source
    
    def wait_until(self, method, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((method,locator)))
    
    def tearDown(self):
        self.driver.quit()
    
    def screenshot(self, name):
        self.driver.save_screenshot('screenshots/{0}-{1}.png'.format(name, datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True

    def select_from_list_by_label(self, locator, element_id, label):
        """Select From List By Visible Text"""
        select = Select(self.driver.find_element(locator, element_id))
        select.select_by_visible_text(label)
    
    def select_from_list_by_value(self, locator, element_id, label):
        """Select From List By Visible Text"""
        select = Select(self.driver.find_element(locator, element_id))
        select.select_by_value(label)
    
    def select_from_list_by_index(self, locator, element_id, label):
        """Select From List By Visible Text"""
        select = Select(self.driver.find_element(locator, element_id))
        select.select_by_index(label)
    
    def agency_group_detail(self, name, file_path, criteria=None, contact="Dataxu_services"):
        self.driver.find_element_by_id("agency_group_name").send_keys(name)
        if criteria == "valid_email":
            self.driver.find_element_by_id("agency_group_organization_attributes_email").send_keys("abc@dataxu.com")
        if criteria == "invalid_email":
            self.driver.find_element_by_id("agency_group_organization_attributes_email").send_keys("abcdataxu.com$")
        if criteria == "255":
            email = "8901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789@dataxu.com"
            self.driver.find_element_by_id("agency_group_organization_attributes_email").send_keys(email)
        self.driver.find_element_by_id("agency_group_organization_attributes_contact_name").send_keys(contact)
        self.driver.find_element_by_id("agency_group_rate_card").send_keys(file_path)
        self.driver.find_element_by_id("agency_group_submit").click()

def login(url, username, password):
    try:
        drivers = driver.getOrCreateWebdriver()
        obj = Tests(drivers)
        drivers.get(url)
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#user_session_email")))
        if username is not None and password is not None:
            obj.send_values(By.CSS_SELECTOR, "#user_session_email", username)
            obj.send_values(By.CSS_SELECTOR, "#user_session_password", password)
            obj.driver.find_element_by_css_selector("#user_session_submit").click()
        obj.close_message_popup()
        WebDriverWait(drivers, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#drop1")))
        obj.switch_to_view(view="Classic")
    except Exception as exception:
        obj.screenshot("login")
        raise exception