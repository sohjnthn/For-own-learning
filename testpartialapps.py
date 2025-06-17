from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from datetime import datetime

from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.utils import Keys

androidOptions = UiAutomator2Options()
androidOptions.platform_name = "Android"
androidOptions.automation_name = "UiAutomator2"
androidOptions.platform_version = "15"
androidOptions.app = "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\app\\com.afwsamples.testdpc_9.0.12-9012_minAPI21(nodpi)_apkmirror.com.apk"

driver2 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=androidOptions)

policyManagementText = driver2.find_element(By.XPATH, "//android.widget.TextView[@text=\"Policy management\"]")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver2.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver2.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

androidOptions = UiAutomator2Options()
androidOptions.platform_name = "Android"
androidOptions.automation_name = "UiAutomator2"
androidOptions.platform_version = "15"
androidOptions.app = "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\app\\ApiDemos-debug.apk"

driver3 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=androidOptions)

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver3.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

appTab = driver3.find_element(By.XPATH, "//android.widget.TextView[@content-desc=\"App\"]")
appTab.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver3.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

searchTab = driver3.find_element(By.XPATH, "//android.widget.TextView[@content-desc=\"Search\"]")
searchTab.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver3.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

invokeSearchTab = driver3.find_element(By.XPATH, "//android.widget.TextView[@content-desc=\"Invoke Search\"]")
invokeSearchTab.click()

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver3.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

prefillQueryTextField = driver3.find_element(By.XPATH, "//android.widget.EditText[@resource-id=\"io.appium.android.apis:id/txt_query_prefill\"]")
prefillQueryTextField.send_keys("Test the text.")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver3.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

datetime = datetime.now()
print("datetime is: " + datetime.__str__())
datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")
datetimeTextString = datetimeText.__str__()
print("datetimeText is: " + datetimeTextString)
driver3.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

