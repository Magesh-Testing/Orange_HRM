#Importing drivers
import logging

from selenium.webdriver.common.by import By
from HRM_Project.pages.explicit_waits import UserWait
from HRM_Project.pages.locators import Locators
from HRM_Project.utils.autosuggets import AutoSuggestHelper

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class HRM_create_user:
    def __init__(self, driver):
        self.driver = driver
        self.wait = UserWait(driver)
        self.autosuggest = AutoSuggestHelper(self.wait)

        logger.info("New user creation initialized...")

    def select_dropdown(self, dropdown_locator, option_text):
        dropdown = self.wait.wait_clickable(dropdown_locator)
        dropdown.click()

        option = (By.XPATH, f"//div[@role='option']//span[text()='{option_text}']")
        self.wait.wait_clickable(option).click()


    def select_user_role(self, role):
        self.select_dropdown(Locators.user_role, role)

    def select_status(self, status):
        self.select_dropdown(Locators.status_dropdown, status)

    def employee_name(self, emp_name):
        emp_box = self.wait.wait_visible(Locators.employee_name)
        emp_box.click()
        emp_box.clear()
        emp_box.send_keys(emp_name[:3])

        first_option =self.wait.wait_visible_all(Locators.employee_first_option)
        #self.wait.wait_clickable(Locators.employee_first_option)
        first_option[0].click()

    def fill_username(self, username):
        self.wait.wait_visible(Locators.create_username).send_keys(username)

    def fill_password(self, password):
        self.wait.wait_visible(Locators.create_password).send_keys(password)

    def fill_confirm_password(self, confirm_password):
        self.wait.wait_visible(Locators.create_confirm_password).send_keys(confirm_password)

    def save_details(self):
        self.wait.wait_clickable(Locators.create_user_save_button).click()

    def logout_from_admin(self):
        self.wait.wait_clickable(Locators.logout_dropdown).click()
        self.wait.wait_clickable(Locators.logout).click()

    def create_user(self, role, status, emp_name, username, password, confirm_password):
        self.wait.wait_clickable(Locators.admin_locators).click()
        self.wait.wait_clickable(Locators.create_user_add_button).click()

        self.select_user_role(role)
        self.select_status(status)
        self.employee_name(emp_name)
        self.fill_username(username)
        self.fill_password(password)
        self.fill_confirm_password(confirm_password)
        self.save_details()

        self.logout_from_admin()
        logger.info("User created completed successfully")