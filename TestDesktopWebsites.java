package hellocucumber;

import io.cucumber.testng.AbstractTestNGCucumberTests;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.MediaEntityBuilder;
import com.aventstack.extentreports.Status;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import io.cucumber.spring.CucumberContextConfiguration;
import org.junit.runner.RunWith;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.io.FileHandler;
import org.testng.annotations.Test;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.time.LocalDateTime;
import java.util.Objects;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.

@CucumberContextConfiguration
@RunWith(Cucumber.class)
@CucumberOptions(
        // features should start with "src/test/resources/features/xxxxxxxxxxx.feature",
        features = "src/test/resources/features/Selenium_Tutorial.feature",
        // glue starts with "src/test/java/#package for the Test Java class with the Given;When;Then annotations#/",
        glue={"src/test/java/hellocucumber/"},
        // plugin = = {"pretty", "html:target/cucumber-reports"}
        plugin = {"pretty", "html:target/cucumber-reports"}
)

public class TestDesktopWebsites {
    // Test.java class should be within src > test

    private WebDriver driver1 = new ChromeDriver();

    private String websiteTitle = "";
    private String capturedScreenshotImageFilepathString = "";

    private String currentLocalDateTimeForExtentSparkReporter = currentLocalDateTimeWithDdMmYyFormat();

    private ExtentReports extentReport = new ExtentReports();
    // should be target/Spark.html, not an actual filepath starting from C:\\
    private ExtentSparkReporter extentSparkReporter = new ExtentSparkReporter("target/Spark_" + currentLocalDateTimeForExtentSparkReporter  + ".html");

    private ExtentTest extentTest = extentReport.createTest("Selenium_Tutorial Test");

    private FirstGroupOfWebsites firstGroupOfWebsites;

    private SecondGroupOfWebsites secondGroupOfWebsites;

    private ThirdGroupOfWebsites thirdGroupOfWebsites;

    public TestDesktopWebsites() throws IOException {
    }



    // Note that this method is not executed, if running the feature with the Given, When, Then lines
    void testMethod() {
        System.out.println("testing the IntelliJ IDEA - Help - Testing - Create Tests - Right-click to generate Test Method for JUnit5.");
    }

    @org.junit.Test
    @org.junit.jupiter.api.Test
    @org.testng.annotations.Test
    @Given("that the easiest way to find WebElements is by driver.findElement; and driver.findElements which returns a List WebElement")
    public void testMethod1() throws IOException {
        // this line only works without an error, in a public method, as it is a public void method
        // the other three lines (originally above this fourth line) are public methods
        extentReport.attachReporter(extentSparkReporter);

        FirstGroupOfWebsites firstGroupOfWebsites = new FirstGroupOfWebsites((ChromeDriver) driver1, extentTest, extentSparkReporter, extentReport);

        System.out.println("testing");
    }

    @org.junit.Test
    @org.junit.jupiter.api.Test
    @org.testng.annotations.Test
    @When("it is not possible to do so for certain WebElements in this way")
    public void testMethod2 () throws IOException {

        SecondGroupOfWebsites secondGroupOfWebsites = new SecondGroupOfWebsites((ChromeDriver) driver1, extentTest, extentSparkReporter, extentReport);

    }

    @org.junit.Test
    @org.junit.jupiter.api.Test
    @org.testng.annotations.Test
    @Then("we use driver.findElement By.tagName\"...\", for which ... can be i for <i> or button for <button>")
    public void testMethod3 () throws IOException {

        ThirdGroupOfWebsites thirdGroupOfWebsites = new ThirdGroupOfWebsites((ChromeDriver) driver1, extentTest, extentSparkReporter, extentReport);

    }

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

        String initialLocalDateTimeStringDaySubstring = initialLocalDateTimeString.substring(8, 10);

        String initialLocalDateTimeStringDashMonthDashSubstring = initialLocalDateTimeString.substring(4, 8);

        String initialLocalDateTimeStringYearSubstring = initialLocalDateTimeString.substring(0, 4);

        String initialLocalDateTimeStringTimeSubString = initialLocalDateTimeString.substring(10);

        // Not providing as (10, 29) which caused an issue, as found out that intialLocalDateTimeString can be have 26, 27, 28, or 29 characters
        String finalLocalDateTimeString = initialLocalDateTimeStringDaySubstring + initialLocalDateTimeStringDashMonthDashSubstring + initialLocalDateTimeStringYearSubstring + initialLocalDateTimeStringTimeSubString;

        if(finalLocalDateTimeString.length()>=1) {
            // index 0 character; 1st character
            dayFirstDigitChar = finalLocalDateTimeString.charAt(0);
        }

        if(finalLocalDateTimeString.length()>=2) {
            // index 1 character; 2nd character
            daySecondDigitChar = finalLocalDateTimeString.charAt(1);
        }

        if(finalLocalDateTimeString.length()>=4) {
            // index 3 character; 4th character
            monthFirstDigitChar = finalLocalDateTimeString.charAt(3);
        }

        if(finalLocalDateTimeString.length()>=5) {
            // index 4 character; 5th character
            monthSecondDigitChar = finalLocalDateTimeString.charAt(4);
        }

        if(finalLocalDateTimeString.length()>=7) {
            // index 6 character; 7th character
            yearFirstDigitChar = finalLocalDateTimeString.charAt(6);
        }

        if(finalLocalDateTimeString.length()>=8) {
            // index 7 character; 8th character
            yearSecondDigitChar = finalLocalDateTimeString.charAt(7);
        }

        if(finalLocalDateTimeString.length()>=9) {
            // index 8 character; 9th character
            yearThirdDigitChar = finalLocalDateTimeString.charAt(8);
        }

        if(finalLocalDateTimeString.length()>=10) {
            // index 9 character; 10th character
            yearFourthDigitChar = finalLocalDateTimeString.charAt(9);
        }

        if(finalLocalDateTimeString.length()>=12) {
            // index 11 character; 12th character
            hourFirstDigitChar = finalLocalDateTimeString.charAt(11);
        }

        if(finalLocalDateTimeString.length()>=13){
            // index 12 character; 13th character
            hourSecondDigitChar = finalLocalDateTimeString.charAt(12);
        }

        if(finalLocalDateTimeString.length()>=15) {
            // index 14 character; 15th character
            minuteFirstDigitChar = finalLocalDateTimeString.charAt(14);
        }

        if(finalLocalDateTimeString.length()>=16) {
            // index 15 character; 16th character
            minuteSecondDigitChar = finalLocalDateTimeString.charAt(15);
        }

        if(finalLocalDateTimeString.length()>=18) {
            // index 17 character; 18th character
            secondFirstDigitChar = finalLocalDateTimeString.charAt(17);
        }

        if(finalLocalDateTimeString.length()>=19) {
            // index 18 character; 19th character
            secondSecondDigitChar = finalLocalDateTimeString.charAt(18);
        }

        if(finalLocalDateTimeString.length()>=21) {
            // index 20 character; 21th character
            subsecondFirstDigitChar = finalLocalDateTimeString.charAt(20);
        }

        if(finalLocalDateTimeString.length()>=22) {
            // index 21 character; 22nd character
            subsecondSecondDigitChar = finalLocalDateTimeString.charAt(21);
        }

        if(finalLocalDateTimeString.length()>=23) {
            // index 22 character; 23rd character
            subsecondThirdDigitChar = finalLocalDateTimeString.charAt(22);
        }

        if(finalLocalDateTimeString.length()>=24) {
            // index 23 character; 24th character
            subsecondFourthDigitChar = finalLocalDateTimeString.charAt(23);
        }

        if(finalLocalDateTimeString.length()>=25) {
            // index 24 character; 25th character
            subsecondFifthDigitChar = finalLocalDateTimeString.charAt(24);
        }

        if(finalLocalDateTimeString.length()>=26) {
            // index 25 character; 26th character
            subsecondSixthDigitChar = finalLocalDateTimeString.charAt(25);
        }

        if(finalLocalDateTimeString.length()>=27) {
            // index 26 character; 27th character
            subsecondSeventhDigitChar = finalLocalDateTimeString.charAt(26);
        }

        if(finalLocalDateTimeString.length()>=28) {
            // index 27 character; 28th character
            subsecondEighthDigitChar = finalLocalDateTimeString.charAt(27);
        }

        if(finalLocalDateTimeString.length()>=29) {
            // index 28 character; 29th character
            subsecondNinthDigitChar = finalLocalDateTimeString.charAt(28);
        }

        // There seems to be an error for which the two digits for day are incorrect, so localDateTime.getDayOfmonth is used(), instead of dayFirstDigitChar and daySecondDigitChar
        return localDateTime.getDayOfMonth() + "-" + monthFirstDigitChar + monthSecondDigitChar + "-" + yearFirstDigitChar + yearSecondDigitChar + yearThirdDigitChar + yearFourthDigitChar + "T" + hourFirstDigitChar + hourSecondDigitChar + minuteFirstDigitChar + minuteSecondDigitChar + secondFirstDigitChar + secondSecondDigitChar + "." + subsecondFirstDigitChar + subsecondSecondDigitChar + subsecondThirdDigitChar + subsecondFourthDigitChar + subsecondFifthDigitChar + subsecondSixthDigitChar + subsecondSeventhDigitChar + subsecondEighthDigitChar + subsecondNinthDigitChar;
    }
}
