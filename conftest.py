from selenium import webdriver
from src.config import Config
import pytest
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()
    