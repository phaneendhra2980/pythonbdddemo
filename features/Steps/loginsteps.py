# Python Behave testing example for Selenium test automation
from behave import *





@given('I navigate to the Google page')
def step_function(context):
    # Add Your Code Here
    context.helperfunc.open('https://www.google.com')
    context.helperfunc.maximize()


@when('I enter a searchterm')
def step_function(context):
    # Add Your Code Here
    iagreebutton = context.helperfunc.find_by_id("L2AGLb")
    iagreebutton.click()

    searchbox = context.helperfunc.find_by_xpath(
        "//input[@class='gLFyf gsfi']")
    searchbox.send_keys('Selenium')


@step('press enter key')
def step_function(context):
    # Add Your Code Here
    googlesearchbutton = context.helperfunc.find_by_xpath(
        "//input[@class='gNO89b' and @value='Google Search']")
    googlesearchbutton.click()


@then('I should see searchresults')
def step_function(context):
    # Add Your Code Here
    assert True is not False
