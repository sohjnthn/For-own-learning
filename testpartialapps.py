from appium.options.android import UiAutomator2Options
from jinja2.nodes import Test

from hellocucumber.hellocucumberpython.testfirstapp import test_first_app

from hellocucumber.hellocucumberpython.testsecondapp import test_second_app

from appium import webdriver
from appium.options.android import UiAutomator2Options

def test_if_websites_can_call_apps():
 androidOptions = UiAutomator2Options()
 androidOptions.platform_name = "Android"
 androidOptions.automation_name = "UiAutomator2"
 androidOptions.platform_version = "15"
 androidOptions.app = "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\app\\com.afwsamples.testdpc_9.0.12-9012_minAPI21(nodpi)_apkmirror.com.apk"

 driver2 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=androidOptions)

 test_first_app(driver2)

 androidOptions = UiAutomator2Options()
 androidOptions.platform_name = "Android"
 androidOptions.automation_name = "UiAutomator2"
 androidOptions.platform_version = "15"
 androidOptions.app = "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\app\\ApiDemos-debug.apk"
 driver3 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=androidOptions)

 test_second_app(driver3)

# This commented-out line is only for directly running Python unit test via this Python file
# Not via the run button of the above function
# test_if_websites_can_call_apps()