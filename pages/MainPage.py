from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class MainPage(BasePage):
    USERNAME_DROPDOWN = (By.ID, "navbarDropdown2")

    def verify_successful_login(self):
        return self.get_text(MainPage.USERNAME_DROPDOWN)
