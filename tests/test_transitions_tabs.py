
from selenium.webdriver.common.by import By
from locators import Locators
from constants import Constants
from utils import login_user


def test_transition_to_tab_sauces(driver):
    driver.get(Constants.LOGIN_URL)
    login_user(driver)
    bread_tab = driver.find_element(By.XPATH, Locators.MAIN_PAGE_SAUCES)
    bread_tab.click()
    active_tab = driver.find_element(By.XPATH, Locators.MAIN_PAGE_ACTIVE_TAB)

    assert active_tab.text == "Соусы"


def test_transition_to_tab_toppings(driver):
    driver.get(Constants.LOGIN_URL)
    login_user(driver)
    bread_tab = driver.find_element(By.XPATH, Locators.MAIN_PAGE_TOPPINGS)
    bread_tab.click()
    active_tab = driver.find_element(By.XPATH, Locators.MAIN_PAGE_ACTIVE_TAB)

    assert active_tab.text == "Начинки"


def test_transition_to_tab_breads(driver):
    driver.get(Constants.LOGIN_URL)
    login_user(driver)
    sauce_tab = driver.find_element(By.XPATH, Locators.MAIN_PAGE_SAUCES)
    sauce_tab.click()
    bread_tab = driver.find_element(By.XPATH, Locators.MAIN_PAGE_BREADS)
    bread_tab.click()
    active_tab = driver.find_element(By.XPATH, Locators.MAIN_PAGE_ACTIVE_TAB)

    assert active_tab.text == "Булки"
