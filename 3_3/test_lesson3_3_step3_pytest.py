from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest

# s = Service('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver.exe')
browser = webdriver.Chrome('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver.exe')


class Test_3_2_13(unittest.TestCase):
    def test_form_1(self):
        link_form_1 = "http://suninjuly.github.io/registration1.html"

        browser.get(link_form_1)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Nik")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Serg")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("test@gmail.com")

        button = browser.find_element(By.TAG_NAME, "button")
        button.click()

        browser.implicitly_wait(3)

        registration = browser.find_element(By.TAG_NAME, "h1")
        registration_text = registration.text

        self.assertEqual(registration_text, "Congratulations! You have successfully registered!",
                         "Registration failed, form_1")

    def test_form_2(self):
        link_form_2 = "http://suninjuly.github.io/registration2.html"

        browser.get(link_form_2)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Nik")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Serg")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("test@gmail.com")

        button = browser.find_element(By.TAG_NAME, "button")
        button.click()

        browser.implicitly_wait(3)

        registration = browser.find_element(By.TAG_NAME, "h1")
        registration_text = registration.text

        self.assertEqual(registration_text, "Congratulations! You have successfully registered!",
                         "Registration failed, form_2")


if __name__ == '__main__':
    unittest.main()
