from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import MainPageLocators as locators_main
from src.locators import AuthPageLocators as locators_auth
from src.data import EXISTING_EMAIL, EXISTING_EMAIL_PASSWORD

def open_login_form(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locators_main.MAIN_LOGIN_BUTTON)
    ).click()


def login(driver, email, password):
    open_login_form(driver)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locators_auth.EMAIL_INPUT)
    ).send_keys(email)

    driver.find_element(*locators_auth.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators_auth.LOGIN_BUTTON).click()


def logout(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators_main.USER_AVATAR))
    logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators_main.LOGOUT_BUTTON))
    logout_button.click()


class TestLogin:
    def test_login_success(self, driver):
        login(driver, EXISTING_EMAIL, EXISTING_EMAIL_PASSWORD)

        user_avatar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators_main.USER_AVATAR))
        assert user_avatar.is_displayed() is True, "Аватар пользователя не отображается после успешной регистрации"
         
        user_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators_main.USER_NAME))
        assert user_name.is_displayed() is True, "Имя пользователя не отображается после успешной регистрации"
    
    def test_logout(self, driver):
        login(driver, EXISTING_EMAIL, EXISTING_EMAIL_PASSWORD)
        logout(driver)
        assert WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators_main.MAIN_LOGIN_BUTTON)).is_displayed() is True, "Кнопка входа не отображается после выхода из аккаунта"

