from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators
from pages.urls import Urls
from data.test_data import TestData


def login_user(driver):
    input_email = driver.find_element(By.XPATH, Locators.LOGIN_INPUT_EMAIL)
    input_email.send_keys(TestData.LOGIN_EMAIL)

    input_password = driver.find_element(By.XPATH, Locators.LOGIN_INPUT_PASSWORD)
    input_password.send_keys(TestData.LOGIN_PASSWORD)

    login_button = driver.find_element(By.XPATH, Locators.LOGIN_PAGE_LOGIN_BUTTON)
    login_button.click()

    # Ждем загрузки главной страницы после логина
    WebDriverWait(driver, 10).until(EC.url_changes(Urls.LOGIN_URL))
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_HEADER))
    )