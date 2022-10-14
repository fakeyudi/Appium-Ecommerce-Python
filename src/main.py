from decouple import config
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# # from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
from appium.webdriver.common.touch_action import TouchAction

# Options are only available since client version 2.3.0


desired_cap = {
	"platformName" : "android",
	"platformVersion" : "9.0",
	"deviceName" : "Google Pixel 3",
	"app" : "bs://2742b99daebf9fc7d74713f9040652a44a54f14b",
	'bstack:options' : {
		"projectName" : "Flipkart Automation",
		"buildName" : "fk1.0",
		"sessionName" : "Test 1",
		"appiumVersion" : "1.18.0",
        "userName" : config('USER'),
        "accessKey" : config('KEY')
	},
}



options = UiAutomator2Options().load_capabilities(desired_cap)
# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
driver.implicitly_wait(30)


#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout
# time.sleep(20)
# lang = driver.find_element(AppiumBy.ID, "com.flipkart.android:id/language_list").find_element(AppiumBy.XPATH, "/android.widget.RelativeLayout[4]/android.widget.RelativeLayout")
driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout").click()
# print(lang)
# lang.click()


driver.find_element(AppiumBy.ID, "com.flipkart.android:id/select_btn").click()

driver.find_element(AppiumBy.ID, "com.flipkart.android:id/custom_back_icon").click()

driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView").click()

driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView").click()

driver.quit()
# If you have uploaded your app, update the test case here.