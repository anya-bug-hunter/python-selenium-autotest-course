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


def test_check_locators_xpath(driver):
    driver.get("https://limestore.com/ru_ru/product/28911_8969_454-temno_krasnyi")
    time.sleep(8)

    title = driver.find_element(By.XPATH, "//div[@class='ProductTitlePrice__title']/h1")
    assert title.text == "ПЛАТЬЕ МАКСИ ИЗ 100% ШЕРСТИ"

    colors = driver.find_elements(By.XPATH, "//div[@class='ColorSelector__items']/child::div")
    assert len(colors) == 2

    button_cart = driver.find_element(By.XPATH, "//span[normalize-space(text())='Добавить в корзину']")
    assert button_cart.is_displayed()

    fit_block = driver.find_element(By.XPATH, "//div[contains(@class, 'text--gray') and position()=last()]")
    assert fit_block.is_displayed()
