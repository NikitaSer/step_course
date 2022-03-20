from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math
import time

s = Service('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver.exe')
webdriver = webdriver.Chrome(service=s)

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    webdriver.get(link)

    tresure = webdriver.find_element(By.CSS_SELECTOR, "#treasure")
    x = tresure.get_attribute("valuex")
    answer = calc(x)

    answer_field = webdriver.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(answer)

    checkbox = webdriver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = webdriver.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    button = webdriver.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    webdriver.quit()
