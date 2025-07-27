from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators
from pages.urls import Urls
from data.test_data import TestData


class TestLogout:

    def login_user(self, driver):
        input_email = driver.find_element(By.XPATH, Locators.LOGIN_INPUT_EMAIL)
        input_email.send_keys(TestData.LOGIN_EMAIL)

        input_password = driver.find_element(By.XPATH, Locators.LOGIN_INPUT_PASSWORD)
        input_password.send_keys(TestData.LOGIN_PASSWORD)

        login_button = driver.find_element(By.XPATH, Locators.LOGIN_PAGE_LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, 5).until(EC.url_changes(Urls.LOGIN_URL))

    def test_logout_from_account_page(self, driver):
        driver.get(Urls.LOGIN_URL)
        self.login_user(driver)
        account_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_ACCOUNT_BUTTON))
        )
        account_button.click()
        logout_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.ACCOUNT_PAGE_LOGOUT_BUTTON))
        )
        logout_button.click()
        WebDriverWait(driver, 2).until(EC.url_changes(Urls.ACCOUNT_PROFILE_URL))

        assert Urls.LOGIN_URL == driver.current_url
