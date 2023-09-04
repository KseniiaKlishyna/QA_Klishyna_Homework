import time

def test_open_cats_section(homepage):
    homepage.open_cats_section()
    time.sleep(3)
    assert homepage._driver.current_url == "https://www.thesprucepets.com/cats-4162124"

def test_open_category_article(categories):
    categories.open_category_article()
    time.sleep(5)
    assert categories._driver.current_url != "https://www.thesprucepets.com/cats-4162124"
