let {By, Builder, Browser, Key} = require('selenium-webdriver');
const assert = require("assert");
const {writeFileSync} = require("node:fs");
const {write} = require("selenium-webdriver/io");
const test = require("node:test");
const { remote } = require('webdriverio');
const { AndroidUiautomator2Driver } = require('appium-android-driver');
const { AndroidDriver } = require("appium-android-driver");

let startIndex = 0
let endIndex = 5
let pdfMagicNumber = 'JVBER'
let imgMagicNumber = 'iVBOR'
let base64Code

var wd = require('selenium-webdriver');
const fs = require("fs");
By = wd.By;
until = wd.until;

(async function testApps() {

    async function takeTheScreenshot() {
        let encodedString = await driver.takeScreenshot();
        const now = new Date();
        const formattedDateTime = `${now.getDate()}-${(now.getMonth() + 1).toString().padStart(2, '0')}-${now.getFullYear().toString().padStart(2, '0')}_${now.getHours().toString().padStart(2, '0')}${now.getMinutes().toString().padStart(2, '0')}${now.getSeconds().toString().padStart(2, '0')}`;
        console.log(formattedDateTime);
        let text1 = formattedDateTime;
        let text2 = "_image.png";
        await writeFileSync(text1.concat("", text2), encodedString, 'base64');
        base64Code = encodedString.slice(startIndex, endIndex);
        assert.strictEqual(base64Code, imgMagicNumber);
        console.log("The takeTheScreenshot() function's returned text is: " + text1 + text2);
        let returnString = text1 + text2;
        console.log("returnString is: " + returnString);
        return returnString;
    }

    function currentDateTime(){
        const now = new Date();
        const formattedDateTime = `${now.getDate()}-${(now.getMonth() + 1).toString().padStart(2, '0')}-${now.getFullYear().toString().padStart(2, '0')}_${now.getHours().toString().padStart(2, '0')}${now.getMinutes().toString().padStart(2, '0')}${now.getSeconds().toString().padStart(2, '0')}`;
        return formattedDateTime;
    }

    let screenshotFilenameArray = [];

    let i = 1;
    let stepNameString = 'Step ' + i;
    const testResults = [
        //{ step: stepNameString, screenshot: screenshotFilenameArray[0], status: 'PASS' },
    ];


    let driver = await remote({
        path: '/wd/hub',
        port: 4723,
        capabilities: {
            platformName: 'Android', // or 'iOS'
            app: "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\app\\com.afwsamples.testdpc_9.0.12-9012_minAPI21(nodpi)_apkmirror.com.apk",
            automationName: 'UiAutomator2', // or 'XCUITest' for iOS
            platformVersion: "16.0",
        }
    });

    let policyManagementText = driver.$("//android.widget.TextView[@text=\"Policy management\"]");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    driver = await remote({
        path: '/wd/hub',
        port: 4723,
        capabilities: {
            platformName: 'Android', // or 'iOS'
            app: "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\app\\ApiDemos-debug.apk",
            automationName: 'UiAutomator2', // or 'XCUITest' for iOS
            platformVersion: "16.0",
        }
    });

    let appTab = driver.$("//android.widget.TextView[@content-desc=\"App\"]");
    appTab.click();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let searchTab = driver.$("//android.widget.TextView[@content-desc=\"Search\"]");
    searchTab.click();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    for (let i = 0; i < 99999; i++) {
        console.log("Wait for the Invoke Search tab to be displayed to take the screenshot image.")
    }

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let invokeSearchTab = driver.$("//android.widget.TextView[@content-desc=\"Invoke Search\"]");
    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    invokeSearchTab.click();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let prefillQueryTextField = driver.$("//android.widget.EditText[@resource-id=\"io.appium.android.apis:id/txt_query_prefill\"]");
    // entering text into a smartphone application's text input field, requires both
    // await, and .addValue("...")
    // .sendKeys("...") for the desktop web browser Google Chrome, does not work in this case
    await prefillQueryTextField.addValue("Test the text.");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    driver = await remote({
        path: '/wd/hub',
        port: 4723,
        capabilities: {
            platformName: 'Android', // or 'iOS'
            app: "C:\\Users\\sohjnthn\\WebstormProjects\\untitled1\\app\\com.microsoft.emmx.canary_138.0.3336.0-333600000_minAPI26(armeabi-v7a)(nodpi)_apkmirror.com.apk",
            automationName: 'UiAutomator2', // or 'XCUITest' for iOS
            platformVersion: "16.0",
        }
    });

    for(let i=0; i<99999; i++) {
        console.log("The app requires time to load.");
    }

    let edgeBrowserDefaultWebpageSearchBar = driver.$("//android.widget.EditText[@resource-id=\"com.microsoft.emmx.canary:id/url_bar\"]");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    edgeBrowserDefaultWebpageSearchBar.click();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    await edgeBrowserDefaultWebpageSearchBar.addValue("MapleStorySEA Unfunded Amino");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let requiredSearchOption = driver.$("//android.widget.TextView[@resource-id=\"com.microsoft.emmx.canary:id/line_1\"]\n");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    requiredSearchOption.click();

    // There may be a very short delay
    for (let i = 0; i < 2; i++) {
        console.log("The required search results webpage is still loading.");
    }

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let searchResultsWebpageView = driver.$("//android.widget.FrameLayout[@content-desc=\"Web View\"]");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    searchResultsWebpageView.click();

    for(let i=0; i<99999; i++) {
        console.log("The app requires time to load.");
    }

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    for(let i=0; i<99999; i++) {
        console.log("The app requires time to load.");
    }

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    for(let i=0; i<99999; i++) {
        console.log("The app requires time to load.");
    }

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i - 1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let htmlContent = '<html><body><h1>Test Report</h1>';
    testResults.forEach(result => {
        htmlContent += `<div>
        <p>Step: ${result.step}</p>
        <p>Status: ${result.status}</p>
        <img src="${result.screenshot}" alt="Screenshot" width="300">
        </div>`;
    });
    htmlContent += '</body></html>';
    fs.writeFileSync('./' + currentDateTime() + '_test-report.html', htmlContent);
    console.log('Report generated: test-report.html');
}())
