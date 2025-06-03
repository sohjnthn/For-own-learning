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
As compared to an IntelliJ IDEA project, the same build.gradle file's text can be used for the Gradle Scripts - build.gradle (Module: app). However, for Android Studio, please remove the inner text for the following text for this to be able to work. The following text, and all other text which is above, and below can remain.

repositories {
}   

Then, the External Libraries folder would appear, such that the build.gradle (Module: app) is no longer displayed or cannot be found. Taking note that this is not related to the remaining visible build.gradle (#Project Name#) file. So the Android Studio project's dependencies need to be checked carefully before syncing.

3. Remember to rename the packages to "com.example.hellocucumber" for the Java files and the testng.xml file.

4. Noting that the Android Studio project's src folder is under the app folder, similar to the InteliiJ IDEA project, add the Selenium_Screenshot_Images folder, target folder, resources folder, features folder under the resources folder, and the smartphone applications' .apk files directly under the Android Studio project's folder, and under the Android Studio Project's folder, to be safe.

5. It is noted that the Android Studio Project was sometimes able to click on the correct (not detectable by Appium for smartphone applications) partialLinkText. For the IntelliJ IDEA project, the correct partialLinkText was never clicked on, as only the next clickable link is clicked on.

6. As the Android Studio project MyApplication5's "Spark" ExtentReports are not restricted by filepaths, they reached MyApplication5 - app - target folder.

7. The desktop web browser (Google Chrome) screenshot images went to the IntelliJ IDEA project Selenium_Tutorial - Selenium_Screenshot_Images folder
(As Selenium_Tutorial was where the original files were located).

8. The smartphone application (Android 15) screenshot images went to the IntelliJ IDEA project Selenium_Android - Selenium_Screenshot_Images folder
(As Selenium_Android was where the original files were located).

9. The Java files and the testng.xml should still be under the src - test - java - package folder for both IntelliJ IDEA (the package folder is cucumber); and Android Studio (the package folder is com.example.cucumber).

10. The src - test folder, contains the resources folder, which contains the features folder for Selenium_Tutorial.feature; and Selenium_Android.feature.

11. The IntelliJ IDEA project creation should create a New Project as Java, to use the Build System as Gradle, the JDK as openjdk-23, Gradle DSL as Groovy; and should tick (check) the Add sample code checkbox.

12. For the case of the IntelliJ IDEA project creation for creating a New Project as Java, to use the Build System as Maven, the JDK as openjdk-23, and should tick (check) the Add sample code checkbox, following online examples did not work. Instead, going to any Java file's import statements, to click on Add maven dependecy - Maven Artifact Search window - Search for Artifact tab - Type in the first few character of the import statement without the word "import" for the search bar, was able to resolve the import statements and the rest of the red text errors (the selected search result should have the same version, or close to the version of the original build.gradle file dependency). This is *not recommended* as it takes a lot of time to check against the original build.gradle dependencies against the Search for Artifact tab. Unfortunately, *unable to cause this to work* (no more red code text errors) due to the error message which affects every driver.get("..."); code line
"java: cannot access org.openqa.selenium.mobile.NetworkConnection
class file for org.openqa.selenium.mobile.NetworkConnection not found".
Each Given, When, Then line of the feature file can be linked to the correct @Given/@When/@Then("..." of the main Java files, but the features cannot be directly run by using the green >>.

