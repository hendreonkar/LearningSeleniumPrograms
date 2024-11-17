import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_js_alert():
    driver= webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    alert_element=driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    alert_element.click()

    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())

    alert=driver.switch_to.alert
    alert.accept()

    result_element=driver.find_element(By.XPATH, "//p[@id='result']")

    assert result_element.text == "You successfully clicked an alert"

def test_js_confirm():
    driver= webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    alert_element=driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    alert_element.click()

    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())

    alert=driver.switch_to.alert
    alert.dismiss()

    result_element=driver.find_element(By.XPATH, "//p[@id='result']")

    assert result_element.text == "You clicked: Cancel"


def test_js_prompt():
    driver= webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    alert_element=driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    alert_element.click()

    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())

    alert=driver.switch_to.alert
    alert.send_keys("Onkar")

    alert.accept()

    result_element=driver.find_element(By.XPATH, "//p[@id='result']")

    assert result_element.text == "You entered: Onkar"


