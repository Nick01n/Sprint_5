from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestLinks
from locators import TestLocators


# Класс для проверки перехода в личный кабинет
class TestNavigationToPersonalAccount:
    def test_navigation_to_personal_account(self, driver, authorized_user):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()
        WebDriverWait(driver, 10).until(EC.url_contains(TestLinks.personal_account_page_link))
        assert driver.current_url == TestLinks.personal_account_page_link, ("Ошибка перехода в личный кабинет.")