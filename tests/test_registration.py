
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants


def test_successful_registration(driver, valid_name, valid_email, valid_password):
    driver.get(Constants.REGISTRATION_URL)
    input_name = driver.find_element(By.XPATH, Locators.REGISTRATION_INPUT_NAME)
    input_name.send_keys(valid_name)
    input_email = driver.find_element(By.XPATH, Locators.REGISTRATION_INPUT_EMAIL)
    input_email.send_keys(valid_email)
    input_password = driver.find_element(By.XPATH, Locators.REGISTRATION_INPUT_PASSWORD)
    input_password.send_keys(valid_password)
    registration_button = driver.find_element(By.XPATH, Locators.REGISTRATION_BUTTON)
    registration_button.click()
    WebDriverWait(driver, 5).until(EC.url_contains("/login"))

    assert driver.current_url == Constants.LOGIN_URL


def test_unsuccessful_registration(driver, valid_name, valid_email, invalid_password):
    driver.get(Constants.REGISTRATION_URL)
    input_name = driver.find_element(By.XPATH, Locators.REGISTRATION_INPUT_NAME)
    input_name.send_keys(valid_name)
    input_email = driver.find_element(By.XPATH, Locators.REGISTRATION_INPUT_EMAIL)
    input_email.send_keys(valid_email)
    input_password = driver.find_element(By.XPATH, Locators.REGISTRATION_INPUT_PASSWORD)
    input_password.send_keys(invalid_password)
    registration_button = driver.find_element(By.XPATH, Locators.REGISTRATION_BUTTON)
    registration_button.click()
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, Locators.REGISTRATION_INVALID_PASSWORD_MESSAGE))
    )

    assert error_message.text == "Некорректный пароль"
