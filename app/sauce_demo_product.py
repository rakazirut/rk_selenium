import pytest
from support.base_config import *
from support.product import *
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
    user_login(chrome_driver)
    yield chrome_driver

def test_verify_top_nav_elements(driver):
    try:
        app_logo = product_elements.get('top_nav') \
            .get('app_logo')
        driver.find_element(By.CLASS_NAME, app_logo)
    except NoSuchElementException:    
        print(f'could not find element {app_logo}')
        driver.close()
        assert False
    try:
        nav_mascot = product_elements.get('top_nav') \
            .get('nav_mascot')
        driver.find_element(By.CLASS_NAME, nav_mascot)
    except NoSuchElementException:    
        print(f'could not find element {nav_mascot}')
        driver.close()
        assert False
    try:
        hamburger_menu = product_elements.get('top_nav') \
            .get('hamburger_menu').get('main_menu_button')
        driver.find_element(By.CLASS_NAME, hamburger_menu)
    except NoSuchElementException:    
        print(f'could not find element {hamburger_menu}')
        driver.close()
        assert False
    try:
        shopping_cart = product_elements.get('top_nav') \
            .get('shopping_cart').get('icon')
        driver.find_element(By.CLASS_NAME, shopping_cart)
    except NoSuchElementException:    
        print(f'could not find element {shopping_cart}')
        driver.close()
        assert False
    try:
        sort_dropdown = product_elements.get('top_nav') \
            .get('sort_dropdown').get('container')
        driver.find_element(By.CLASS_NAME, sort_dropdown)
        assert True
    except NoSuchElementException:
        print(f'could not find element {sort_dropdown}')
        driver.close()
        assert False
    driver.close()