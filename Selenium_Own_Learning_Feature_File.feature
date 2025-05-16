Feature: Learning Google Chrome desktop web browser automation with IntelliJ Idea,
  Java, Selenium, and Cucumber

  Scenario: How to find WebElements which cannot be found with name, id, className,
  and partialLinkText
    Given that the easiest way to find WebElements is by driver.findElement; and driver.findElements which returns a List WebElement
    When it is not possible to do so for certain WebElements in this way
    Then we use driver.findElement By.tagName"...", for which ... can be i for <i> or button for <button>


