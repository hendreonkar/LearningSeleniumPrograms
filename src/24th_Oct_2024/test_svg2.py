"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_svg():
    driver= webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    list_svg_elements=driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in list_svg_elements:
        print(state.get_attribute("aria-label"))
        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)
 """


import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("SVG")
@allure.description("Verify svg")
def test_verify_svg():
    driver = webdriver.Firefox()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    agree_element=driver.find_element(By.XPATH, "//*[@id='notice_policy']/div[2]/input")
    agree_element.click()
    #name() or local-name()

    # //*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']

    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in list_of_states:
        print(state.get_attribute("aria-label"))
        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)
    driver.quit()
