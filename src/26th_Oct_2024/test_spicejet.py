from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def test_spicejet_web():
    driver=webdriver.Chrome()
    driver.get("https://www.spicejet.com")
    #//*[@class="css-1cwyjr8 r-homxoj r-ubezar r-10paoce r-13qz1uu" and @value=""]

    time.sleep(10)

    from_city=driver.find_elements(By.XPATH,"//input[@class='css-1cwyjr8 r-homxoj r-ubezar r-10paoce r-13qz1uu'] ")
    #from_city=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div[3]/div[2]/div[3]/div/div[1]/div[1]/div[2]/input")

    action=ActionChains(driver=driver)
    action.move_to_element(from_city[0]).click().send_keys("pnq").perform()
    #time.sleep(2)
    #(action.move_to_element(from_city).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform())
    time.sleep(10)
    driver.quit()