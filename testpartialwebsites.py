from selenium import webdriver

from datetime import datetime

from hellocucumber.hellocucumberpython.testpartialapps import test_if_websites_can_call_apps

from hellocucumber.hellocucumberpython.testfirstgroupofwebsites import test_first_group_of_websites
from hellocucumber.hellocucumberpython.testsecondgroupofwebsites import test_second_group_of_websites
from hellocucumber.hellocucumberpython.testthirdgroupofwebsites import test_third_group_of_websites

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
            report.write(f'<img src="{screenshot}" alt="{step}" style="width:600px;"><br>')
        report.write("</body></html>")
    print(f"Report generated: {report_path}")

screenshots = {}

def test_if_websites_can_be_split():
    driver1 = webdriver.Chrome()
    first_websites_screenshots = test_first_group_of_websites(driver1)
    second_websites_screenshots = test_second_group_of_websites(driver1)
    third_websites_screenshots = test_third_group_of_websites(driver1)

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
    screenshots = {**first_websites_screenshots, **second_websites_screenshots, **third_websites_screenshots}
    generate_html_report(screenshots)

    # Only for executing testpartialapps.py
    test_if_websites_can_call_apps()
