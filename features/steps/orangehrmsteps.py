from behave import *
from selenium import webdriver


@given('Launch chrome brower')
def launchBrower(context):
    context.driver = webdriver.chrome("config/chromedriver.exe")


@when('open orangeHrm home page')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then('verify that the logo present on page')
def verifyLogo(context):
    logo = context.driver.find_element_by_xpath("").is_displayed()
    assert logo is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
