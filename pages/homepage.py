import logging
from selenium.common.exceptions import TimeoutException
from HRM_Project.pages.locators import Locators
from HRM_Project.pages.explicit_waits import UserWait

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class HRM_Homepage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = UserWait(self.driver)

    logger.info("Homepage element validation initialized")
    def validate_presence_of_login_fields(self):
        try:
            self.wait.wait_visible(Locators.login_username)
            self.wait.wait_visible(Locators.login_password)
            self.wait.wait_clickable(Locators.login_submit)
            return True
        except Exception as e:
            print(f"Error validating login fields {e}")
            return False

    def is_login_error_displayed(self, uname, pwd):
        self.wait.wait_visible(Locators.login_username).send_keys(uname)
        self.wait.wait_visible(Locators.login_password).send_keys(pwd)
        self.wait.wait_clickable(Locators.login_submit).click()
        return self.wait.wait_visible(Locators.login_error).is_displayed()

    def validate_valid_username_password(self, valid_usrname, valid_password):
        if "dashboard" in self.driver.current_url:
            return True
        self.wait.wait_visible(Locators.login_username).send_keys(valid_usrname)
        self.wait.wait_visible(Locators.login_password).send_keys(valid_password)
        self.wait.wait_clickable(Locators.login_submit).click()
        self.wait.wait_visible(Locators.logout_dropdown).is_displayed()
        return True

    def validate_main_menu_items(self):
        menus= [Locators.admin_locators,
        Locators.PIM_locators,
        Locators.leave_locators,
        Locators.time_locators,
        Locators.recruitment_locators,
        Locators.Myinfo_locators,
        Locators.Performance_locators,
        Locators.dashboard_menu_locators
                ]
        return all(self.wait.wait_visible_and_clickable(menu).is_enabled() for menu in menus)

    def logout_functionality(self):
        profile_dropdown=self.wait.wait_clickable(Locators.logout_dropdown)
        profile_dropdown.click()
        logout_click=self.wait.wait_clickable(Locators.logout)
        logout_click.click()
        return True

    def forgot_password(self, username):
        self.wait.wait_clickable(Locators.forgot_password).click()
        self.wait.wait_visible(Locators.forgot_password_username).send_keys(username)
        self.wait.wait_clickable(Locators.forgot_password_reset).click()
        return self.wait.wait_visible(Locators.forgot_password_reset_message)
    logger.info("Elements in homepage validated")