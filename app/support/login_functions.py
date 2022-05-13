from support.login import login_elements, login_verbiage
from selenium.webdriver.common.by import By

def user_login(driver, username = login_verbiage.get('usernames').get('standard'),\
    password = login_verbiage.get('password')):
    if username is not None: 
        driver.find_element(By.CSS_SELECTOR, login_elements.get('user_field')) \
            .send_keys(username)
    if password is not None:
        driver.find_element(By.CSS_SELECTOR, login_elements.get('pass_field')) \
            .send_keys(password)
    driver.find_element(By.CSS_SELECTOR, login_elements.get('login_button')) \
        .click()