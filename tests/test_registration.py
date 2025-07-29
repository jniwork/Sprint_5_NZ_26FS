from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators
from pages.urls import Urls
from data.test_data import TestData
from utils.generators import generate_name, generate_email, generate_password


class TestRegistration:

    def test_successful_registration(self, driver):
        valid_name = generate_name()
        valid_email = generate_email()
        valid_password = generate_password()

        driver.get(Urls.REGISTRATION_URL)
        input_name = driver.find_element(By.XPATH, Locators.REGISTRATION_INPUT_NAME)
        input_name.send_keys(valid_name)
        input_email = driver.find_element(By.XPATH, Locators.REGISTRATION_INPUT_EMAIL)
        input_email.send_keys(valid_email)
        input_password = driver.find_element(By.XPATH, Locators.REGISTRATION_INPUT_PASSWORD)
        input_password.send_keys(valid_password)
        registration_button = driver.find_element(By.XPATH, Locators.REGISTRATION_BUTTON)
        registration_button.click()
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))

        assert driver.current_url == Urls.LOGIN_URL

    def test_unsuccessful_registration(self, driver):
        valid_name = generate_name()
        valid_email = generate_email()
        invalid_password = generate_password(5)

        driver.get(Urls.REGISTRATION_URL)
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

        assert error_message.text == TestData.INVALID_PASSWORD_ERROR_MESSAGE
