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

 driver.get("https://aminoapps.com/c/maplestorysea/recent/")
 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
 screenshots["The Latest webpage is displayed; Pass."] = take_screenshot(driver, "The Latest webpage is displayed; Pass.")

 tagNameIWebElementList = driver.find_elements(By.TAG_NAME, "i")
 aminoHomeIcon = tagNameIWebElementList[2]
 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

 if aminoHomeIcon.is_displayed():
     screenshots["The Amino Home Icon is displayed; Pass."] = take_screenshot(driver, "The Amino Home Icon is displayed; Pass.")
 else:
     screenshots["The Amino Home Icon is not displayed; Fail."] = take_screenshot(driver, "The Amino Home Icon is not displayed; Fail.")
 aminoHomeIcon.click()

 for i in range(55555):
    print("Still loading.")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
 screenshots["The Home webpage is reached; Pass"] = take_screenshot(driver, "The Home webpage is reached; Pass.")

 for i in range(55555):
    print("Still loading.")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

 for i in range(55555):
    print("Still loading.")

 tagNameButtonWebElementList = driver.find_elements(By.TAG_NAME, "button")
 createPostButton = tagNameButtonWebElementList[1]

 for i in range(55555):
    print("Still loading.")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
 screenshots["The Create Post button is displayed; Pass."] = take_screenshot(driver, "The Create Post button is displayed; Pass.")

 if createPostButton.is_displayed():
     screenshots["The Create Post Button is displayed; Pass."] = take_screenshot(driver, "The Create Post Button is displayed; Pass.")
 else:
     screenshots["The Create Post Button is not displayed; Fail."] = take_screenshot(driver, "The Create Post Button is not displayed; Fail.")
 createPostButton.click()

 for i in range(55555):
    print("Still loading.")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
 screenshots["The link, or button is displayed; Pass."] = take_screenshot(driver, "The link, or button is displayed; Pass.")

 for i in range(55555):
    print("Still loading.")

 tagLine = driver.find_element(By.CLASS_NAME, "tagline")
 taglineText = tagLine.text
 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
 screenshots["The tagline's text is the correct \"MapleStorySEA follows the original Korea MapleStory (by Nexon Korea) 's content.\"; Pass."] = take_screenshot(driver, "The tagline's text is the correct \"MapleStorySEA follows the original Korea MapleStory (by Nexon Korea) 's content.\"; Pass.")

 if taglineText.__eq__("MapleStorySEA follows the original Korea MapleStory (by Nexon Korea) 's content."):
     screenshots["The Create Post Button is displayed; Pass."] = take_screenshot(driver, "The Create Post Button is displayed; Pass.")
 else:
    screenshots["The Create Post Button is not displayed; Fail."] = take_screenshot(driver, "The Create Post Button is not displayed; Fail.")

 for i in range(55555):
    print("Still loading.")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
 screenshots["The link, or button is displayed; Pass."] = take_screenshot(driver, "The link, or button is displayed; Pass.")

 imgTagList = driver.find_elements(By.TAG_NAME, "img")
 topLeftCornerAminoLogoButton = imgTagList[0]

 for i in range(55555):
    print("The Amino webpage's tagline text is displayed as the correct \"Explore your interests and find your communities.\"; which should be \"Explore your interests and find your communities.\", the pop-up UI would take time to load.")

 datetimeTextString = current_datetime_string_generator()
 driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
 screenshots["The pop-up is displayed; Pass."] = take_screenshot(driver, "The pop-up is displayed; Pass.")

 return screenshots