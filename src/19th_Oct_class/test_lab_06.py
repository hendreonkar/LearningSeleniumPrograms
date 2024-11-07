import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure

@pytest.mark.positive
@allure.title("Account Creation")
@allure.description("Creat an account on awesomeqa.com")

def test_project4_account_creation():
    driver=webdriver.Edge()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name_element=driver.find_element(By.XPATH, "//input[@id ='input-firstname']" )
    first_name_element.send_keys("Johny")
    last_name_element=driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name_element.send_keys("Sena")
    email_element=driver.find_element(By.XPATH, "//input[@id='input-email']")
    email_element.send_keys("john.sena@test2.com")
    telephone_element=driver.find_element(By.XPATH, "//input[@placeholder='Telephone']")
    telephone_element.send_keys("1234567890")
    password_element=driver.find_element(By.XPATH, "//input[@id='input-password']")
    password_element.send_keys("awesome")
    cnf_password_element=driver.find_element(By.XPATH, "//input[@name='confirm']")
    cnf_password_element.send_keys("awesome")
    checkbox_element=driver.find_element(By.XPATH, "//input[@name='agree']")
    checkbox_element.click()
    continue_element=driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_element.click()

    time.sleep(3)

    assert driver.current_url=="https://awesomeqa.com/ui/index.php?route=account/success"


