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

    microsoftBingSearchBar.send_keys("MapleStorySEA Unfunded Amino")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The Microsoft Bing search bar's search term \"MapleStorySEA Unfunded Amino\" has been entered; Pass."] = take_screenshot(driver, "The Microsoft Bing search bar's search term \"MapleStorySEA Unfunded Amino\" has been entered; Pass.")

    microsoftBingSearchBarMagnifyingGlassButton = driver.find_element(By.ID, "search_icon")

    if microsoftBingSearchBarMagnifyingGlassButton.is_displayed():
        screenshots["The Microsoft Bing search bar's magnifying glass button is displayed; Pass."] = take_screenshot(driver, "The Microsoft Bing search bar's magnifying glass button is displayed; Pass.")
    else:
        screenshots["The Microsoft Bing search bar's magnifying glass button is not displayed; Fail."] = take_screenshot(driver, "The Microsoft Bing search bar's magnifying glass button is not displayed; Fail.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    microsoftBingSearchBarMagnifyingGlassButton.click()

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The Search Results webpage has been reached; Pass."] = take_screenshot(driver, "The Search Results webpage has been reached; Pass.")

    # driver.get("https://www.bing.com/search?q=MapleStorySEA+Unfunded+Amino")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    searchTab = driver.find_element(By.ID, "b-scopeListItem-copilotsearch")

    if searchTab.is_displayed():
        screenshots["The Search tab is displayed; Pass."] = take_screenshot(driver, "The Search tab is displayed; Pass.")
    else:
        screenshots["The Search tab is not displayed; Fail."] = take_screenshot(driver, "The Search tab is not displayed; Fail.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    searchTab.click()

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")


    allTab = driver.find_element(By.ID, "b-scopeListItem-web")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    if allTab.is_displayed():
        screenshots["The All tab is displayed; Pass."] = take_screenshot(driver, "The All tab is displayed; Pass.")
    else:
        screenshots["The All tab is not displayed; Fail."] = take_screenshot(driver, "The All tab is not displayed; Fail.")

    allTab.click()

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if driver.title.__eq__("MapleStorySEA Unfunded Amino - Search"):
        screenshots["The Search Results webpage is reached; Pass."] = take_screenshot(driver, "The Search Results webpage is reached; Pass.")
    else:
        screenshots["The Search Results webpage is not reached; Fail."] = take_screenshot(driver, "The Search Results webpage is not reached; Fail.")

    requiredSearchResultLink = driver.find_element(By.PARTIAL_LINK_TEXT, "Featured | [MapleStorySEA] Unfunded Tips")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    for i in range(50):
        requiredSearchResultLink.send_keys(Keys.ARROW_DOWN)

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The bottom of the Search Results webpage is reached; Pass."] = take_screenshot(driver, "The bottom of the Search Results webpage is reached; Pass.")

    for i in range(50):
        requiredSearchResultLink.send_keys(Keys.ARROW_UP
                                           )
    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The top of the Search Results webpage is reached, and the required search result's partialLinkText would now be clicked on; Pass."] = take_screenshot(driver, "The top of the Search Results webpage is reached, and the required search result's partialLinkText would now be clicked on; Pass.")

    requiredSearchResultLink.click()

    for i in range(55555):
        print("Waiting for the loading to be completed.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The Amino webpage has been reached; Pass."] = take_screenshot(driver, "The Amino webpage has been reached; Pass.")

    driver.get("https://aminoapps.com/c/maplestorysea/home/")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The Amino webpage has been reached; Pass."] = take_screenshot(driver, "The Amino webpage has been reached; Pass.")

    aminoSearchBar = driver.find_element(By.CLASS_NAME, "nav-search-input")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if(aminoSearchBar.is_displayed()):
        screenshots["The Amino search bar is displayed; Pass."] = take_screenshot(driver, "The Amino search bar is displayed; Pass.")
    else:
        screenshots["The Amino search bar is not displayed; Fail."] = take_screenshot(driver, "The Amino search bar is not displayed; Fail.")

    aminoSearchBar.send_keys("MapleStorySEA Unfunded Amino")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if(aminoSearchBar.is_displayed()):
        screenshots["The Amino search bar is displayed; Pass."] = take_screenshot(driver, "The Amino search bar is displayed; Pass.")
    else:
        screenshots["The Amino search bar is not displayed; Fail."] = take_screenshot(driver, "The Amino search bar is not displayed; Fail.")

    maplestoryseaUnfundedAminoString = "MapleStorySEA Unfunded Amino"
    maplestoryseaUnfundedAminoStringLength = maplestoryseaUnfundedAminoString.__len__()
    for i in range(maplestoryseaUnfundedAminoStringLength):
        aminoSearchBar.send_keys(Keys.BACK_SPACE)

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if(aminoSearchBar.is_displayed()):
        screenshots["The Amino search bar is displayed; Pass."] = take_screenshot(driver, "The Amino search bar is displayed; Pass.")
    else:
        screenshots["The Amino search bar is not displayed; Fail."] = take_screenshot(driver, "The Amino search bar is not displayed; Fail.")

    aminoSearchBar.send_keys("MapleStorySEA Unfunded Amino")
    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if(aminoSearchBar.is_displayed()):
        screenshots["The Amino search bar is displayed; Pass."] = take_screenshot(driver, "The Amino search bar is displayed; Pass.")
    else:
        screenshots["The Amino search bar is not displayed; Fail."] = take_screenshot(driver, "The Amino search bar is not displayed; Fail.")

    threeWebElementsList = driver.find_elements(By.TAG_NAME, "svg")
    aminoSearchBarMagnifyingGlassButton = threeWebElementsList[0]
    # aminoSearchBar.send_keys("MapleStorySEA Unfunded Amino")
    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if(aminoSearchBarMagnifyingGlassButton.is_displayed()):
        screenshots["The Amino search bar's magnifying glass button is displayed; Pass."] = take_screenshot(driver, "The Amino search bar's magnifying glass button is displayed; Pass.")
    else:
        screenshots["The Amino search bar's magnifying glass button is not displayed; Fail."] = take_screenshot(driver, "The Amino search bar's magnifying glass button is not displayed; Fail.")

    aminoSearchBarMagnifyingGlassButton.click()

    tagNameH3WebElementList = driver.find_elements(By.TAG_NAME, "h3")
    popularPostsText = tagNameH3WebElementList[0]
    popularPostsTextString = popularPostsText.text
    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if popularPostsTextString.__eq__("Popular posts"):
        screenshots["The Popular Posts' section's Popular Posts title is displayed; Pass."] = take_screenshot(driver, "The Popular Posts' section's Popular Posts title is displayed; Pass.")
    else:
        screenshots["The Popular Posts' section's Popular Posts title is not displayed; Fail."] = take_screenshot(driver, "TThe Popular Posts' section's Popular Posts title is not displayed; Fail.")

    driver.get("https://aminoapps.com/c/maplestorysea/home/")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    privacyNoticeAcceptButton = driver.find_element(By.CLASS_NAME, "confirm-close")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    if privacyNoticeAcceptButton.is_displayed():
        screenshots["The Privacy Notice Accept Button is displayed; Pass."] = take_screenshot(driver, "The Privacy Notice Accept Button is displayed; Pass.")
    else:
        screenshots["The Privacy Notice Accept Button is not displayed; Fail."] = take_screenshot(driver, "The Privacy Notice Accept Button is not displayed; Fail.")

    privacyNoticeAcceptButton.click()

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The Privacy Notice pop-up has been closed; Pass."] = take_screenshot(driver, "The Privacy Notice pop-up has been closed; Pass.")

    for i in range(55555):
        print("Still loading.")

    freeCharacterSlotExpansionCoupon = driver.find_element(By.CLASS_NAME, "overflow-hidden")
    if freeCharacterSlotExpansionCoupon.is_displayed():
        screenshots["The Reddit Advice Button is displayed; Pass."] = take_screenshot(driver, "The Reddit Advice Button is displayed; Pass.")
    else:
        screenshots["The Reddit Advice Button is not displayed; Fail."] = take_screenshot(driver, "The Reddit Advice Button is not displayed; Fail.")


    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    freeCharacterSlotExpansionCoupon.click()

    for i in range(55555):
        print("Still loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The Reddit advice webpage is reached; Pass."] = take_screenshot(driver, "The Reddit advice webpage is reached; Pass.")

    driver.get("https://aminoapps.com/c/maplestorysea/home/")

    for i in range(55555):
        print("Still loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["Back to the Home webpage for the first time; Pass"] = take_screenshot(driver, "Back to the Home webpage for the first time; Pass.")

    fourOverflowHiddenClassnameWebElementList = driver.find_elements(By.CLASS_NAME, "overflow-hidden")

    for i in range(55555):
        print("Still loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

    requiredThirdOverflowHiddenClassnameElement = fourOverflowHiddenClassnameWebElementList[2]

    for i in range(55555):
        print("Still loading.")
    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["Back to the Home webpage for the second time; Pass."] = take_screenshot(driver, "Back to the Home webpage for the second time; Pass.")

    if requiredThirdOverflowHiddenClassnameElement.is_displayed():
        screenshots["The Unfunded Training Advice Button is displayed; Pass."] = take_screenshot(driver, "The Unfunded Training Advice Button is displayed; Pass.")
    else:
        screenshots["The Unfunded Training Advice Button is not displayed; Fail."] = take_screenshot(driver, "The Unfunded Training Advice Button is not displayed; Fail.")
    requiredThirdOverflowHiddenClassnameElement.click()

    for i in range(55555):
        print("Still loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The Unfunded Training Advice webpage has been reached; Pass."] = take_screenshot(driver, "The Unfunded Training Advice webpage has been reached; Pass.")

    driver.get("https://aminoapps.com/c/maplestorysea/home/")

    sevenLabelClassnameWebElementList = driver.find_elements(By.CLASS_NAME, "label")
    requiredSecondLabelClassnameElement = sevenLabelClassnameWebElementList[1]

    for i in range(55555):
        print("Still loading.")

    requiredSecondLabelClassnameElement.click()

    for i in range(55555):
        print("Still loading.")

    datetimeTextString = current_datetime_string_generator()
    driver.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
    screenshots["The Latest webpage is displayed; Pass."] = take_screenshot(driver, "The Latest webpage is displayed; Pass.")

    return screenshots
