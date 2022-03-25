import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc():
    return math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser, fixture 'browser'")
    browser = webdriver.Chrome(
        'C:/Users/mykyta.serhiienko/Desktop/nik/python_course/environments/selenium_env/Scripts/chromedriver.exe')
    yield browser
    print("\nquit browser, yield")
    browser.quit()


class TestMainPage1:
    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                      "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1",
                                      "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"
                                      ])
    def test_param_links(self, browser, link):
        print(f"\nstart {link}")

        browser.implicitly_wait(10)

        browser.get(link)

        text_field = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
        text_field.send_keys(calc())

        submit_button = browser.find_element(By.CSS_SELECTOR, '.submit-submission[type="button"]')
        submit_button.click()

        feedback_hint = browser.find_element(By.CSS_SELECTOR, ".smart-hints__feedback .smart-hints__hint")
        feedback_hint_text = feedback_hint.text

        assert feedback_hint_text == "Correct!", f"\nfeedback_hint is '{feedback_hint_text}' != 'Correct!' for the link = {link}\n"

        print(f"finish {link}")
