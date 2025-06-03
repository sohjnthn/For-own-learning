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

Android Studio is able to use the same files, but with the renaming of the package "com.example.hellocucumber" (screenshot images and ExtentReports are only able to go to the related IntelliJ IDEA projects' related folders):

1. Do not delete all package folders for an Android Studio project (they look similar to the IntelliJ IDEA project package folders), otherwise, a new AndroidStudio project should be created.

2. The new Android Studio project should be created as a "No Activity" project, with the language "Java", and the build configuration language "Groovy DSL (build.gradle)".

3. Remember to rename the packages to "com.example.hellocucumber" for the Java files and the testng.xml file.

4. Noting that the Android Studio project's src folder is under the app folder, similar to the InteliiJ IDEA project, add the Selenium_Screenshot_Images folder, target folder, resources folder, features folder under the resources folder, and the smartphone applications' .apk files directly under the Android Studio project's folder, and under the Android Studio Project's folder, to be safe.

5. It is noted that the Android Studio Project was sometimes able to click on the correct (not detectable by Appium for smartphone applications) partialLinkText. For the IntelliJ IDEA project, the correct partialLinkText was never clicked on, as only the next clickable link is clicked on.

6. As the Android Studio project MyApplication5's "Spark" ExtentReports are not restricted by filepaths, they reached MyApplication5 - app - target folder.

7. The desktop web browser (Google Chrome) screenshot images went to the IntelliJ IDEA project Selenium_Tutorial - Selenium_Screenshot_Images folder.
(As Selenium_Tutorial was where the original files were located.)

8. The smartphone application (Android 15) screenshot images went to the IntelliJ IDEA project Selenium_Android - Selenium_Screenshot_Images folder.
(As Selenium_Android was where the original files were located.)

9. The Java files and the testng.xml should still be under the src - test - java - package folder for both IntelliJ IDEA; and Android Studio.
*1* IntelliJ IDEA package folder name: hellocucumber
*2* Android Studio package folder name: com.example.hellocucumber

11. The src - test folder, contains the resources folder, which contains the features folder for Selenium_Tutorial.feature; and Selenium_Android.feature.
