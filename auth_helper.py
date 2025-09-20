from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestLinks
from generator import Generator
from locators import TestLocators

# Класс для авторизации и регистрации пользователей через Selenium.
class AuthHelper:
    
    @staticmethod
    def login(driver, email, password):
        
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.EMAIL_LOCATOR))
        driver.find_element(*TestLocators.EMAIL_LOCATOR).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_LOCATOR).send_keys(password)
        
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()

    
    @staticmethod
    def registration(driver, email, password, name="Тест"):
        def fill_registration_form(driver, email, password, name):
            
            WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.NAME_LOCATOR))
            driver.find_element(*TestLocators.NAME_LOCATOR).send_keys(name)
            driver.find_element(*TestLocators.EMAIL_LOCATOR).send_keys(email)
            driver.find_element(*TestLocators.PASSWORD_LOCATOR).send_keys(password)
            driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()

        fill_registration_form(driver, email, password, name)

        
        while AuthHelper.is_user_already_exists(driver):
            email = Generator.generate_email() 
            driver.refresh()  
            fill_registration_form(driver, email, password, name)

    
    @staticmethod
    def confirm_login_success(driver):
        
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))

    
    @staticmethod
    def confirm_registration_success(driver):
        
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.login_page_link))

    
    @staticmethod
    def is_user_already_exists(driver):
        
        try:
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.ERROR_MESSAGE_LOCATOR))
            return True  
        except TimeoutException:
            return False  