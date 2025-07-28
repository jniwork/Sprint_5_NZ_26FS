from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators
from pages.urls import Urls
from data.test_data import TestData
from helpers.auth_helper import login_user


class TestTransitions:

    def test_transition_to_account(self, driver):
        driver.get(Urls.LOGIN_URL)
        login_user(driver)
        account_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_ACCOUNT_BUTTON))
        )
        account_button.click()

        assert Urls.ACCOUNT_URL == driver.current_url

    def test_transition_to_constructor(self, driver):
        driver.get(Urls.LOGIN_URL)
        login_user(driver)
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
        login_user(driver)
        logo_button = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_LOGO))
        )
        logo_button.click()
        header_text = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_HEADER))
        ).text

        assert header_text == TestData.BURGER_HEADER_TEXT
