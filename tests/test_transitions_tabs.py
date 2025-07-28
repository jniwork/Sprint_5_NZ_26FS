import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators
from pages.urls import Urls
from data.test_data import TestData
from helpers.auth_helper import login_user


class TestTransitionsTabs:

    @pytest.mark.parametrize("tab_locator,expected_text", [
        (Locators.MAIN_PAGE_SAUCES, TestData.TAB_NAMES['sauces']),
        (Locators.MAIN_PAGE_TOPPINGS, TestData.TAB_NAMES['toppings']),
        (Locators.MAIN_PAGE_BREADS, TestData.TAB_NAMES['breads'])
    ])
    def test_transition_to_tabs(self, driver, tab_locator, expected_text):
        driver.get(Urls.LOGIN_URL)
        login_user(driver)
        if expected_text == TestData.TAB_NAMES['breads']:
            sauce_tab = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locators.MAIN_PAGE_SAUCES))
            )
            sauce_tab.click()
            WebDriverWait(driver, 5).until(
                EC.text_to_be_present_in_element((By.XPATH, Locators.MAIN_PAGE_ACTIVE_TAB), TestData.TAB_NAMES['sauces'])
            )
        tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, tab_locator))
        )
        tab.click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, Locators.MAIN_PAGE_ACTIVE_TAB), expected_text)
        )

        active_tab = driver.find_element(By.XPATH, Locators.MAIN_PAGE_ACTIVE_TAB)
        assert active_tab.text == expected_text
