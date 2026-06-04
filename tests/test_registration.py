
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.locators import RegistrationPageLocators as locators_reg
from src.locators import AuthPageLocators as locators_auth
from src.locators import MainPageLocators as locators_main
from src.config import Config
from src.helpers import generate_random_email, generate_random_password
from src.data import INVALID_EMAIL, EXISTING_EMAIL 
import pytest

def open_registration_form(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locators_main.MAIN_LOGIN_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locators_reg.NO_ACCOUNT_BUTTON)
    ).click()


def register(driver, email, password):
    open_registration_form(driver)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locators_reg.EMAIL_INPUT)
    ).send_keys(email)

    driver.find_element(*locators_reg.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators_reg.PASSWORD_REPEAT_INPUT).send_keys(password)
    driver.find_element(*locators_reg.CREATE_ACCOUNT_BUTTON).click()


class TestRegistration:

    def test_registration_success(self, driver):

        email_data, password_data = generate_random_email(), generate_random_password()        
        register(driver, email_data, password_data)

        user_avatar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators_main.USER_AVATAR))
        assert user_avatar.is_displayed() is True, "Аватар пользователя не отображается после успешной регистрации"
         
        user_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators_main.USER_NAME))
        assert user_name.is_displayed() is True, "Имя пользователя не отображается после успешной регистрации"



    @pytest.mark.parametrize("email", [INVALID_EMAIL, EXISTING_EMAIL])
    def test_registration_error(self, driver, email):

        email_data = email
        password_data = generate_random_password()

        register(driver, email_data, password_data)

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators_reg.ERROR_TEXT))
        assert error_message.is_displayed() is True, "Сообщение об ошибке не отображается при вводе некорректного email"
  
        