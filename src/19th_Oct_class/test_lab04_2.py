#import time
import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)

@pytest.mark.negative
@allure.title("Negative- testing login case")
@allure.description("Testing login case by giving username and password")

def test_Project2_login_negative_test():
#1. Go to the URL
    driver=webdriver.Firefox()
    driver.get("https://app.vwo.com/#/login")

    """
    <input type="email" class="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi">
    <input type="password" class="text-input W(100%)" name="password" id="login-password" data-qa="jobodapuxe">
    """
#2. Find elements and send keys
    username_web_element=driver.find_element(By.ID, "login-username")
    username_web_element.send_keys("abc@yahoo.com")
    password_web_element=driver.find_element(By.ID, "login-password")
    password_web_element.send_keys("Admin@201")
    submit_web_element=driver.find_element(By.ID, "js-login-btn")
    submit_web_element.click()

#wait for some time
    ignore_list=[ElementNotVisibleException,ElementNotSelectableException]

#Fluent wait
    (WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description"))))

#3. Verify the message

    """
    <div class="notification-box-description" 
    id="js-notification-box-msg" data-qa="rixawilomi">
    Your email, password, IP address or location did not match</div>

    """
    #Your email, password, IP address or location did not match

    message_web_element=driver.find_element(By.CLASS_NAME, "notification-box-description")
    assert message_web_element.text == "Your email, password, IP address or location did not match"

    driver.quit()