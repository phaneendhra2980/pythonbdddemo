from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class SearchPage(BasePage):

    local_directories = {
        "pop_up_i_agree_button": (
            By.ID, 'L2AGLb'
        ),
        "searching_button": (
            By.CLASS_NAME, 'gNO89b'),
        "searching_box": (
            By.CLASS_NAME, 'gLFyf gsfi'),


    }

    def press_pop_up_button_i_agree(self):
        self.browser.find_element(
            *self.local_directories["pop_up_i_agree_button"]).click()

    def insert_text_to_search_bar(self, text):
        self.browser.find_element(
            *self.local_directories["searching_bar"]).send_keys(text)

    def press_google_search_button_search_page(self):
        self.browser.find_element(
            *self.local_directories["searching_button"]).click()
