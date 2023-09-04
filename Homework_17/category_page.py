from Homework_17.base_page import BasePage
from Homework_17.article_page import ArticlePage
from Homework_17.core.categories_locators import CategoriesLocators
import time
from selenium.webdriver.common.action_chains import ActionChains


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoriesLocators()

    def open_category_article(self):
        self.close_overlay()
        time.sleep(3)
        article_link = self.wait_for_element(self.locators.category_article_locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", article_link)
        time.sleep(3)
        ActionChains(self._driver).move_to_element(article_link).double_click().perform()
        return ArticlePage(self._driver)