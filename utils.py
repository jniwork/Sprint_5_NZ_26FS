from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants

fake = Faker()
fake_ru = Faker('ru_RU')


def generate_name():
    return fake_ru.first_name()


def generate_email():
    return f'nikolay_zhuravlev_26fs{fake.numerify("###")}@{fake.domain_name()}'


def generate_password(length=6):
    return fake.password(length=length)


def login_user(driver):
    input_email = driver.find_element(By.XPATH, Locators.LOGIN_INPUT_EMAIL)
    input_email.send_keys(Constants.LOGIN_EMAIL)

    input_password = driver.find_element(By.XPATH, Locators.LOGIN_INPUT_PASSWORD)
    input_password.send_keys(Constants.LOGIN_PASSWORD)

    login_button = driver.find_element(By.XPATH, Locators.LOGIN_PAGE_LOGIN_BUTTON)
    login_button.click()

    WebDriverWait(driver, 5).until(EC.url_changes(Constants.LOGIN_URL))
