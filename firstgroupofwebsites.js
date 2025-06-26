const {By, Builder, Browser, Key} = require('selenium-webdriver');
const assert = require("assert");
const {writeFileSync} = require("node:fs");
const {write} = require("selenium-webdriver/io");
const test = require("node:test");

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
        return text1.concat(" ", text2);
    }

    let driver;

    driver = await new Builder().forBrowser(Browser.CHROME).build();
    await driver.get("https://demo.guru99.com/");

    let title1 = await driver.getTitle();

    await takeTheScreenshot();

    let emailInputField = await driver.findElement(By.name("emailid"));

    await takeTheScreenshot();

    emailInputField.sendKeys("abc@gmail.com");

    await takeTheScreenshot();

    let submitButton = driver.findElement(By.name("btnLogin"));

    await takeTheScreenshot();

    submitButton.click();

    await takeTheScreenshot();

    let title2 = driver.getTitle();

    await takeTheScreenshot();

    await driver.get("https://www.bing.com");

    let title3 = driver.getTitle();

    if(title3 === "Search - Microsoft Bing"){
        console.log("title3 Pass.");
    }

    await takeTheScreenshot();

    let microsoftBingSearchBar = driver.findElement(By.name("q"));

    await takeTheScreenshot();

    microsoftBingSearchBar.sendKeys("MapleStorySEA Unfunded Amino");

    await takeTheScreenshot();

    microsoftBingSearchBar.sendKeys(Key.ENTER);

    await takeTheScreenshot();

    let title4 = driver.getTitle();

    let searchTab = driver.findElement(By.id("b-scopeListItem-copilotsearch"));

    await takeTheScreenshot();

    searchTab.click();

    await takeTheScreenshot();

    // This element keeps being stale (using a for loop does not work), so it cannot be found
    //let allTab = driver.findElement(By.id("b-scopeListItem-web"));
    // allTab.click();

    driver.get("https://www.bing.com/search?pglt=299&q=MapleStorySEA+Unfunded+Amino+-+Search");
    await takeTheScreenshot();

    let title5 = driver.getTitle();

    await takeTheScreenshot();

    let requiredSearchResultLink = driver.findElement(By.partialLinkText("Featured | [MapleStorySEA] Unfunded Tips"));

    await takeTheScreenshot();

    for (let i = 0; i < 50; i++) {
        //requiredSearchResultPartialLinkText.sendKeys(Keys.DOWN);
        requiredSearchResultLink.sendKeys(Key.DOWN);
    }

    await takeTheScreenshot();

    for (let i = 0; i < 50; i++) {
        //requiredSearchResultPartialLinkText.sendKeys(Keys.DOWN);
        requiredSearchResultLink.sendKeys(Key.UP);
    }

    await takeTheScreenshot();

    requiredSearchResultLink.click();

    await takeTheScreenshot();

    driver.get("https://aminoapps.com/c/maplestorysea/home/");

    let title6 = driver.getTitle();

    await takeTheScreenshot();

    let aminoSearchBar = driver.findElement(By.className("nav-search-input"));

    await takeTheScreenshot();

    aminoSearchBar.sendKeys("MapleStory Unfunded Amino");

    await takeTheScreenshot();

    let aminoSearchTerm = "MapleStorySEA Unfunded Amino";
    let aminoSearchTermLength = aminoSearchTerm.length;
    for (let i = 0; i < aminoSearchTermLength; i++) {
        aminoSearchBar.sendKeys(Key.BACK_SPACE);
    }
    await takeTheScreenshot();

    aminoSearchBar.sendKeys("MapleStory Unfunded Amino");

    await takeTheScreenshot();

    aminoSearchBar.sendKeys(Key.ENTER);

    let tagNameH3WebElementList = driver.findElements(By.tagName("h3"));
    let popularPostsText = tagNameH3WebElementList[0]

    await takeTheScreenshot();

    driver.get("https://aminoapps.com/c/maplestorysea/home/");

    let title7 = driver.getTitle();


    await takeTheScreenshot();

    let privacyNoticeAcceptButton = driver.findElement(By.className("confirm-close"));

    await takeTheScreenshot();

    privacyNoticeAcceptButton.click();

    await takeTheScreenshot();

    let freeCharacterSlotExpansionCoupon = driver.findElement(By.className("overflow-hidden"));

    await takeTheScreenshot();

    freeCharacterSlotExpansionCoupon.click();

    await takeTheScreenshot();

    let title8 = driver.getTitle();


    await takeTheScreenshot();

    driver.get("https://aminoapps.com/c/maplestorysea/home/");

    await takeTheScreenshot();

    let title9 = driver.getTitle();


    await takeTheScreenshot();

    let fourOverflowHiddenClassnameWebElementList = driver.findElements(By.className("overflow-hidden"));
    let requiredThirdOverflowHiddenClassnameElement = fourOverflowHiddenClassnameWebElementList[2];

    await takeTheScreenshot();

    await takeTheScreenshot();

    driver.get("https://aminoapps.com/c/maplestorysea/home/");

    let title11 = driver.getTitle();


    await takeTheScreenshot();

    let sevenLabelClassnameWebElementList = driver.findElements(By.className("label"));
    let requiredSecondLabelClassnameElement = sevenLabelClassnameWebElementList[1];

    await takeTheScreenshot();

    let title12 = driver.getTitle();

    driver.get("https://aminoapps.com/c/maplestorysea/recent/");

    let title13 = await driver.getTitle();

    await takeTheScreenshot();

    driver.get("https://aminoapps.com/c/maplestorysea/home/");

    await takeTheScreenshot();
}())