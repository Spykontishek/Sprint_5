import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants
from faker import Faker

faker = Faker()

class TestRegistration:
    # Позитивный тест регистрации:
    def test_registration_use_correct_values_success(self,driver):
        email = faker.email()
        driver.get(Constants.REG_URL)
        driver.find_element(*Locators.NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOG_URL))
        current_url = driver.current_url
        assert current_url == Constants.LOG_URL

    # Негативный тест регистрации с некорректным паролем:
    def test_registration_use_incorrect_password_error(self,driver):
        driver.get(Constants.REG_URL)
        driver.find_element(*Locators.NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys('12345')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.find_element(*Locators.PASSWORD_ERROR).text == "Некорректный пароль"

    # Негативный тест регистрации с пустым именем:
    def test_registration_use_empty_name_error(self,driver):
        driver.get(Constants.REG_URL)
        driver.find_element(*Locators.NAME).send_keys('')
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.REG_URL))
        current_url = driver.current_url
        assert current_url == Constants.REG_URL

class TestAuthorization:
    # Позитивный тест входа через кнопку "Войти в аккаунт"
    def test_login_from_main_page_use_correct_values_success(self,reg):
        reg.get(Constants.URL)
        reg.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        reg.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        reg.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        reg.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(reg, 3).until(EC.url_to_be(Constants.URL))
        current_url = reg.current_url
        assert current_url == Constants.URL

    # Позитивный тест входа через кнопку "Личный кабинет"
    def test_login_from_personal_account_button_use_correct_values_success(self,reg):
        reg.get(Constants.URL)
        reg.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        reg.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        reg.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        reg.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(reg, 3).until(EC.url_to_be(Constants.URL))
        current_url = reg.current_url
        assert current_url == Constants.URL

    # Позитивный тест входа через кнопку "Войти" в форме регистрации:
    def test_login_from_register_form_use_correct_values_success(self,reg):
        reg.get(Constants.REG_URL)
        reg.find_element(*Locators.LOGIN_BUTTON_FROM_REGISTER_OR_RESTORE_PASSWORD_FORM).click()
        reg.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        reg.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        reg.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(reg, 3).until(EC.url_to_be(Constants.URL))
        current_url = reg.current_url
        assert current_url == Constants.URL

    # Позитивный тест входа через кнопку "Войти" в форме восстановления пароля:
    def test_login_from_restore_password_form_use_correct_values_success(self,reg):
        reg.get(Constants.RES_PAS_URL)
        reg.find_element(*Locators.LOGIN_BUTTON_FROM_REGISTER_OR_RESTORE_PASSWORD_FORM).click()
        reg.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        reg.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        reg.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(reg, 3).until(EC.url_to_be(Constants.URL))
        current_url = reg.current_url
        assert current_url == Constants.URL

class TestPersonalArea:
    # Тест перехода в личный кабинет авторизованным пользователем:
    def test_go_to_personal_account_success(self,login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 3).until(EC.url_to_be(Constants.USER_URL))
        current_url = login.current_url
        assert current_url  == Constants.USER_URL

class TestButtonsFromHeader:
    # Тест нажатия на конструктор с личного кабинета:
    def test_go_to_constructor_from_personal_account_success(self,login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 3).until(EC.url_to_be(Constants.USER_URL))
        login.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(login, 3).until(EC.url_to_be(Constants.URL))
        current_url = login.current_url
        assert current_url  == Constants.URL

    # Тест нажатия на логотип c личного кабинета:
    def test_go_to_logo_from_personal_account_success(self,login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 3).until(EC.url_to_be(Constants.USER_URL))
        login.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(login, 3).until(EC.url_to_be(Constants.URL))
        current_url = login.current_url
        assert current_url  == Constants.URL

class TestLogout:
# Тест выхода из аккаунта:
    def test_logout_success(self,login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 3).until(EC.url_to_be(Constants.USER_URL))
        login.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(login, 3).until(EC.url_to_be(Constants.LOG_URL))
        current_url = login.current_url
        assert current_url  == Constants.LOG_URL


class TestConstructor:
    # Тест перехода к разделу "Начинки" в конструкторе:
    def test_go_to_fillings_in_constructor_success(self,driver):
        driver.get(Constants.URL)
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((Locators.PRESSED_FILLINGS_BUTTON)))
        fillings_button_class = driver.find_element(*Locators.FILLINGS_BUTTON).get_attribute('class')
        assert 'tab_tab_type_current' in fillings_button_class

    # Тест перехода к разделу "Соусы" в конструкторе:
    def test_go_to_sauces_in_constructor_success(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((Locators.PRESSED_SAUCES_BUTTON)))
        sauces_button_class = driver.find_element(*Locators.SAUCES_BUTTON).get_attribute('class')
        assert 'tab_tab_type_current' in sauces_button_class
    # Тест перехода к разделу "Соусы" в конструкторе:
    def test_go_to_buns_in_constructor_success(self, driver):
        driver.get(Constants.URL)
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((Locators.PRESSED_BUNS_BUTTON)))
        buns_button_class = driver.find_element(*Locators.BUNS_BUTTON).get_attribute('class')
        assert 'tab_tab_type_current' in buns_button_class








