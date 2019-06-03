Feature: Order
  Scenario: Search goods and order one of them
  Given website 'rozetka.com.ua/ua'
    Then page title include text 'ROZETKA'
    Then input in search text 'украина'
    Then push button search
    Then page search has results for search
    Then set category as ukrainian souvenirs
    Then set the country manufacturer Ukraine
    Then set the minimum price of the goods as '100'
    Then set the maximum price of the goods as '2000'
    Then click on the first element
    Then push the button 'to basket'
    Then push the button 'order'
    Then input name and last name as 'Імя Прізвище'
    Then input phone number as '+380666666666'
    Then input email as 'n1232ame@gmail.com'
    Then push the button 'next'
    Then input name as 'Імя'
    Then input last name as 'Прізвище'
    Then select 'New mail' office
    Then button 'confirm order' is active
    Then close webdriver

