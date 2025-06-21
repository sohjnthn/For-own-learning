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

screenshots = {}

def test_second_group_of_websites(driver):

 driver.get("https://aminoapps.com/c/maplestorysea/recent/")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
 screenshots["The Latest webpage is reached; Pass"] = take_screenshot(driver, "The Latest webpage is reached; Pass.")

 return screenshots