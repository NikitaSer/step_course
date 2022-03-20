from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver.exe')
webdriver = webdriver.Chrome(service=s)

link = "http://suninjuly.github.io/selects1.html"

try:
    webdriver.get(link)

    num_1 = webdriver.find_element(By.ID, "num1")
    num_1_int = int(num_1.text)

    num_2 = webdriver.find_element(By.ID, "num2")
    num_2_int = int(num_2.text)

    sum = num_1_int + num_2_int
    print(sum)
    select = Select(webdriver.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum))

    button = webdriver.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    webdriver.quit()
