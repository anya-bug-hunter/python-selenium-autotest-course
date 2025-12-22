import time

from selenium.webdriver.common.by import By


def test_check_title(driver):
    driver.get("https://limestore.com/ru_ru/")
    expected_title = "LIME | Официальный магазин"
    time.sleep(8)
    actual_title = driver.title
    assert actual_title == expected_title, "Заголовок страницы неверный!"


def test_check_locators_css(driver):
    driver.get("https://limestore.com/ru_ru/")
    time.sleep(8)

    logo = driver.find_element(By.ID, "logo")
    assert logo.is_displayed()

    search_input = driver.find_element(By.NAME, "search")
    assert not search_input.is_displayed()

    icon_buttons = driver.find_elements(By.CLASS_NAME, "btn-control")
    assert len(icon_buttons) == 4

    buttons = driver.find_elements(By.TAG_NAME, "button")
    assert len(buttons) > 1

    menu = driver.find_element(By.CSS_SELECTOR, "#logo .hamburger-menu.burger")
    menu.click()

    time.sleep(1)