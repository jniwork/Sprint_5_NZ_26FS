import pytest
from selenium import webdriver
from utils import generate_name, generate_email, generate_password


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def valid_name():
    return generate_name()


@pytest.fixture(scope="function")
def valid_email():
    return generate_email()


@pytest.fixture(scope="function")
def valid_password():
    return generate_password()

@pytest.fixture(scope="function")
def invalid_password():
    return generate_password(5)