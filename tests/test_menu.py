from steps.login_page_steps import LoginPageSteps
from steps.menu_steps.menu_page_steps import MenuPageSteps


class TestMenu:

    def test_translate(self):
        login_steps = LoginPageSteps
        login_steps.login()
        menu_steps = MenuPageSteps
        menu_steps.menu_page_steps()
