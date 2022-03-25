import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser, fixture 'browser'")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser, yield")
    browser.quit()


class TestMainPage1():
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        print("\nstart test1 smoke")
        browser.get(link)
        browser.find_element(By.ID, "login_link")
        print("finish test1 smoke")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("\nstart test2 regression")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2 regression")
