import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_check_title(driver):
    driver.get("https://limestore.com/ru_ru/")
    expected_title = "LIME | Официальный магазин"
    time.sleep(8)
    actual_title = driver.title
    assert actual_title == expected_title, "Заголовок страницы неверный!"
