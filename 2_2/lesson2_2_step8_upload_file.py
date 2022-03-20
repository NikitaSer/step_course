import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver.exe')
browser = webdriver.Chrome(service=s)

link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)

    first_name_elem = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name_elem.send_keys("Nik")

    last_name_elem = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name_elem.send_keys("Serg")

    email_elem = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email_elem.send_keys("test@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "upload_me.txt")

    choose_file_button = browser.find_element(By.ID, "file")
    choose_file_button.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
