from selenium.webdriver.common.by import By

from datetime import datetime

from selenium.webdriver.common.utils import Keys

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

def test_first_group_of_websites(driver):

    driver.get("https://demo.guru99.com/")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    emailInputField = driver.find_element(By.NAME, "emailid")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if emailInputField.is_displayed():
        screenshots["The Email Input Field is displayed; Pass."] = take_screenshot(driver, "The Email Input Field is displayed; Pass.")
    else:
        screenshots["The Email Input Field is not displayed; Fail."] = take_screenshot(driver, "The Email Input Field is not displayed; Fail.")

    emailInputField.send_keys("abc@gmail.com")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if emailInputField.is_displayed():
        screenshots["The Email Input Field's text \"abc@gmail.com\" is displayed; Pass."] = take_screenshot(driver, "The Email Input Field's text \"abc@gmail.com\" is displayed; Pass.")
    else:
        screenshots["The Email Input Field's text \"abc@gmail.com\" is not displayed; Fail."] = take_screenshot(driver, "The Email Input Field's text \"abc@gmail.com\" is not displayed; Fail.")

    submitButton = driver.find_element(By.NAME, "btnLogin")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if submitButton.is_displayed():
        screenshots["The Submit Button is displayed; Pass."] = take_screenshot(driver, "The Submit Button is displayed; Pass.")
    else:
        screenshots["The Submit Button is not displayed; Fail."] = take_screenshot(driver, "The Submit Button is not displayed; Fail.")

    submitButton.click()

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The resulting webpage has been reached; Pass."] = take_screenshot(driver, "The resulting webpage has been reached; Pass.")

    driver.get("https://www.bing.com")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if driver.title.__eq__("Search - Microsoft Bing"):
        screenshots["The Microsoft Bing webpage has been reached; Pass."] = take_screenshot(driver, "The Microsoft Bing webpage has been reached; Pass.")
    else:
        screenshots["The Microsoft Bing webpage has not been reached; Fail."] = take_screenshot(driver, "The Microsoft Bing webpage has been reached; Fail.")

    microsoftBingSearchBar = driver.find_element(By.NAME, "q")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    if microsoftBingSearchBar.is_displayed():
        screenshots["The Microsoft Bing search bar is displayed; Pass."] = take_screenshot(driver, "The Microsoft Bing search bar is displayed; Pass.")
    else:
        screenshots["The Microsoft Bing search bar is not displayed; Fail."] = take_screenshot(driver, "The Microsoft Bing search bar is not displayed; Fail.")

    microsoftBingSearchBar.send_keys("MapleStorySEA (South-East Asia) tips [Facebook notes]")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The Microsoft Bing search bar's search term \"MapleStorySEA (South-East Asia) tips [Facebook notes]\" has been entered; Pass."] = take_screenshot(driver, "The Microsoft Bing search bar's search term \"MapleStorySEA (South-East Asia) tips [Facebook notes]\" has been entered; Pass.")

    microsoftBingSearchBarMagnifyingGlassButton = driver.find_element(By.ID, "search_icon")

    if microsoftBingSearchBarMagnifyingGlassButton.is_displayed():
        screenshots["The Microsoft Bing search bar's magnifying glass button is displayed; Pass."] = take_screenshot(driver, "The Microsoft Bing search bar's magnifying glass button is displayed; Pass.")
    else:
        screenshots["The Microsoft Bing search bar's magnifying glass button is not displayed; Fail."] = take_screenshot(driver, "The Microsoft Bing search bar's magnifying glass button is not displayed; Fail.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    microsoftBingSearchBarMagnifyingGlassButton.click()

    for i in range(99999):
        print("Wait for the initial \"MapleStorySEA (South-East Asia) tips [Facebook notes] - Search\" webpage to finish loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The Search Results webpage has been reached; Pass."] = take_screenshot(driver, "The Search Results webpage has been reached; Pass.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    #searchTab = driver.find_element(By.ID, "b-scopeListItem-copilotsearch")

    #if searchTab.is_displayed():
        #screenshots["The Search tab is displayed; Pass."] = take_screenshot(driver, "The Search tab is displayed; Pass.")
    #else:
        #screenshots["The Search tab is not displayed; Fail."] = take_screenshot(driver, "The Search tab is not displayed; Fail.")

    #datetimeTextString = current_datetime_string_generator()
    #driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    #searchTab.click()

    #datetimeTextString = current_datetime_string_generator()
    #driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    #allTab = driver.find_element(By.ID, "b-scopeListItem-web")

    #datetimeTextString = current_datetime_string_generator()
    #driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    #if allTab.is_displayed():
        #screenshots["The All tab is displayed; Pass."] = take_screenshot(driver, "The All tab is displayed; Pass.")
    #else:
        #screenshots["The All tab is not displayed; Fail."] = take_screenshot(driver, "The All tab is not displayed; Fail.")

    #allTab.click()

    driver.get("https://maplestoryseatips.blogspot.com/")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if datetimeTextString.__eq__(datetimeTextString):
        screenshots["The Search Results webpage is reached; Pass."] = take_screenshot(driver, "The Search Results webpage is reached; Pass.")
    else:
        screenshots["The Search Results webpage is not reached; Fail."] = take_screenshot(driver, "The Search Results webpage is not reached; Fail.")

    displayedText = driver.find_element(By.PARTIAL_LINK_TEXT, "[MapleStorySEA] Typed some extra things here")

    if displayedText.is_displayed():
        print("https://maplestoryseatips.blogspot.com/ is reached")
        screenshots["The default Blogger webpage is reached; Pass."] = take_screenshot(driver, "The default Blogger webpage is reached; Pass.")
    else:
        print("https://maplestoryseatips.blogspot.com/ is not reached.")
        screenshots["The default Blogger webpage is not reached; Fail."] = take_screenshot(driver, "The default Blogger webpage is not reached; Fail.")

    toggleList1 = driver.find_elements(By.CLASS_NAME, "post-count-link")
    zippyToggleOpenForTheYear2026 = toggleList1[45]

    for i in range(5):
        zippyToggleOpenForTheYear2026.send_keys(Keys.DOWN)
        datetimeTextString = current_datetime_string_generator()
        driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    if zippyToggleOpenForTheYear2026.is_displayed():
        print("zippyToggleOpenForTheYear2026 is displayed (the className post-count-link of the text 2026 is used for finding the text at the right of the arrow).")
        screenshots["zippyToggleOpenForTheYear2026 is displayed (the className post-count-link of the text 2026 is used for finding the text at the right of the arrow); Pass."] = take_screenshot(driver, "zippyToggleOpenForTheYear2026 is displayed (the className post-count-link of the text 2026 is used for finding the text at the right of the arrow); Pass.")
    else:
        print("zippyToggleOpenForTheYear2026 is not displayed (the className post-count-link of the text 2026 is used for finding the text at the right of the arrow).")
        screenshots["zippyToggleOpenForTheYear2026 is not displayed (the className post-count-link of the text 2026 is used for finding the text at the right of the arrow); Fail."] = take_screenshot(driver, "zippyToggleOpenForTheYear2026 is not displayed (the className post-count-link of the text 2026 is used for finding the text at the right of the arrow); Fail.")

    tagAWebElementList = driver.find_elements(By.TAG_NAME, "a")
    arrowForToggleOpenForTheYear2026 = tagAWebElementList[128]
    arrowForToggleOpenForTheYear2026.click()

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    if arrowForToggleOpenForTheYear2026.is_displayed():
        print("arrowForToggleOpenForTheYear2026 (the actual arrow at the left of the text 2026 via the tagName a) should be closed (point rightwards).")
        screenshots["arrowForToggleOpenForTheYear2026 (the actual arrow at the left of the text 2026 via tagName a) is closed (points rightwards); Pass."] = take_screenshot(driver, "arrowForToggleOpenForTheYear2026 (the actual arrow at the left of the text 2026 via tagName a) is closed (points rightwards); Pass.")
    else:
        print("arrowForToggleOpenForTheYear2026 (the actual arrow at the left of the text 2026 via tagName a) is not closed incorrectly (is still pointing downwards).")
        screenshots["arrowForToggleOpenForTheYear2026 (the actual arrow at the left of the text 2026 via tagName a) is not closed (still pointing downwards); Fail."] = take_screenshot(driver, "arrowForToggleOpenForTheYear2026 (the actual arrow at the left of the text 2026 via tagName a) is not closed (still pointing downwards); Fail.")

    theText2026 = driver.find_element(By.PARTIAL_LINK_TEXT, "2026")
    theText2026.click()

    displayedText2 = driver.find_element(By.PARTIAL_LINK_TEXT, "[MapleStorySEA] Create your own guild to boost all characters' damage ranges")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    if displayedText2.is_displayed():
        print("The bottommost note for January 2026 is displayed.")
        screenshots["The bottommost note for January 2026 is displayed; Pass."] = take_screenshot(driver, "The bottommost note for 2026 (the first note for January 2026) is displayed at the bottom of the current webpage; Pass.")
    else:
        print("The bottommost note for January 2026 is not displayed.")
        screenshots["The bottommost note for January 2026 is not displayed; Fail."] = take_screenshot(driver, "The bottommost note for 2026 (the first note for January 2026) is not displayed at the bottom of the current webpage; Fail.")

    for i in range (5):
        displayedText2.send_keys(Keys.DOWN)
        datetimeTextString = current_datetime_string_generator()
        driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    if displayedText2.is_displayed:
        print("The bottommost note for 2026 is displayed; and is reached.")
        screenshots["The bottommost note for 2026 is displayed; and is reached; Pass."] = take_screenshot(driver, "The bottommost note for 2026 (the first note for January 2026) is displayed at the bottom of the current webpage; and is reached; Pass.")
    else:
        print("The bottommost note for 2026 is not displayed; and is not reached.")
        screenshots["The bottommost note for 2026 is not displayed; and is not reached; Fail."] = take_screenshot(driver, "The bottommost note for 2026 (the first note for January 2026) is not displayed at the bottom of the current webpage; and is not reached; Fail.")


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

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    #threeWebElementsList = driver.find_elements(By.TAG_NAME, "svg")
    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    #tagNameH3WebElementList = driver.find_elements(By.TAG_NAME, "h3")
    #popularPostsText = tagNameH3WebElementList[0]
    #popularPostsTextString = popularPostsText.text
    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    for i in range(55555):
        print("Still loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    for i in range(55555):
        print("Still loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    for i in range(55555):
        print("Still loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    for i in range(55555):
        print("Still loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    for i in range(55555):
        print("Still loading.")
    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    for i in range(55555):
        print("Still loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    #sevenLabelClassnameWebElementList = driver.find_elements(By.CLASS_NAME, "label")
    #requiredSecondLabelClassnameElement = sevenLabelClassnameWebElementList[1]

    #requiredSecondLabelClassnameElement.click()

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    return screenshots
