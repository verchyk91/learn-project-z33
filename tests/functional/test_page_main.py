import pytest


@pytest.mark.functional
def test(firefox):
    firefox.get("http://localhost:8000/")
    assert "Study Project Z33" in firefox.title
    assert "Progress" in firefox.page_source