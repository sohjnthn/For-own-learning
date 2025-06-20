from appium import webdriver
from appium.options.android import UiAutomator2Options
from jinja2.nodes import Test
from selenium.webdriver.common.by import By

from datetime import datetime

import os

def current_datetime_string_generator():
    datetimee = datetime.now()
    print("datetime is: " + datetimee.__str__())
    datetimeeText = datetimee.strftime("%d-%m-%Y %H%M%S.%f")
    datetimeeTextString = datetimeeText.__str__()
    print("datetimeText is: " + datetimeeTextString)
    return datetimeeTextString

def take_screenshot(driver, step_name):
    datetimeeeText = datetime.now().strftime("%d-%m-%Y %H%M%S.%f")
    datetimeeeTextString = datetimeeeText.__str__()
    screenshot_path = os.path.join("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeeeTextString + "_screenshot.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path

def generate_html_report(screenshots):
    report_path = "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Html_Reports\\" + current_datetime_string_generator() + "_test_report.html"
    with open(report_path, "w") as report:
        report.write("<html><head><title>Test Report</title></head><body>")
        report.write("<h1>Test Report with Screenshots</h1>")
        for step, screenshot in screenshots.items():
            report.write(f"<h2>{step}</h2>")
            report.write(f'<img src="{screenshot}" alt="{step}" style="width:600px;"><br>')
        report.write("</body></html>")
    print(f"Report generated: {report_path}")

screenshots = {}

def test_first_app(driver):
    policyManagementText = driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Policy management\"]")

    for i in range(100):
        print("Waiting for the display to complete the loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    if policyManagementText.is_displayed():
        screenshots["\"Policy management\" is displayed; Pass."] = take_screenshot(driver, "\"Policy management\" is displayed; Pass.")
    else:
        screenshots["\"Policy management\" is not displayed; Fail."] = take_screenshot(driver, "\"Policy management\" is not displayed; Fail.")

    generate_html_report(screenshots)