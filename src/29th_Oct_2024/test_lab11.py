
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
import time

def test_shadow_dom_js():
    chrome_options=webdriver.ChromeOptions()
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    # Scroll into the view where div is present
    username_div=driver.find_element(By.XPATH, "//div[@id='userName']")
    driver.execute_script("arguments[0].scrollIntoView(true);",username_div)

    input_box=driver.execute_script("return document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza')")
    input_box.send_keys("farmhouse")

    time.sleep(5)
    driver.quit()