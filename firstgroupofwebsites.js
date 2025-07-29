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

(async function firstGroupOfWebsites() {

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
        console.log("The takeTheScreenshot() function's returned text is: " + text1.concat(" ", text2));
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

    driver.get("https://demo.guru99.com/");


    let title1 = await driver.getTitle();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let emailInputField = await driver.findElement(By.name("emailid"));

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    emailInputField.sendKeys("abc@gmail.com");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let submitButton = driver.findElement(By.name("btnLogin"));

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    submitButton.click();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let title2 = driver.getTitle();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    await driver.get("https://www.bing.com");

    let title3 = driver.getTitle();

    if(title3 === "Search - Microsoft Bing"){
        console.log("title3 Pass.");
    }

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let microsoftBingSearchBar = driver.findElement(By.name("q"));

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    microsoftBingSearchBar.sendKeys("MapleStorySEA Unfunded Amino");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    microsoftBingSearchBar.sendKeys(Key.ENTER);

    for (let i=0; i<99999; i++){
        console.log("Wait for the initial \"MapleStorySEA Unfunded Amino - Search\" webpage to finish loading.");
    }

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let title4 = driver.getTitle();

    let searchTab = driver.findElement(By.id("b-scopeListItem-copilotsearch"));

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    searchTab.click();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    // This element keeps being stale (using a for loop does not work), so it cannot be found
    //let allTab = driver.findElement(By.id("b-scopeListItem-web"));
    // allTab.click();

    driver.get("https://www.bing.com/search?pglt=299&q=MapleStorySEA+Unfunded+Amino+-+Search");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let title5 = driver.getTitle();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let requiredSearchResultLink = driver.findElement(By.partialLinkText("Featured | [MapleStorySEA] Unfunded Tips"));

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    for (let i = 0; i < 50; i++) {
        //requiredSearchResultPartialLinkText.sendKeys(Keys.DOWN);
        requiredSearchResultLink.sendKeys(Key.DOWN);
    }

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    for (let i = 0; i < 50; i++) {
        //requiredSearchResultPartialLinkText.sendKeys(Keys.DOWN);
        requiredSearchResultLink.sendKeys(Key.UP);
    }

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    requiredSearchResultLink.click();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    driver.get("https://aminoapps.com/c/maplestorysea/home/");

    let title6 = driver.getTitle();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let aminoSearchBar = driver.findElement(By.className("nav-search-input"));

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    aminoSearchBar.sendKeys("MapleStorySEA Unfunded Amino");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let aminoSearchTerm = "MapleStorySEA Unfunded Amino";
    let aminoSearchTermLength = aminoSearchTerm.length;
    for (let i = 0; i < aminoSearchTermLength; i++) {
        aminoSearchBar.sendKeys(Key.BACK_SPACE);
    }

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    aminoSearchBar.sendKeys("MapleStorySEA Unfunded Amino");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let threeWebElementsList = driver.findElements(By.tagName("svg"));
    let aminoSearchBarMagnifyingGlassButton = threeWebElementsList[0]
    // Have tried, even
    // let aminoSearchBarMagnifyingGlassButton = driver.findElement(By.tagName("svg"));
    // would cause an error if
    // aminoSearchBarMagnifyingGlassButton.click()
    // is used, despite this being the first element of the list
    aminoSearchBar.sendKeys(Key.ENTER);

    let popularPostsText = driver.findElement(By.tagName("h3"));
    // popularPostsText is the first of the two elements for this array, if using
    // let tagNameH3WebElementArray = driver.findElements(By.tagName("h3"));


    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    driver.get("https://aminoapps.com/c/maplestorysea/home/");

    let title7 = driver.getTitle();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let privacyNoticeAcceptButton = driver.findElement(By.className("confirm-close"));

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    privacyNoticeAcceptButton.click();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    // Note: This currently refers to the featured Reddit Advice note's button to click on
    // Only Java for IntelliJ IDEA; and Python for Webstorm, can find the current third (from the top) WebElement
    // (This file is for Javascript for Webstorm)
    // which uses the same className
    // Which would be for the "Unfunded Training Advice from Level 1 to Level 200?" note's button
    let freeCharacterSlotExpansionCoupon = driver.findElement(By.className("overflow-hidden"));

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    // For which the featured Reddit Advice note's button is clicked on to reach the Reddit Advice note
    freeCharacterSlotExpansionCoupon.click();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let title8 = driver.getTitle();


    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    driver.get("https://aminoapps.com/c/maplestorysea/home/");

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let title9 = driver.getTitle();


    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let fourOverflowHiddenClassnameWebElementArray = driver.findElements(By.className("overflow-hidden"));
    // The third of four elements is for the "Unfunded Training Advice from Level 1 to Level 200?" link


    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    driver.get("https://aminoapps.com/c/maplestorysea/home/");

    let title11 = driver.getTitle();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let sevenLabelClassnameWebElementArray = driver.findElements(By.className("label"));
    // The second of seven elements for this array is for the Latest tab

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    let title12 = driver.getTitle();
    // It is not possible to reach the correct webpage without causing an error for Javascript
    // So the website address needs to be manually provided
    driver.get("https://aminoapps.com/c/maplestorysea/recent/");

    let title13 = await driver.getTitle();

    screenshotFilenameArray.push(await takeTheScreenshot());
    console.log("length of screenshotFilenameArray is: " + screenshotFilenameArray.length);
    testResults.push({step: stepNameString, screenshot: screenshotFilenameArray[i-1], status: 'PASS'});
    i = i + 1;
    stepNameString = 'Step ' + i;

    // It is not possible to reach the correct webpage without causing an error for Javascript
    // So the website address needs to be manually provided
    driver.get("https://aminoapps.com/c/maplestorysea/home/");

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
}())