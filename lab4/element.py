from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).send_keys(Keys.CONTROL + 'A' + Keys.DELETE )
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")

class BasePageButton(object):
    """Base page class that is initialized on every page button class."""

    def click(self, page):
        driver = page.driver
        WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        element.click()
