import pytest

url = "http://localhost:8000"


@pytest.mark.functional
def test_html(chrome):
    chrome.get(f"{url}/")
    assert "Fireworks" in chrome.title
    assert "Big" in chrome.page_source
    assert "/s/main.css" in chrome.page_source
    assert "/i/logo.png" in chrome.page_source
    assert (
        """<progress id="progress" value="9" max="26">34%</progress>"""
        in chrome.page_source
    )


@pytest.mark.functional
def test_logo_svg(chrome):
    chrome.get(f"{url}/i/logo.png")
    assert "png" in chrome.page_source


@pytest.mark.functional
def test_main_css(chrome, main_css):
    chrome.get(f"{url}/s/main.css")
    assert main_css in chrome.page_source
