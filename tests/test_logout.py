from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators
from pages.urls import Urls
from helpers.auth_helper import login_user


class TestLogout:

    def test_logout_from_account_page(self, driver):
        driver.get(Urls.LOGIN_URL)
        login_user(driver)
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
