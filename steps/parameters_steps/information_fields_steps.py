import time

import pyautogui

from pages.parameters.information_fields_page import InformationFieldsPage


class InformationFieldsSteps:

    @staticmethod
    def add_redact_delete_info_fields_steps():
        information_fields_page = InformationFieldsPage()
        kay = "test kay"
        desc = "test description"
        value = "test value"
        red_desc = "redact test description"
        information_fields_page.click_parameters_menu()
        information_fields_page.is_enabled_information_field_menu()
        information_fields_page.click_information_field_menu()
        information_fields_page.is_visible()
        information_fields_page.click_add_new_info()
        information_fields_page.fill_kay_word(kay)
        information_fields_page.fill_desc(desc)
        information_fields_page.click_add_button()
        information_fields_page.click_back()
        added_info_list = information_fields_page.get_added_info_edits_buttons()
        last_info_edit = added_info_list[len(added_info_list) - 1]
        last_info_edit.click()
        information_fields_page.fill_value(value)
        information_fields_page.redact_desc(red_desc)
        information_fields_page.click_save_button()
        information_fields_page.click_back()
        redacted_info_list = information_fields_page.get_redacted_info_delete_buttons()
        last_info_delete = redacted_info_list[len(redacted_info_list) - 1]
        last_info_delete.click()
        information_fields_page.click_confirm_delete()

