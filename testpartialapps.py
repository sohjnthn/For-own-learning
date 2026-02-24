from hellocucumber.hellocucumberpython.testfirstapp import test_first_app

from hellocucumber.hellocucumberpython.testsecondapp import test_second_app

from appium import webdriver
from appium.options.android import UiAutomator2Options

from datetime import datetime

def current_datetime_string_generator():
 datetimee = datetime.now()
 print("datetime is: " + datetimee.__str__())
 datetimeeText = datetimee.strftime("%d-%m-%Y %H%M%S.%f")
 datetimeeTextString = datetimeeText.__str__()
 print("datetimeText is: " + datetimeeTextString)
 return datetimeeTextString

def generate_html_report(screenshots):
 report_path = "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Html_Reports\\" + current_datetime_string_generator() + "_test_report.html"
 with open(report_path, "w") as report:
  report.write("<html><head><title>Test Report</title></head><body>")
  report.write("<h1>Test Report with Screenshots</h1>")
  for step, screenshot in screenshots.items():
   report.write(f"<h2>{step}</h2>")
   report.write(f'<img src="{screenshot}" alt="{step}" style="height:476px;width:238px;"><br>')
  report.write("</body></html>")
 print(f"Report generated: {report_path}")

screenshots = {}

def test_if_websites_can_call_apps():
 androidOptions = UiAutomator2Options()
 androidOptions.platform_name = "Android"
 androidOptions.automation_name = "UiAutomator2"
 androidOptions.platform_version = "15"
 androidOptions.app = "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\app\\com.afwsamples.testdpc_9.0.12-9012_minAPI21(nodpi)_apkmirror.com.apk"

 driver2 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=androidOptions)

 first_app_screenshots = test_first_app(driver2)

 androidOptions = UiAutomator2Options()
 androidOptions.platform_name = "Android"
 androidOptions.automation_name = "UiAutomator2"
 androidOptions.platform_version = "15"
 androidOptions.app = "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\app\\ApiDemos-debug.apk"
 driver3 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=androidOptions)

 second_app_screenshots = test_second_app(driver3)

 # This is how at least two key-value lists can be merged together into a new list
 # The key is the step String; and the value is the screenshot (file) path
 # This is different from a non-key-value list for which
 # at least two lists can be merged by using
 # newlist = firstlist + lastlist
 # for which the list elements can be retrieved by using
 # newlist[i]
 # for which i is an int number
 # like how a list of WebElements's specific element for the int position (which starts from 0)
 # is retrieved
 screenshots = {**first_app_screenshots, **second_app_screenshots}

 generate_html_report(screenshots)
