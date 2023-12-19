import time

from pages.translate.translate_page import TranslatePage


class TranslatePageSteps:
    @staticmethod
    def translate_page_steps():
        translate_page = TranslatePage()
        kay_word = "test_kay"
        kay_value = "test_value"
        red_value = "redact_test_value"
        translate_page.click_translate_menu()
        translate_page.is_visible()
        translate_page.click_add_new_button()
        translate_page.fill_kay_word(kay_word)
        translate_page.fill_value(kay_value)
        translate_page.click_add_button()
        translate_page.is_visible()
        added_translate_list = translate_page.find_edit_button()
        first_info_edit = added_translate_list[0]
        first_info_edit.click()
        translate_page.redact_value(red_value)
        translate_page.click_add_button()
        translate_page.click_back()
        translate_page.is_visible()
        delete_button_list = translate_page.find_delete_button()
        first_delete_button = delete_button_list[0]
        first_delete_button.click()
        translate_page.click_confirm_delete()
