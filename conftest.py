import pytest

from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920, 1080")
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome()

    yield driver

    driver.quit()
