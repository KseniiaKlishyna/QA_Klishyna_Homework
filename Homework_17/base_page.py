from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Homework_17.core.base_locators import BaseLocators
from Homework_17.core.cookies_and_locators import Cookies
from Homework_17.core.cookies_and_locators import LocalStorage


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 15)
        self.locators = BaseLocators()
        self.cookies = Cookies(self._driver)
        self.local_storage = LocalStorage(self._driver)

    def wait_for_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def close_overlay(self):
        overlay_present = False

        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self.locators.overlay_locator))
            overlay_present = True
        except TimeoutException:
            pass

        if overlay_present:
            close_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.locators.close_button_locator))
            close_button.click()
            WebDriverWait(self._driver, 10).until(EC.invisibility_of_element_located(self.locators.overlay_locator))

    def return_element(self, locator):
        return self._driver.find_element(*locator)

