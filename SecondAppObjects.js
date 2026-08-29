import { writeFileSync, existsSync, mkdirSync } from 'node:fs';
import path from 'node:path';

export class SecondAppObjects {
    constructor(driver, targetDir) {
        this.driver = driver;
        this.targetDir = targetDir;
        this.steps = [];
    }

    async takeScreenshot(description) {
        if (!existsSync(this.targetDir)) {
            mkdirSync(this.targetDir, { recursive: true });
        }
        const now = new Date();
        const day = String(now.getDate()).padStart(2, '0');
        const month = String(now.getMonth() + 1).padStart(2, '0');
        const year = now.getFullYear();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        const milliseconds = String(now.getMilliseconds()).padStart(3, '0').padEnd(9, '0');

        let filename = `${day}-${month}-${year}T${hours}${minutes}${seconds}.${milliseconds}_screenshot.png`;
        let filepath = path.join(this.targetDir, filename);

        let encodedString = await this.driver.takeScreenshot();
        writeFileSync(filepath, Buffer.from(encodedString, 'base64'));

        this.steps.push({
            description: description,
            image: filename
        });
        return filename;
    }

    async execute() {
        let appTab = await this.driver.$('//android.widget.TextView[@content-desc="App"]');
        await this.takeScreenshot("Click on App Tab");
        await appTab.click();

        let searchTab = await this.driver.$('//android.widget.TextView[@content-desc="Search"]');
        await this.takeScreenshot("Click on Search Tab");
        await searchTab.click();

        let invokeSearchTab = await this.driver.$('//android.widget.TextView[@content-desc="Invoke Search"]');
        await this.takeScreenshot("Click on Invoke Search Tab");
        await invokeSearchTab.click();

        let prefillQueryTextField = await this.driver.$('//android.widget.EditText[@resource-id="io.appium.android.apis:id/txt_query_prefill"]');
        await this.takeScreenshot("Locate prefill query text field");
        await prefillQueryTextField.setValue("Test the text.");
        await this.takeScreenshot("Set text value to 'Test the text.'");
        console.log("Second App Execution Completed.");
        return this.steps;
    }
}