from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.common.by import By


class GooglePage:
    SEARCH_BOX = (By.NAME, "q")
    RESULT_HEADINGS = (By.CSS_SELECTOR, "h3")
    
    def __init__(self, driver, timeout=10,base_url=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.url = base_url

    def open(self):
        self.driver.get(self.url)
        self.wait.until(EC.visibility_of_element_located(GooglePage.SEARCH_BOX))
        logging.info("Opened Google homepage")

    def search(self, query):
        box = self.wait.until(EC.element_to_be_clickable(GooglePage.SEARCH_BOX))
        box.clear()
        box.send_keys(query, Keys.RETURN)

    def get_results_text(self):
        self.wait.until(EC.presence_of_all_elements_located(GooglePage.RESULT_HEADINGS))
        return [r.text for r in self.driver.find_elements(GooglePage.RESULT_HEADINGS)]