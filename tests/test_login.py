
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from utils import login_user


def test_login_from_main_page(driver):
    driver.get(Constants.BASE_URL)
    main_page_login_button = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.LOGIN_MAIN_PAGE_BUTTON))
    )
    main_page_login_button.click()
    login_user(driver)

    assert driver.current_url == Constants.BASE_URL


def test_login_from_account_page(driver):
    driver.get(Constants.BASE_URL)
    account_button = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.ACCOUNT_PAGE_LOGIN_BUTTON))
    )
    account_button.click()
    login_user(driver)

    assert driver.current_url == Constants.BASE_URL


def test_login_from_registration_page(driver):
    driver.get(Constants.REGISTRATION_URL)
    login_registration_page_button = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.REGISTRATION_PAGE_LOGIN_BUTTON))
    )
    login_registration_page_button.click()
    login_user(driver)

    assert driver.current_url == Constants.BASE_URL


def test_login_from_forgot_password_page(driver):
    driver.get(Constants.FORGOT_PASSWORD_URL)
    login_registration_page_button = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.FORGOT_PASSWORD_PAGE_LOGIN_BUTTON))
    )
    login_registration_page_button.click()
    login_user(driver)

    assert driver.current_url == Constants.BASE_URL
