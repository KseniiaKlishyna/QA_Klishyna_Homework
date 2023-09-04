from Homework_17.base_page import BasePage
from Homework_17.core.home_page_locators import HomepPageLocators
from Homework_17.category_page import CategoryPage
import time
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomepPageLocators()


    def search_for_phrase(self, text):
        self.close_overlay()
        search_input = self.wait_for_element(self.locators.search_field_locator)
        search_input.click()
        search_input.send_keys(text)
        search_button = self.wait_for_element(self.locators.search_button_locator)
        search_button.click()

    def open_article(self):
        self.close_overlay()
        time.sleep(3)
        article_link = self.wait_for_element(self.locators.article_locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", article_link)
        ActionChains(self._driver).move_to_element(article_link).click().perform()

    def open_cats_section(self):
        self.close_overlay()
        cats_section_link = self.wait_for_element(self.locators.cats_section_locator)
        cats_section_link.click()
        return CategoryPage(self._driver)

    def open_about_us(self):
        self.close_overlay()
        about_us = self.wait_for_element(self.locators.about_us_locator)
        about_us.click()

    def return_to_main(self):
        self.close_overlay()
        main_page = self.wait_for_element(self.locators.main_page_locator)
        main_page.click()
