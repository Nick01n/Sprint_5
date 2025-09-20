from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestLinks
from locators import TestLocators


# Класс для проверки переходов к разделам конструктора
class TestNavigationInConstructor:
    def test_navigation_to_buns(self, driver):
        driver.get(TestLinks.main_page_link)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_SAUCE_LOCATOR)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_BUN_LOCATOR)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.ACTIVE_TAB_BUN_LOCATOR))
        buns_tab = driver.find_element(*TestLocators.ACTIVE_TAB_BUN_LOCATOR)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = buns_tab.get_attribute('class')
        assert expected_class in actual_class, "Вкладка 'Булки' не активна."

    def test_navigation_to_sauces(self, driver):
        driver.get(TestLinks.main_page_link)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_SAUCE_LOCATOR)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.ACTIVE_TAB_SAUCE_LOCATOR))
        sauces_tab = driver.find_element(*TestLocators.ACTIVE_TAB_SAUCE_LOCATOR)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = sauces_tab.get_attribute('class')
        assert expected_class in actual_class, "Вкладка 'Соусы' не активна."

    def test_navigation_to_fillings(self, driver):
        driver.get(TestLinks.main_page_link)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_FILLING_LOCATOR)).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(TestLocators.ACTIVE_TAB_FILLING_LOCATOR))
        fillings_tab = driver.find_element(*TestLocators.ACTIVE_TAB_FILLING_LOCATOR)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = fillings_tab.get_attribute('class')
        assert expected_class in actual_class, "Вкладка 'Начинки' не активна."