from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 15)

    def wait_for_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def close_overlay(self):
        overlay_locator = ('css selector', '.onetrust-pc-dark-filter')
        overlay_present = False

        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(overlay_locator))
            overlay_present = True
        except TimeoutException:
            pass

        if overlay_present:
            close_button_locator = ('xpath', "//button[@id='onetrust-accept-btn-handler']")
            close_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(close_button_locator))
            close_button.click()
            WebDriverWait(self._driver, 10).until(EC.invisibility_of_element_located(overlay_locator))
