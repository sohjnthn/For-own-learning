import { By } from 'selenium-webdriver';
import assert from 'assert';
import { writeFileSync, existsSync, mkdirSync } from 'node:fs';

const TARGET_DIR = './target';

export class ThirdGroupOfWebsites {
    constructor(driver) {
        this.driver = driver;
        this.startIndex = 0;
        this.endIndex = 5;
        this.imgMagicNumber = 'iVBOR';
        this.base64Code = '';
    }

    async takeTheScreenshot() {
        if (!existsSync(TARGET_DIR)) {
            mkdirSync(TARGET_DIR, { recursive: true });
        }
        let encodedString = await this.driver.takeScreenshot();
        const now = new Date();
        const formattedDateTime = `${now.getDate().toString().padStart(2, '0')}-${(now.getMonth() + 1).toString().padStart(2, '0')}-${now.getFullYear()}_${now.getHours().toString().padStart(2, '0')}${now.getMinutes().toString().padStart(2, '0')}${now.getSeconds().toString().padStart(2, '0')}`;
        let screenshotFilename = `${TARGET_DIR}/screenshot_${formattedDateTime}.png`;

        writeFileSync(screenshotFilename, Buffer.from(encodedString, 'base64'));

        this.base64Code = encodedString.slice(this.startIndex, this.endIndex);
        assert.strictEqual(this.base64Code, this.imgMagicNumber);

        return screenshotFilename;
    }

    async executeTests(startStepNum = 1) {
        let results = [];
        let stepNum = startStepNum;

        await this.driver.get("https://www.bing.com");
        let screenshotFilename = await this.takeTheScreenshot();

        results.push({
            step: `Step ${stepNum}: https://www.bing.com is reached`,
            screenshot: screenshotFilename,
            status: 'PASS'
        });
        stepNum++;

        return { results, nextStep: stepNum };
    }
}