from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.CSS_SELECTOR, 'button.button:nth-child(2)')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    MIN_PRICE = (By.ID, 'price[min]')
    MAX_PRICE = (By.ID, 'price[max]')

