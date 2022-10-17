from decouple import config
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from .locators import getXpath, getID

desired_cap = {
	"platformName" : "android",
	"platformVersion" : "9.0",
	"deviceName" : "Google Pixel 3",
	"app" : "bs://2742b99daebf9fc7d74713f9040652a44a54f14b",
	'bstack:options' : {
		"projectName" : "Flipkart Automation",
		"buildName" : "fk2.0",
		"sessionName" : "Test 1",
		"appiumVersion" : "1.18.0",
        "userName" : "fakeyudi_G2oCF9", #config('USER'),
        "accessKey" : "CpfyyphpBjyypJC9Ptfe" #config('KEY')
	},
}

options = UiAutomator2Options().load_capabilities(desired_cap)

scenarios('../features/AppTest.feature')


@given(u'Launch the App')
def launchApp(context):
	context.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
	context.driver.implicitly_wait(30)


@then(u'I should select English')
def selectEnglish(context):
	context.driver.find_element(AppiumBy.XPATH, getXpath("English")).click()
	context.driver.find_element(AppiumBy.ID, getID("Next")).click()


@then(u'I should close Login')
def closeLogin(context):
	context.driver.find_element(AppiumBy.ID, getID("Close")).click()


@then(u'I should click on Mobile')
def clickMobile(context):
	context.driver.find_element(AppiumBy.XPATH, getXpath("Mobile")).click()


@then(u'I select iPhone')
def selectiPhone(context):
	context.driver.find_element(AppiumBy.XPATH, getXpath("iPhone")).click()


@then(u'Close the app')
def closeApp(context):
	context.driver.quit()

