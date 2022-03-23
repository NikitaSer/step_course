import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser, fixture 'browser'")
    s = Service('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver'
                '.exe')
    browser = webdriver.Chrome(service=s)
    yield browser
    print("\nquit browser, yield")
    browser.quit()


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        print("\nstart test1")
        browser.get(link)
        browser.find_element(By.ID, "login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("\nstart test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")
