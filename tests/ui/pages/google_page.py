from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time

class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com"
        self.search_box = (By.NAME, "q")
        self.result_headings = (By.CSS_SELECTOR, "h3")

    def open(self):
        self.driver.get(self.url)
        logging.info("Opened Google homepage")

    def search(self, query):
        box = self.driver.find_element(*self.search_box)
        box.clear()
        box.send_keys(query)
        box.send_keys(Keys.RETURN)
        logging.info(f"Searched for '{query}'")
        time.sleep(2)  # simple wait for results to load

    def validate_results(self, query):
        results = self.driver.find_elements(*self.result_headings)
        assert any(query.lower() in r.text.lower() for r in results), f"'{query}' not found in results"
        logging.info(f"Results validated for '{query}'")