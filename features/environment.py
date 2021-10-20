from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave.fixture import use_fixture_by_tag
from Pages.search_bar import SearchPage
from helper.helper_web import get_browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 
def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)
 
    # Reading the browser type from the configuration file for Selenium Python Tutorial
    helper_func = get_browser(config.get('Environment', 'Browser'))
    context.helperfunc = helper_func
    #context.search_bar = SearchPage(
        #helper_func = get_browser(config.get('Environment', 'Browser')))
    
    # Local Chrome WebDriver
    #if context.browser == "chrome":
      #context.driver = webdriver.Chrome('C:\Automation\pythonbdddemo\chromedriver\chromedriver.exe')

def after_all(context):
    context.helperfunc.close()



def wait_for_click_element(context, find_it):
    try:
        wait = WebDriverWait(context.browser, 15)
        expected_element = EC.element_to_be_clickable(find_it)
        wait.until(expected_element)
    except TimeoutError:
        raise