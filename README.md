For own learning of IntelliJ IDEA, Java, Selenium, Cucumber, Appium, ExtentReport, and TestNG for finding a manual software tester job in Singapore.

The reason for why the original Selenium_Android project's screenshot image filepath was not accepted, was due to missing "_" characters for the required folder.

Therefore, there is no need to re-create a new Java project.

Similarly, Android Studio, and Eclipse for Java, for the imported IntelliJ IDEA Project "Selenium_Tutorial", would always click on the next partialLinkText (weblink) for the (Microsoft) Edge Canary smartphone application for the Microsoft Bing search results webpage, instead of the correct partialLinkText (weblink) for the desktop Google Chrome web browser - Microsoft Bing search results web page.

Android Studio, and Eclipse for Java are able to display the build.gradle files, so there is no issue for adding; or removing dependencies.

*
Eclipse for Java cannot be used to test for smartphone applications; as URL is not accepted. Only IntelliJ IDEA, and Android Studio accept URL.

DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
desiredCapabilities.setCapability("platformName", "Android");
desiredCapabilities.setCapability("appium:platformVersion", "15.0");
desiredCapabilities.setCapability("appium:app", "C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\app\\com.afwsamples.testdpc_9.0.12-9012_minAPI21(nodpi)_apkmirror.com.apk");
desiredCapabilities.setCapability("appium:automationName", "UiAutomator2");
driver1 = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), desiredCapabilities);

DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
desiredCapabilities.setCapability("platformName", "Android");
desiredCapabilities.setCapability("appium:platformVersion", "15.0");
desiredCapabilities.setCapability("appium:app", "C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\app\\ApiDemos-debug.apk");
desiredCapabilities.setCapability("appium:automationName", "UiAutomator2");
driver2 = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), desiredCapabilities);

desiredCapabilities = new DesiredCapabilities();
desiredCapabilities.setCapability("platformName", "Android");
desiredCapabilities.setCapability("appium:platformVersion", "15.0");
desiredCapabilities.setCapability("appium:app", "C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\app\\com.microsoft.emmx.canary_138.0.3336.0-333600000_minAPI26(armeabi-v7a)(nodpi)_apkmirror.com.apk");
desiredCapabilities.setCapability("appium:automationName", "UiAutomator2");
driver3 = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), desiredCapabilities);
*


The third App (ThirdAppObjects.java), which is the (Microsoft) Edge Canary App, can only work if all for loops for delaying purposes, to prevent errors which occur from the slow loading and manual clicking of permissions, are provided as

for (int i=0; i < 9999999; i++){
  System.out.println("...");
}

This also ensures that while it is not possible to search for the individual web elements like the desktop Google Chrome web browser for the Microsoft Bing search results webpage for the same search term, the correct search term is clicked on for a very less percentage of tries. As tested with the IntelliJ IDEA project "Selenium_Tutorial" 's testng.xml file for running the hellocucumber package's TestDesktopWebsites.java and TestAndroidApps.java. Android Studio still clicked on the next partialLinkText (weblink).

Searched online, would try https://inspector.appiumpro.com/ - Web/Hybrid App Mode button for resolving the third App. Unfortunately, have searched online, switching the context does not help, as the Web/Hybrid App Mode - WebElement still cannot by the running code.

Searched online for how to use IntelliJ IDEA's virtual Android device (Help > Find Action... > Search for "Device Manager"), the virtual Android device is only able to run the first two Apps (and is unable to do so for the third App, which may be a smartphone application which uses both the default mode, and the Web/Hybrid App Mode), but TestAndroidApps.java needs to set the respective code line(s) to

desiredCapabilities.setCapability("appium:platformVersion", "16.0");

(As the Android API level is fixed at 36.0;
still able to click on permission notification buttons manually via Running Devices)

The physical Android testing device uses 

desiredCapabilities.setCapability("appium:platformVersion", "15.0");

(The Android API level is 35.0)

The methods
1. public static String takeScreenshot(WebDriver driver) throws IOException { ... } - Only use this public static String method for the page Java classes
2. public static String currentLocalDateTimeWithDdMmYyFormat() throws IOException { ... } - Only use this public static String method for the main Java classes which call the new page Java classes objects
, are required as the character ':' is not accepted for the filename.
The else { ... } code lines are not required as they are for System.out.println("...");   
Most of the two methods' comment lines are not required.
For String initialLocalDateTimeStringTimeSubString = initialLocalDateTimeString.substring(10);
Do not use (10,29), as initialLocalDateTimeString has 26, 27, 28, or 29 characters
All digit characters are to be initialised to '0', as we would be providing all 29 characters.
Only if a certain number of characters is reached, then each character would be assigned with the detected character.

Declare the following three lines above each Given/When/Then method of the main Java class, which needs to call a new page Java class's object:
@org.junit.Test
@org.junut.jupiter.api.Test
@org.testng.annotations.Test

Sometimes, the third line of the above may be displayed as:
@Test

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

13. Tried to import the IntelliJ IDEA project Selenium_Tutorial (which contains the testng.xml file for running both main Java classes (for the desktop websites; and for the real Android 15 device smarphone applications) to the Eclipse IDE for Java projects. Not able to actually run one of the two feature files, and not able to run the testng.xml file. Cucumber (the feature files' Given, When, and Then lines cannot reach the Java files' related code); and TestNG (red text errors are displayed) are not recognised - Later resolved by forced download for "https://testng.org/testng-1.0.dtd", for the testng.xml file. Each method of the two main Java classes can be run by clicking on Run, for Run | Debug manually; and each main Java class can be run manually by clicking on Run All. The "Spark" ExtentReport went to the target folder of the IntelliJ IDEA project Selenium_Tutorial. This is after searching for the related plugins to install for Selenium, Cucumber, Appium, and TestNG. The testng.xml file can also be run, it seemed that everything was entirely executed, but much slower than for the desktop web browser websites as compared to running each main Java class separately, such that a WebElement for the third method of the main Java class for the desktop web browser websites, was not detected, but was actually reached based on visual inspection. *It would be better to use IntelliJ IDEA to run both the Cucumber feature files; and testng.xml.*

=

Conclusion: It is better to use IntelliJ IDEA - Java project - build.gradle (Gradle DSL as Groovy) - opensdk-23; or Android Studio -"No Activity" project, with the language "Java", and the build configuration language "Groovy DSL (build.gradle)". Some configurations which cannot run (Eclipse IDE for Java, cannot run Cucumber feature files, and cannot allow URL for testing smartphone applications); or being unable to run driver.get("...) code lines (IntelliJ IDEA - Java - Maven project). There is some issue for which Eclipse - testng.xml's running does not work once the first method for testing the smartphone applications runs.
