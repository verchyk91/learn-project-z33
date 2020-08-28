import pytest
from selenium import webdriver

import settings


@pytest.yield_fixture(scope="function", autouse=True)
def chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")

    browser = webdriver.Firefox(executable_path="/home/dmitry/geckodriver")
    browser.get('http://www.google.com')
    browser.implicitly_wait(10)

    try:
        yield browser
    finally:
        browser.close()
        browser.quit()


@pytest.yield_fixture(scope="function", autouse=True)
def main_css():
    path = settings.STATIC_DIR / "styles" / "main.css"
    with path.open("r") as src:
        yield src.read()


@pytest.yield_fixture(scope="function", autouse=True)
def logo_png():
    path = settings.STATIC_DIR / "images" / "logo.png"
    with path.open("rb") as src:
        yield src.read()
