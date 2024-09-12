import pytest
from selenium import webdriver


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    # Close the WebDriver instance
    driver.quit()