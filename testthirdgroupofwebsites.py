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

screenshots = {}

def test_third_group_of_websites(driver):

 driver.get("https://maplestoryseatips.blogspot.com/")
 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
 screenshots["The default Blogger webpage is displayed; Pass."] = take_screenshot(driver, "The default Blogger webpage is displayed; Pass.")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

 #tagNameButtonWebElementList = driver.find_elements(By.TAG_NAME, "button")
 #createPostButton = tagNameButtonWebElementList[1]

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

 return screenshots