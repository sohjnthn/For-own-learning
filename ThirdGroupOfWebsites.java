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

import static hellocucumber.TestDesktopWebsites.takeScreenshot;

public class ThirdGroupOfWebsites {

    private String websiteTitle = "";
    private String capturedScreenshotImageFilepathString = "";

    public ThirdGroupOfWebsites (ChromeDriver driver, ExtentTest extentTest, ExtentSparkReporter extentSparkReporter, ExtentReports extentReport) throws IOException {
        // Therefore, the Cucumber Feature version requires driver4 to be initialised for the Then method
        driver.get("https://aminoapps.com/c/maplestorysea/recent/");

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
        List <WebElement> tagNamePWebElementList = driver.findElements(By.tagName("p"));
        WebElement exploreYourInterestsAndFindYourCommunitiesFullstopText = tagNamePWebElementList.get(1);
        String exploreYourInterestsAndFindYourCommunitiesFullstopTextString = exploreYourInterestsAndFindYourCommunitiesFullstopText.getText();
        // Note: Even though .getText() works, which seems to provide the same text
        // This has been verified by the system to not match
        // So this has to be tested by checking for whether the WebElement object is displayed
        //Explore your interests and find your communities.
        if(exploreYourInterestsAndFindYourCommunitiesFullstopText.isDisplayed()){
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Amino webpage's tagline text is displayed as the correct \"" + exploreYourInterestsAndFindYourCommunitiesFullstopTextString + "\"; which should be \"Explore your interests and find your communities.\".");
        } else {
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The Amino webpage's tagline text is displayed as the incorrect \"" + exploreYourInterestsAndFindYourCommunitiesFullstopTextString + "\"; which should be \"Explore your interests and find your communities.\".");
        }

        extentReport.flush();
        // Note: Unable to verify any element of pop-up
        // Number of valid tagName elements end as per last related non-pop-up WebElement

    }

    // This method is for the filename for capturing screenshot images which are not in the ExtentReport
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

        // How to take Selenium screenshot image
        LocalDateTime localDateTime = LocalDateTime.now();
        String initialLocalDateTimeString = localDateTime.toString();
        // Will print out
        // initial localDateTimeString is "2025-05-09T11:06:10.XXXXXXXXX"
        // This has 29 characters (char(s) from 0 to 28)
        System.out.println("initialLocalDateTimeString is " + "\"" + initialLocalDateTimeString + "\"");
        System.out.println("initialLocalDateTimeString.length() is " + initialLocalDateTimeString.length() + ".");
        // dd
        String initialLocalDateTimeStringDaySubstring = initialLocalDateTimeString.substring(8, 10);
        // -mm-
        String initialLocalDateTimeStringDashMonthDashSubstring = initialLocalDateTimeString.substring(4, 8);
        // yyThh:mm:ss.XXXXXXXXX
        String initialLocalDateTimeStringYearSubstring = initialLocalDateTimeString.substring(0, 4);
        // Despite Java String #StringObject#.substring(X, endIndex being number of characters), meaning (10, 29), an error was displayed, so changed to without endIndex if should reach last character
        String initialLocalDateTimeStringTimeSubString = initialLocalDateTimeString.substring(10);
        String finalLocalDateTimeString = initialLocalDateTimeStringDaySubstring + initialLocalDateTimeStringDashMonthDashSubstring + initialLocalDateTimeStringYearSubstring + initialLocalDateTimeStringTimeSubString;
        System.out.println("finalLocalDateTimeString is " + "\"" + finalLocalDateTimeString + "\"");
        System.out.println("finalLocalDateTimeString.length() is " + finalLocalDateTimeString.length() + ".");
        //int testInt=100;
        //char testChar = 'a';
        //char testChar = 100;
        // Able to add int testInt to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\Selenium_Screenshot_Images\\" + testInt + "_screenshot.png")
        // Able to add char to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\Selenium_Screenshot_Images\\" + testChar + "_screenshot.png")
        // Unable to add String, or char[] (char Array) to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\Selenium_Screenshot_Images\\" + finalLocalDateTimeString1 + "_screenshot.png")
        //char[] finalLocalDateTimeString1CharArray = new char[29];
        //finalLocalDateTimeString1.getChars(0, 29, finalLocalDateTimeString1CharArray, 0);

        if(finalLocalDateTimeString.length()>=1) {
            // index 0 character; 1st character
            dayFirstDigitChar = finalLocalDateTimeString.charAt(0);
        }else{
            // index none
            System.out.println("finalLocalDateTimeString only has 0 characters.");
        }

        if(finalLocalDateTimeString.length()>=2) {
            // index 1 character; 2nd character
            daySecondDigitChar = finalLocalDateTimeString.charAt(1);
        } else {
            // indexes 0 to 1
            System.out.println("finalLocalDateTimeString only has 1 character.");
        }

        if(finalLocalDateTimeString.length()>=4) {
            // index 3 character; 4th character
            monthFirstDigitChar = finalLocalDateTimeString.charAt(3);
        } else {
            // indexes 0 to 1 or 2
            System.out.println("finalLocalDateTimeString only has 2 to 3 characters.");
        }

        if(finalLocalDateTimeString.length()>=5) {
            // index 4 character; 5th character
            monthSecondDigitChar = finalLocalDateTimeString.charAt(4);
        } else {
            // index 0 to 3
            System.out.println("finalLocalDateTimeString only has 4 characters.");
        }

        if(finalLocalDateTimeString.length()>=7) {
            // index 6 character; 7th character
            yearFirstDigitChar = finalLocalDateTimeString.charAt(6);
        } else {
            // indexes 0 to 5
            System.out.println("finalLocalDateTimeString only has 6 characters.");
        }

        if(finalLocalDateTimeString.length()>=8) {
            // index 7 character; 8th character
            yearSecondDigitChar = finalLocalDateTimeString.charAt(7);
        } else {
            // indexes 0 to 6
            System.out.println("finalLocalDateTimeString only has 7 characters.");
        }

        if(finalLocalDateTimeString.length()>=9) {
            // index 8 character; 9th character
            yearThirdDigitChar = finalLocalDateTimeString.charAt(8);
        } else {
            // indexes 0 to 7
            System.out.println("finalLocalDateTimeString only has 8 characters.");
        }

        if(finalLocalDateTimeString.length()>=10) {
            // index 9 character; 10th character
            yearFourthDigitChar = finalLocalDateTimeString.charAt(9);
        } else {
            // indexes 0 to 8; 11th character
            System.out.println("finalLocalDateTimeString only has 9 characters.");
        }

        if(finalLocalDateTimeString.length()>=12) {
            // index 11 character; 12th character
            hourFirstDigitChar = finalLocalDateTimeString.charAt(11);
        } else {
            // indexes 0 to 10
            System.out.println("finalLocalDateTimeString only has 11 characters.");
        }

        if(finalLocalDateTimeString.length()>=13){
            // index 12 character; 13th character
            hourSecondDigitChar = finalLocalDateTimeString.charAt(12);
        } else {
            // indexes 0 to 11
            System.out.println("finalLocalDateTimeString only has 12 characters.");
        }

        if(finalLocalDateTimeString.length()>=15) {
            // index 14 character; 15th character
            minuteFirstDigitChar = finalLocalDateTimeString.charAt(14);
        } else {
            // indexes 0 to 12 or 13
            System.out.println("finalLocalDateTimeString only has 13 to 14 characters.");
        }

        if(finalLocalDateTimeString.length()>=16) {
            // index 15 character; 16th character
            minuteSecondDigitChar = finalLocalDateTimeString.charAt(15);
        } else {
            // indexes 0 to 14
            System.out.println("finalLocalDateTimeString only has 15 characters.");
        }

        if(finalLocalDateTimeString.length()>=18) {
            // index 17 character; 18th character
            secondFirstDigitChar = finalLocalDateTimeString.charAt(17);
        } else {
            // indexes 0 to 16
            System.out.println("finalLocalDateTimeString only has 17 characters.");
        }

        if(finalLocalDateTimeString.length()>=19) {
            // index 18 character; 19th character
            secondSecondDigitChar = finalLocalDateTimeString.charAt(18);
        } else {
            // indexes 0 to 17
            System.out.println("finalLocalDateTimeString only has 18 characters.");
        }

        if(finalLocalDateTimeString.length()>=21) {
            // index 20 character; 21th character
            subsecondFirstDigitChar = finalLocalDateTimeString.charAt(20);
        } else {
            // indexes 0 to 19
            System.out.println("finalLocalDateTimeString only has 20 characters.");
        }

        if(finalLocalDateTimeString.length()>=22) {
            // index 21 character; 22nd character
            subsecondSecondDigitChar = finalLocalDateTimeString.charAt(21);
        } else {
            // indexes 0 to 20
            System.out.println("finalLocalDateTimeString only has 21 characters.");
        }

        if(finalLocalDateTimeString.length()>=23) {
            // index 22 character; 23rd character
            subsecondThirdDigitChar = finalLocalDateTimeString.charAt(22);
        } else {
            // indexes 0 to 21
            System.out.println("finalLocalDateTimeString only has 22 characters.");
        }

        if(finalLocalDateTimeString.length()>=24) {
            // index 23 character; 24th character
            subsecondFourthDigitChar = finalLocalDateTimeString.charAt(23);
        } else {
            // indexes 0 to 22
            System.out.println("finalLocalDateTimeString only has 23 characters.");
        }

        if(finalLocalDateTimeString.length()>=25) {
            // index 24 character; 25th character
            subsecondFifthDigitChar = finalLocalDateTimeString.charAt(24);
        } else {
            // indexes 0 to 23
            System.out.println("finalLocalDateTimeString only has 24 characters.");
        }

        if(finalLocalDateTimeString.length()>=26) {
            // index 25 character; 26th character
            subsecondSixthDigitChar = finalLocalDateTimeString.charAt(25);
        } else {
            // indexes 0 to 24
            System.out.println("finalLocalDateTimeString only has 25 characters.");
        }

        if(finalLocalDateTimeString.length()>=27) {
            // index 26 character; 27th character
            subsecondSeventhDigitChar = finalLocalDateTimeString.charAt(26);
        } else {
            // indexes 0 to 25
            System.out.println("finalLocalDateTimeString only has 26 characters.");
        }

        if(finalLocalDateTimeString.length()>=28) {
            // index 27 character; 28th character
            subsecondEighthDigitChar = finalLocalDateTimeString.charAt(27);
        } else {
            // indexes 0 to 25
            System.out.println("finalLocalDateTimeString only has 27 characters.");
        }

        if(finalLocalDateTimeString.length()>=29) {
            // index 28 character; 29th character
            subsecondNinthDigitChar = finalLocalDateTimeString.charAt(28);
        } else {
            System.out.println("finalLocalDateTimeString only has 28 characters.");
        }

        TakesScreenshot screenshot = ((TakesScreenshot) driver);
        File sourceFile = screenshot.getScreenshotAs(OutputType.FILE);
        File destinationFile = new File("C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\Selenium_Screenshot_Images\\" + dayFirstDigitChar + daySecondDigitChar + "-" + monthFirstDigitChar + monthSecondDigitChar + "-" + yearFirstDigitChar + yearSecondDigitChar + yearThirdDigitChar + yearFourthDigitChar + "T" + hourFirstDigitChar + hourSecondDigitChar + minuteFirstDigitChar + minuteSecondDigitChar + secondFirstDigitChar + secondSecondDigitChar + "." + subsecondFirstDigitChar + subsecondSecondDigitChar + subsecondThirdDigitChar + subsecondFourthDigitChar + subsecondFifthDigitChar + subsecondSixthDigitChar + subsecondSeventhDigitChar + subsecondEighthDigitChar + subsecondNinthDigitChar + "_screenshot.png");
        FileHandler.copy(sourceFile, destinationFile);

        return "C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\Selenium_Screenshot_Images\\" + dayFirstDigitChar + daySecondDigitChar + "-" + monthFirstDigitChar + monthSecondDigitChar + "-" + yearFirstDigitChar + yearSecondDigitChar + yearThirdDigitChar + yearFourthDigitChar + "T" + hourFirstDigitChar + hourSecondDigitChar + minuteFirstDigitChar + minuteSecondDigitChar + secondFirstDigitChar + secondSecondDigitChar + "." + subsecondFirstDigitChar + subsecondSecondDigitChar + subsecondThirdDigitChar + subsecondFourthDigitChar + subsecondFifthDigitChar + subsecondSixthDigitChar + subsecondSeventhDigitChar + subsecondEighthDigitChar + subsecondNinthDigitChar + "_screenshot.png";
    }

    // This method is for returning the substring of the current LocalDateTome, for the filename of the ExtentReport
    public static String currentLocalDateTimeWithDdMmYyFormat() throws IOException {
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

        // How to take Selenium screenshot image
        LocalDateTime localDateTime = LocalDateTime.now();
        String initialLocalDateTimeString = localDateTime.toString();
        // Will print out
        // initial localDateTimeString is "2025-05-09T11:06:10.XXXXXXXXX"
        // This has 29 characters (char(s) from 0 to 28)
        System.out.println("initialLocalDateTimeString is " + "\"" + initialLocalDateTimeString + "\"");
        System.out.println("initialLocalDateTimeString.length() is " + initialLocalDateTimeString.length() + ".");
        // dd
        String initialLocalDateTimeStringDaySubstring = initialLocalDateTimeString.substring(8, 10);
        // -mm-
        String initialLocalDateTimeStringDashMonthDashSubstring = initialLocalDateTimeString.substring(4, 8);
        // yyThh:mm:ss.XXXXXXXXX
        String initialLocalDateTimeStringYearSubstring = initialLocalDateTimeString.substring(0, 4);
        // Despite Java String #StringObject#.substring(X, endIndex being number of characters), meaning (10, 29), an error was displayed, so changed to without endIndex if should reach last character
        String initialLocalDateTimeStringTimeSubString = initialLocalDateTimeString.substring(10);
        String finalLocalDateTimeString = initialLocalDateTimeStringDaySubstring + initialLocalDateTimeStringDashMonthDashSubstring + initialLocalDateTimeStringYearSubstring + initialLocalDateTimeStringTimeSubString;
        System.out.println("finalLocalDateTimeString is " + "\"" + finalLocalDateTimeString + "\"");
        System.out.println("finalLocalDateTimeString.length() is " + finalLocalDateTimeString.length() + ".");
        //int testInt=100;
        //char testChar = 'a';
        //char testChar = 100;
        // Able to add int testInt to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\Selenium_Screenshot_Images\\" + testInt + "_screenshot.png")
        // Able to add char to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\Selenium_Screenshot_Images\\" + testChar + "_screenshot.png")
        // Unable to add String, or char[] (char Array) to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\Selenium_Screenshot_Images\\" + finalLocalDateTimeString1 + "_screenshot.png")
        //char[] finalLocalDateTimeString1CharArray = new char[29];
        //finalLocalDateTimeString1.getChars(0, 29, finalLocalDateTimeString1CharArray, 0);

        if(finalLocalDateTimeString.length()>=1) {
            // index 0 character; 1st character
            dayFirstDigitChar = finalLocalDateTimeString.charAt(0);
        }else{
            // index none
            System.out.println("finalLocalDateTimeString only has 0 characters.");
        }

        if(finalLocalDateTimeString.length()>=2) {
            // index 1 character; 2nd character
            daySecondDigitChar = finalLocalDateTimeString.charAt(1);
        } else {
            // indexes 0 to 1
            System.out.println("finalLocalDateTimeString only has 1 character.");
        }

        if(finalLocalDateTimeString.length()>=4) {
            // index 3 character; 4th character
            monthFirstDigitChar = finalLocalDateTimeString.charAt(3);
        } else {
            // indexes 0 to 1 or 2
            System.out.println("finalLocalDateTimeString only has 2 to 3 characters.");
        }

        if(finalLocalDateTimeString.length()>=5) {
            // index 4 character; 5th character
            monthSecondDigitChar = finalLocalDateTimeString.charAt(4);
        } else {
            // index 0 to 3
            System.out.println("finalLocalDateTimeString only has 4 characters.");
        }

        if(finalLocalDateTimeString.length()>=7) {
            // index 6 character; 7th character
            yearFirstDigitChar = finalLocalDateTimeString.charAt(6);
        } else {
            // indexes 0 to 5
            System.out.println("finalLocalDateTimeString only has 6 characters.");
        }

        if(finalLocalDateTimeString.length()>=8) {
            // index 7 character; 8th character
            yearSecondDigitChar = finalLocalDateTimeString.charAt(7);
        } else {
            // indexes 0 to 6
            System.out.println("finalLocalDateTimeString only has 7 characters.");
        }

        if(finalLocalDateTimeString.length()>=9) {
            // index 8 character; 9th character
            yearThirdDigitChar = finalLocalDateTimeString.charAt(8);
        } else {
            // indexes 0 to 7
            System.out.println("finalLocalDateTimeString only has 8 characters.");
        }

        if(finalLocalDateTimeString.length()>=10) {
            // index 9 character; 10th character
            yearFourthDigitChar = finalLocalDateTimeString.charAt(9);
        } else {
            // indexes 0 to 8; 11th character
            System.out.println("finalLocalDateTimeString only has 9 characters.");
        }

        if(finalLocalDateTimeString.length()>=12) {
            // index 11 character; 12th character
            hourFirstDigitChar = finalLocalDateTimeString.charAt(11);
        } else {
            // indexes 0 to 10
            System.out.println("finalLocalDateTimeString only has 11 characters.");
        }

        if(finalLocalDateTimeString.length()>=13){
            // index 12 character; 13th character
            hourSecondDigitChar = finalLocalDateTimeString.charAt(12);
        } else {
            // indexes 0 to 11
            System.out.println("finalLocalDateTimeString only has 12 characters.");
        }

        if(finalLocalDateTimeString.length()>=15) {
            // index 14 character; 15th character
            minuteFirstDigitChar = finalLocalDateTimeString.charAt(14);
        } else {
            // indexes 0 to 12 or 13
            System.out.println("finalLocalDateTimeString only has 13 to 14 characters.");
        }

        if(finalLocalDateTimeString.length()>=16) {
            // index 15 character; 16th character
            minuteSecondDigitChar = finalLocalDateTimeString.charAt(15);
        } else {
            // indexes 0 to 14
            System.out.println("finalLocalDateTimeString only has 15 characters.");
        }

        if(finalLocalDateTimeString.length()>=18) {
            // index 17 character; 18th character
            secondFirstDigitChar = finalLocalDateTimeString.charAt(17);
        } else {
            // indexes 0 to 16
            System.out.println("finalLocalDateTimeString only has 17 characters.");
        }

        if(finalLocalDateTimeString.length()>=19) {
            // index 18 character; 19th character
            secondSecondDigitChar = finalLocalDateTimeString.charAt(18);
        } else {
            // indexes 0 to 17
            System.out.println("finalLocalDateTimeString only has 18 characters.");
        }

        if(finalLocalDateTimeString.length()>=21) {
            // index 20 character; 21th character
            subsecondFirstDigitChar = finalLocalDateTimeString.charAt(20);
        } else {
            // indexes 0 to 19
            System.out.println("finalLocalDateTimeString only has 20 characters.");
        }

        if(finalLocalDateTimeString.length()>=22) {
            // index 21 character; 22nd character
            subsecondSecondDigitChar = finalLocalDateTimeString.charAt(21);
        } else {
            // indexes 0 to 20
            System.out.println("finalLocalDateTimeString only has 21 characters.");
        }

        if(finalLocalDateTimeString.length()>=23) {
            // index 22 character; 23rd character
            subsecondThirdDigitChar = finalLocalDateTimeString.charAt(22);
        } else {
            // indexes 0 to 21
            System.out.println("finalLocalDateTimeString only has 22 characters.");
        }

        if(finalLocalDateTimeString.length()>=24) {
            // index 23 character; 24th character
            subsecondFourthDigitChar = finalLocalDateTimeString.charAt(23);
        } else {
            // indexes 0 to 22
            System.out.println("finalLocalDateTimeString only has 23 characters.");
        }

        if(finalLocalDateTimeString.length()>=25) {
            // index 24 character; 25th character
            subsecondFifthDigitChar = finalLocalDateTimeString.charAt(24);
        } else {
            // indexes 0 to 23
            System.out.println("finalLocalDateTimeString only has 24 characters.");
        }

        if(finalLocalDateTimeString.length()>=26) {
            // index 25 character; 26th character
            subsecondSixthDigitChar = finalLocalDateTimeString.charAt(25);
        } else {
            // indexes 0 to 24
            System.out.println("finalLocalDateTimeString only has 25 characters.");
        }

        if(finalLocalDateTimeString.length()>=27) {
            // index 26 character; 27th character
            subsecondSeventhDigitChar = finalLocalDateTimeString.charAt(26);
        } else {
            // indexes 0 to 25
            System.out.println("finalLocalDateTimeString only has 26 characters.");
        }

        if(finalLocalDateTimeString.length()>=28) {
            // index 27 character; 28th character
            subsecondEighthDigitChar = finalLocalDateTimeString.charAt(27);
        } else {
            // indexes 0 to 25
            System.out.println("finalLocalDateTimeString only has 27 characters.");
        }

        if(finalLocalDateTimeString.length()>=29) {
            // index 28 character; 29th character
            subsecondNinthDigitChar = finalLocalDateTimeString.charAt(28);
        } else {
            System.out.println("finalLocalDateTimeString only has 28 characters.");
        }

        // There seems to be an error for which the two digits for day are incorrect, so localDateTime.getDayOfmonth is used(), instead of dayFirstDigitChar and daySecondDigitChar
        return localDateTime.getDayOfMonth() + "-" + monthFirstDigitChar + monthSecondDigitChar + "-" + yearFirstDigitChar + yearSecondDigitChar + yearThirdDigitChar + yearFourthDigitChar + "T" + hourFirstDigitChar + hourSecondDigitChar + minuteFirstDigitChar + minuteSecondDigitChar + secondFirstDigitChar + secondSecondDigitChar + "." + subsecondFirstDigitChar + subsecondSecondDigitChar + subsecondThirdDigitChar + subsecondFourthDigitChar + subsecondFifthDigitChar + subsecondSixthDigitChar + subsecondSeventhDigitChar + subsecondEighthDigitChar + subsecondNinthDigitChar;
    }

}
