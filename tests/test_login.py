from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators
from pages.urls import Urls
from data.test_data import TestData


class TestLogin:

    def login_user(self, driver):
        input_email = driver.find_element(By.XPATH, Locators.LOGIN_INPUT_EMAIL)
        input_email.send_keys(TestData.LOGIN_EMAIL)

        input_password = driver.find_element(By.XPATH, Locators.LOGIN_INPUT_PASSWORD)
        input_password.send_keys(TestData.LOGIN_PASSWORD)

        login_button = driver.find_element(By.XPATH, Locators.LOGIN_PAGE_LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, 5).until(EC.url_changes(Urls.LOGIN_URL))

    def test_login_from_main_page(self, driver):
        driver.get(Urls.BASE_URL)
        main_page_login_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.LOGIN_MAIN_PAGE_BUTTON))
        )
        main_page_login_button.click()
        self.login_user(driver)

        assert driver.current_url == Urls.BASE_URL

    def test_login_from_account_page(self, driver):
        driver.get(Urls.BASE_URL)
        account_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_ACCOUNT_BUTTON))
        )
        account_button.click()
        self.login_user(driver)

        assert driver.current_url == Urls.BASE_URL

    def test_login_from_registration_page(self, driver):
        driver.get(Urls.REGISTRATION_URL)
        login_registration_page_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.REGISTRATION_PAGE_LOGIN_BUTTON))
        )
        login_registration_page_button.click()
        self.login_user(driver)

        assert driver.current_url == Urls.BASE_URL

    def test_login_from_forgot_password_page(self, driver):
        driver.get(Urls.FORGOT_PASSWORD_URL)
        login_registration_page_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.FORGOT_PASSWORD_PAGE_LOGIN_BUTTON))
        )
        login_registration_page_button.click()
        self.login_user(driver)

        assert driver.current_url == Urls.BASE_URL
