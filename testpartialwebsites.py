import keyword
from collections.abc import KeysView

from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime

from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.utils import Keys

driver1 = webdriver.Chrome()

driver1.get("https://demo.guru99.com/")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

emailInputField = driver1.find_element(By.NAME, "emailid")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

emailInputField.send_keys("abc@gmail.com")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

submitButton = driver1.find_element(By.NAME, "btnLogin")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

submitButton.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

driver1.get("https://www.bing.com")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

microsoftBingSearchBar = driver1.find_element(By.NAME, "q")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

microsoftBingSearchBar.send_keys("MapleStorySEA Unfunded Amino")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

microsoftBingSearchBarMagnifyingGlassButton = driver1.find_element(By.ID, "search_icon")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

microsoftBingSearchBarMagnifyingGlassButton.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

driver1.get("https://www.bing.com/search?q=MapleStorySEA+Unfunded+Amino")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

searchTab = driver1.find_element(By.ID, "b-scopeListItem-copilotsearch")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

searchTab.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

allTab = driver1.find_element(By.ID, "b-scopeListItem-web")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

allTab.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

requiredSearchResultLink = driver1.find_element(By.PARTIAL_LINK_TEXT, "Featured | [MapleStorySEA] Unfunded Tips")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

for i in range(50):
 requiredSearchResultLink.send_keys(Keys.ARROW_DOWN)

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

for i in range(50):
    requiredSearchResultLink.send_keys(Keys.ARROW_UP
                                       )
datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")


requiredSearchResultLink.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

aminoSearchBar = driver1.find_element(By.CLASS_NAME, "nav-search-input")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

aminoSearchBar.send_keys("MapleStorySEA Unfunded Amino")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

threeWebElementsList = driver1.find_elements(By.TAG_NAME, "svg")
aminoSearchBarMagnifyingGlassButton = threeWebElementsList[0]
aminoSearchBarMagnifyingGlassButton.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

privacyNoticeAcceptButton = driver1.find_element(By.CLASS_NAME, "confirm-close")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

privacyNoticeAcceptButton.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

freeCharacterSlotExpansionCoupon = driver1.find_element(By.CLASS_NAME, "overflow-hidden")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

freeCharacterSlotExpansionCoupon.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

fourOverflowHiddenClassnameWebElementList = driver1.find_elements(By.CLASS_NAME, "overflow-hidden")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

requiredThirdOverflowHiddenClassnameElement = fourOverflowHiddenClassnameWebElementList[2]

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

requiredThirdOverflowHiddenClassnameElement.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

sevenLabelClassnameWebElementList = driver1.find_elements(By.CLASS_NAME, "label")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

requiredSecondLabelClassnameElement = sevenLabelClassnameWebElementList[1]

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

requiredSecondLabelClassnameElement.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

driver1.get("https://aminoapps.com/c/maplestorysea/recent/")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

tagNameIWebElementList = driver1.find_elements(By.TAG_NAME, "i")
aminoHomeIcon = tagNameIWebElementList[2]
aminoHomeIcon.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

tagNameButtonWebElementList = driver1.find_elements(By.TAG_NAME, "button")
createPostButton = tagNameButtonWebElementList[1]

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

createPostButton.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

tagLine = driver1.find_element(By.CLASS_NAME, "tagline")
taglineText = tagLine.text

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

imgTagList = driver1.find_elements(By.TAG_NAME, "img")
topLeftCornerAminoLogoButton = imgTagList[0]

for i in range(1000):
 print("The Amino webpage's tagline text is displayed as the correct \"Explore your interests and find your communities.\"; which should be \"Explore your interests and find your communities.\", the pop-up UI would take time to load.")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")


