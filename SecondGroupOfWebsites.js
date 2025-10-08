const {By, Builder, Browser, Key} = require('selenium-webdriver');
const assert = require("assert");
const {writeFileSync} = require("node:fs");
const {write} = require("selenium-webdriver/io");
const test = require("node:test");
const fs = require('fs');
// const WebDriverIO = require("WebDriverIO");

let startIndex = 0
let endIndex = 5
let pdfMagicNumber = 'JVBER'
let imgMagicNumber = 'iVBOR'
let base64Code

(async function SecondGroupOfWebsites() {

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

    let driver;

    driver = await new Builder().forBrowser(Browser.CHROME).build();

    driver.get("https://aminoapps.com/c/maplestorysea/recent/");

    let title13 = await driver.getTitle();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    // Unable to identify Create Post button as
    // > Create Post <
    // has whitespace character(s) directly after ">"; and/or directly before "<"

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
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

    // Does nothing (the fourth html report is not generated)
    // return testResults;

}())