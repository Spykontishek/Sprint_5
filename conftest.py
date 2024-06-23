import pytest
from selenium import webdriver
from constants import Constants
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()

# Регистрация аккаунта
@pytest.fixture
def reg(driver):
    driver.get(Constants.REG_URL)
    driver.find_element(*Locators.NAME).send_keys(Constants.NAME)
    driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    return driver

# Авторизация
@pytest.fixture
def login(driver):
    driver.get(Constants.LOG_URL)
    driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver

