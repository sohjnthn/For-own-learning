const {By, Builder, Browser, Key} = require('selenium-webdriver');
const FirstGroupOfWebsites = require ('./FirstGroupOfWebsites.js');
const SecondGroupOfWebsites = require ('./SecondGroupOfWebsites.js');
const ThirdGroupOfWebsites = require ('./ThirdGroupOfWebsites.js');
const fs = require("fs");

let driver;

async function MainWebsites(){

    driver = await new Builder().forBrowser(Browser.CHROME).build();

    // *Need to run multiple times as the html reports can be incorrect due to overwriting of screenshot images;
    // and due to screenshot images being blank if Steps i do not start from 1 for the page JavaScript files.*

    // Steps 1 to 39: This is for the original 39 screenshot images.
    const FirstGroupOfWebsites = new FirstGroupOfWebsites();

    // Note: The step numbers i for each page JavaScript file should start from 1,
    // so that the screenshot images are displayed (would not be blank) for the html reports from
    // the second page JavaScript file onwards

    // Steps 1 to 2: This is only for reaching the Latest tab https://aminoapps.com/c/maplestorysea/recent/ with the driver
    const SecondGroupOfWebsites = new SecondGroupOfWebsites();

    // Steps: 1 to 4: This is only for reaching the Home tab https://aminoapps.com/c/maplestorysea/home/ with the driver,
    // then going to the Latest tab by locating the text "Latest" (there should be no whitespace characters after > and before < for Inspect)
    const ThirdGroupOfWebsites = new ThirdGroupOfWebsites();

    // For each page JavaScript file, only immediately after the first driver.get("..."); statement,
    // let title1 = await driver.getTitle(); should be used, so that the first screenshot image of the html report would not be uncaptured
    // title1's number 1 can be any number

    // Using for loops to try to cause later (the second and third) page JavaScript files to run actually
    // prevents the first page JavaScript file from starting due to the for loop delay

    // Screenshot images for the html reports for the second page JavaScript file onwards can be incorrect

    // Text which are supposed to be entered are sometimes not captured by the screenshot images

    // Does nothing (the fourth html report is not generated)
    // const testResults = [...FirstGroupOfWebsites, ...SecondGroupOfWebsites, ...ThirdGroupOfWebsites];

    // Does nothing (the fourth html report is not generated)
    // let htmlContent = '<html><body><h1>Test Report</h1>';
    // testResults.forEach(result => {
        // htmlContent += `<div>
        // <p>Step: ${result.step}</p>
        // <p>Status: ${result.status}</p>
        // <img src="${result.screenshot}" alt="Screenshot" width="300">
    // </div>`;
    // });
    // htmlContent += '</body></html>';
    // fs.writeFileSync('./' + currentDateTime() + '_test-report.html', htmlContent);
    // console.log('Report generated: test-report.html');
}


