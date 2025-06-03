For own learning of IntelliJ IDEA, Java, Selenium, Cucumber, Appium, ExtentReport, and TestNG for finding a manual software tester job in Singapore.

Observation:
For each Java class, "private" can only be provided for the objects above the Java class's methods only if at most one (non-detectable as a WebElement) permission button needs to be manually clicked on.

Therefore, "private" can only be provided for the main Java class; and three page Java classes for testing the Google Chrome desktop web browser websites.

Otherwise, the entire main Java class; and the related page Java classes (for which one of the page Java classes is affected), should not use private for the Java objects.

This happened for the third page Java class for testing the third smartphone application which requires a very long time to click on the non-detectable permissions (the Cucumber Then method of the main Java class, calls the new objects of the second and third smartphone appications, and each page Java class is for each smartphone application in this case), for the testing for the Android smartphone applications with a real Android 15 device.

As searched online, for the real Android testing device, for both before and after any testing, go to the device's Settings, search for "Apps", click on Apps, click on App management, search for "ui", and click on the two io.appium.uiautomator2.server apps (only if present) to uninstall both of them.

As it is not possible to correctly click on the correct search result (which cannot be detected by Appium, which detects the entire Webview comprising of the search bar, the tabs near the search bar, and each displayed search result) for the Android - Microsoft Edge Canary web browser - Microsoft Bing search result webpage, it is noticed that trying to attempt a click, always clicks on the next element after the correct element (this refers to the required partialLinkText for the desktop web browser Google Chrome version of the Microsoft Bing search results), so other webpages of the Amino webpage, or a Twitter webpage was accessed.

So the above working changes have been manually edited for this repository.

It is better to add all possible permissions via the Android testing device - Settings - Search for "Apps" - Apps - App Management - Click on the related smartphone applications for testing, to allow all possible permissions, so that the Android testing device can wait for some more time for the case of multiple permission requests which cannot be detected by the Appium Inspector weblink (for example, (Microsoft) Edge Canary from APKMirror for Android 15).

Reasons for why Android Studio cannot allow Cucumber; and TestNG to work, for the same code (use IntelliJ IDEA Community instead):

1. Android Studio may be looking for a different filepath, but the affected page Java class, and its main Java class did not mention the stated filepath. 

2. It is not possible to link the Selenium_Tutorial.feature; and Selenium_Android.feature files to the main Java files which declare the test steps.

3. Even if the "hellocucumber" package folder of IntelliJ IDEA is copied to the Android Studio project, testng.xml for TestNG does not allow "hellocucumber.mainClassNameWithoutDotJava to be used". The hellocucumber package folder for IntelliJ IDEA, becomes a normal directory folder for Android Studio.

Thank you.
