import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class SephoraTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def close_modal_window(self):
        try:
            close_modal_button = self.driver.find_element(by='xpath', value='/html[1]/body[1]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]')
            close_modal_button.click()
            time.sleep(5)
        except:
            pass

    def test_open_website(self):
        self.driver.get("https://www.sephora.com/shop/makeup-cosmetics")
        self.close_modal_window()

        self.assertEqual("Makeup | Sephora", self.driver.title)
        self.driver.implicitly_wait(10)


    def test_open_basket(self):
        self.driver.get("https://www.sephora.com/shop/makeup-cosmetics")
        self.close_modal_window()

        basket_button = self.driver.find_element(by='xpath', value='//a[@id="inline_basket_trigger"]')
        actions = ActionChains(self.driver)
        actions.double_click(basket_button).perform()
        time.sleep(5)

        self.assertEqual("Basket | Sephora", self.driver.title)


    def test_search_element(self):
        self.driver.get("https://www.sephora.com/shop/makeup-cosmetics")
        self.close_modal_window()

        search_input = self.driver.find_element(by='xpath', value='//input[@id="site_search_input"]')
        search_input.send_keys("lipstick")
        time.sleep(5)
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)

        search_element = self.driver.find_element(by='xpath', value='//span[contains(text(),"lipstick")]')
        self.assertIsNotNone(search_element)


    def test_sort_elements(self):
        self.driver.get("https://www.sephora.com/shop/makeup-cosmetics")
        self.close_modal_window()

        sort_button = self.driver.find_element(by='xpath', value='//button[@id="cat_sort_menu_trigger"]')
        sort_button.click()
        time.sleep(2)
        sort_by_top_rated = self.driver.find_element(by='xpath', value='//body/div[2]/div[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[3]')
        sort_by_top_rated.click()
        time.sleep(5)
        expected_url = "https://www.sephora.com/shop/makeup-cosmetics?sortBy=TOP_RATED"
        current_url = self.driver.current_url
        self.assertEqual(expected_url, current_url)


    def test_filter_by_price(self):
        self.driver.get("https://www.sephora.com/shop/makeup-cosmetics")
        self.close_modal_window()
        time.sleep(2)
        price_range_button = self.driver.find_element(by='xpath', value='//body/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[6]/fieldset[18]/button[1]')
        price_range_button.click()
        time.sleep(2)
        under_25_option = self.driver.find_element(by='xpath', value='//body/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[6]/fieldset[18]/div[2]/div[1]/label[1]')
        under_25_option.click()
        time.sleep(5)

        expected_url = "https://www.sephora.com/shop/makeup-cosmetics?pl=min&ph=25"
        current_url = self.driver.current_url
        self.assertEqual(expected_url, current_url)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
