from argparse import Action

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.chrome.options import Options
import time

@allure.title("Action, Windows, Iframe")
@allure.description("Testing Action, Windows, Iframe")

def test_task3():
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver= webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/test/ab/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")
    driver.maximize_window()
    #time.sleep(5)

    main_window_handle= driver.current_window_handle

    list=driver.find_elements(By.XPATH, "//img[@data-qa='danawobuqa']")

    variation=list[1]

    actions= ActionChains(driver=driver)

    actions.click(variation).perform()

    time.sleep(15)

    all_handles=driver.window_handles
    print(all_handles)

    for handle in all_handles:
        if handle!=main_window_handle:
            driver.switch_to.window(handle)
            #child window
            driver.switch_to.frame("heatmap-iframe")
            click_map=driver.find_element(By.XPATH,"//div[@data-qa='liqokuxuba']")
            click_map.click()

            time.sleep(20)



    driver.quit()





