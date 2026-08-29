import { remote } from 'webdriverio';
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { FirstAppObjects } from './FirstAppObjects.js';
import { SecondAppObjects } from './SecondAppObjects.js';
import { ThirdAppObjects } from './ThirdAppObjects.js';

const TARGET_DIR = path.resolve(process.cwd(), 'target');

async function TestAndroidApps() {
    if (!existsSync(TARGET_DIR)) {
        mkdirSync(TARGET_DIR, { recursive: true });
    }

    let reportData = [];

    // App 1 Execution
    let driver1 = await remote({
        hostname: '127.0.0.1',
        port: 4723,
        path: '/wd/hub',
        capabilities: {
            platformName: 'Android',
            'appium:platformVersion': '16.0',
            'appium:app': 'C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\app\\com.afwsamples.testdpc_9.0.12-9012_minAPI21(nodpi)_apkmirror.com.apk',
            'appium:automationName': 'UiAutomator2'
        }
    });
    try {
        let app1 = new FirstAppObjects(driver1, TARGET_DIR);
        let steps = await app1.execute();
        reportData.push({ appName: 'First App (TestDPC)', status: 'Passed', steps });
    } catch (e) {
        reportData.push({ appName: 'First App (TestDPC)', status: 'Failed', steps: [], error: e.message });
    } finally {
        await driver1.deleteSession();
    }

    // App 2 Execution
    let driver2 = await remote({
        hostname: '127.0.0.1',
        port: 4723,
        path: '/wd/hub',
        capabilities: {
            platformName: 'Android',
            'appium:platformVersion': '16.0',
            'appium:app': 'C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\app\\ApiDemos-debug.apk',
            'appium:automationName': 'UiAutomator2'
        }
    });
    try {
        let app2 = new SecondAppObjects(driver2, TARGET_DIR);
        let steps = await app2.execute();
        reportData.push({ appName: 'Second App (API Demos)', status: 'Passed', steps });
    } catch (e) {
        reportData.push({ appName: 'Second App (API Demos)', status: 'Failed', steps: [], error: e.message });
    } finally {
        await driver2.deleteSession();
    }

    // App 3 Execution
    let driver3 = await remote({
        hostname: '127.0.0.1',
        port: 4723,
        path: '/wd/hub',
        capabilities: {
            platformName: 'Android',
            'appium:platformVersion': '16.0',
            'appium:app': 'C:\\Users\\sohjnthn\\IdeaProjects\\Selenium_Tutorial\\app\\com.microsoft.emmx.canary_138.0.3336.0-333600000_minAPI26(armeabi-v7a)(nodpi)_apkmirror.com.apk',
            'appium:automationName': 'UiAutomator2'
        }
    });
    try {
        let app3 = new ThirdAppObjects(driver3, TARGET_DIR);
        let steps = await app3.execute();
        reportData.push({ appName: 'Third App (Edge Canary)', status: 'Passed', steps });
    } catch (e) {
        reportData.push({ appName: 'Third App (Edge Canary)', status: 'Failed', steps: app3?.steps || [], error: e.message });
    } finally {
        try {
            await driver3.deleteSession();
        } catch (err) {}
    }

    // Generate HTML Report
    const htmlReportPath = path.join(TARGET_DIR, 'TestExecutionReport.html');
    const htmlContent = `<!DOCTYPE html>
<html>
<head>
    <title>Android Test Execution Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background: #f9f9fb; color: #333; }
        h1 { color: #0056b3; }
        .app-section { background: #fff; border-radius: 8px; padding: 20px; margin-bottom: 25px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { padding: 10px 12px; border: 1px solid #e1e4e8; text-align: left; vertical-align: middle; }
        th { background-color: #0056b3; color: white; }
        .Passed { color: #28a745; font-weight: bold; }
        .Failed { color: #dc3545; font-weight: bold; }
        img { width: 120px; height: auto; border: 1px solid #ddd; border-radius: 4px; cursor: pointer; transition: 0.2s; }
        img:hover { transform: scale(1.8); }
        .error-msg { background: #ffe6e6; color: #dc3545; padding: 10px; margin-top: 10px; border-radius: 4px; font-size: 14px; }
    </style>
</head>
<body>
    <h1>Android Test Automation Execution Report</h1>
    <p><strong>Generated on:</strong> ${new Date().toLocaleString()}</p>
    
    ${reportData.map(app => `
        <div class="app-section">
            <h2>${app.appName} - <span class="${app.status}">${app.status}</span></h2>
            ${app.error ? `<div class="error-msg"><strong>Error / Crash Details:</strong> ${app.error}</div>` : ''}
            <table>
                <tr>
                    <th style="width: 10%;">Step</th>
                    <th style="width: 50%;">Description</th>
                    <th style="width: 40%;">Screenshot</th>
                </tr>
                ${app.steps.length > 0 ? app.steps.map((s, index) => `
                    <tr>
                        <td><strong>#${index + 1}</strong></td>
                        <td>${s.description}</td>
                        <td><a href="${s.image}" target="_blank"><img src="${s.image}" alt="Step ${index + 1}"/></a></td>
                    </tr>
                `).join('') : `<tr><td colspan="3" style="text-align: center; color: #dc3545;">No steps executed or session terminated immediately.</td></tr>`}
            </table>
        </div>
    `).join('')}
</body>
</html>`;

    writeFileSync(htmlReportPath, htmlContent);
    console.log(`Rich HTML Report generated at: ${htmlReportPath}`);
}

TestAndroidApps().catch(console.error);