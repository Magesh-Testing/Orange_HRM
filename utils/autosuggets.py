from selenium.webdriver.common.keys import Keys
import time

class AutoSuggestHelper:

    def __init__(self, wait):
        self.wait = wait

    def select_first_option(self, input_locator, options_locator, text):

        #Generic method to handle auto-suggest dropdowns
        input_box = self.wait.wait_visible(input_locator)
        input_box.click()
        input_box.clear()

        # Type only first few characters
        input_box.send_keys(text[:3])
        time.sleep(1)  # allow dropdown to populate

        options = self.wait.wait_visible_all(options_locator)

        if not options:
            raise Exception("Auto-suggest options not loaded")

        options[0].click()