from pages.menues.menu_page import MenuPage


class MenuPageSteps:

    @staticmethod
    def menu_page_steps():
        value = "test_title"
        red_value = "red_title_test"
        menu_page = MenuPage()
        menu_page.is_visible()
        menu_page.click_add_new_button()
        menu_page.fill_head_name(value)
        menu_page.click_add_button()
        added_menu_list = menu_page.find_edit_button()
        last_menu_edit = added_menu_list[len(added_menu_list) - 1]
        last_menu_edit.click()
        menu_page.redact_head_name(red_value)
        menu_page.click_add_button()
        menu_page.click_back()
        redacted_menu_list = menu_page.find_delete_button()
        last_menu_delete = redacted_menu_list[len(redacted_menu_list) - 1]
        last_menu_delete.click()
        menu_page.click_confirm_delete()

