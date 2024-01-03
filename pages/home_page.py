from pages.base_page import BasePage
from utils.constants import YATRA_URL

class HomePage(BasePage):
    def open(self):
        self.driver.get(YATRA_URL)

    def search_flights(self, from_city, to_city, departure_date):
        # Implement code to search for flights on the home page
        pass