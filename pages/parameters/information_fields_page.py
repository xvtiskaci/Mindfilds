from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm


class InformationFieldsPage(BaseForm):
    __parameters_menu = Button(By.XPATH, "//a[@title='პარამეტრები']", "პარამეტრების მენიუ")
    __information_field_menu = Button(By.XPATH, "//a[@title='ინფორმაციული ველები']", "ინფორმაციული ველების მენიუ")
    __add_new_info = Button(By.XPATH, "//div[@class='add']", "ახლის დამატება")
    __kay_word = Input(By.XPATH, "//input[@id='keyword']", "გასაღები")
    __desc = Input(By.XPATH, "//textarea[@id='desc']", "აღწერა")
    __add_button = Button(By.XPATH, "//button[@class='gilaki']", "დამატება")
    __back = Button(By.XPATH, "//div[@class='back_to']", "უკან გამოსვლა")
    __edits_buttons_list = Button(By.XPATH, "//li[@class='edit']//a", "დამატებული ინფოს ედითის ღილაკი")
    __value = Input(By.XPATH, "//input[@id='value']", "მნიშვნელობა")
    __desc_redact = Input(By.XPATH, "//textarea[@id='desc']", "აღწერა დარედაქტება")
    __save_button = Button(By.XPATH, "//button[@class='gilaki']", "შენახვა")
    __delete_buttons_list = Button(By.XPATH, "//li[@class='delete']//a", "დარედაქტირებული ინფოს წაშლის ღილაკი")
    __delete_confirm = Button(By.XPATH, "//button[@class='gilaki yes']", "წაშლა")

    def __init__(self):
        super().__init__(By.XPATH, "//h1[@class='title']//span[contains(text(),'პარამეტრები')]",
                         "პარამეტრების დასახელება ზედა მარცხენა კუთხეში")

    def click_parameters_menu(self):
        self.__parameters_menu.click()

    def click_information_field_menu(self):
        self.__information_field_menu.click()

    def is_enabled_information_field_menu(self):
        self.__information_field_menu.is_enabled()

    def click_add_new_info(self):
        self.__add_new_info.click()

    def fill_kay_word(self, kay):
        self.__kay_word.send_text(kay)

    def fill_desc(self, desc):
        self.__desc.send_text(desc)

    def click_add_button(self):
        self.__add_button.click()

    def click_back(self):
        self.__back.click()

    def get_added_info_edits_buttons(self):
        return self.__edits_buttons_list.find_elements()

    def fill_value(self, value):
        self.__value.send_text(value)

    def redact_desc(self, red_desc):
        self.__desc_redact.clear_and_fill(red_desc)

    def click_save_button(self):
        self.__save_button.click()

    def get_redacted_info_delete_buttons(self):
        return self.__delete_buttons_list.find_elements()

    def click_confirm_delete(self):
        self.__delete_confirm.click()
