from behave import *
from selenium import webdriver
import page
import time

#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given("website '{url}'")
def step(context, url):
    context.browser = webdriver.Firefox(executable_path=r"./geckodriver")
    context.browser.get("https://rozetka.com.ua/ua/")
    context.main_page = page.MainPage(context.browser)

@then("page title include text '{text}'")
def step(context, text):
    assert context.main_page.is_title_matches(text), f"{text} title doesn't match."

@then("input in search text '{text}'")
def step(context, text):
    context.main_page.search_text_element = text

# Теперь нажмем на кнопку "Найти"
@then('push button search')
def step(context):
    context.main_page.click_go_button()

@then("page search has results for search")
def step(context):
    context.search_results_page = page.SearchResultsPage(context.browser)
    #Verifies that the results page is not empty
    assert context.search_results_page.is_results_found(), "No results found."

@then("set category as ukrainian souvenirs")
def step(context):
    context.search_results_page.set_category_ukrainian_souvenirs()

@then("set the country manufacturer Ukraine")
def step(context):
    context.search_results_page.set_country_producer_ukraine()

@then("set the minimum price of the goods as '{price}'")
def step(context, price):
    context.search_results_page.minimum_price_element = price
    context.search_results_page.update_range_price()

@then("set the maximum price of the goods as '{price}'")
def step(context, price):
    context.search_results_page.maximum_price_element = price
    context.search_results_page.update_range_price()

@then("click on the first element")
def step(context):
    context.search_results_page.click_first_product()
    context.product_page = page.ProductPage(context.browser)

@then("push the button 'to basket'")
def step(context):
    context.product_page.click_buy_product()

@then("push the button 'order'")
def step(context):
    context.product_page.click_to_order()
    context.order_page = page.OrderPage(context.browser)

@then("input name and last name as '{text}'")
def step(context, text):
    context.order_page.name_and_sorname_text_element = text

@then("input phone number as '{text}'")
def step(context, text):
    context.order_page.mobile_phone_text_element = text

@then("input email as '{text}'")
def step(context, text):
    context.order_page.email_text_element = 'n1232ame@gmail.com'

@then("push the button 'next'")
def step(context):
    time.sleep(5)
    context.order_page.click_next_step()

@then("input name as '{text}'")
def step(context, text):
    context.order_page.name_text_element = text

@then("input last name as '{text}'")
def step(context, text):
    context.order_page.sorname_text_element = text

@then("select 'New mail' office")
def step(context):
    context.order_page.click_select_np()

@then("button 'confirm order' is active")
def step(context):
    time.sleep(5)
    assert context.order_page.make_order_button_is_unnable(), 'Button confirmation of the order is not unnable'

@then("close webdriver")
def step(context):
        context.browser.close()

