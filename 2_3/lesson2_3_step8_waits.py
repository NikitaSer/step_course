import time
import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver.exe')
browser = webdriver.Chrome(service=s)

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser.get(link)

    button = browser.find_element(By.ID, "book")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button.click()

    x = browser.find_element(By.ID, "input_value")
    x_text = x.text
    x_int = int(x.text)

    answer = calc(x_int)

    input = browser.find_element(By.CSS_SELECTOR, "[name='text']")
    input.send_keys(answer)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click();

finally:
    time.sleep(5)
    browser.quit()
