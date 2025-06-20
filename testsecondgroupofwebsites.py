from selenium import webdriver

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

def test_second_group_of_websites(driver):

 driver.get("https://aminoapps.com/c/maplestorysea/recent/")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
 screenshots["The Latest webpage is reached; Pass"] = take_screenshot(driver, "The Latest webpage is reached; Pass.")

 generate_html_report(screenshots)