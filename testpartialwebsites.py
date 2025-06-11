from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import ImageGrab


driver1 = webdriver.Chrome()

driver1.get("https://demo.guru99.com/")

i = 1
iString = str(i)

screenshot = ImageGrab.grab()
screenshot.save("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + iString + "_" + "screenshot.png")

emailInputField = driver1.find_element(By.NAME, "emailid")

emailInputField.send_keys("abc@gmail.com")

submitButton = driver1.find_element(By.NAME, "btnLogin")

submitButton.click()

driver1.get("https://www.bing.com")

microsoftBingSearchBar = driver1.find_element(By.NAME, "q")

microsoftBingSearchBar.send_keys("MapleStorySEA Unfunded Amino")

microsoftBingSearchBarMagnifyingGlassButton = driver1.find_element(By.ID, "search_icon")

microsoftBingSearchBarMagnifyingGlassButton.click()

driver1.get("https://www.bing.com/search?q=MapleStorySEA+Unfunded+Amino")

searchTab = driver1.find_element(By.ID, "b-scopeListItem-copilotsearch")

searchTab.click()

allTab = driver1.find_element(By.ID, "b-scopeListItem-web")

allTab.click()

requiredSearchResultLink = driver1.find_element(By.PARTIAL_LINK_TEXT, "Featured | [MapleStorySEA] Unfunded Tips")

requiredSearchResultLink.click()

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

aminoSearchBar = driver1.find_element(By.CLASS_NAME, "nav-search-input")

aminoSearchBar.send_keys("MapleStorySEA Unfunded Amino")

threeWebElementsList = driver1.find_elements(By.TAG_NAME, "svg")
aminoSearchBarMagnifyingGlassButton = threeWebElementsList[0]
aminoSearchBarMagnifyingGlassButton.click()

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

privacyNoticeAcceptButton = driver1.find_element(By.CLASS_NAME, "confirm-close")

privacyNoticeAcceptButton.click()

freeCharacterSlotExpansionCoupon = driver1.find_element(By.CLASS_NAME, "overflow-hidden")

freeCharacterSlotExpansionCoupon.click()

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

fourOverflowHiddenClassnameWebElementList = driver1.find_elements(By.CLASS_NAME, "overflow-hidden")

requiredThirdOverflowHiddenClassnameElement = fourOverflowHiddenClassnameWebElementList[2]

requiredThirdOverflowHiddenClassnameElement.click()

driver1.get("https://aminoapps.com/c/maplestorysea/home/")

sevenLabelClassnameWebElementList = driver1.find_elements(By.CLASS_NAME, "label")

requiredSecondLabelClassnameElement = sevenLabelClassnameWebElementList[1]

requiredSecondLabelClassnameElement.click()

driver1.get("https://aminoapps.com/c/maplestorysea/recent/")

driver1.get("https://aminoapps.com/c/maplestorysea/recent/")

tagNameIWebElementList = driver1.find_elements(By.TAG_NAME, "i")
aminoHomeIcon = tagNameIWebElementList[2]
aminoHomeIcon.click()

tagNameButtonWebElementList = driver1.find_elements(By.TAG_NAME, "button")
createPostButton = tagNameButtonWebElementList[1]

tagLine = driver1.find_element(By.CLASS_NAME, "tagline")
taglineText = tagLine.text

i = i + 1
iString = str(i)

screenshot = ImageGrab.grab()
screenshot.save("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + iString + "_" + "screenshot.png")

