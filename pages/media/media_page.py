from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from elements.input import Input
from pages.base_form import BaseForm


class MediaPage(BaseForm):
    __media_menu = Button(By.XPATH, "//a[@title='მედია']", "მედიას მენიუზე დაკლიკება")
    __file_input = Input(By.XPATH, "//input[@class='file-input']", "ფაილის ატვირთვა")
    __search = Input(By.XPATH, "//input[@id='search']", "მედიას სერჩი")
    __added_photo = Element(By.XPATH, "//li[@class='widget light']", "დამატებული ფოტო")
    __delete_file = Button(By.XPATH, "//a[@title='წაშლა']", "დამატებული ფაილის წაშლა")
    __confirm_delete = Button(By.XPATH, "//button[contains(text(),'წაშლა')]", "წაშლის დადასტურება")

    def __init__(self):
        super().__init__(By.XPATH, "//h1[@class='title']//span[contains(text(),'მედია')]", "ის რომ დახმარების გვერდზეა")

    def click_media_menu(self):
        self.__media_menu.click()

    def send_photo(self, photo):
        self.__file_input.upload_image(photo)

    def fill_search(self, photo_name):
        self.__search.send_text(photo_name)

    def move_to_photo(self):
        self.__added_photo.move_to_element()

    def click_delete_button(self):
        self.__delete_file.click()

    def click_confirm_delete(self):
        self.__confirm_delete.click()
