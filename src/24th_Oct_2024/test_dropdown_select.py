from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def test_dropdown():
    driver=webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    select_dropdown=driver.find_element(By.XPATH, "//select[@id='dropdown']")
    select=Select(select_dropdown)

    select.select_by_visible_text("Option 2")

    time.sleep(5)

    driver.close()