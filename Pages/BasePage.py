from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator),
                                                    message=f"Can't find element by locator {locator}")

    def input_text(self, element, text):
        self.find_element(element).send_keys(text)

    def click_element(self, element):
        self.find_element(element).click()

    def get_text(self, element):
        return self.find_element(element).text

    def navigate_to(self, site_link):
        self.driver.get(site_link)
        self.driver.maximize_window()
