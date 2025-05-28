from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from PIL import ImageGrab

androidOptions = UiAutomator2Options()
androidOptions.platform_name = "Android"
androidOptions.automation_name = "UiAutomator2"
androidOptions.platform_version = "15"
androidOptions.app = "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\app\\ApiDemos-debug.apk"

driver2 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=androidOptions)
i = 1
iString = str(i)
screenshot = ImageGrab.grab()
screenshot.save("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + iString + "_" + "screenshot.png")



appTab = driver2.find_element(By.XPATH, "//android.widget.TextView[@content-desc=\"App\"]")
appTab.click()

searchTab = driver2.find_element(By.XPATH, "//android.widget.TextView[@content-desc=\"Search\"]")
searchTab.click()

invokeSearchTab = driver2.find_element(By.XPATH, "//android.widget.TextView[@content-desc=\"Invoke Search\"]")
invokeSearchTab.click()

prefillQueryTextField = driver2.find_element(By.XPATH, "//android.widget.EditText[@resource-id=\"io.appium.android.apis:id/txt_query_prefill\"]")
prefillQueryTextField.send_keys("Test the text.")

i = i + 1
iString = str(i)
screenshot = ImageGrab.grab()
screenshot.save("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + iString + "_" + "screenshot.png")
