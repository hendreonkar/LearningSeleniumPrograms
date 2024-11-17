from selenium   import webdriver
from selenium.webdriver.common.by import By

import time
import allure

@allure.title("Serach macmini")
@allure.description("Print titles and prices")
def test_search_macmini_print_titles():
    driver= webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_box_element=driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    search_box_element.send_keys("macmini")
    search_button_element=driver.find_element(By.CSS_SELECTOR, "input[value='Search']")
    search_button_element.click()

    #list_titles_elements=driver.find_elements(By.CSS_SELECTOR, "div.s-item__title")
    list_prices_elements=driver.find_elements(By.CSS_SELECTOR, "//span[@class='s-item__price']")


    #for i in list_titles_elements:
        #print (i.text)

    for j in list_prices_elements:
        print(j.text)






    time.sleep(5)
    driver.quit()
