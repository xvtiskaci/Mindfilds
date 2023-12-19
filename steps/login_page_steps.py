from pages.login_page import LoginPage


class LoginPageSteps:
    @staticmethod
    def login():
        email = "welcome@artmedia.ge"
        password = "PaSsword!123"
        login_page = LoginPage()
        login_page.is_visible()
        login_page.close_php()
        login_page.fill_username(email)
        login_page.fill_password(password)
        login_page.click_login_button()



