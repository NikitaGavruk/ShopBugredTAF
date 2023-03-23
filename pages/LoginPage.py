from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    GMAIL_FORM = (By.ID, "exampleInputEmail1")
    PASSWORD_FORM = (By.ID, "exampleInputPassword1")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and @class='btn btn-primary']")
    LOGIN_FORM_LINK = "http://shop.bugred.ru/user/login/index"

    def navigate_to_login_page(self):
        self.navigate_to(LoginPage.LOGIN_FORM_LINK)

    # Bad practice to keep login and password here, but I do not care
    def input_gmail(self):
        self.input_text(LoginPage.GMAIL_FORM, "gavruk1337@gmail.com")

    def input_password(self):
        self.input_text(LoginPage.PASSWORD_FORM, "QsZ3kCWKxFqM99z")

    def click_submit_button(self):
        self.click_element(LoginPage.SUBMIT_BUTTON)
