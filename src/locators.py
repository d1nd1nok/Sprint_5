from selenium.webdriver.common.by import By

class RegistrationPageLocators:

    NO_ACCOUNT_BUTTON = By.XPATH, ".//button[contains(text(),'Нет аккаунта')]"
    EMAIL_INPUT = By.XPATH, "//h1[contains(text(),'Зарегистрироваться')]/ancestor::form//input[@name='email']"
    PASSWORD_INPUT = By.NAME, "password"
    PASSWORD_REPEAT_INPUT = By.NAME, "submitPassword"
    CREATE_ACCOUNT_BUTTON = By.XPATH, "//button[contains(text(),'Создать аккаунт')]"
    ERROR_TEXT = By.XPATH, "//span[contains(text(), 'Ошибка')]"



class AuthPageLocators:

    EMAIL_INPUT = By.NAME, "email"
    PASSWORD_INPUT = By.NAME, "password"
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(),'Войти')]"
    


class MainPageLocators:

    MAIN_LOGIN_BUTTON = By.XPATH, "//div[contains(@class, 'header_flexRow')]//button[contains(text(), 'Вход')]"
    CREATE_AD_BUTTON = By.XPATH, "//div[contains(@class, 'header_flexRow')]//button[contains(text(), 'Разместить')]"
    USER_AVATAR = By.CLASS_NAME, "svgSmall"
    USER_NAME = By.XPATH, ".//h3[contains(text(), 'User.')]"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(text(), 'Выйти')]"
    FOOTER = By.XPATH, ".//div[contains(@class, 'App_linkBlock')]"
    CARD = By.XPATH, "//div[contains(@class, 'card')]"



class AdPageLocators:

    TITLE_INPUT = By.NAME, "name"
    DESCRIPTION_INPUT = By.CSS_SELECTOR, "textarea[name='description']"
    PRICE_INPUT = By.NAME, "price"
    CREATE_AD_BUTTON = By.XPATH, "//button[contains(text(), 'Опубликовать')]"
