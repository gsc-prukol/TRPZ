import unittest
from selenium import webdriver
import page
import time

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"./geckodriver")
        self.driver.get("https://rozetka.com.ua/ua/")
        # self.driver.find_element_by_id('1').value_of_css_property('background-color') # v.send_keys(100)

    def test_search_in_rozetka_ua(self):
        """
        Tests rozetka.ua search feature. Searches for the word "украинская" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        #Load the main page. In this case the home page of Python.og.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "украина"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."
        search_results_page.set_category_ukrainian_souvenirs()
        search_results_page.set_country_producer_ukraine()
        search_results_page.minimum_price_element = 100
        search_results_page.maximum_price_element = 2000
        search_results_page.update_range_price()
        search_results_page.click_first_product()
        product_page = page.ProductPage(self.driver)
        product_page.click_buy_product()
        product_page.click_to_order()
        order_page = page.OrderPage(self.driver)
        order_page.name_and_sorname_text_element = "Імя Прізвище"
        order_page.mobile_phone_text_element = '+380666666666'
        order_page.email_text_element = 'n1232ame@gmail.com'
        time.sleep(5)
        order_page.click_next_step()
        order_page.name_text_element = 'Імя'
        order_page.sorname_text_element = 'Прізвище'
        order_page.click_select_np()
        time.sleep(5)
        assert order_page.make_order_button_is_unnable(), 'Button confirmation of the order is not unnable'
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()