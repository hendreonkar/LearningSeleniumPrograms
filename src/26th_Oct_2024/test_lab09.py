from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys


def test_actions_p1():
    driver=webdriver.Chrome()

    driver.get("https://awesomeqa.com/practice.html")

    first_name=driver.find_element(By.XPATH,"//input[@name='firstname']")
    #keydown
    actions=ActionChains(driver=driver)

    (actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"onkar").key_up(Keys.SHIFT).perform())

    time.sleep(10)
    driver.quit()


def test_actions_p2():
    driver=webdriver.Chrome()

    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    link=driver.find_element(By.XPATH,"//a[@id='click']")
    link.click()

    time.sleep(2)

    action_builders=ActionBuilder(driver=driver)
    action_builders.pointer_action.pointer_up(MouseButton.BACK)
    action_builders.perform()

    time.sleep(10)
    driver.quit()

def test_actios_p3():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    draggable = driver.find_element(By.ID,"draggable")

    action=ActionChains(driver=driver)
    action.click_and_hold(on_element=draggable).perform()

    time.sleep(10)

    droppable=driver.find_element(By.ID,"droppable")
    action.drag_and_drop(source=draggable,target=droppable).perform()

    time.sleep(10)
    driver.quit()