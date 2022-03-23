# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture()
# def browser():
#     print("\nstart browser 'fixture browser")
#     s = Service('C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver'
#                 '.exe')
#     browser = webdriver.Chrome(service=s)
#     yield browser
#     print("\nquit browser")
#     browser.quit()
#
#
# class TestMainPage1():
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.ID, "login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("\n^_^ scope class")
    yield
    print("\n:3 scope class")


@pytest.fixture()
def very_important_fixture():
    print("\n:), fixture()")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print("\n:-Р, autouse=True")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        y = 100

    def test_second_smiling_faces(self, prepare_faces):
        x = 50