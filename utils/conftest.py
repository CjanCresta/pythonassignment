import pytest
from selenium import webdriver
from utils.config import BROWSER


@pytest.fixture
def browser():
    if BROWSER.lower() == "chrome":
        driver = webdriver.Chrome()
    elif BROWSER.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    yield driver

    # Teardown: Quit the browser after the test
    driver.quit()