import os
import time

import pyautogui

from pages.media.media_page import MediaPage


class MediaPageSteps:
    @staticmethod
    def add_file_in_media_steps():
        media_page = MediaPage()
        photo = os.path.abspath("../resources/photos/Ghvtiso.jpg")
        photo_name = "Ghvtiso"
        media_page.click_media_menu()
        media_page.is_visible()
        media_page.send_photo(photo)
        time.sleep(10)
        media_page.fill_search(photo_name)
        pyautogui.press("enter")
        media_page.move_to_photo()
        media_page.click_delete_button()
        media_page.click_confirm_delete()
