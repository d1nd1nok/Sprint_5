from selenium import webdriver
from src.config import Config
import pytest
@pytest.fixture(scope="function")
def driver():
    try:
        driver = webdriver.Chrome()
        driver.get(Config.BASE_URL)
        yield driver 
           
    finally:
        driver.quit()