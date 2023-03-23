from pages import MainPage
from pages.MainPage import MainPage
from steps import LoginPageSteps
from steps.LoginPageSteps import LoginPageSteps


def test_login(browser):
    login_page_steps = LoginPageSteps(browser)
    main_page = MainPage(browser)

    login_page_steps.perform_login()
    login_username = main_page.verify_successful_login()
    assert 'Никита' in login_username
