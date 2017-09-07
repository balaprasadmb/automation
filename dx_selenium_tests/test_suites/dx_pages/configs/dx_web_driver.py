from pytractor.webdriver import Firefox
from selenium import webdriver
import os

class DXWebDriver(object):

    def __init__(self):
        self.driver = None

    def get_browser(self):
        if self.driver != None:
            return self.driver
        else:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", os.path.abspath(os.path.dirname(__file__) + '/../../../data/downloaded_files/'))
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
            self.driver = Firefox(firefox_profile=profile)
            self.driver.ignore_synchronization = True
            return self.driver

    def close_driver(self):
        if self.driver is not None:
            self.driver.close()
