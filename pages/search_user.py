#Validate presence of the newly created user in the admin user
import logging

from HRM_Project.pages.locators import Locators
from HRM_Project.pages.explicit_waits import UserWait
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Search_user:
    def __init__(self, search_user_driver):
        self.driver = search_user_driver
        self.wait = UserWait(self.driver)
    logger.info("user search initialized")
    def search_user(self, username):
        # Click Admin menu
        self.wait.wait_visible_and_clickable(Locators.admin_locators).click()

        # Enter username in search field
        search_box = self.wait.wait_visible(Locators.search_text)
        search_box.clear()
        search_box.send_keys(username)

        # Click Search button
        self.wait.wait_visible_and_clickable(Locators.search_btn).click()

        # Verify user appears in results table
        try:
            rows = self.wait.wait_presence_all_element(Locators.admin_table_rows)
            for row in rows:
                if username in row.text:
                    return True
        except TimeoutException:
            return False
    logger.info("Serch user completed")