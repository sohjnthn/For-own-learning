import { Builder } from 'selenium-webdriver';
import { FirstGroupOfWebsites } from './FirstGroupOfWebsites.js';
import { SecondGroupOfWebsites } from './SecondGroupOfWebsites.js';
import { ThirdGroupOfWebsites } from './ThirdGroupOfWebsites.js';
import { writeFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs';

const TARGET_DIR = './target';

function generateBase64HtmlReport(results) {
    if (!existsSync(TARGET_DIR)) {
        mkdirSync(TARGET_DIR, { recursive: true });
    }

    const now = new Date();
    const formattedDateTime = `${now.getDate().toString().padStart(2, '0')}-${(now.getMonth() + 1).toString().padStart(2, '0')}-${now.getFullYear()}_${now.getHours().toString().padStart(2, '0')}${now.getMinutes().toString().padStart(2, '0')}${now.getSeconds().toString().padStart(2, '0')}`;
    const reportPath = `${TARGET_DIR}/Spark_${formattedDateTime}.html`;

    let htmlContent = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>Desktop Website Test Report</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f9; }
                h1 { color: #333; }
                .step-card { background: #fff; padding: 15px; margin-bottom: 15px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
                .PASS { color: green; font-weight: bold; }
                .FAIL { color: red; font-weight: bold; }
                img { max-width: 100%; height: auto; margin-top: 10px; border: 1px solid #ccc; border-radius: 4px; display: block; }
            </style>
        </head>
        <body>
            <h1>Desktop Website Test Report</h1>
            <p>Generated on: ${now.toLocaleString()}</p>
    `;

    for (let res of results) {
        htmlContent += `
            <div class="step-card">
                <h3>${res.step} - Status: <span class="${res.status}">${res.status}</span></h3>
        `;

        try {
            if (res.screenshot && existsSync(res.screenshot)) {
                const imageBuffer = readFileSync(res.screenshot);
                const base64Image = imageBuffer.toString('base64');
                htmlContent += `<img src="data:image/png;base64,${base64Image}" alt="${res.step}"><br>`;
            } else {
                htmlContent += `<p style="color: orange;">[Screenshot file missing on disk]</p>`;
            }
        } catch (err) {
            htmlContent += `<p style="color: red;">[Could not embed image: ${err.message}]</p>`;
        }

        htmlContent += `</div>`;
    }

    htmlContent += `
        </body>
        </html>
    `;

    writeFileSync(reportPath, htmlContent);
    console.log(`HTML Report generated: ${reportPath}`);
}

async function TestDesktopWebsites() {
    let driver = await new Builder().forBrowser('chrome').build();
    let allTestResults = [];
    let currentStep = 1;

    try {
        let firstWebsite = new FirstGroupOfWebsites(driver);
        let testOutput1 = await firstWebsite.executeTests(currentStep);
        allTestResults.push(...testOutput1.results);
        currentStep = testOutput1.nextStep;

        let secondWebsite = new SecondGroupOfWebsites(driver);
        let testOutput2 = await secondWebsite.executeTests(currentStep);
        allTestResults.push(...testOutput2.results);
        currentStep = testOutput2.nextStep;

        let thirdWebsite = new ThirdGroupOfWebsites(driver);
        let testOutput3 = await thirdWebsite.executeTests(currentStep);
        allTestResults.push(...testOutput3.results);
        currentStep = testOutput3.nextStep;

        generateBase64HtmlReport(allTestResults);

        console.log(`All desktop website tests completed successfully. Final step reached: ${currentStep - 1}`);
    } catch (error) {
        console.error("Error running desktop website tests:", error);
    } finally {
        await driver.quit();
    }
}

TestDesktopWebsites();