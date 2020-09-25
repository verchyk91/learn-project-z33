from datetime import datetime
from functools import wraps

from selenium import webdriver

from framework import settings


def build_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")

    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(4)

    return browser


def screenshot_on_failure(test):
    @wraps(test)
    def decorated_test(browser, request, *args, **kwargs):
        try:
            test(browser, request, *args, **kwargs)
        except Exception:
            ts = datetime.now().strftime(f"%Y.%m.%d.%H.%M.%S")
            test_name = f"{request.module.__name__}.{test.__name__}"
            png = f"{test_name}.{ts}.png"
            html = f"{test_name}.{ts}.html"
            png_path = (settings.ARTIFACTS_DIR / png).resolve()
            html_path = (settings.ARTIFACTS_DIR / html).resolve()
            with html_path.open("w") as _dst:
                _dst.write(browser.page_source)
            browser.save_screenshot(png_path.as_posix())
            raise

    return decorated_test
