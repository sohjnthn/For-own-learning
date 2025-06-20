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

def test_second_app(driver):
    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    appTab = driver.find_element(By.XPATH, "//android.widget.TextView[@content-desc=\"App\"]")
    if appTab.is_displayed():
        screenshots["The App tab is displayed; Pass."] = take_screenshot(driver, "The App tab is displayed; Pass.")
    else:
        screenshots["The App tab is not displayed; Fail."] = take_screenshot(driver, "The App tab is not displayed; Fail.")
    appTab.click()

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    searchTab = driver.find_element(By.XPATH, "//android.widget.TextView[@content-desc=\"Search\"]")
    if searchTab.is_displayed():
        screenshots["The Search tab is displayed; Pass."] = take_screenshot(driver, "The Search tab is displayed; Pass.")
    else:
        screenshots["The Search tab is not displayed; Fail."] = take_screenshot(driver, "The Search tab is not displayed; Fail.")
    searchTab.click()

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    invokeSearchTab = driver.find_element(By.XPATH, "//android.widget.TextView[@content-desc=\"Invoke Search\"]")
    if invokeSearchTab.is_displayed():
        screenshots["The Invoke Search tab is displayed; Pass."] = take_screenshot(driver, "The Invoke Search tab is displayed; Pass.")
    else:
        screenshots["The Invoke Search tab is not displayed; Fail."] = take_screenshot(driver, "The Invoke Search tab is not displayed; Fail.")
    invokeSearchTab.click()

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    prefillQueryTextField = driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id=\"io.appium.android.apis:id/txt_query_prefill\"]")
    if prefillQueryTextField.is_displayed():
        screenshots["The Prefill Query Text Field is displayed; Pass."] = take_screenshot(driver, "The Prefill Query Text Field is displayed; Pass.")
    else:
        screenshots["The Prefill Query Text Field is not displayed; Fail."] = take_screenshot(driver, "The Prefill Query Text Field is not displayed; Fail.")
    prefillQueryTextField.send_keys("Test the text.")

    for i in range(100):
        print("Waiting for the display to complete the loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    if prefillQueryTextField.is_displayed():
        screenshots["The Prefill Query Text Field's entered text \"Test the text.\" is displayed; Pass."] = take_screenshot(driver, "The Prefill Query Text Field's entered text \"Test the text.\" is displayed; Pass.")
    else:
        screenshots["The Prefill Query Text Field's entered text \"Test the text.\" is not displayed; Fail."] = take_screenshot(driver, "The Prefill Query Text Field's entered text \"Test the text.\" is not displayed; Fail.")

    generate_html_report(screenshots)