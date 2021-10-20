from selenium import webdriver
from helper.helper_base import HelperFunc
 
def get_browser(browser):
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome('C:\Automation\pythonbdddemo\chromedriver\chromedriver.exe'))