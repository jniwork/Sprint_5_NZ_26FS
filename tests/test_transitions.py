
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from utils import login_user


def test_transition_to_account(driver):
    driver.get(Constants.LOGIN_URL)
    login_user(driver)
    account_button = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_ACCOUNT_BUTTON))
    )
    account_button.click()

    assert Constants.ACCOUNT_URL == driver.current_url


def test_transition_to_constructor(driver):
    driver.get(Constants.LOGIN_URL)
    login_user(driver)
    constructor_button = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_CONSTRUCTOR_BUTTON))
    )
    constructor_button.click()
    header_text = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_HEADER))
    ).text

    assert header_text == "Соберите бургер"

def test_transition_to_constructor_from_logo(driver):
    driver.get(Constants.LOGIN_URL)
    login_user(driver)
    logo_button = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_LOGO))
    )
    logo_button.click()
    header_text = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_HEADER))
    ).text

    assert header_text == "Соберите бургер"