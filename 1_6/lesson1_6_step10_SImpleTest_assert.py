from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver.exe')
browser = webdriver.Chrome(service=s)

link = "http://suninjuly.github.io/registration1.html"

try:
    #код, который заполняет обязательные поля
    browser.get(link)
    input1 = browser.find_element(By.CLASS_NAME, "first")
    input1.send_keys("Nik")

    input2 = browser.find_element(By.CLASS_NAME, "second")
    input2.send_keys("Serg")

    input3 = browser.find_element(By.CLASS_NAME, "third")
    input3.send_keys("test@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    #Сравниваем текс при успешной регистрации
    registration = browser.find_element(By.TAG_NAME, "h1")
    registration_text = registration.text

    assert "Congratulations! You have successfully registered!" == registration_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
