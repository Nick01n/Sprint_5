from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestLinks
from locators import TestLocators


# Класс для проверки навигации из Личного кабинета в Конструктор
class TestNavigationToConstructor:
    def test_navigation_from_account_to_constructor(self, driver, authorized_user):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()
        WebDriverWait(driver, 10).until(EC.url_contains(TestLinks.personal_account_page_link))
        assert driver.current_url == TestLinks.personal_account_page_link, ("Ошибка перехода в личный кабинет.")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUTTON_LOCATOR)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, ("Ошибка перехода на страницу конструктора.")

   
    def test_navigation_from_account_to_constructor_via_logo(self, driver, authorized_user):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()
        WebDriverWait(driver, 10).until(EC.url_contains(TestLinks.personal_account_page_link))
        assert driver.current_url == TestLinks.personal_account_page_link, ("Ошибка перехода в личный кабинет.")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGO_LOCATOR)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, ("Ошибка перехода на главную страницу по клику на логотип.")