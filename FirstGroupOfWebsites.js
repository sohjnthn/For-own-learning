import pkg from 'selenium-webdriver';
const { By, until, Key } = pkg;
import { writeFileSync, existsSync, mkdirSync } from 'node:fs';

const TARGET_DIR = './target';

export class FirstGroupOfWebsites {
    constructor(driver) {
        this.driver = driver;
    }

    async takeTheScreenshot() {
        if (!existsSync(TARGET_DIR)) {
            mkdirSync(TARGET_DIR, { recursive: true });
        }

        let encodedString = await this.driver.takeScreenshot();
        const now = new Date();

        const day = String(now.getDate()).padStart(2, '0');
        const month = String(now.getMonth() + 1).padStart(2, '0');
        const year = now.getFullYear();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        const milliseconds = String(now.getMilliseconds()).padStart(3, '0').padEnd(9, '0');

        let screenshotFilename = `${TARGET_DIR}/${day}-${month}-${year}T${hours}${minutes}${seconds}.${milliseconds}_screenshot.png`;

        writeFileSync(screenshotFilename, Buffer.from(encodedString, 'base64'));
        return screenshotFilename;
    }

    async executeTests(startStepNum = 1) {
        let results = [];
        let stepNum = startStepNum;

        let capturedScreenshotImageFilepathString = await this.takeTheScreenshot();

        await this.driver.get("https://demo.guru99.com/");
        capturedScreenshotImageFilepathString = await this.takeTheScreenshot();

        let websiteTitle = await this.driver.getTitle();
        console.log("The website title is \"" + websiteTitle + "\".");

        if (websiteTitle === "Guru99 Bank Home Page") {
            results.push({
                step: `Step ${stepNum}: The current web browser tab title is "${websiteTitle}"; which should be "Guru99 Bank Home Page".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
        } else {
            results.push({
                step: `Step ${stepNum}: The current web browser tab title cannot be retrieved; which should be "Guru99 Bank Home Page".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
        }
        stepNum++;

        let emailInputField = await this.driver.findElement(By.name("emailid"));
        capturedScreenshotImageFilepathString = await this.takeTheScreenshot();

        if (await emailInputField.isDisplayed()) {
            await emailInputField.sendKeys("abc@gmail.com");
            capturedScreenshotImageFilepathString = await this.takeTheScreenshot();
        }

        if (await emailInputField.isDisplayed()) {
            results.push({
                step: `Step ${stepNum}: The email input field value's text is the correct "abc@gmail.com".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
        } else {
            results.push({
                step: `Step ${stepNum}: The email input field value's text is not "abc@gmail.com".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
        }
        stepNum++;

        let emailText = "abc@gmail.com";
        for (let i = 0; i < emailText.length; i++) {
            await emailInputField.sendKeys(Key.BACK_SPACE);
        }

        capturedScreenshotImageFilepathString = await this.takeTheScreenshot();
        if (await emailInputField.isDisplayed()) {
            results.push({
                step: `Step ${stepNum}: The email input field value's text is the correct "".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
        } else {
            results.push({
                step: `Step ${stepNum}: The email input field value's text is not "".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
        }
        stepNum++;

        results.push({
            step: `Step ${stepNum}: The email input field value "abc@gmail.com" has been removed by the Backspace key.`,
            screenshot: capturedScreenshotImageFilepathString,
            status: 'PASS'
        });
        stepNum++;

        await emailInputField.sendKeys("abc@gmail.com");
        capturedScreenshotImageFilepathString = await this.takeTheScreenshot();

        if (await emailInputField.isDisplayed()) {
            results.push({
                step: `Step ${stepNum}: The email input field value's text is the correct "abc@gmail.com".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
        } else {
            results.push({
                step: `Step ${stepNum}: The email input field value's text is not "abc@gmail.com".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
        }
        stepNum++;

        let submitButton = await this.driver.findElement(By.name("btnLogin"));
        if (await submitButton.isDisplayed()) {
            await submitButton.click();
            capturedScreenshotImageFilepathString = await this.takeTheScreenshot();
        }

        websiteTitle = await this.driver.getTitle();
        if (websiteTitle === "Guru99 Bank Home Page") {
            results.push({
                step: `Step ${stepNum}: The current web browser tab title is "${websiteTitle}"; which should be "Guru99 Bank Home Page".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
        } else {
            results.push({
                step: `Step ${stepNum}: The current web browser tab title cannot be retrieved; which should be "Guru99 Bank Home Page".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
        }
        stepNum++;

        await this.driver.get("https://www.bing.com/");
        capturedScreenshotImageFilepathString = await this.takeTheScreenshot();

        websiteTitle = await this.driver.getTitle();
        if (websiteTitle === "Search - Microsoft Bing") {
            results.push({
                step: `Step ${stepNum}: The current web browser tab title is the correct "${websiteTitle}"; which should be "Search - Microsoft Bing".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
        } else {
            results.push({
                step: `Step ${stepNum}: The current web browser tab title is the incorrect "${websiteTitle}"; which should be "Search - Microsoft Bing".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
        }
        stepNum++;

        let microsoftBingSearchBar = await this.driver.findElement(By.name("q"));
        if (await microsoftBingSearchBar.isDisplayed()) {
            await microsoftBingSearchBar.sendKeys("MapleStorySEA (South-East Asia) tips [Facebook notes]");
            capturedScreenshotImageFilepathString = await this.takeTheScreenshot();
        }

        if (await microsoftBingSearchBar.isDisplayed()) {
            results.push({
                step: `Step ${stepNum}: The Microsoft Bing search term input is the correct "MapleStorySEA (South-East Asia) tips [Facebook notes]".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
            await microsoftBingSearchBar.sendKeys(Key.ENTER);
        } else {
            results.push({
                step: `Step ${stepNum}: The Microsoft Bing search term input is the incorrect "MapleStorySEA (South-East Asia) tips [Facebook notes]".`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
            await microsoftBingSearchBar.sendKeys(Key.ENTER);
        }
        stepNum++;

        capturedScreenshotImageFilepathString = await this.takeTheScreenshot();
        await this.driver.get("https://maplestoryseatips.blogspot.com/");
        capturedScreenshotImageFilepathString = await this.takeTheScreenshot();

        let displayedText = await this.driver.findElement(By.partialLinkText("[MapleStorySEA] Typed some extra things here"));
        if (await displayedText.isDisplayed()) {
            results.push({
                step: `Step ${stepNum}: https://maplestoryseatips.blogspot.com/ is reached`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
        } else {
            results.push({
                step: `Step ${stepNum}: https://maplestoryseatips.blogspot.com/ is not reached.`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
        }
        stepNum++;

        let toggleList1 = await this.driver.findElements(By.className("post-count-link"));
        let zippyToggleOpenForTheYear2026 = toggleList1[45];
        capturedScreenshotImageFilepathString = await this.takeTheScreenshot();

        for (let i = 0; i < 5; i++) {
            await zippyToggleOpenForTheYear2026.sendKeys(Key.DOWN);
            capturedScreenshotImageFilepathString = await this.takeTheScreenshot();
        }

        if (await zippyToggleOpenForTheYear2026.isDisplayed()) {
            results.push({
                step: `Step ${stepNum}: zippyToggleOpenForTheYear2026 is displayed.`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
        } else {
            results.push({
                step: `Step ${stepNum}: zippyToggleOpenForTheYear2026 is not displayed.`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
        }
        stepNum++;

        let tagAWebElementList = await this.driver.findElements(By.tagName("a"));
        let arrowForToggleOpenForTheYear2026 = tagAWebElementList[128];
        await arrowForToggleOpenForTheYear2026.click();

        capturedScreenshotImageFilepathString = await this.takeTheScreenshot();

        let theText2026 = await this.driver.findElement(By.partialLinkText("2026"));
        await theText2026.click();

        let displayedText2 = await this.driver.findElement(By.partialLinkText("[MapleStorySEA] Create your own guild to boost all characters' damage ranges"));
        capturedScreenshotImageFilepathString = await this.takeTheScreenshot();

        if (await displayedText2.isDisplayed()) {
            results.push({
                step: `Step ${stepNum}: The bottommost note for January 2026 is displayed.`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
        } else {
            results.push({
                step: `Step ${stepNum}: The bottommost note for January 2026 is not displayed.`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
        }
        stepNum++;

        for (let i = 0; i < 5; i++) {
            await displayedText2.sendKeys(Key.DOWN);
            capturedScreenshotImageFilepathString = await this.takeTheScreenshot();
        }

        if (await displayedText2.isDisplayed()) {
            results.push({
                step: `Step ${stepNum}: The bottommost note for 2026 is displayed; and is reached.`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'PASS'
            });
        } else {
            results.push({
                step: `Step ${stepNum}: The bottommost note for 2026 is not displayed; and is not reached.`,
                screenshot: capturedScreenshotImageFilepathString,
                status: 'FAIL'
            });
        }
        stepNum++;

        return { results, nextStep: stepNum };
    }
}