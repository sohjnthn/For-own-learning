For own learning of IntelliJ IDEA, Java, Selenium, Cucumber, Appium, ExtentReport, and TestNG for finding a manual software tester job in Singapore.

Observation:
For each Java class, "private" can only be provided for the objects above the Java class's methods only if at most one (non-detectable as a WebElement) permission button needs to be manually clicked on.

Therefore, "private" can only be provided for the main Java class; and three page Java classes for testing the Google Chrome desktop web browser websites.

Otherwise, the entire main Java class; and the related page Java classes (for which one of the page Java classes is affected), should not use private for the Java objects.

This happened for the third page Java class for testing the third smartphone application which requires a very long time to click on the non-detectable permissions (the Cucumber Then method of the main Java class, calls the new objects of the second and third smartphone appications, and each page Java class is for each smartphone application in this case), for the testing for the Android smartphone applications with a real Android 15 device.

As searched online, for the real Android testing device, for both before and after any testing, go to the device's Settings, search for "Apps", click on Apps, click on App management, search for "ui", and click on the two UiAutomator2-related apps (only if present) to uninstall both of them.

As it is not possible to correctly click on the correct search result (which cannot be detected by Appium, which detects the entire Webview comprising of the search bar, the tabs near the search bar, and each displayed search result) for the Android - Microsoft Edge Canary web browser - Microsoft Bing search result webpage, it is noticed that trying to attempt a click, always clicks on the next element after the correct element (this refers to the required partialLinkText for the desktop web browser Google Chrome version of the Microsoft Bing search results), so other webpages of the Amino webpage, or a Twitter webpage was accessed.

So the above working changes have been manually edited for this repository.

Thank you.
