from selenium import webdriver

from selenium.webdriver.common.by import By
import time

def test_make_appointment():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

   # 1 - Find the element the anchor tag
    """
    < a
    id = "btn-make-appointment"
    href = "./profile.php#login"


    class ="btn btn-dark btn-lg" > Make Appointment < / a >

    """
    make_appointment_element= driver.find_element(By.ID, "btn-make-appointment")

    make_appointment_element.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(10)
    driver.quit()
