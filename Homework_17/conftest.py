import pytest
from selenium.webdriver import Chrome
from Homework_17.home_page import HomePage
from Homework_17.category_page import CategoryPage


@pytest.fixture(scope="session")
def driver(request):
    driver = Chrome()

    yield driver
    driver.quit()


@pytest.fixture
def homepage(driver):
    driver.get("https://www.thesprucepets.com/")
    yield HomePage(driver)
