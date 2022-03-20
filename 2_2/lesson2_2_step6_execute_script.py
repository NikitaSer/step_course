import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math

s = Service('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver.exe')
browser = webdriver.Chrome(service=s)

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x_text = x_element.text

    answer = calc(x_text)

    input_text = browser.find_element(By.CLASS_NAME, "form-control")
    input_text.send_keys(answer)

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()

    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
