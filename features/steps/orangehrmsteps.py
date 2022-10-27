from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager



@given('launch chrome brower')
def launchBrower(context):
    # context.driver = webdriver.Chrome()
    # context.driver = webdriver.Chrome(executable_path='C:\\Users\Vibhor\Desktop\Driver\chromedriver.exe')
    context.driver = webdriver.Chrome()


@when('open orangeHrm home page')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then('verify that the logo present on page')
def verifyLogo(context):
    context.driver.implicitly_wait(20)
    logo_status = context.driver.find_element(By.XPATH, "//div[@class='orangehrm-login-branding']//img").is_displayed()
    assert logo_status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
