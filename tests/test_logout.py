
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from utils import login_user

def test_logout_from_account_page(driver):
    driver.get(Constants.LOGIN_URL)
    login_user(driver)
    account_button = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_ACCOUNT_BUTTON))
    )
    account_button.click()
    logout_button = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.ACCOUNT_PAGE_LOGOUT_BUTTON))
    )
    logout_button.click()
    WebDriverWait(driver, 2).until(EC.url_changes(Constants.ACCOUNT_PROFILE_URL))

    assert Constants.LOGIN_URL == driver.current_url