from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators
from pages.urls import Urls
from helpers.auth_helper import login_user


class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get(Urls.BASE_URL)
        main_page_login_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.LOGIN_MAIN_PAGE_BUTTON))
        )
        main_page_login_button.click()
        login_user(driver)

        assert driver.current_url == Urls.BASE_URL

    def test_login_from_account_page(self, driver):
        driver.get(Urls.BASE_URL)
        account_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_ACCOUNT_BUTTON))
        )
        account_button.click()
        login_user(driver)

        assert driver.current_url == Urls.BASE_URL

    def test_login_from_registration_page(self, driver):
        driver.get(Urls.REGISTRATION_URL)
        login_registration_page_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.REGISTRATION_PAGE_LOGIN_BUTTON))
        )
        login_registration_page_button.click()
        login_user(driver)

        assert driver.current_url == Urls.BASE_URL

    def test_login_from_forgot_password_page(self, driver):
        driver.get(Urls.FORGOT_PASSWORD_URL)
        login_registration_page_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.FORGOT_PASSWORD_PAGE_LOGIN_BUTTON))
        )
        login_registration_page_button.click()
        login_user(driver)

        assert driver.current_url == Urls.BASE_URL
