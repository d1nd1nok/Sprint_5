from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import MainPageLocators as locators_main
from src.locators import AuthPageLocators as locators_auth
from src.data import EXISTING_EMAIL, EXISTING_EMAIL_PASSWORD

class TestLogin:
    def test_login_success(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locators_main.MAIN_LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locators_auth.EMAIL_INPUT)
        ).send_keys(EXISTING_EMAIL)

        driver.find_element(*locators_auth.PASSWORD_INPUT).send_keys(EXISTING_EMAIL_PASSWORD)
        driver.find_element(*locators_auth.LOGIN_BUTTON).click()

        user_avatar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators_main.USER_AVATAR))
        assert user_avatar.is_displayed() is True, "Аватар пользователя не отображается после успешной регистрации"
         
        user_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators_main.USER_NAME))
        assert user_name.is_displayed() is True, "Имя пользователя не отображается после успешной регистрации"
    
    def test_logout(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locators_main.MAIN_LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locators_auth.EMAIL_INPUT)
        ).send_keys(EXISTING_EMAIL)

        driver.find_element(*locators_auth.PASSWORD_INPUT).send_keys(EXISTING_EMAIL_PASSWORD)
        driver.find_element(*locators_auth.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators_main.USER_AVATAR))
        logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators_main.LOGOUT_BUTTON))
        logout_button.click()
        assert WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators_main.MAIN_LOGIN_BUTTON)).is_displayed() is True, "Кнопка входа не отображается после выхода из аккаунта"

