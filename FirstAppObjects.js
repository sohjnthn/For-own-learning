import { writeFileSync, existsSync, mkdirSync } from 'node:fs';
import path from 'node:path';

export class FirstAppObjects {
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
        let policyManagementText = await this.driver.$('//android.widget.TextView[@text="Policy management"]');
        if (await policyManagementText.isDisplayed()) {
            await this.takeScreenshot("Check Policy Management is displayed");
            console.log("First App Pass: Policy Management found.");
        } else {
            await this.takeScreenshot("Policy Management not found");
            console.log("First App Fail: Policy Management not found.");
        }
        return this.steps;
    }
}