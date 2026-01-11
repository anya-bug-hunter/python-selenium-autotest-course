import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


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


def test_implicit_wait(driver):
    driver.implicitly_wait(10)
    driver.get("https://limestore.com/ru_ru/product/28911_8969_454-temno_krasnyi")

    title = driver.find_element(By.XPATH, "//div[@class='ProductTitlePrice__title']/h1")
    assert title.text == "ПЛАТЬЕ МАКСИ ИЗ 100% ШЕРСТИ"


def test_check_explicit_wait(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://limestore.com/ru_ru/product/28911_8969_454-temno_krasnyi")

    wait.until(EC.title_contains("Платье макси из 100% шерсти темно-красный цвет - LIMÉ"))

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='ProductTitlePrice__title']/h1")
    ))

    menu_open_button = driver.find_element(By.CSS_SELECTOR, "div.hamburger-menu.burger")
    menu_open_button.click()

    parfum_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='mainmenu__kind' and text()='Парфюмерия']")
        ))
    parfum_menu.click()

    menu_link = driver.find_element(By.XPATH, "//a[@class='mainmenu__link']/span")
    menu_link.click()

    wait.until(EC.text_to_be_present_in_element(
        (By.XPATH, "//a[@class='mainmenu__link']/span"), "ЖЕНСКИЕ АРОМАТЫ"
    ))


def test_check_fluent_wait(driver):
    wait = WebDriverWait(
        driver,
        timeout=10,
        poll_frequency=0.2,
        ignored_exceptions=[NoSuchElementException]
    )

    driver.get("https://limestore.com/ru_ru/product/28911_8969_454-temno_krasnyi")

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='ProductTitlePrice__title']/h1")
    ))
