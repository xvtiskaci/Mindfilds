from steps.login_page_steps import LoginPageSteps
from steps.parameters_steps.help_page_steps import HelpPageSteps


class TestHelpPage:
    def test_help_page(self):
        login_steps = LoginPageSteps
        login_steps.login()
        help_page_steps = HelpPageSteps
        help_page_steps.check_all_help_menu_steps()
