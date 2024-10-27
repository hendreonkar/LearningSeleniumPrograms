from selenium import webdriver


def test_open_url():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.title == "CURA Healthcare Service"