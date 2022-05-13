import pytest
from support.base_config import *
from support.login import *
from support.login_functions import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(baseUrl)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver


def test_verify_url(driver):
    try:
        assert driver.current_url == f"{baseUrl}/"
    except AssertionError:
        print('URL is not correct')
        driver.close()
        assert False
    driver.close()


def test_verify_elements(driver):
    try:
        login_logo = login_elements.get('login_logo')
        driver.find_element(By.CLASS_NAME, login_logo)
    except NoSuchElementException:    
        print(f'could not find element {login_logo}')
        driver.close()
        assert False
    try:
        mascot_img = login_elements.get('mascot_img')
        driver.find_element(By.CLASS_NAME, mascot_img)
    except NoSuchElementException:    
        print(f'could not find element {mascot_img}')
        driver.close()
        assert False
    try:
        login_button = login_elements.get('login_button')
        driver.find_element(By.CSS_SELECTOR, login_button)
    except NoSuchElementException:    
        print(f'could not find element {login_button}')
        driver.close()
        assert False
    try:
        pass_field = login_elements.get('pass_field')
        driver.find_element(By.CSS_SELECTOR, pass_field)
    except NoSuchElementException:    
        print(f'could not find element {pass_field}')
        driver.close()
        assert False
    try:
        user_field = login_elements.get('user_field')
        driver.find_element(By.CSS_SELECTOR, user_field)
        assert True
    except NoSuchElementException:
        print(f'could not find element {user_field}')
        driver.close()
        assert False
    driver.close()


def test_verify_username_and_password_required_for_login(driver):
    user_login(driver, None, None)
    try:
        assert driver.find_element(By.CLASS_NAME, login_elements.get('error_msg')) \
            .text == login_verbiage.get('error_msg').get('username')
    except AssertionError:
        print('error message is not correct')
        driver.close()
        assert False
    try:
        user_field = driver.find_element(
            By.CSS_SELECTOR, login_elements.get('user_field'))
        assert 'error' in user_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for username field')
        driver.close()
        assert False
    try:
        pass_field = driver.find_element(
            By.CSS_SELECTOR, login_elements.get('pass_field'))
        assert 'error' in pass_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for password field')
        driver.close()
        assert False
    try:
        user_cross = driver.execute_script(
            "return arguments[0].nextElementSibling", user_field)
        assert 'times-circle' in user_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find X button within username field')
        driver.close()
        assert False
    try:
        pass_cross = driver.execute_script(
            "return arguments[0].nextElementSibling", pass_field)
        assert 'times-circle' in pass_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find X button within password field')
        driver.close()
        assert False
    driver.close()


def test_verify_password_required_for_login(driver):
    user_field = driver.find_element(
            By.CSS_SELECTOR, login_elements.get('user_field'))
    user_login(driver, login_verbiage.get('usernames').get('standard'), None)
    try:
        assert driver.find_element(By.CLASS_NAME, login_elements.get('error_msg')) \
            .text == login_verbiage.get('error_msg').get('password')
    except AssertionError:
        print('error message is not correct')
        driver.close()
        assert False
    try:
        assert 'error' in user_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for username field')
        driver.close()
        assert False
    try:
        pass_field = driver.find_element(
            By.CSS_SELECTOR, login_elements.get('user_field'))
        assert 'error' in pass_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for password field')
        driver.close()
        assert False
    try:
        user_cross = driver.execute_script(
            "return arguments[0].nextElementSibling", user_field)
        assert 'times-circle' in user_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find X button within username field')
        driver.close()
        assert False
    try:
        pass_cross = driver.execute_script(
            "return arguments[0].nextElementSibling", pass_field)
        assert 'times-circle' in pass_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find X button within password field')
        driver.close()
        assert False
    driver.close()

def test_verify_username_required_for_login(driver):
    pass_field = driver.find_element(
            By.CSS_SELECTOR, login_elements.get('pass_field'))
    user_login(driver, None, login_verbiage.get('password'))
    try:
        assert driver.find_element(By.CLASS_NAME, login_elements.get('error_msg')) \
            .text == login_verbiage.get('error_msg').get('username')
    except AssertionError:
        print('error message is not correct')
        driver.close()
        assert False
    try:
        user_field = driver.find_element(
            By.CSS_SELECTOR, login_elements.get('user_field'))
        assert 'error' in user_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for username field')
        driver.close()
        assert False
    try:
        assert 'error' in pass_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for password field')
        driver.close()
        assert False
    try:
        user_cross = driver.execute_script(
            "return arguments[0].nextElementSibling", user_field)
        assert 'times-circle' in user_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find X button within username field')
        driver.close()
        assert False
    try:
        pass_cross = driver.execute_script(
            "return arguments[0].nextElementSibling", pass_field)
        assert 'times-circle' in pass_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find X button within password field')
        driver.close()
        assert False
    driver.close()

def test_verify_incorrect_username_and_password(driver):
    pass_field = driver.find_element(
            By.CSS_SELECTOR, login_elements.get('pass_field'))
    user_field = driver.find_element(
            By.CSS_SELECTOR, login_elements.get('user_field'))
    user_login(driver, login_verbiage.get('usernames').get('standard'), login_verbiage.get('usernames').get('standard'))
    try:
        assert driver.find_element(By.CLASS_NAME, login_elements.get('error_msg')) \
            .text == login_verbiage.get('error_msg').get('wrongpass')
    except AssertionError:
        print('error message is not correct')
        driver.close()
        assert False
    try:
        assert 'error' in user_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for username field')
        driver.close()
        assert False
    try:
        assert 'error' in pass_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for password field')
        driver.close()
        assert False
    try:
        user_cross = driver.execute_script(
            "return arguments[0].nextElementSibling", user_field)
        assert 'times-circle' in user_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find X button within username field')
        driver.close()
        assert False
    try:
        pass_cross = driver.execute_script(
            "return arguments[0].nextElementSibling", pass_field)
        assert 'times-circle' in pass_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find X button within password field')
        driver.close()
        assert False
    driver.close()

def test_verify_locked_user_login(driver):
    pass_field = driver.find_element(
            By.CSS_SELECTOR, login_elements.get('pass_field'))
    user_field = driver.find_element(
            By.CSS_SELECTOR, login_elements.get('user_field'))
    user_login(driver, login_verbiage.get('usernames').get('locked'), login_verbiage.get('password'))
    try:
        assert driver.find_element(By.CLASS_NAME, login_elements.get('error_msg')) \
            .text == login_verbiage.get('error_msg').get('locked')
    except AssertionError:
        print('error message is not correct')
        # driver.close()
        assert False
    try:
        assert 'error' in user_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for username field')
        driver.close()
        assert False
    try:
        assert 'error' in pass_field.get_attribute('class')
    except AssertionError:
        print('could not find classname `error` for password field')
        driver.close()
        assert False
    try:
        user_cross = driver.execute_script(
            "return arguments[0].nextElementSibling", user_field)
        assert 'times-circle' in user_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find X button within username field')
        driver.close()
        assert False
    try:
        pass_cross = driver.execute_script(
            "return arguments[0].nextElementSibling", pass_field)
        assert 'times-circle' in pass_cross.get_attribute('data-icon')
    except AssertionError:
        print('could not find X button within password field')
        driver.close()
        assert False
    driver.close()

def test_verify_problem_user_login(driver):
    user_login(driver, login_verbiage.get('usernames').get('problem'), login_verbiage.get('password'))
    WebDriverWait(driver, 10).until(EC.url_changes(baseUrl))
    try:
        assert driver.current_url == f"{baseUrl}/inventory.html"
    except AssertionError:
        print(driver.current_url)
        driver.close()
        assert False
    driver.close()

def test_verify_performance_glitch_user_login(driver):
    user_login(driver, login_verbiage.get('usernames').get('glitch'), login_verbiage.get('password'))
    WebDriverWait(driver, 10).until(EC.url_changes(baseUrl))
    try:
        assert driver.current_url == f"{baseUrl}/inventory.html"
    except AssertionError:
        print(driver.current_url)
        driver.close()
        assert False
    driver.close()

def test_verify_standard_user_login(driver):
    user_login(driver)
    WebDriverWait(driver, 10).until(EC.url_changes(baseUrl))
    try:
        assert driver.current_url == f"{baseUrl}/inventory.html"
    except AssertionError:
        print(driver.current_url)
        driver.close()
        assert False
    driver.close()
