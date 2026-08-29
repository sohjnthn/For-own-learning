import { writeFileSync, existsSync, mkdirSync } from 'node:fs';
import path from 'node:path';

export class ThirdAppObjects {
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
        let edgeBrowserDefaultWebpageSearchBar = await this.driver.$('//android.widget.EditText[@resource-id="com.microsoft.emmx.canary:id/url_bar"]');
        await this.takeScreenshot("Locate Edge browser search bar");
        await edgeBrowserDefaultWebpageSearchBar.click();

        await edgeBrowserDefaultWebpageSearchBar.setValue("MapleStorySEA (South-East Asia) tips [Facebook notes]");
        await this.takeScreenshot("Enter search term in search bar");

        await this.driver.keys('Enter');

        try {
            await this.driver.execute('mobile: scroll', { direction: 'down' });
        } catch (e) {}
        await this.takeScreenshot("Scroll down search results page");

        for (let j = 0; j < 9; j++) {
            // Check if session/app is still alive before capturing frames
            try {
                await this.takeScreenshot(`Additional inspection frame ${j + 1}`);
            } catch (err) {
                console.log(`App closed or unresponsive during frame ${j + 1}: ${err.message}`);
                break;
            }
        }
        console.log("Third App Execution Completed.");
        return this.steps;
    }
}