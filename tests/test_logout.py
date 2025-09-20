from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestLinks
from locators import TestLocators


# Класс для проверки выхода
class TestLogout:
    def test_logout_from_personal_account(self, driver, authorized_user):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON_LOCATOR)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.login_page_link))
        assert driver.current_url == TestLinks.login_page_link, ("Ошибка выхода из личного кабинета и перехода на страницу логина.")
