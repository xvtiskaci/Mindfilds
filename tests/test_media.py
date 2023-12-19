from steps.login_page_steps import LoginPageSteps
from steps.media_steps.media_page_steps import MediaPageSteps


class TestMedia:

    def test_media(self):
        login_steps = LoginPageSteps
        login_steps.login()
        media_page_steps = MediaPageSteps
        media_page_steps.add_file_in_media_steps()
