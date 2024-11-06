from webbrowser import Chrome

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time

def test_task3():

    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.youtube.com/Venus")
    page_src=driver.page_source
    assert "Music" in page_src
    driver.close()


def test_task4():

    #chrome_options=Options()
    #chrome_options.add_argument("--incognito")
    #chrome_options.add_argument("--headless")

    driver = webdriver.Edge()
    driver.get("https://www.youtube.com/Venus")
    time.sleep(7)
    driver.close()

def test_task5():
    driver=webdriver.Firefox()
    driver.get("https://app.vwo.com")
    time.sleep(7)
    driver.close()