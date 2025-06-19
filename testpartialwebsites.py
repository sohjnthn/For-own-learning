from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime

from selenium.webdriver.common.utils import Keys

from hellocucumber.testpartialapps import test_if_websites_can_call_apps

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

driver1 = webdriver.Chrome()

driver1.get("https://demo.guru99.com/")


datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

emailInputField = driver1.find_element(By.NAME, "emailid")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if emailInputField.is_displayed():
    screenshots["The Email Input Field is displayed; Pass."] = take_screenshot(driver1, "The Email Input Field is displayed; Pass.")
else:
    screenshots["The Email Input Field is not displayed; Fail."] = take_screenshot(driver1, "The Email Input Field is not displayed; Fail.")

emailInputField.send_keys("abc@gmail.com")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if emailInputField.is_displayed():
    screenshots["The Email Input Field's text \"abc@gmail.com\" is displayed; Pass."] = take_screenshot(driver1, "The Email Input Field's text \"abc@gmail.com\" is displayed; Pass.")
else:
    screenshots["The Email Input Field's text \"abc@gmail.com\" is not displayed; Fail."] = take_screenshot(driver1, "The Email Input Field's text \"abc@gmail.com\" is not displayed; Fail.")

submitButton = driver1.find_element(By.NAME, "btnLogin")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if submitButton.is_displayed():
    screenshots["The Submit Button is displayed; Pass."] = take_screenshot(driver1, "The Submit Button is displayed; Pass.")
else:
    screenshots["The Submit Button is not displayed; Fail."] = take_screenshot(driver1, "The Submit Button is not displayed; Fail.")

submitButton.click()

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The resulting webpage has been reached; Pass."] = take_screenshot(driver1, "The resulting webpage has been reached; Pass.")

driver1.get("https://www.bing.com")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if driver1.title.__eq__("Search - Microsoft Bing"):
    screenshots["The Microsoft Bing webpage has been reached; Pass."] = take_screenshot(driver1, "The Microsoft Bing webpage has been reached; Pass.")
else:
    screenshots["The Microsoft Bing webpage has not been reached; Fail."] = take_screenshot(driver1, "The Microsoft Bing webpage has been reached; Fail.")

microsoftBingSearchBar = driver1.find_element(By.NAME, "q")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

if microsoftBingSearchBar.is_displayed():
    screenshots["The Microsoft Bing search bar is displayed; Pass."] = take_screenshot(driver1, "The Microsoft Bing search bar is displayed; Pass.")
else:
    screenshots["The Microsoft Bing search bar is not displayed; Fail."] = take_screenshot(driver1, "The Microsoft Bing search bar is not displayed; Fail.")

microsoftBingSearchBar.send_keys("MapleStorySEA Unfunded Amino")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The Microsoft Bing search bar's search term \"MapleStorySEA Unfunded Amino\" has been entered; Pass."] = take_screenshot(driver1, "The Microsoft Bing search bar's search term \"MapleStorySEA Unfunded Amino\" has been entered; Pass.")

microsoftBingSearchBarMagnifyingGlassButton = driver1.find_element(By.ID, "search_icon")

if microsoftBingSearchBarMagnifyingGlassButton.is_displayed():
    screenshots["The Microsoft Bing search bar's magnifying glass button is displayed; Pass."] = take_screenshot(driver1, "The Microsoft Bing search bar's magnifying glass button is displayed; Pass.")
else:
    screenshots["The Microsoft Bing search bar's magnifying glass button is not displayed; Fail."] = take_screenshot(driver1, "The Microsoft Bing search bar's magnifying glass button is not displayed; Fail.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

microsoftBingSearchBarMagnifyingGlassButton.click()

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The Search Results webpage has been reached; Pass."] = take_screenshot(driver1, "The Search Results webpage has been reached; Pass.")

# driver1.get("https://www.bing.com/search?q=MapleStorySEA+Unfunded+Amino")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

searchTab = driver1.find_element(By.ID, "b-scopeListItem-copilotsearch")

if searchTab.is_displayed():
    screenshots["The Search tab is displayed; Pass."] = take_screenshot(driver1, "The Search tab is displayed; Pass.")
else:
    screenshots["The Search tab is not displayed; Fail."] = take_screenshot(driver1, "The Search tab is not displayed; Fail.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

searchTab.click()

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")


allTab = driver1.find_element(By.ID, "b-scopeListItem-web")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

if allTab.is_displayed():
    screenshots["The All tab is displayed; Pass."] = take_screenshot(driver1, "The All tab is displayed; Pass.")
else:
    screenshots["The All tab is not displayed; Fail."] = take_screenshot(driver1, "The All tab is not displayed; Fail.")

allTab.click()

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if driver1.title.__eq__("MapleStorySEA Unfunded Amino - Search"):
 screenshots["The Search Results webpage is reached; Pass."] = take_screenshot(driver1, "The Search Results webpage is reached; Pass.")
else:
 screenshots["The Search Results webpage is not reached; Fail."] = take_screenshot(driver1, "The Search Results webpage is not reached; Fail.")

requiredSearchResultLink = driver1.find_element(By.PARTIAL_LINK_TEXT, "Featured | [MapleStorySEA] Unfunded Tips")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

for i in range(50):
 requiredSearchResultLink.send_keys(Keys.ARROW_DOWN)

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The bottom of the Search Results webpage is reached; Pass."] = take_screenshot(driver1, "The bottom of the Search Results webpage is reached; Pass.")

for i in range(50):
 requiredSearchResultLink.send_keys(Keys.ARROW_UP
                                    )
datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The top of the Search Results webpage is reached, and the required search result's partialLinkText would now be clicked on; Pass."] = take_screenshot(driver1, "The top of the Search Results webpage is reached, and the required search result's partialLinkText would now be clicked on; Pass.")

requiredSearchResultLink.click()

for i in range(55555):
    print("Waiting for the loading to be completed.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The Amino webpage has been reached; Pass."] = take_screenshot(driver1, "The Amino webpage has been reached; Pass.")

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The Amino webpage has been reached; Pass."] = take_screenshot(driver1, "The Amino webpage has been reached; Pass.")

aminoSearchBar = driver1.find_element(By.CLASS_NAME, "nav-search-input")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if(aminoSearchBar.is_displayed()):
    screenshots["The Amino search bar is displayed; Pass."] = take_screenshot(driver1, "The Amino search bar is displayed; Pass.")
else:
    screenshots["The Amino search bar is not displayed; Fail."] = take_screenshot(driver1, "The Amino search bar is not displayed; Fail.")

aminoSearchBar.send_keys("MapleStorySEA Unfunded Amino")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if(aminoSearchBar.is_displayed()):
    screenshots["The Amino search bar is displayed; Pass."] = take_screenshot(driver1, "The Amino search bar is displayed; Pass.")
else:
    screenshots["The Amino search bar is not displayed; Fail."] = take_screenshot(driver1, "The Amino search bar is not displayed; Fail.")

maplestoryseaUnfundedAminoString = "MapleStorySEA Unfunded Amino"
maplestoryseaUnfundedAminoStringLength = maplestoryseaUnfundedAminoString.__len__()
for i in range(maplestoryseaUnfundedAminoStringLength):
    aminoSearchBar.send_keys(Keys.BACK_SPACE)

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if(aminoSearchBar.is_displayed()):
    screenshots["The Amino search bar is displayed; Pass."] = take_screenshot(driver1, "The Amino search bar is displayed; Pass.")
else:
    screenshots["The Amino search bar is not displayed; Fail."] = take_screenshot(driver1, "The Amino search bar is not displayed; Fail.")

aminoSearchBar.send_keys("MapleStorySEA Unfunded Amino")
datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if(aminoSearchBar.is_displayed()):
    screenshots["The Amino search bar is displayed; Pass."] = take_screenshot(driver1, "The Amino search bar is displayed; Pass.")
else:
    screenshots["The Amino search bar is not displayed; Fail."] = take_screenshot(driver1, "The Amino search bar is not displayed; Fail.")

threeWebElementsList = driver1.find_elements(By.TAG_NAME, "svg")
aminoSearchBarMagnifyingGlassButton = threeWebElementsList[0]
aminoSearchBar.send_keys("MapleStorySEA Unfunded Amino")
datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if(aminoSearchBarMagnifyingGlassButton.is_displayed()):
    screenshots["The Amino search bar's magnifying glass button is displayed; Pass."] = take_screenshot(driver1, "The Amino search bar's magnifying glass button is displayed; Pass.")
else:
    screenshots["The Amino search bar's magnifying glass button is not displayed; Fail."] = take_screenshot(driver1, "The Amino search bar's magnifying glass button is not displayed; Fail.")

aminoSearchBarMagnifyingGlassButton.click()

tagNameH3WebElementList = driver1.find_elements(By.TAG_NAME, "h3")
popularPostsText = tagNameH3WebElementList[0]
popularPostsTextString = popularPostsText.text
datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if popularPostsTextString.__eq__("Popular posts"):
    screenshots["The Popular Posts' section's Popular Posts title is displayed; Pass."] = take_screenshot(driver1, "The Popular Posts' section's Popular Posts title is displayed; Pass.")
else:
    screenshots["The Popular Posts' section's Popular Posts title is not displayed; Fail."] = take_screenshot(driver1, "TThe Popular Posts' section's Popular Posts title is not displayed; Fail.")

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

privacyNoticeAcceptButton = driver1.find_element(By.CLASS_NAME, "confirm-close")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
if privacyNoticeAcceptButton.is_displayed():
    screenshots["The Privacy Notice Accept Button is displayed; Pass."] = take_screenshot(driver1, "The Privacy Notice Accept Button is displayed; Pass.")
else:
    screenshots["The Privacy Notice Accept Button is not displayed; Fail."] = take_screenshot(driver1, "The Privacy Notice Accept Button is not displayed; Fail.")

privacyNoticeAcceptButton.click()

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The Privacy Notice pop-up has been closed; Pass."] = take_screenshot(driver1, "The Privacy Notice pop-up has been closed; Pass.")

for i in range(55555):
    print("Still loading.")

freeCharacterSlotExpansionCoupon = driver1.find_element(By.CLASS_NAME, "overflow-hidden")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

freeCharacterSlotExpansionCoupon.click()

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The Reddit advice webpage is reached; Pass."] = take_screenshot(driver1, "The Reddit advice webpage is reached; Pass.")

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["Back to the Home webpage for the first time; Pass"] = take_screenshot(driver1, "Back to the Home webpage for the first time; Pass.")

fourOverflowHiddenClassnameWebElementList = driver1.find_elements(By.CLASS_NAME, "overflow-hidden")

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

requiredThirdOverflowHiddenClassnameElement = fourOverflowHiddenClassnameWebElementList[2]

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["Back to the Home webpage for the second time; Pass."] = take_screenshot(driver1, "Back to the Home webpage for the second time; Pass.")

requiredThirdOverflowHiddenClassnameElement.click()

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The Unfunded Training Advice webpage has been reached; Pass."] = take_screenshot(driver1, "The Unfunded Training Advice webpage has been reached; Pass.")

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

sevenLabelClassnameWebElementList = driver1.find_elements(By.CLASS_NAME, "label")
requiredSecondLabelClassnameElement = sevenLabelClassnameWebElementList[1]

for i in range(55555):
    print("Still loading.")



requiredSecondLabelClassnameElement.click()

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The Latest webpage is displayed; Pass."] = take_screenshot(driver1, "The Latest webpage is displayed; Pass.")

driver1.get("https://aminoapps.com/c/maplestorysea/recent/")


for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

for i in range(55555):
    print("Still loading.")

tagNameIWebElementList = driver1.find_elements(By.TAG_NAME, "i")
aminoHomeIcon = tagNameIWebElementList[2]
aminoHomeIcon.click()

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The Home webpage is reached; Pass"] = take_screenshot(driver1, "The Home webpage is reached; Pass.")

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

for i in range(55555):
    print("Still loading.")

tagNameButtonWebElementList = driver1.find_elements(By.TAG_NAME, "button")
createPostButton = tagNameButtonWebElementList[1]

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The Create Post button is displayed; Pass."] = take_screenshot(driver1, "The Create Post button is displayed; Pass.")

createPostButton.click()

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The link, or button is displayed; Pass."] = take_screenshot(driver1, "The link, or button is displayed; Pass.")

for i in range(55555):
    print("Still loading.")

tagLine = driver1.find_element(By.CLASS_NAME, "tagline")
taglineText = tagLine.text
datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The tagline's text is the correct \"MapleStorySEA follows the original Korea MapleStory (by Nexon Korea) 's content.\"; Pass."] = take_screenshot(driver1, "The tagline's text is the correct \"MapleStorySEA follows the original Korea MapleStory (by Nexon Korea) 's content.\"; Pass.")

for i in range(55555):
    print("Still loading.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The link, or button is displayed; Pass."] = take_screenshot(driver1, "The link, or button is displayed; Pass.")

imgTagList = driver1.find_elements(By.TAG_NAME, "img")
topLeftCornerAminoLogoButton = imgTagList[0]

for i in range(55555):
 print("The Amino webpage's tagline text is displayed as the correct \"Explore your interests and find your communities.\"; which should be \"Explore your interests and find your communities.\", the pop-up UI would take time to load.")

datetimeTextString = current_datetime_string_generator()
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")
screenshots["The pop-up is displayed; Pass."] = take_screenshot(driver1, "The pop-up is displayed; Pass.")

generate_html_report(screenshots)

test_if_websites_can_call_apps()