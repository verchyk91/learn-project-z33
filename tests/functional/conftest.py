import pytest
from selenium import webdriver


@pytest.yield_fixture(scope="function", autouse=True)
def firefox():
    firefox = webdriver.Firefox()
    firefox.add_argument("headless")

    browser = webdriver.Firefox(firefox=firefox)
    browser.implicitly_wait(10)

    try:
        yield browser
    finally:
        browser.close()
        browser.quit()