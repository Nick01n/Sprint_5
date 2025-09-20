import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver

from auth_helper import AuthHelper
from data import TestLinks
from generator import Generator


# фикстура для драйверов
@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()  
    chrome_options.add_argument('--window-size=1955,1050')  
    driver = webdriver.Chrome(options=chrome_options) 
    yield driver  
    driver.quit()  


@pytest.fixture
def test_email():
    return Generator.generate_email()


@pytest.fixture
def test_password():
    return Generator.generate_password()


@pytest.fixture
def registered_user(driver, test_email, test_password):
    driver.get(TestLinks.registration_page_link)
    AuthHelper.registration(driver, test_email, test_password)
    AuthHelper.confirm_registration_success(driver)
    return test_email, test_password


@pytest.fixture
def authorized_user(driver, registered_user):
    test_mail, test_pass = registered_user
    AuthHelper.login(driver, test_mail, test_pass)
    AuthHelper.confirm_login_success(driver)