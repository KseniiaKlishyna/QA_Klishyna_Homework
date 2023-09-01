from Homework_17.base_page import BasePage
import time
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def search_for_phrase(self, text):
        self.close_overlay()
        search_field_locator = ('xpath', "//input[@id='header-search']")
        search_input = self.wait_for_element(search_field_locator)
        search_input.click()
        search_input.send_keys(text)
        search_button_locator = ('xpath', "//button[contains(text(),'Search')]")
        search_button = self.wait_for_element(search_button_locator)
        search_button.click()

    def open_article(self):
        self.close_overlay()
        time.sleep(3)
        article_locator = ('xpath', "//body/main/div[2]/a[2]/div[1]/div[1]/span[1]/span[1]")
        article_link = self.wait_for_element(article_locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", article_link)
        ActionChains(self._driver).move_to_element(article_link).click().perform()

    def open_cats_section(self):
        self.close_overlay()
        cats_section_locator = ('xpath', "//nav/ul/li[2]/a[1]")
        cats_section_link = self.wait_for_element(cats_section_locator)
        cats_section_link.click()

    def open_about_us(self):
        self.close_overlay()
        about_us_locator = ('xpath', "//span[contains(text(),'About Us')]")
        about_us = self.wait_for_element(about_us_locator)
        about_us.click()

    def return_to_main(self):
        self.close_overlay()
        main_page_locator = ('xpath', "//header/a[@id='header__logo_1-0']/*[1]")
        main_page = self.wait_for_element(main_page_locator)
        main_page.click()
