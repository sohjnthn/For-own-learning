This webpage:
https://github.com/sohjnthn/For-own-learning

Resume:
https://github.com/sohjnthn/For-own-learning/blob/main/Soh%20Jiong%20Hao%20Resume.pdf

LinkedIn:
https://www.linkedin.com/in/soh-jiong-hao-69aa38186

=

Updated interview introduction text:

"Good morning, my name is Jiong Hao. I am a 5-year manual software tester; and 2-month hardware tester.

For my latest past work for manual software testing, for the client company Prudential, the project PRUForce@Pulse is for the web browser and mobile applications, which are used by the insurance agents, to add leads to their campaigns.

This requires the use of MongoDB for verifying the test records; and LifeAsia for inquiring the test insurance agent, client, and insurance proposal or policy details.

The JIRA numbers, which are the JIRA Story, Requirement, or Epic by the Business Analysts, are distributed by the QA Lead to the QA Team. As a QA, the Microsoft Excel test plan files are created.

For each test case, the Microsoft Excel test results files, which consist of the test steps and the test screenshot images, are uploaded via the JIRA X-Ray plugin, to the JIRA Test - Execute Test webpage - Execution Evidence section.

If a defect is found, a JIRA Test Defect is raised to the related developer. After the defect is resolved, the affected test step would be retested to be pass.

The QA Lead may request for the QA to create the Microsoft Word knowledge transfer files to explain the past tested JIRA numbers' test steps and test screenshot images, to the rest of the QA Team.

For my non-work experience, I have learnt basic automation testing with IntelliJ IDEA, Java, Selenium with the Selenium documentation's page object model, Cucumber, Appium, ExtentReport, TestNG, ChromeDriver, and AndroidDriver; as well as with Webstorm, Python, webdriver.Chrome(), webdriver.Remote(...), and html report by manually running the Python "test_" function.

For the client company DBS, the Intraday Liquidity Management System project, is for using the Finacle (SG) functions to find the monthly repayment amount and the monthly interest, based on the loan tenor or the loan period; and the amount which is owed, which may involve using a collateral such as a property or a vehicle. Also, the ACCP Regional Initiate project is for the Maker and Checker process for Audit confirmation, for Singapore, India, and Indonesia. Moreover, the Singapore - Intelligent Process Automation project is for the processing of the customer's loan requests.

For the client company UOB, the Recycler + Coin Side Car project is for the coin deposit machine; the TMRW project is for the Thailand and Indonesia customers to set their budget; and the GEB NextGen - HK Release project is for the Hong Kong customers to carry out amount transfers and payment of bills by using simplified Chinese. Also, the My Wealth Planner project is for customers to purchase investment products based on their financial situation, and risk appetite. Moreover, the eComm project is for the Thailand and Indonesia customers to be provide their personal and employment details for onboarding, with the assistance of a live agent.

For the company Cube Payment, the work was mainly for carrying out hardware testing for UOB; and GPAP credit card terminal parameters.

In the future, I wish to be able to contribute to your company, and to be able to gain more experience.

Thank you."

=

Updated job search list:

I am looking for a part-time; internship; contract; or permanent job, with no required past work experience, for at least a duration of 3 months, for a monthly salary of $2,000 in Singapore.

[1]

(Including fresh/entry level)

Test/

Associate Test/

Manual/

Manual Test/

Tester/

UAT (User Acceptance Testing)/

Software Test/

Quality Assurance

[2]

Data entry

[3]

Library

[4]

Bank teller

[5]

(Non-retail/sales/warehouse/logistics/charity ambassador)

Grit/

Min A (Minimum A Levels)/

Min Diploma (Minimum Diploma)/

Intern/

Quick Hiring/

No Interview/

No Experience/

Training Provided/

Entry Level/

Solutions/

Career/

Talent/

Hire/

Job/

Gov/

Govt/

Government/

Month contract/

Year contract/

Temp/

Temporary/

Perm/

Permanent/

Office Hours/

Immediate/

Urgent/

Part Time

[6]

(Non-retail/sales/marketing/roadshow/target/
KPI/challenge/accounting/
food and beverage/night-shift)

Attraction/

Administrative/

Admin/

Admin Assistant/

Admin Executive/

Personal Assistant/

Executive Assistant/

Centre admin/

Learning centre admin/

Tuition centre admin/

Centre Administrator/

Education course consultant/

Education advisor/

Teacher/

School/

Education/

SG Ambassador

[7]

(Non-retail/sales/marketing/night-shift)

Healthcare/

Hospital/

Polyclinic/

Billing Assistant Gov Healthcare/

Usher/

Medical/

Healthcare customer service/

Clinic/

Clinic attendant/

Patient/

Patient relationship officer/

Patient service associate/

Ward food service associate/

Clinic assistant/

Dental/

Dental assistant/

Healthcare reception/

Healthcare porter

Thank you.

=

Note:

Amino webpages are no longer accessible from December 2025 onwards.

=

Note:

On 12 October 2025, removed MainWebsites.js (which seems to be the cause of the incorrect screenshot images issue); ran the second and third page JavaScript files for the desktop web browser Google Chrome directly from the related first page JavaSCript file, which did not encounter incorrect screenshot images for the second and third page JavaScript files' html reports.

Even though it is stated that there are initialisation errors, the html reports do not have issues.

The Step names for each of the all three page JavaScript files would still start from Step i, for which i starts from 1.

Noted that it is not possible to run all files parallelly together, if the first page JavaScript file only runs the second page JavaScript file; and the second page JavaScript files.

=

Note:

On 8 October 2025, tried to return testResults (the JavaScript array for 

//{ step: stepNameString, screenshot: screenshotFilenameArray[0], status: 'PASS' };) 

for each of the three page JavaScript files, and tried to create a new report via the main JavaScript file with the following:

const {By, Builder, Browser, Key} = require('selenium-webdriver');

const FirstGroupOfWebsites = require ('./FirstGroupOfWebsites.js');

const SecondGroupOfWebsites = require ('./SecondGroupOfWebsites.js');

const ThirdGroupOfWebsites = require ('./ThirdGroupOfWebsites.js');

const fs = require("fs");

let driver;

async function MainWebsites(){

   driver = await new Builder().forBrowser(Browser.CHROME).build();

   // *Need to run multiple times as the html reports can be incorrect due to overwriting of screenshot images;
   
   // and due to screenshot images being blank if Steps i do not start from 1 for the page JavaScript files.*

   // Steps 1 to 39: This is for the original 39 screenshot images.
   
   const FirstGroupOfWebsites = new FirstGroupOfWebsites();

   // Note: The step numbers i for each page JavaScript file should start from 1,
   
   // so that the screenshot images are displayed (would not be blank) for the html reports from
   
   // the second page JavaScript file onwards

   // Steps 1 to 2: This is only for reaching the Latest tab https://aminoapps.com/c/maplestorysea/recent/ with the driver
   
   const SecondGroupOfWebsites = new SecondGroupOfWebsites();

   // Steps: 1 to 4: This is only for reaching the Home tab https://aminoapps.com/c/maplestorysea/home/ with the driver,
   
   // then going to the Latest tab by locating the text "Latest" (there should be no whitespace characters after > and before < for Inspect)
   
   const ThirdGroupOfWebsites = new ThirdGroupOfWebsites();

   // For each page JavaScript file, only immediately after the first driver.get("..."); statement,
   
   // let title1 = await driver.getTitle(); should be used, so that the first screenshot image of the html report would not be uncaptured
   
   // title1's number 1 can be any number

   // Using for loops to try to cause later (the second and third) page JavaScript files to run actually
   
   // prevents the first page JavaScript file from starting due to the for loop delay

   // Screenshot images for the html reports for the second page JavaScript file onwards can be incorrect

   // Text which are supposed to be entered are sometimes not captured by the screenshot images

   // Does nothing (the fourth html report is not generated)
   
   // const testResults = [...FirstGroupOfWebsites, ...SecondGroupOfWebsites, ...ThirdGroupOfWebsites];

   // Does nothing (the fourth html report is not generated)
   
   // let htmlContent = '<html><body><h1>Test Report</h1>';
   
   // testResults.forEach(result => {
   
   // htmlContent += `<div>
   
   // <p>Step: ${result.step}</p>
   
   // <p>Status: ${result.status}</p>
   
   // <img src="${result.screenshot}" alt="Screenshot" width="300">
   
   // </div>`;
   
   // });
   
   // htmlContent += '</body></html>';

   // fs.writeFileSync('./' + currentDateTime() + '_test-report.html', htmlContent);
   
   // console.log('Report generated: test-report.html');

}

Unfortunately, only three (not four) html reports are created. They seem to be stable now. The second and third html reports finish executing first, and only display the screenshot images if the first step number i starts from 1 (have tried, even with i not starting from 1, such that the screenshot images are displayed blank, only three; and not four html reports are generated).

Therefore, the new JavaScript files and reports would be uploaded, and the non-working code is commented out (including the commented out 

// Does nothing (the fourth html report is not generated)

// return testResults;

statements for the three Page object files).

We can only guarantee that if the commented out lines are uncommented, they do not affect the automation testing.

Have tried, as the physical Android device smartphone applications would keep opening repeatedly with the default starting screens, so the entire testing fails
(should continue to use one single page JavaScript file to test all three smartphone applications). 

=

Note:

On 7 October 2025, noted that viewing the html reports for Java (via Current File - TestNG option); Python (via Current File); and JavaScript do not display the screenshot images if viewed directly via the IDEs.

The screenshot images are only displayed if the html reports are opened via File Explorer, with a web browser.

1. For Python, if only a single JavaScript class is run on its own (via Current File), the screenshot images are only displayed if the html reports are opened via File Explorer, with a web browser.

2. For Python, if we refer to the Google Search - AI Overview, to try to run one single page JavaScript class (any other import and non-import statements for the other two page JavaScript files need to be commented out) in a single async function via the main JavaScript file, the screenshot images are displayed if the html report is opened via File Explorer, with a web browser.

3. For Python, if we refer to the Google Search - AI Overview, to try to run the three separate page JavaScript classes in a single async function via the main JavaScript file, the three Google Chrome web browser windows (each with one single web browser tab) are run at the same time, using for loops would not delay the next function from executing, with all three separate html reports displaying all respective screenshot images.

Since it is not possible to actually possible to use JavaScript to separate into sequential parts, then it is only possible to use this method to run separate test steps or test cases at the same time (parallelly, the step numbers i for each JavaScript file need to start with i, so that the screenshot images for the html reports from the second page JavaScript file onwards would not be blank), such as with the following MainWebsites.js (which would not be provided in the related Microsoft Word file for Selenium with JavaScript due to the issues which cannot be resolved).

*Note: For doing so parallelly, the screenshot images can sometimes be incorrect for the html reports due to overwriting which cannot be controlled; so multiple tries are required with manual visual checking of the screenshot images.*

const {By, Builder, Browser, Key} = require('selenium-webdriver');

const FirstGroupOfWebsites = require ('./FirstGroupOfWebsites.js');

const SecondGroupOfWebsites = require ('./SecondGroupOfWebsites.js');

const ThirdGroupOfWebsites = require ('./ThirdGroupOfWebsites.js');

const fs = require("fs");

let driver;

async function MainWebsites(){

   driver = await new Builder().forBrowser(Browser.CHROME).build();

   // Steps 1 to 39: This is for the original 39 screenshot images.
   
   const FirstGroupOfWebsites = new FirstGroupOfWebsites();

   // Note: The step numbers i for each page JavaScript file should start from 1,
   
   // so that the screenshot images are displayed (would not be blank) for the html reports from
   
   // the second page JavaScript file onwards

   // Steps 1 to 2: This is only for reaching the Latest tab https://aminoapps.com/c/maplestorysea/recent/ with the driver
   
   const SecondGroupOfWebsites = new SecondGroupOfWebsites();

   // Steps: 1 to 4: This is only for reaching the Home tab https://aminoapps.com/c/maplestorysea/home/ with the driver,
   
   // then going to the Latest tab by locating the text "Latest" (there should be no whitespace characters after > and before < for Inspect)

   const ThirdGroupOfWebsites = new ThirdGroupOfWebsites();

   // For each page JavaScript file, only immediately after the first driver.get("..."); statement,
   
   // let title1 = await driver.getTitle(); should be used, so that the first screenshot image of the html report would not be uncaptured
   
   // title1's number 1 can be any number

   // Using for loops to try to cause later (the second and third) page JavaScript files to run actually
   
   // prevents the first page JavaScript file from starting due to the for loop delay
    
   // Screenshot images for the html reports for the second page JavaScript file onwards can be incorrect
    
   // Text which are supposed to be entered are sometimes not captured by the screenshot images
   
}

=

Note:

From 19 September 2025 to 21 September 2025, testing the Java; Python; and JavaScript version for the desktop web browser Google Chrome, has an issue for which a human verification prevents the detection of the All tab (while at the Search tab webpage), for the Microsoft Bing search results webpage for the search term "MapleStorySEA Unfunded Amino".

The only way to bypass this error is to comment out the code lines for finding and clicking on the Search tab (to go to the Search tab webpage), and the All tab (while at the Search tab webpage) - This cannot be done by using the driver to go to another webpage; or by clicking on a valid Inspect identifier. Manually carrying out this does not display the human verification.

It is still not possible to switch the context to "WEBVIEW_chrome" for testing the third Android smartphone application (the Microsoft Edge Canary smartphone application), for Java; and JavaScript.

=

Microsoft Word file for learning Java for basic automation testing - with the Selenium documentation's page object model
(the file is not visible for the webpage, but can be downloaded) - 1 ExtentReport for testing websites; and 1 ExtentReport for testing the three smartphone applications:

https://github.com/sohjnthn/For-own-learning/blob/main/10%20June%202025%20testng.xml%20to%20combine%20both%20feature%20files.docx

Observation:

1) JavaScript can direct to one of the Amino webpages for the Third Android smartphone application which are near the first search result (The Microsoft Edge Canary Android smartphone application) for most of the time; but Java, and Python are unable to do so, for clicking on the search results webpage's WebView directly.

2) JavaScript cannot find the WebElements which need to be found via
let List = driver.findElements(By.---("---"));

It is better to do so using Java; or Python, for the desktop web browser Google Chrome.

3) Python cannot be used to test the Third Android smartphone application as it is a Hybrid App which has a web browser (the application would open, and then close).

4) The JavaScript screenshot images would only be displayed for the Html Report, if the JavaScript screenshot image files are in the same folder as the JavaScript files, and the Html Report.

5) To be able to overcome the restriction for which JavaScript is unable to interact with a WebElement, which can only be found via

let List = driver.findElements(By.---("---"));

Given that the element has displayed text; and the text (which would be displayed in white font colour by inspecting the element) can also be found by inspecting the element for a webpage via a web browser.

We should use 

requiredElement = await driver.findElement(By.xpath("//*[contains(text(), 'Unfunded Training Advice from Level 1 to Level 200?')]"));

So that the element can be clicked on, for example.

requiredElement.click();

This is only applicable for the white text which is directly after ">"; and which is directly before "<". White text with whitespace character(s) before the first letter; and/or after the last letter cannot work (createPostButton is affected).

6) However, it is not possible to do so for non-text WebElements which need to be identified in the same way, for the same identifier, for an Array of at least two WebElements, for JavaScript (aminoHomeIcon is affected).

Will change this accordingly for firstgroupofwebsites.js

Therefore, only the latest Java, Python, and JavaScript Html Reports for the desktop web browser Google Chrome have been uploaded; and the latest JavaScript Html Report for the three Android smartphone applications has been uploaded.

A gentle reminder that only the computer, or laptop which generated the html report, can view the report via a web browser, for which the screenshot images are displayed, only if the screenshot image files are still present.

The html report's screenshot images are not displayed, once it is downloaded to another computer, laptop, or smartphone.

Note:

If the "Spark" ExtentReport file is opened via the IntelliJ IDEA IDE, the images are displayed if the file is opened via a web browser. Thank you.

Microsoft Word file for learning Python for basic automation testing - Without the third smartphone application which is a web browser, as the third smartphone application opens and closes - with the Selenium documentation's page object model
(the file is not visible for the webpage, but can be downloaded) - 1 Html Report for testing websites; and 1 Html Report for testing the first two smartphone applications:
https://github.com/sohjnthn/For-own-learning/blob/main/20%20June%202025%20Webstorm%20Test%20Partially%20With%20Html%20Report%20only%20being%20generated%20if%20WebElement(s)%20can%20be%20found%20-%20Websites%20calls%20Apps.docx

Note:
The Html Report file (if viewed via a web browser) does not display the screenshot images if the file is opened directly from the WebStorm IDE. Please kindly open the file directly via File Explorer to be able to view the screenshot images for the file. Thank you.

Have tried, having difficulties for Webstorm with JavaScript - Only able to automate desktop web browser Google Chrome, but some WebElements cannot be detected; if statements or console.log(...) statements are not working, so unable to use conditions to verify that WebElements are displayed, or find the text for non-input text WebElements, unable to use the Selenium documentation's page object model for JavaScript, able to generate the html report; and unable to open or automate an Android App for Javascript:

https://github.com/sohjnthn/For-own-learning/blob/main/26%20July%202025%20-%20Only%20able%20to%20automate%20desktop%20web%20browser%20Google%20Chrome%2C%20and%20some%20WebElements%20cannot%20be%20detected%20(unable%20to%20automate%20Android%20Apps)..docx

Note:

FirstGroupOfWebsites.java for the IntelliJ IDEA (Community) IDE; and testfirstgroupofwebsites.py for the Webstorm IDE, can cause the laptop to have very slow loading, due to high memory usage for the large file size(s).

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

14. For Webstorm, for testpartialwebsites.py and testpartialapps.py, able to save the screenshot image files by following the Selenium screenshot images, with the screenshot image filenames having the format "dd-mm-yyyy hhmmss.xxxxxx".
    
datetime = datetime.now()

print("datetime is: " + datetime.__str__())

datetimeText = datetime.strftime("%d-%m-%Y %H%M%S.%f")

datetimeTextString = datetimeText.__str__()

print("datetimeText is: " + datetimeTextString)

driver1.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

One extra repeating of the above code lines is required for the last screenshot image to be taken for a driver for the correct UI; unlike IntelliJ IDEA - Java which does not require this to be done, to display the correct UI.

Noting that the third smartphone application opens, and then closes automatically after manually clicking on the permission buttons, for the case of testpartialapps.py, so the related code would be removed.

Found the issue for why the print statements would not be generated if the above code is in a Python function. datetime should be datetimee, excluding for datetime.now()

Unfortunately, unable to actually run a test with ExtentReport; or pytest, even though the displayed UI is correct.

Therefore, searched online for how to create a html report with the taken screenshot images (while keeping the same screenshot image filename format), which requires the import statement:

import os

// This single Python method is the original method for creating the screenshot images which are not for a html report.**

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

// I apologise, the following text's size(s) cannot be reduced.

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

Noting that this report does not state Pass; or Fail, we can add in "; Pass."; or ": Fail." for this report. So it is still possible to use the similar if and else statements as compared to the Java form of the testing.

if policyManagementText.is_displayed():
 screenshots["\"Policy management\" is displayed; Pass."] = take_screenshot(driver2, "\"Policy management\" is displayed; Pass.")
else:
 screenshots["\"Policy management\" is not displayed; Fail."] = take_screenshot(driver2, "\"Policy management\" is not displayed; Fail.")

Due to missing screenshot images for the html report, added in:
for i in range(100):
 print("Waiting for the display to complete the loading.")

The non-report screenshot images' code is still included to be safe.

datetimeTextString = current_datetime_string_generator()
driver2.save_screenshot("C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\Python_Screenshot_Images\\" + datetimeTextString + "_" + "screenshot.png")

For the Webstorm IDE, Python files for the same package are run together, so to run each file alone, temporarily drag the non-related files outside of the package folder. This can be seen for editing the Run configuration. As encountered the issue for which testpartialwebsites.py kept running first before testpartialapps.pay was run; even though only testpartialwebsites.py should be run. Please kindly take note to use the Python Unittests in #PythonFilename# configuration for running each file.
<img width="956" alt="image" src="https://github.com/user-attachments/assets/cdbebb3d-3dde-4612-a984-61701d2864ea" />


At the bottom of each Python file, remember to include the following:
generate_html_report(screenshots)

The opened Google Chrome web browser keeps closing. This should be due to copy and paste mistakes (removing if and else, but keeping the "Pass" message); and due to the Webstorm IDE being unable to detect some WebElements for both the desktop web browser Google Chrome; and the third smartphone application.

Remember to provide unique step_name(s) for each Python file; as only the first time for which the same step-name is used, is reflected in the html report. Do not provide extra duplicate step_name(s), as this causes a lot of time to be wasted.

Additionally, given that testpartialapps.py has less code as compared to testpartialwebsites.py (need to edit the indentation once this is carried out), managed to call a method to execute testpartialapps.py after executing testpartialwebsites.py, such that both Python files' respective html report(s) are generated.

By adding the following to the import statements for testpartialwebsites.py:
from hellocucumber.testpartialapps import test_if_websites_can_call_apps

By adding the method at the bottom of testpartialwebsites.py, directly below testpartialwebsites.py's own 
generate_html_report(screenshots):
test_if_websites_can_call_apps()

The code line 
def test_if_websites_can_call_apps():
, for testpartialapps.py, is directly below the following line:
screenshots = {}

This is done by executing the Python unit test for testpartialwebsites.py

Now able to create the two main Python file(s)' two respective Html Reports.

As manually run by clicking on the run (green right-pointing triangle) for the following testpartialswebsites.py function:
def test_if_websites_can_be_split():
    driver1 = webdriver.Chrome()
    first_websites_screenshots = test_first_group_of_websites(driver1)
    second_websites_screenshots = test_second_group_of_websites(driver1)
    third_websites_screenshots = test_third_group_of_websites(driver1)

    # This is how at least two key-value lists can be merged together into a new list
    # The key is the step String; and the value is the screenshot (file) path
    # This is different from a non-key-value list for which
    # at least two lists can be merged by using
    # newlist = firstlist + lastlist
    # for which the list elements can be retrieved by using
    # newlist[i]
    # for which i is an int number
    # like how a list of WebElements's specific element for the int position (which starts from 0)
    # is retrieved
    screenshots = {**first_websites_screenshots, **second_websites_screenshots, **third_websites_screenshots}
    generate_html_report(screenshots)

    # Only for executing testpartialapps.py
    test_if_websites_can_call_apps()

=

Conclusion: It is better to use IntelliJ IDEA - Java project - build.gradle (Gradle DSL as Groovy) - opensdk-23; or Android Studio -"No Activity" project, with the language "Java", and the build configuration language "Groovy DSL (build.gradle)". Some configurations which cannot run (Eclipse IDE for Java, cannot run Cucumber feature files, and cannot allow URL for testing smartphone applications); or being unable to run driver.get("...) code lines (IntelliJ IDEA - Java - Maven project). There is some issue for which Eclipse - testng.xml's running does not work once the first method for testing the smartphone applications runs.
