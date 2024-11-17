from selenium import webdriver
from selenium.webdriver.common.by import By

def test_svg():
    driver= webdriver.Edge()
    driver.get("https://flipkart.com")

    search_box_element=driver.find_element(By.XPATH, "//input[@name='q']")
    search_box_element.send_keys("Nothing phone 2a")

    list_svg_elements= driver.find_elements(By.XPATH, "//*[name()='svg']")
    list_svg_elements[0].click()
    
