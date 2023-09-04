from Homework_17.core.base_locators import BaseLocators
class CategoriesLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.category_article_locator = ('xpath', " //body[1]/main[1]/section[1]/div[4]/div[2]/div[1]/a[1]")