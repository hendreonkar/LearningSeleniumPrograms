from selenium import webdriver
import time


def test_open_url():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_data=driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    time.sleep(10)
    driver.quit()

