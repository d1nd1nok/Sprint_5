from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from src.locators import MainPageLocators as locators_main
from src.locators import AdPageLocators as locators_ad
from tests.test_login import login
from src.data import EXISTING_EMAIL, EXISTING_EMAIL_PASSWORD
from src.helpers import generate_random_ad
from selenium.webdriver.common.by import By
from src.config import Config


def open_ad_creation_form(driver):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locators_main.CREATE_AD_BUTTON)
    )
    try:
        button.click()
    except StaleElementReferenceException:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locators_main.CREATE_AD_BUTTON)
        )
        button.click()


def create_ad(driver):
    title, description, price = generate_random_ad()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locators_ad.TITLE_INPUT)
    ).send_keys(title)

    description_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locators_ad.DESCRIPTION_INPUT)
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", description_input)
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators_ad.DESCRIPTION_INPUT)
    ).send_keys(description)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locators_ad.PRICE_INPUT)
    ).send_keys(str(price))

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locators_ad.CREATE_AD_BUTTON)
    ).click()


def length_of_ads(driver):
    cards = driver.find_elements(*locators_main.CARD)
    return len(cards)


class TestAd:

    def test_create_ad_logged_in(self, driver):
        login(driver, EXISTING_EMAIL, EXISTING_EMAIL_PASSWORD)
        open_ad_creation_form(driver)

        WebDriverWait(driver, 10).until(
            EC.url_contains(f"{Config.BASE_URL}/create-lisiting")
        )

        assert f"{Config.BASE_URL}/create-lisiting" in driver.current_url

        create_ad(driver)

        WebDriverWait(driver, 10).until(
            EC.url_contains(f"{Config.BASE_URL}")
        )

        assert f"{Config.BASE_URL}" in driver.current_url


    def test_create_ad_not_logged_in(self, driver):

        open_ad_creation_form(driver)
        assert driver.current_url == f"{Config.BASE_URL}/login", "Пользователь не был перенаправлен на страницу авторизации при попытке создать объявление без входа в систему"


