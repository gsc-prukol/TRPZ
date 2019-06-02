from element import *
from locators import *

class SearchTextElement(BasePageTextElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = MainPageLocators.SEARCH_TEXT_ELEMENT

class SearchButton(BasePageButton):
    """This class is button the search text from the specified locator"""

    #The locator for button search where search is trigerret
    locator = MainPageLocators.GO_BUTTON

class MinimumPriceTextElement(BasePageTextElement):
    """This class gets the minimum price field from the specified locator"""

    # The locator for minimum price box where minimum price string is entered
    locator = SearchResultsPageLocators.MIN_PRICE

class MaximumPriceTextElement(BasePageTextElement):
    """This class gets the maximum price field from the specified locator"""

    # The locator for maximum price box where maximum price string is entered
    locator = SearchResultsPageLocators.MAX_PRICE

class UpdateRangePriceButton(BasePageButton):
    """This class is button the update range price from the specified locator"""

    #The locator for button update range price where price filter is trigerret
    locator = SearchResultsPageLocators.RANGE_PRICE_SUBMIT

class UkrainianSouvenirsAnchor(BasePageAnchor):
    """This class is anchor  to ukrainian souvenirs from the specified locator"""

    #The locator for the ukrainian souvenir where ukrainian souvenir is trigerret
    locator = SearchResultsPageLocators.UKRAINIAN_SOUVENIRS

class ProducerUkraineCheckbox(BasePageCheckBox):
    """This class is checkbox the produce Ukraine from the specified locator"""

    #The locator for checkbox produce Ukrain where produce filter is trigerret
    locator = SearchResultsPageLocators.PRODUCE_URRAIN_CHECKBOX

class FirstProductElement(BasePageClickableElement):
    """This class is element to go to the first product page"""

    #The locator for the first product in where the first product is entered
    locator = SearchResultsPageLocators.FIRST_PRODUCT

class BuyProductButton(BasePageButton):
    """todo"""

    #todo
    locator = ProductPageLocators.BUY_BUTTON

class ToOrderButton(BasePageButton):
    """"todo"""

    #todo
    locator = ProductPageLocators.TO_ORDER_BUTTON


class NameAndSornameTextElement(BasePageTextElement):
    """todo"""

    # todo
    locator = OrderPageLocators.NAME_AND_SORNAME

class MobilePhoneTextElement(BasePageTextElement):
    """todo"""

    # todo
    locator = OrderPageLocators.MOBILE_PHONE

class EmailTextElement(BasePageTextElement):
    """todo"""

    # todo
    locator = OrderPageLocators.EMAIL

class NextStepButton(BasePageButton):
    """todo"""

    #todo
    locator = OrderPageLocators.NEXT_STEP_BUTTON

class NPSelectAnchor(BasePageAnchor):
    """todo"""

    #todo
    locator = OrderPageLocators.SELECT_NP

class NPSelect2Anchor(BasePageAnchor):
    locator = OrderPageLocators.SELECT_NP2

class NameTextElement(BasePageTextElement):
    """todo"""

    # todo
    locator = OrderPageLocators.NAME


class SornameTextElement(BasePageTextElement):
    """todo"""

    # todo
    locator = OrderPageLocators.SORNAME

class MakeOrderButton(BasePageButton):
    locator = OrderPageLocators.CONFIRMATION_ORDER

    def is_unnable(self, page):
        element = self.element(page)
        color = element.value_of_css_property('background-color')
        return color == 'rgb(0, 160, 70)'



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

    minimum_price_element = MinimumPriceTextElement()
    maximum_price_element = MaximumPriceTextElement()
    update_range_price_button = UpdateRangePriceButton()
    ukrainian_souvenirs_anchor = UkrainianSouvenirsAnchor()
    prodecer_ukraine_checkbox = ProducerUkraineCheckbox()
    first_product_element = FirstProductElement()

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source


    def update_range_price(self):
        """Triggers the range price"""
        self.update_range_price_button.click(self)

    def set_category_ukrainian_souvenirs(self):
        """Set category as ukrainian souvenirs"""
        self.ukrainian_souvenirs_anchor.click(self)

    def set_country_producer_ukraine(self):
        """Set country producer as Ukraine souvenirs"""
        self.prodecer_ukraine_checkbox.click(self)

    def click_first_product(self):
        """Go to page first product"""
        self.first_product_element.click(self)

class ProductPage(BasePage):
    """Product page action methods come here"""
    bay_product_button = BuyProductButton()
    to_order_button = ToOrderButton()


    def click_buy_product(self):
        self.bay_product_button.click(self)

    def click_to_order(self):
        self.to_order_button.click(self)

class OrderPage(BasePage):
    """todo"""
    name_and_sorname_text_element = NameAndSornameTextElement()
    mobile_phone_text_element = MobilePhoneTextElement()
    email_text_element = EmailTextElement()
    next_step_button = NextStepButton()
    np_select_anchor = NPSelectAnchor()
    np_select2_anchor = NPSelect2Anchor()
    name_text_element = NameTextElement()
    sorname_text_element = SornameTextElement()
    make_order_button = MakeOrderButton()
    def click_next_step(self):
        self.next_step_button.click(self)

    def click_select_np(self):
        self.np_select_anchor.click(self)
        self.np_select2_anchor.click(self)

    def make_order_button_is_unnable(self):
        return self.make_order_button.is_unnable(self)
