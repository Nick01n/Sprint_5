from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from auth_helper import AuthHelper
from data import TestLinks
from locators import TestLocators


# Класс для проверки входа
class TestLogin:
    def test_login_from_main_page(self, driver, registered_user):
        test_mail, test_pass = registered_user
        driver.get(TestLinks.main_page_link)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON_LOCATOR)).click()
        AuthHelper.login(driver, test_mail, test_pass)
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, ("Ошибка перехода на главную страницу после логина.")


    def test_login_from_personal_account_button(self, driver, registered_user):
        test_mail, test_pass = registered_user
        driver.get(TestLinks.main_page_link)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()
        AuthHelper.login(driver, test_mail, test_pass)
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, ("Ошибка перехода на главную страницу после логина.")


    def test_login_from_registration_link(self, driver, registered_user):
        test_mail, test_pass = registered_user
        driver.get(TestLinks.registration_page_link)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)).click()
        AuthHelper.login(driver, test_mail, test_pass)
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, ("Ошибка перехода на главную страницу после логина.")


    def test_login_from_forgot_password_link(self, driver, registered_user):
        test_mail, test_pass = registered_user
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)).click()
        AuthHelper.login(driver, test_mail, test_pass)
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, ("Ошибка перехода на главную страницу после логина.")