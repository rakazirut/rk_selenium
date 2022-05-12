import pytest
import sys
from support.base_config import *
from support.login import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture(autouse=True)
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://www.saucedemo.com/')
    chrome_driver.maximize_window()
    yield chrome_driver


def test_verify_url(driver):
    assert driver.current_url == baseUrl
    driver.close()


def test_verify_elements(driver):
    try:
        driver.find_element(By.CLASS_NAME, login_elements.get('login_logo'))
        driver.find_element(By.CLASS_NAME, login_elements.get('mascot_img'))
        driver.find_element(
            By.CSS_SELECTOR, login_elements.get('login_button'))
        driver.find_element(By.CSS_SELECTOR, login_elements.get('pass_field'))
        driver.find_element(By.CSS_SELECTOR, login_elements.get('user_field'))
        assert True
    except NoSuchElementException:
        print('could not find elements')
        driver.close()
        assert False
    driver.close()


def test_verify_username_and_password_required_for_login(driver):
    driver.find_element(By.CSS_SELECTOR, login_elements.get('login_button')) \
        .click()
    driver.find_element(By.CLASS_NAME, login_elements.get('error_msg')) \
        .text == login_verbiage.get('error_msg').get('username')
    try:
        username_field = driver.find_element(By.CSS_SELECTOR, login_elements.get('user_field'))
        assert 'error' in username_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for username field')
        driver.close()
        assert False
    try:
        password_field = driver.find_element(By.CSS_SELECTOR, login_elements.get('user_field'))
        assert 'error' in password_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for password field')
        driver.close()
        assert False
    try:
        user_cross = driver.execute_script("return arguments[0].nextElementSibling", username_field)
        assert 'times-circle' in user_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find error X for username field')
        driver.close()
        assert False
    try:
        pass_cross = driver.execute_script("return arguments[0].nextElementSibling", password_field)
        assert 'times-circle' in pass_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find error X for password field')
        driver.close()
        assert False


    driver.close()
