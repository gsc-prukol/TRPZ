from element import BasePageElement, BasePageButton
from locators import *

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = MainPageLocators.SEARCH_TEXT_ELEMENT

class SearchButton(BasePageButton):
    """This class is button the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = MainPageLocators.GO_BUTTON

class MinimumPriceElement(BasePageElement):
    """This class gets the minimum price field from the specified locator"""

    # The locator for search box where search string is entered
    locator = SearchResultsPageLocators.MIN_PRICE

class MaximumPriceElement(BasePageElement):
    """This class gets the maximum price field from the specified locator"""

    # The locator for search box where search string is entered
    locator = SearchResultsPageLocators.MAX_PRICE

class UpdateRangePriceButton(BasePageButton):
    """This class is button the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = SearchResultsPageLocators.RANGE_PRICE_SUBMIT


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. rozetka.ua"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()
    search_button = SearchButton()
    def is_title_matches(self):
        """Verifies that the hardcoded text "Пошук" appears in page title"""
        return "ROZETKA" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        self.search_button.click(self)


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    minimum_price_element = MinimumPriceElement()
    maximum_price_element = MaximumPriceElement()
    update_range_price_button = UpdateRangePriceButton()
    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source


    def update_range_price(self):
        """Triggers the range price"""
        self.update_range_price_button.click(self)