from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.CSS_SELECTOR, 'button.button:nth-child(2)')
    SEARCH_TEXT_ELEMENT = (By.CSS_SELECTOR, '.search-form__input')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    MIN_PRICE = (By.NAME, 'price[min]')
    MAX_PRICE = (By.ID, 'price[max]')
    RANGE_PRICE_SUBMIT = (By.ID, 'submitprice')
    UKRAINIAN_SOUVENIRS = (By.CSS_SELECTOR, r'#\38 0260 a')
    PRODUCE_URRAIN_CHECKBOX = (By.CSS_SELECTOR, r'#sort_98900 > li:nth-child(3) > label:nth-child(1)')
    FIRST_PRODUCT = (By.CSS_SELECTOR, r'div.g-i-tile:nth-child(1)')

class ProductPageLocators(object):
    """class for product locators. All product page locators should come here"""
    BUY_BUTTON = (By.CSS_SELECTOR, r'button.btn-link-i:nth-child(2)')
    TO_ORDER_BUTTON = (By.CSS_SELECTOR, r'button.btn-link-green')

class OrderPageLocators(object):
    """todo"""
    NAME_AND_SORNAME = (By.CSS_SELECTOR, r'#reciever_name')
    MOBILE_PHONE = (By.CSS_SELECTOR, r'#reciever_phone')
    EMAIL = (By.CSS_SELECTOR, r'#reciever_email')
    NEXT_STEP_BUTTON = (By.CSS_SELECTOR, '.opaque > button:nth-child(1)')
    SELECT_NP = (By.CSS_SELECTOR, r'.dropdown-link')
    SELECT_NP2 = (By.CSS_SELECTOR, r'li.pickups-select-dropdown-l-i:nth-child(2) > a:nth-child(1)')
    NAME = (By.CSS_SELECTOR, r'div.check-order-i:nth-child(4) > div:nth-child(1) > div:nth-child(9) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
    SORNAME = (By.CSS_SELECTOR, r'div.check-order-i:nth-child(4) > div:nth-child(1) > div:nth-child(8) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
    CONFIRMATION_ORDER = (By.CSS_SELECTOR, r'.check-submit')