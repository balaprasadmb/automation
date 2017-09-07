from selenium import webdriver

DRIVER = None

def getOrCreateWebdriver():
    global DRIVER
    DRIVER = DRIVER or webdriver.Firefox()
    return DRIVER