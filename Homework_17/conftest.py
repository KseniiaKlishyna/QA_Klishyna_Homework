import pytest
from selenium.webdriver import Safari
from Homework_17.home_page import HomePage


@pytest.fixture(scope="session")
def driver(request):
    driver = Safari()
    driver.get("https://www.thesprucepets.com/")

    yield driver
    driver.quit()


@pytest.fixture
def homepage(driver):
    yield HomePage(driver)
