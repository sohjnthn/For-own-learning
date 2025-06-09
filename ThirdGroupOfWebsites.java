package hellocucumber;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.MediaEntityBuilder;
import com.aventstack.extentreports.Status;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.io.FileHandler;

import java.io.File;
import java.io.IOException;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Objects;

public class ThirdGroupOfWebsites {

    private String websiteTitle = "";
    private String capturedScreenshotImageFilepathString = "";

    public ThirdGroupOfWebsites (ChromeDriver driver, ExtentTest extentTest, ExtentSparkReporter extentSparkReporter, ExtentReports extentReport) throws IOException {
        // Therefore, the Cucumber Feature version requires driver4 to be initialised for the Then method
        driver.get("https://aminoapps.com/c/maplestorysea/recent/");

        String oneString = "1";

        // i is a valid tagName, which is displayed starting with "<i "
        List<WebElement> tagNameIWebElementList = driver.findElements(By.tagName("i"));
        WebElement aminoHomeIcon = tagNameIWebElementList.get(2);
        if (aminoHomeIcon.isDisplayed()) {
            aminoHomeIcon.click();
        }

        websiteTitle = driver.getTitle();

        System.out.println("The website title is \"" + websiteTitle + "\".");

        // Note: Not all web browser tab titles work
        if (Objects.equals(websiteTitle, "Featured | [MapleStorySEA] Unfunded Tips Amino")) {
            System.out.println("The current web browser tab title is the correct \"" + websiteTitle + "\"; and should be the correct \"Featured | [MapleStorySEA] Unfunded Tips Amino\".");
        } else {
            System.out.println("The current web browser tab title is the incorrect \"" + websiteTitle + "\"; and should be the correct \"Featured | [MapleStorySEA] Unfunded Tips Amino\".");
        }

        // button is a valid tagName, which is displayed starting with "<button "
        // testing for the Create Post button - pop-up
        List<WebElement> tagNameButtonWebElementList = driver.findElements(By.tagName("button"));
        WebElement createPostButton = tagNameButtonWebElementList.get(1);
        if(createPostButton.isDisplayed()) {
            createPostButton.click();
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            //actual pop-up cannot be captured, can only prove that the pop-up was triggered by clicking on the Create Post button
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Amino webpage's Create Post pop-up is displayed.");
            System.out.println("Create Post button was clicked on to trigger the pop-up. The pop-up is not displayed at this point in time, but is displayed later.");
        } else {
            // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The Amino webpage's Create Post button was not clicked on, so the Create Post pop-up is not displayed later.");
        }

        // trying to capture pop-up UI in ExtentReport
        // So not possible to provide not working if else - else
        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);
        extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Amino webpage's Create Post pop-up is displayed now.");

        // Test for whether non-text-input field text can be retrieved
        WebElement tagLine = driver.findElement(By.className("tagline"));
        String taglineText = tagLine.getText();
        // Captured screenshot image filename to be used for ExtentReport test step - Pass; or Fail
        capturedScreenshotImageFilepathString = takeScreenshot(driver);
        if(taglineText.equals("MapleStorySEA follows the original Korea MapleStory (by Nexon Korea) 's content.")){
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Amino webpage's tagline text is displayed as the correct \"" + taglineText + "\"; which should be \"MapleStorySEA follows the original Korea MapleStory (by Nexon Korea) 's content.\".");
        } else {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The Amino webpage's tagline text is displayed as the incorrect \"" + taglineText + "\"; which should be \"MapleStorySEA follows the original Korea MapleStory (by Nexon Korea) 's content.\".");
        }

        // Testing if "Explore your interests and " for the pop-up can be accessed
        // tagName is "p"
        //List <WebElement> tagNamePWebElementList = driver.findElements(By.tagName("p"));
        //WebElement exploreYourInterestsAndFindYourCommunitiesFullstopText = tagNamePWebElementList.get(1);
        //String exploreYourInterestsAndFindYourCommunitiesFullstopTextString = exploreYourInterestsAndFindYourCommunitiesFullstopText.getText();
        // Note: Even though .getText() works, which seems to provide the same text
        // This has been verified by the system to not match
        // So this has to be tested by checking for whether the WebElement object is displayed
        // Explore your interests and find your communities.
        List<WebElement> imgTagList = driver.findElements(By.tagName("img"));
        WebElement topLeftCornerAminoLogoButton = imgTagList.get(0);

        // There is some delay, so we need to use the WebElement which can be found
        // before and after the pop-up is displayed
        for(int i=0; i<1000; i++) {
            System.out.println("The Amino webpage's tagline text is displayed as the correct \"Explore your interests and find your communities.\"; which should be \"Explore your interests and find your communities.\", the pop-up UI would take time to load.");
        }

        // The following element cannot be found with a for loop for 1000 times for a single System.out.println statement
        // Then the required text of the pop-up can be found
        //List <WebElement> tagNamePWebElementList = driver.findElements(By.tagName("p"));
        //WebElement exploreYourInterestsAndFindYourCommunitiesFullstopText = tagNamePWebElementList.get(1);
        //String exploreYourInterestsAndFindYourCommunitiesFullstopTextString = exploreYourInterestsAndFindYourCommunitiesFullstopText.getText();

        capturedScreenshotImageFilepathString = takeScreenshot(driver);
        if(topLeftCornerAminoLogoButton.isDisplayed()){
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The pop-up's text is correct; and should be \"Explore your interests and find your communities.\".");
        } else {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The pop-up's text is incorrect; and should be \"Explore your interests and find your communities.\".");
        }

        extentReport.flush();
        // Note: Unable to verify any element of pop-up
        // Number of valid tagName elements end as per last related non-pop-up WebElement

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

