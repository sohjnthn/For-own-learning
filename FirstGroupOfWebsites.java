package hellocucumber;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.MediaEntityBuilder;
import com.aventstack.extentreports.Status;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import org.apache.tools.ant.types.resources.First;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.io.FileHandler;

import java.io.File;
import java.io.IOException;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Objects;

public class FirstGroupOfWebsites {

    private String websiteTitle = "";
    private String capturedScreenshotImageFilepathString = "";

    public FirstGroupOfWebsites (ChromeDriver driver, ExtentTest extentTest, ExtentSparkReporter extentSparkReporter, ExtentReports extentReport) throws IOException {
        System.out.println("testing");

        String capturedScreenshotImageFilepathString = new String("");
        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        driver.get("https://demo.guru99.com/");
        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);


        // The web browser tab's title (depends on the website)
        String websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        // Note: Not all web browser tab titles work
        if (Objects.equals(websiteTitle, "Guru99 Bank Home Page")) {
            // requires actual filepath of takeScreenshot(WebDriver object)
            System.out.println("The current web browser tab title is " + "\"" + websiteTitle + "\"; which should be \"Guru99 Bank Home Page\".");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The current web browser tab title is " + "\"" + websiteTitle + "\"; which should be \"Guru99 Bank Home Page\".");
        } else {
            System.out.println("The current web browser tab title cannot be retrieved; which should be \"Guru99 Bank Home Page\".");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The current web browser tab title cannot be retrieved; which should be \"Guru99 Bank Home Page\".");
        }

        WebElement emailInputField = driver.findElement(By.name("emailid"));
        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);
        // check for empty String for email input field value
        //String emailInputFieldText = emailInputField.getText();

        // Only for testing purposes, to ensure that WebElement object.getText() works
        // Capture screenshot image, and input field text value immediately after sending the String to the input field
        if (emailInputField.isDisplayed()) {
            emailInputField.sendKeys("abc@gmail.com");
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
        }

        // actual verification for pass or fail
        // check for email input field value being "abc@gmail.com"
        // emailInputFieldText = emailInputField.getText();
        // Note: Text input field cannot allow Selenium to find the text with WebElement object.getText();
        if (emailInputField.isDisplayed()) {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The email input field value's text is the correct \"abc@gmail.com\".");
        } else {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The email input field value's text is not \"abc@gmail.com\".");
        }

        String emailText = "abc@gmail.com";
        int emailLength = emailText.length();
        // To use backspace to clear the initially entered emailText
        for (int i = 0; i < emailLength; i++) {
            emailInputField.sendKeys(Keys.BACK_SPACE);
        }

        // check for the email input field value being ""
        // emailInputFieldText = emailInputField.getText();
        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);
        if (emailInputField.isDisplayed()) {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The email input field value's text is the correct \"\".");
        } else {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The email input field value's text is not \"\".");
        }

        //emailInputFieldText = emailInputField.getText();
        extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The email input field value \"abc@gmail.com\" has been removed by the Backspace key.");

        emailInputField.sendKeys("abc@gmail.com");
        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        //emailInputFieldText = emailInputField.getText();
        // check for email input field value being "abc@gmail.com"
        if (emailInputField.isDisplayed()) {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The email input field value's text is the correct \"abc@gmail.com\".");
        } else {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The email input field value's text is not \"abc@gmail.com\".");
        }

        // The Submit button
        WebElement submitButton = driver.findElement(By.name("btnLogin"));
        if (submitButton.isDisplayed()) {
            submitButton.click();
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
        }

        // The web browser tab's title (depends on the website)
        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        // Note: Not all web browser tab titles work
        if (Objects.equals(websiteTitle, "Guru99 Bank Home Page")) {
            // requires actual filepath of takeScreenshot(WebDriver object)
            System.out.println("The current web browser tab title is " + "\"" + websiteTitle + "\"; which should be \"Guru99 Bank Home Page\".");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The current web browser tab title is " + "\"" + websiteTitle + "\"; which should be \"Guru99 Bank Home Page\".");
        } else {
            System.out.println("The current web browser tab title cannot be retrieved; which should be \"Guru99 Bank Home Page\".");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The current web browser tab title cannot be retrieved; which should be \"Guru99 Bank Home Page\".");
        }

        driver.get("https://www.bing.com/");
        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        // The web browser tab's title (depends on the website)
        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        // Note: Not all web browser tab titles work
        if (Objects.equals(websiteTitle, "Search - Microsoft Bing")) {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The current web browser tab title is the correct " + "\"" + websiteTitle + "\"; which should be \"Search - Microsoft Bing\".");
        } else {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The current web browser tab title is the incorrect" + "\"" + websiteTitle + "\"; which should be \"Search - Microsoft Bing\".");
        }

        WebElement microsoftBingSearchBar = driver.findElement(By.name("q"));
        // String microsoftBingSearchBarText = microsoftBingSearchBar.getText();
        // Selenium does not allow text input field value to be retrieved with WebElement object.getText();
        // Search bar should initially have an empty String
        if (microsoftBingSearchBar.isDisplayed()) {
            microsoftBingSearchBar.sendKeys("MapleStorySEA (South-East Asia) tips [Facebook notes]");
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
        }

        if (microsoftBingSearchBar.isDisplayed()) {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Microsoft Bing search term input is the correct \"MapleStorySEA (South-East Asia) tips [Facebook notes]\".");
            microsoftBingSearchBar.sendKeys(Keys.ENTER);
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            //capturedScreenshotImageFilepathString = takeScreenshot(driver);
        } else {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The Microsoft Bing search term input is the incorrect \"MapleStorySEA (South-East Asia) tips [Facebook notes]\".");
            microsoftBingSearchBar.sendKeys(Keys.ENTER);
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            //capturedScreenshotImageFilepathString = takeScreenshot(driver);
        }

        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        // Note: Not all web browser tab titles work
        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        // Search engine result Search tab
        // id is based on the line above highlighted text for inspected element
        // Still on the same initial Search Results webpage
        // Should only check for whether the WebElement searchTab is displayed
        //WebElement searchTab = driver.findElement(By.id("b-scopeListItem-copilotsearch"));
        //if (searchTab.isDisplayed()) {
            //searchTab.click();
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            //capturedScreenshotImageFilepathString = takeScreenshot(driver);
            //extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Microsoft Bing search results - Search tab has been reached.");
        //} else {
            //searchTab.click();
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            //capturedScreenshotImageFilepathString = takeScreenshot(driver);
            //extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The Microsoft Bing search results - Search tab has not been reached.");
        //}

        // Go back to All tab from Search tab webpage
        // id is based on the line above highlighted text for inspected element
        //WebElement allTab = driver.findElement(By.id("b-scopeListItem-web"));
        //if (allTab.isDisplayed()) {
            //allTab.click();
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            //capturedScreenshotImageFilepathString = takeScreenshot(driver);
            //extentTest.addScreenCaptureFromPath(capturedScreensh  otImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Microsoft Bing search results - All tab has been reached.");
        //} else {
            //allTab.click();
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            //capturedScreenshotImageFilepathString = takeScreenshot(driver);
            //extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The Microsoft Bing search results - All tab has not been reached.");
        //}

        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        // Note: Not all web browser tab titles work
        //if (Objects.equals(websiteTitle, "MapleStorySEA (South-East Asia) tips [Facebook notes] - Search")){
            //System.out.println("The current web browser tab title is " + "\"" + websiteTitle + "\".");
            //extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Microsoft Bing search results webpage has been reached.");
        //} else {
            //System.out.println("The current web browser tab title cannot be retrieved.");
            //extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The Microsoft Bing search results webpage has not been reached.");
        //}


        // web browser search engine result uses partialLinkText is not working, due to YouTube videos being displayed at the right sometimes
        // Due to video section appearing at the right
        // Which causes less text for the Microsoft Bing search results hyperlink to be displayed
        //WebElement requiredSearchResultLink = driver.findElement(By.partialLinkText("MapleStorySEA (South-East Asia) tips [Facebook notes] - Search"));
        // Use tagName "a" instead
        // Cannot use tagName, keeps changing position in List <WebElement>
        //List <WebElement> tagNameAWebElementList = driver.findElements(By.tagName("a"));
        //WebElement requiredSearchResultLink = tagNameAWebElementList.get(30);
        // String requiredSearchResultPartialLinkTextString = requiredSearchResultPartialLinkText.getText();
        //String requiredSearchResultLinkText = requiredSearchResultLink.getText();
        //if (requiredSearchResultLink.isDisplayed()) {
            //for (int i = 0; i < 50; i++) {
                //requiredSearchResultPartialLinkText.sendKeys(Keys.DOWN);
                //requiredSearchResultLink.sendKeys(Keys.DOWN);
            //}
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            //capturedScreenshotImageFilepathString = takeScreenshot(driver);


            //for (int i = 0; i < 50; i++) {
                //requiredSearchResultPartialLinkText.sendKeys(Keys.UP);
                //requiredSearchResultLink.sendKeys(Keys.UP);
            //}
            //takeScreenshot(driver);

            //requiredSearchResultPartialLinkText.click();
            //requiredSearchResultLink.click();
            //}
        //}

        // Problem: Search engine search result opens in a new web browser tab
        // New ChromeDriver object needs to be created to open a new web browser window
        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        driver.get("https://maplestoryseatips.blogspot.com/");

        String webBrowserTabTitle1 = driver.getTitle();

        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        // For some reason, unable to get the correct web browser title text
        WebElement displayedText = driver.findElement(By.partialLinkText("[MapleStorySEA] Typed some extra things here"));

        if (displayedText.isDisplayed()){
            System.out.println("https://maplestoryseatips.blogspot.com/ is reached");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "https://maplestoryseatips.blogspot.com/ is reached");
        } else {
            System.out.println("https://maplestoryseatips.blogspot.com/ is not reached.");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "https://maplestoryseatips.blogspot.com/ is not reached");
        }

        List<WebElement> toggleList1 = driver.findElements(By.className("post-count-link"));
        // tagName span means 0 to 107
        // tagName a means 0 to 108

        // Note that this is not the arrow to click on, this is only for the text which is at the right of the arrow
        WebElement zippyToggleOpenForTheYear2026 = toggleList1.get(45);

        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        for(int i=0; i<5; i++){
            zippyToggleOpenForTheYear2026.sendKeys(Keys.DOWN);
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
        }

        if (zippyToggleOpenForTheYear2026.isDisplayed()){
            System.out.println("zippyToggleOpenForTheYear2026 is displayed (the className post-count-link of the text 2026 is used for finding the text at the right of the arrow).");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "zippyToggleOpenForTheYear2026 is displayed (the className post-count-link of the text 2026 is used for finding the text at the right of the arrow).");
        } else {
            System.out.println("zippyToggleOpenForTheYear2026 is not displayed (the className post-count-link of the text 2026 is used for finding the text at the right of the arrow).");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "zippyToggleOpenForTheYear2026 is not displayed (the className post-count-link of the text 2026 is used for finding the text at the right of the arrow).");
        }

        List<WebElement> tagAWebElementList = driver.findElements(By.tagName("a"));
        // The actual arrow at the left of the text 2026
        WebElement arrowForToggleOpenForTheYear2026 = tagAWebElementList.get(128);
        // The position should still be 108 (actual 109th as this is from 0 to 108) after the arrow changes to point rightwards.
        arrowForToggleOpenForTheYear2026.click();

        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        WebElement theText2026 = driver.findElement(By.partialLinkText("2026"));
        theText2026.click();

        // For some reason, unable to get the correct web browser title text
        // The following refers to the partialLinkText title of the second note, which should be at the bottom of the webpage
        WebElement displayedText2 = driver.findElement(By.partialLinkText("[MapleStorySEA] Create your own guild to boost all characters' damage ranges"));

        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        if(displayedText2.isDisplayed()){
            System.out.println("The bottommost note for January 2026 is displayed.");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The bottommost note for January 2026 is displayed.");
        }else{
            System.out.println("The bottommost note for January 2026 is not displayed.");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The bottommost note for January 2026 is not displayed..");
        }

        for (int i=0; i<5; i++) {
            displayedText2.sendKeys(Keys.DOWN);
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
        }

        if(displayedText2.isDisplayed()){
            System.out.println("The bottommost note for 2026 is displayed; and is reached.");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The bottommost note for January 2026 is displayed; and is reached.");
        }else{
            System.out.println("The bottommost note for 2026 is not displayed; and is not reached.");
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The bottommost note for January 2026 is not displayed; and is not reached.");
        }

        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);

        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        // Note: Not all web browser tab titles work

        // findElements is for more than one matching object with the same class/name/id/partialLinkText which cannot be uniquely identified
        // Base this on the Inspect - Ctrl+F order or position, search with "" marks
        // className for this case is "overflow-hidden"
        //List<WebElement> sevenLabelClassnameWebElementList = driver.findElements(By.className("label"));
        // Spell Trace and Star Force Enhancement
        //WebElement requiredSecondLabelClassnameElement = sevenLabelClassnameWebElementList.get(1);

        //websiteTitle = driver.getTitle();

        //System.out.println("The website title is \"" + websiteTitle + "\".");

        // Note: Not all web browser tab titles work
    }

    public static String takeScreenshot(WebDriver driver) throws IOException {
        char dayFirstDigitChar = '0';
        char daySecondDigitChar = '0';
        char monthFirstDigitChar = '0';
        char monthSecondDigitChar = '0';
        char yearFirstDigitChar = '0';
        char yearSecondDigitChar = '0';
        char yearThirdDigitChar = '0';
        char yearFourthDigitChar = '0';
        char hourFirstDigitChar = '0';
        char hourSecondDigitChar = '0';
        char minuteFirstDigitChar = '0';
        char minuteSecondDigitChar = '0';
        char secondFirstDigitChar = '0';
        char secondSecondDigitChar = '0';
        char subsecondFirstDigitChar = '0';
        char subsecondSecondDigitChar = '0';
        char subsecondThirdDigitChar = '0';
        char subsecondFourthDigitChar = '0';
        char subsecondFifthDigitChar = '0';
        char subsecondSixthDigitChar = '0';
        // Issue - Missing these three digits
        char subsecondSeventhDigitChar = '0';
        char subsecondEighthDigitChar = '0';
        char subsecondNinthDigitChar = '0';

        LocalDateTime localDateTime = LocalDateTime.now();

        String initialLocalDateTimeString = localDateTime.toString();

        String initialLocalDateTimeStringDaySubstring = initialLocalDateTimeString.substring(8, 10);

        String initialLocalDateTimeStringDashMonthDashSubstring = initialLocalDateTimeString.substring(4, 8);

        String initialLocalDateTimeStringYearSubstring = initialLocalDateTimeString.substring(0, 4);

        // Not providing as (10, 29) which caused an issue, as found out that intialLocalDateTimeString can be have 26, 27, 28, or 29 characters
        String initialLocalDateTimeStringTimeSubString = initialLocalDateTimeString.substring(10);

        String finalLocalDateTimeString = initialLocalDateTimeStringDaySubstring + initialLocalDateTimeStringDashMonthDashSubstring + initialLocalDateTimeStringYearSubstring + initialLocalDateTimeStringTimeSubString;

        if(finalLocalDateTimeString.length()>=1) {
            dayFirstDigitChar = finalLocalDateTimeString.charAt(0);
        }

        if(finalLocalDateTimeString.length()>=2) {
            daySecondDigitChar = finalLocalDateTimeString.charAt(1);
        }

        if(finalLocalDateTimeString.length()>=4) {
            monthFirstDigitChar = finalLocalDateTimeString.charAt(3);
        }

        if(finalLocalDateTimeString.length()>=5) {
            monthSecondDigitChar = finalLocalDateTimeString.charAt(4);
        }

        if(finalLocalDateTimeString.length()>=7) {
            yearFirstDigitChar = finalLocalDateTimeString.charAt(6);
        }

        if(finalLocalDateTimeString.length()>=8) {
            yearSecondDigitChar = finalLocalDateTimeString.charAt(7);
        }

        if(finalLocalDateTimeString.length()>=9) {
            yearThirdDigitChar = finalLocalDateTimeString.charAt(8);
        }

        if(finalLocalDateTimeString.length()>=10) {
            yearFourthDigitChar = finalLocalDateTimeString.charAt(9);
        }

        if(finalLocalDateTimeString.length()>=12) {
            hourFirstDigitChar = finalLocalDateTimeString.charAt(11);
        }

        if(finalLocalDateTimeString.length()>=13){
            hourSecondDigitChar = finalLocalDateTimeString.charAt(12);
        }

        if(finalLocalDateTimeString.length()>=15) {
            minuteFirstDigitChar = finalLocalDateTimeString.charAt(14);
        }

        if(finalLocalDateTimeString.length()>=16) {
            minuteSecondDigitChar = finalLocalDateTimeString.charAt(15);
        }

        if(finalLocalDateTimeString.length()>=18) {
            secondFirstDigitChar = finalLocalDateTimeString.charAt(17);
        }

        if(finalLocalDateTimeString.length()>=19) {
            secondSecondDigitChar = finalLocalDateTimeString.charAt(18);
        }

        if(finalLocalDateTimeString.length()>=21) {
            subsecondFirstDigitChar = finalLocalDateTimeString.charAt(20);
        }

        if(finalLocalDateTimeString.length()>=22) {
            subsecondSecondDigitChar = finalLocalDateTimeString.charAt(21);
        }

        if(finalLocalDateTimeString.length()>=23) {
            subsecondThirdDigitChar = finalLocalDateTimeString.charAt(22);
        }

        if(finalLocalDateTimeString.length()>=24) {
            subsecondFourthDigitChar = finalLocalDateTimeString.charAt(23);
        }

        if(finalLocalDateTimeString.length()>=25) {
            subsecondFifthDigitChar = finalLocalDateTimeString.charAt(24);
        }

        if(finalLocalDateTimeString.length()>=26) {
            subsecondSixthDigitChar = finalLocalDateTimeString.charAt(25);
        }

        if(finalLocalDateTimeString.length()>=27) {
            subsecondSeventhDigitChar = finalLocalDateTimeString.charAt(26);
        }

        if(finalLocalDateTimeString.length()>=28) {
            subsecondEighthDigitChar = finalLocalDateTimeString.charAt(27);
        }

        if(finalLocalDateTimeString.length()>=29) {
            subsecondNinthDigitChar = finalLocalDateTimeString.charAt(28);
        }

        TakesScreenshot screenshot = ((TakesScreenshot) driver);
        File sourceFile = screenshot.getScreenshotAs(OutputType.FILE);
        File destinationFile = new File("C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\Selenium_Screenshot_Images\\" + dayFirstDigitChar + daySecondDigitChar + "-" + monthFirstDigitChar + monthSecondDigitChar + "-" + yearFirstDigitChar + yearSecondDigitChar + yearThirdDigitChar + yearFourthDigitChar + "T" + hourFirstDigitChar + hourSecondDigitChar + minuteFirstDigitChar + minuteSecondDigitChar + secondFirstDigitChar + secondSecondDigitChar + "." + subsecondFirstDigitChar + subsecondSecondDigitChar + subsecondThirdDigitChar + subsecondFourthDigitChar + subsecondFifthDigitChar + subsecondSixthDigitChar + subsecondSeventhDigitChar + subsecondEighthDigitChar + subsecondNinthDigitChar + "_screenshot.png");
        FileHandler.copy(sourceFile, destinationFile);

        return "C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\Selenium_Screenshot_Images\\" + dayFirstDigitChar + daySecondDigitChar + "-" + monthFirstDigitChar + monthSecondDigitChar + "-" + yearFirstDigitChar + yearSecondDigitChar + yearThirdDigitChar + yearFourthDigitChar + "T" + hourFirstDigitChar + hourSecondDigitChar + minuteFirstDigitChar + minuteSecondDigitChar + secondFirstDigitChar + secondSecondDigitChar + "." + subsecondFirstDigitChar + subsecondSecondDigitChar + subsecondThirdDigitChar + subsecondFourthDigitChar + subsecondFifthDigitChar + subsecondSixthDigitChar + subsecondSeventhDigitChar + subsecondEighthDigitChar + subsecondNinthDigitChar + "_screenshot.png";
    }
}
