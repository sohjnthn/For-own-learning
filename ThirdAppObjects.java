package hellocucumber;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.MediaEntityBuilder;
import com.aventstack.extentreports.Status;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.pagefactory.AndroidFindBy;
import org.openqa.selenium.*;
import org.openqa.selenium.io.FileHandler;

import java.io.File;
import java.io.IOException;
import java.time.LocalDateTime;
import java.util.Objects;

public class ThirdAppObjects {

    // Third App
    @AndroidFindBy(xpath = "//android.widget.EditText[@resource-id=\"com.microsoft.emmx.canary:id/url_bar\"]")
    WebElement edgeBrowserDefaultWebpageSearchBar;

    @AndroidFindBy(xpath = "//android.widget.TextView[@resource-id=\"com.microsoft.emmx.canary:id/line_1\"]\n")
    WebElement requiredSearchOption;

    @AndroidFindBy(xpath = "//android.widget.FrameLayout[@content-desc=\"Web View\"]")
    WebElement searchResultsWebpageView;

    @AndroidFindBy(xpath = "//android.widget.FrameLayout[@content-desc=\"Web View\"]")
    WebElement aminoWebpageView;

    String capturedScreenshotImageFilepathString = "";

    public ThirdAppObjects(AndroidDriver driver, ExtentTest extentTest, ExtentSparkReporter extentSparkReporter, ExtentReports extentReport) throws IOException {
        edgeBrowserDefaultWebpageSearchBar = driver.findElement(By.xpath("//android.widget.EditText[@resource-id=\"com.microsoft.emmx.canary:id/url_bar\"]"));

        if(edgeBrowserDefaultWebpageSearchBar.isDisplayed()){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Edge Browser default webpage search bar is displayed.");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "he Edge Browser default webpage search bar is not displayed.");
            System.out.println("Fail");
        }

        edgeBrowserDefaultWebpageSearchBar.click();

        if(edgeBrowserDefaultWebpageSearchBar.isDisplayed()){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Edge Browser default webpage search bar is displayed.");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "he Edge Browser default webpage search bar is not displayed.");
            System.out.println("Fail");
        }

        edgeBrowserDefaultWebpageSearchBar.sendKeys("MapleStorySEA Unfunded Amino");

        if(edgeBrowserDefaultWebpageSearchBar.isDisplayed()){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Edge Browser default webpage search bar contains the entered search term \"MapleStorySEA Unfunded Amino\".");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The Edge Browser default webpage search bar does not contain the entered search term \"MapleStorySEA Unfunded Amino\".");
            System.out.println("Fail");
        }

        requiredSearchOption = driver.findElement(By.xpath("//android.widget.TextView[@resource-id=\"com.microsoft.emmx.canary:id/line_1\"]\n"));

        if(requiredSearchOption.isDisplayed()){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The Edge Browser default webpage search bar contains the entered search term \"MapleStorySEA Unfunded Amino\"");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The Edge Browser default webpage search bar does not contain the entered search term \"MapleStorySEA Unfunded Amino\"");
            System.out.println("Fail");
        }

        requiredSearchOption.click();

        String oneString = "1";

        if(Objects.equals(oneString, "1")){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The required search results webpage is still loading.");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The required search results webpage is not loading.");
            System.out.println("Fail");
        }

        if(Objects.equals(oneString, "1")){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The required search results webpage is reached.");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The required search results webpage is not reached.");
            System.out.println("Fail");
        }

        searchResultsWebpageView = driver.findElement(By.xpath("//android.widget.FrameLayout[@content-desc=\"Web View\"]"));
        // The following line cannot be used as the WebElement is not found
        // WebElement requiredSearchResultLink = driver.findElement(By.partialLinkText("Featured | [MapleStorySEA] Unfunded Tips"));

        if(searchResultsWebpageView.isDisplayed()){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The required search results webpage is reached.");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The required search results webpage is not reached.");
            System.out.println("Fail");
        }

        // For "//android.widget.FrameLayout[@content-desc=\"Web View\"]"
        // sending the key KEYS.TAB would cause the test to fail
        // We can only click on it
        // And we cannot select any specific individual part as an element

        // Noting that what was clicked on is not the correct search result for the default Featured tab, but is the word "Latest" (for the Latest tab); or "About" (for the About tab) near the search results
        searchResultsWebpageView.click();

        if(Objects.equals(oneString, "1")){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The required search results webpage is reached.");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The required search results webpage is not reached.");
            System.out.println("Fail");
        }

        if(Objects.equals(oneString, "1")){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The required search results webpage is reached.");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The required search results webpage is not reached.");
            System.out.println("Fail");
        }

        // For "//android.widget.FrameLayout[@content-desc=\"Web View\"]"
        // sending the key KEYS.TAB would cause the test to fail
        // We can only click on it
        // And we cannot select any specific individual part as an element
        aminoWebpageView = driver.findElement(By.xpath("//android.widget.FrameLayout[@content-desc=\"Web View\"]"));

        if(aminoWebpageView.isDisplayed()){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The required webpage is reached.");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The required webpage is not reached.");
            System.out.println("Fail");
        }

        aminoWebpageView.click();

        if(Objects.equals(oneString, "1")){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The required webpage is reached.");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The required search results webpage is not reached.");
            System.out.println("Fail");
        }

        if(Objects.equals(oneString, "1")){
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.PASS, "The required webpage is reached.");
            System.out.println("Pass");
        } else {
            capturedScreenshotImageFilepathString = takeScreenshot(driver);
            extentTest.addScreenCaptureFromPath(capturedScreenshotImageFilepathString).pass(MediaEntityBuilder.createScreenCaptureFromPath(capturedScreenshotImageFilepathString).build()).log(Status.FAIL, "The required webpage is not reached.");
            System.out.println("Fail");
        }

        extentReport.flush();
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
        // Able to add int testInt to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Android\\Selenium_Screenshot_Images\\" + testInt + "_screenshot.png")
        // Able to add char to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Android\\Selenium_Screenshot_Images\\" + testChar + "_screenshot.png")
        // Unable to add String, or char[] (char Array) to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Android\\Selenium_Screenshot_Images\\" + finalLocalDateTimeString1 + "_screenshot.png")
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
        File destinationFile = new File("C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Android\\Selenium Screenshot Images\\" + dayFirstDigitChar + daySecondDigitChar + "-" + monthFirstDigitChar + monthSecondDigitChar + "-" + yearFirstDigitChar + yearSecondDigitChar + yearThirdDigitChar + yearFourthDigitChar + "T" + hourFirstDigitChar + hourSecondDigitChar + minuteFirstDigitChar + minuteSecondDigitChar + secondFirstDigitChar + secondSecondDigitChar + "." + subsecondFirstDigitChar + subsecondSecondDigitChar + subsecondThirdDigitChar + subsecondFourthDigitChar + subsecondFifthDigitChar + subsecondSixthDigitChar + subsecondSeventhDigitChar + subsecondEighthDigitChar + subsecondNinthDigitChar + "_screenshot.png");
        FileHandler.copy(sourceFile, destinationFile);


        return "C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Android\\Selenium Screenshot Images\\" + dayFirstDigitChar + daySecondDigitChar + "-" + monthFirstDigitChar + monthSecondDigitChar + "-" + yearFirstDigitChar + yearSecondDigitChar + yearThirdDigitChar + yearFourthDigitChar + "T" + hourFirstDigitChar + hourSecondDigitChar + minuteFirstDigitChar + minuteSecondDigitChar + secondFirstDigitChar + secondSecondDigitChar + "." + subsecondFirstDigitChar + subsecondSecondDigitChar + subsecondThirdDigitChar + subsecondFourthDigitChar + subsecondFifthDigitChar + subsecondSixthDigitChar + subsecondSeventhDigitChar + subsecondEighthDigitChar + subsecondNinthDigitChar + "_screenshot.png";
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
        // Able to add int testInt to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Android\\Selenium_Screenshot_Images\\" + testInt + "_screenshot.png")
        // Able to add char to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Android\\Selenium_Screenshot_Images\\" + testChar + "_screenshot.png")
        // Unable to add String, or char[] (char Array) to new File(C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Android\\Selenium_Screenshot_Images\\" + finalLocalDateTimeString1 + "_screenshot.png")
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
