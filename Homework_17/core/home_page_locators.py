from Homework_17.core.base_locators import BaseLocators

class HomepPageLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.search_field_locator = ('xpath', "//input[@id='header-search']")
        self.search_button_locator = ('xpath', "//button[contains(text(),'Search')]")
        self.article_locator = ('xpath', "//body/main/div[2]/a[2]/div[1]/div[1]/span[1]/span[1]")
        self.cats_section_locator = ('xpath', "//nav/ul/li[2]/a[1]")
        self.about_us_locator = ('xpath', "//span[contains(text(),'About Us')]")
        self.main_page_locator = ('xpath', "//header/a[@id='header__logo_1-0']/*[1]")