import time


def test_open_article(homepage):
    time.sleep(5)
    homepage.open_article()
    time.sleep(3)
    assert homepage._driver.current_url != "https://www.thesprucepets.com"


def test_search_dogs(homepage):
    homepage.search_for_phrase('dogs')
    time.sleep(5)
    assert homepage._driver.current_url == "https://www.thesprucepets.com/search?q=dogs"


def test_open_cats_section(homepage):
    homepage.open_cats_section()
    time.sleep(3)
    assert homepage._driver.current_url == "https://www.thesprucepets.com/cats-4162124"


def test_open_about_us(homepage):
    homepage.open_about_us()
    time.sleep(3)
    assert homepage._driver.current_url == "https://www.thesprucepets.com/about-us-4776796"


def test_return_to_main_page(homepage):
    homepage.open_cats_section()
    homepage.return_to_main()
    time.sleep(2)
    assert homepage._driver.current_url == "https://www.thesprucepets.com/"
