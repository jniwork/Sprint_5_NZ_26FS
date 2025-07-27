from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators
from pages.urls import Urls
from data.test_data import TestData


class TestTransitions:

    def login_user(self, driver):
        input_email = driver.find_element(By.XPATH, Locators.LOGIN_INPUT_EMAIL)
        input_email.send_keys(TestData.LOGIN_EMAIL)

        input_password = driver.find_element(By.XPATH, Locators.LOGIN_INPUT_PASSWORD)
        input_password.send_keys(TestData.LOGIN_PASSWORD)

        login_button = driver.find_element(By.XPATH, Locators.LOGIN_PAGE_LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, 5).until(EC.url_changes(Urls.LOGIN_URL))

    def test_transition_to_account(self, driver):
        driver.get(Urls.LOGIN_URL)
        self.login_user(driver)
        account_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_ACCOUNT_BUTTON))
        )
        account_button.click()

        assert Urls.ACCOUNT_URL == driver.current_url

    def test_transition_to_constructor(self, driver):
        driver.get(Urls.LOGIN_URL)
        self.login_user(driver)
        constructor_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_CONSTRUCTOR_BUTTON))
        )
        constructor_button.click()
        header_text = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_HEADER))
        ).text

        assert header_text == TestData.BURGER_HEADER_TEXT

    def test_transition_to_constructor_from_logo(self, driver):
        driver.get(Urls.LOGIN_URL)
        self.login_user(driver)
        logo_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_LOGO))
        )
        logo_button.click()
        header_text = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_HEADER))
        ).text

        assert header_text == TestData.BURGER_HEADER_TEXT
