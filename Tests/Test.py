from Pages import MainPage
from Pages.MainPage import MainPage
from Steps import LoginPageSteps
from Steps.LoginPageSteps import LoginPageSteps


def test_login(browser):
    login_page_steps = LoginPageSteps(browser)
    main_page = MainPage(browser)

    login_page_steps.perform_login()
    login_username = main_page.verify_successful_login()
    assert 'Никита' in login_username
