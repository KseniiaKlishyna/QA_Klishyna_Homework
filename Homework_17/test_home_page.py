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


def test_open_about_us(homepage):
    homepage.open_about_us()
    time.sleep(3)
    assert homepage._driver.current_url == "https://www.thesprucepets.com/about-us-4776796"


def test_return_to_main_page(homepage):
    homepage.open_cats_section()
    homepage.return_to_main()
    time.sleep(2)
    assert homepage._driver.current_url == "https://www.thesprucepets.com/"

def test_cookies(homepage):
    time.sleep(5)
    homepage.cookies.set_cookie("test_cookie", "test")
    cookie = homepage.cookies.get_cookie("test_cookie")
    assert cookie['value'] == "test"

def test_local_storage(homepage):
    time.sleep(3)
    homepage.local_storage.set_item("test_key", "green")
    value = homepage.local_storage.get_item("test_key")
    assert value == "green"
    homepage.local_storage.remove_item("test_key")
    value = homepage.local_storage.get_item("test_key")
    assert value is None
