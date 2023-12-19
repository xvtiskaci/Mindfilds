from steps.login_page_steps import LoginPageSteps
from steps.translate_steps.translate_page_steps import TranslatePageSteps


class TestTranslate:

    def test_translate(self):
        login_steps = LoginPageSteps
        login_steps.login()
        translate_steps = TranslatePageSteps
        translate_steps.translate_page_steps()
