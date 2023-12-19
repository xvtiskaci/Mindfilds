from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_form import BaseForm


class HelpPage(BaseForm):
    __parameters_menu = Button(By.XPATH, "//a[@title='პარამეტრები']", "პარამეტრების მენიუ")
    __help_menu = Button(By.XPATH, "//a[contains(text(),'დახმარება')]", "დახმარება მენიუ")
    __back = Button(By.XPATH, "//a[contains(text(),'« უკან')]", "უკან დაბრუნების ღილაკი")
    __pages = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'გვერდები')]", "გვერდები")
    __shortcodes = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'შორთკოდები')]", "შორთკოდები")
    __terms = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'ტერმინები')]", "ტერმინები")
    __comments = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'კომენტარები')]", "კომენტარები")
    __user = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'მომხმარებელი')]", "მომხმარებელი")
    __roles = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'როლები')]", "როლები")
    __slider = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'სლაიდერი')]", "სლაიდერი")
    __subscribers = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'გამომწერები')]", "გამომწერები")
    __banners = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'ბანერები')]", "ბანერები")
    __tests = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'ტესტები')]", "ტესტები")
    __survey = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'გამოკითხვა')]", "გამოკითხვა")
    __calculators = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'კალკულატორები')]", "კალკულატორები")
    __facebook_share = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'facebook გაზიარება')]", "facebook გაზიარება")
    __media = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'მედია')]", "მედია")
    __translate = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'თარგმნა')]", "თარგმნა")
    __params_info = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'პარამეტრები » ინფ. ველები')]", "პარამეტრები » ინფ. ველები")
    __params_log = Button(By.XPATH, "//nav[@class='widget medium']//li[contains(.,'პარამეტრები » ლოგირება')]", "პარამეტრები » ლოგირება")

    def __init__(self):
        super().__init__(By.XPATH, "//span[contains(text(),'დახმარება')]", "ის რომ დახმარების გვერდზეა")

    def click_help_menu(self):
        self.__help_menu.click()

    def click_parameters_menu(self):
        self.__parameters_menu.click()

    def click_back(self):
        self.__back.click()

    def click_pages(self):
        self.__pages.click()

    def click_shortcodes(self):
        self.__shortcodes.click()

    def click_terms(self):
        self.__terms.click()

    def click_comments(self):
        self.__comments.click()

    def click_user(self):
        self.__user.click()

    def click_roles(self):
        self.__roles.click()

    def click_slider(self):
        self.__slider.click()

    def click_subscribers(self):
        self.__subscribers.click()

    def click_banners(self):
        self.__banners.click()

    def click_tests(self):
        self.__tests.click()

    def click_survey(self):
        self.__survey.click()

    def click_calculators(self):
        self.__calculators.click()

    def click_facebook_share(self):
        self.__facebook_share.click()

    def click_media(self):
        self.__media.click()

    def click_translate(self):
        self.__translate.click()

    def click_params_info(self):
        self.__params_info.click()

    def click_params_log(self):
        self.__params_log.click()
