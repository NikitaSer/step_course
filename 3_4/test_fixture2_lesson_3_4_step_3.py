import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print("\nstart browser from test... ITS DEFINED FIXTURE 'browser'")
    s = Service('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    return browser

class TestMainPage1():
    def test_quest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "login_link")

    def test_quest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")