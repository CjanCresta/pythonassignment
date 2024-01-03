import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_search_flight(browser):
    browser.get("https://www.yatra.com/")

    try:

        depart_from_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'BE_flight_origin_city'))
        )
        depart_from_input.send_keys('Kathmandu')

        depart_from_input.send_keys(Keys.ARROW_DOWN, Keys.ENTER)


        going_to_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'BE_flight_arrival_city'))
        )
        going_to_input.send_keys('Biratnagar')


        going_to_input.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

        # Click on the student fare checkbox
        student_fare_checkbox = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'studentFare'))
        )
        student_fare_checkbox.click()

        search_button = browser.find_element(By.ID, 'BE_flight_flsearch_btn')
        search_button.click()


        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-listing'))
        )

        # Perform assertions or additional actions based on the search results
        assert "Search Results" in browser.title
        # Add more assertions as needed

    except (NoSuchElementException, TimeoutException) as e:
        pytest.fail(f"Element not found: {str(e)}")

if __name__ == "__main__":
    pytest.main(['-v', 'test_yatra.py'])