from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm


class TranslatePage(BaseForm):
    __translate_menu = Button(By.XPATH, "//a[@title='თარგმნა']", "თარგმნის მენიუ")
    __add_new_button = Button(By.XPATH, "//div[@class='add']", "ახლის დამატების ღილაკი")
    __field_kay_word = Input(By.XPATH, "//input[@id='keyword']", "გასაღების ველი")
    __field_value = Input(By.XPATH, "//textarea[@id='value']", "მნიშვნელობის ველი")
    __add_button = Button(By.XPATH, "//button[@class='gilaki']", "დამატების ღილაკი")
    __back = Button(By.XPATH, "//div[@class='back_to']", "უკან გამოსვლა")
    __edits_buttons_list = Button(By.XPATH, "//li[@class='edit']//a", "დამატებული პარამეტრის ედითის ღილაკი")
    __delete_buttons_list = Button(By.XPATH, "//li[@class='delete']//a", "დარედაქტირებული პარამეტრის წაშლის ღილაკი")
    __confirm_delete = Button(By.XPATH, "//button[@class='gilaki yes']", "წაშლის დადასტურება")

    def __init__(self):
        super().__init__(By.XPATH, "//h1[@class='title']//span[contains(text(),'თარგმნა')]",
                         "თარგმნის დასახელება ზედა მარცხენა კუთხეში")

    def click_translate_menu(self):
        self.__translate_menu.click()

    def click_add_new_button(self):
        self.__add_new_button.click()

    def fill_kay_word(self, kay_word):
        self.__field_kay_word.send_text(kay_word)

    def fill_value(self, kay_value):
        self.__field_value.send_text(kay_value)

    def click_add_button(self):
        self.__add_button.click()

    def click_back(self):
        self.__back.click()

    def find_edit_button(self):
        return self.__edits_buttons_list.find_elements()

    def redact_value(self, red_value):
        self.__field_value.clear_and_fill(red_value)

    def find_delete_button(self):
        return self.__delete_buttons_list.find_elements()

    def click_confirm_delete(self):
        self.__confirm_delete.click()
