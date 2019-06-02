from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def element(self, page):
        """Gets the webelement of the specified object"""
        driver = page.driver
        WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(*self.locator))
        return driver.find_element(*self.locator)


class BasePageTextElement(BasePageElement):
    """Base page class that is initialized on every page text class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        element = self.element(obj)
        element.send_keys(Keys.CONTROL + 'A' + Keys.DELETE )
        element.send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        element = self.element(obj)
        return element.get_attribute("value")

class BasePageClickableElement(BasePageElement):
    """Base page class that is initialized on every page clickable element class."""
    def click(self, page):
        element = self.element(page)
        element.click()


class BasePageButton(BasePageClickableElement):
    """Base page class that is initialized on every page button class."""

    pass

class BasePageCheckBox(BasePageClickableElement):
    """Base page class that is initialized on every page checbox class."""

    pass

class BasePageAnchor(BasePageClickableElement):
    """Base page class that is initialized on every page anchor class."""

    def href(self, page):
        element = self.element(page)
        return element.get_attribute('href')

class BasePageSelectElement(BasePageElement):
    """todo"""

    def select_by_index(self, page, index):
        """todo"""
        element = Select(self.element(page))
        element.select_by_index(index)

    def select_by_value(self, page, value):
        """todo"""
        element = Select(self.element(page))
        element.select_by_value(value)

    def select_by_visible_text(self, page, text):
        """todo"""
        element = Select(self.element(page))
        element.select_by_visible_text(text)
