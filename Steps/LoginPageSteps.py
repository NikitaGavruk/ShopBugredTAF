
from Pages.LoginPage import LoginPage


class LoginPageSteps(LoginPage):

    def perform_login(self):
        self.navigate_to_login_page()
        self.input_gmail()
        self.input_password()
        self.click_submit_button()
