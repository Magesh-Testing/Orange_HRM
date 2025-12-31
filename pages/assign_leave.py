import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from HRM_Project.pages.explicit_waits import UserWait
from HRM_Project.pages.locators import Locators

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class AssignLeave:
    def __init__(self, driver):
        self.driver = driver
        self.wait = UserWait(driver)
        logger.info("AssignLeave page object initialized")

    def user_leave_assigning(self):
        logger.info("Starting leave assignment process")
        try:
            # 1. Navigate to Assign Leave
            logger.info("Navigating to Leave assigning module")
            self.wait.wait_clickable(Locators.leave_locators).click()
            self.wait.wait_clickable(Locators.assign_leave_menu).click()

            # 2. Employee Name
            emp = self.wait.wait_visible(Locators.employee_name_input)
            emp.clear()
            emp.send_keys("an")
            emp.send_keys(Keys.ARROW_DOWN)
            emp.send_keys(Keys.ENTER)
            #self.wait.wait_clickable(Locators.employee_first_option).click()

            # 3. Leave Type
            self.wait.wait_clickable(Locators.leave_type_dropdown).click()
            self.wait.wait_clickable(Locators.leave_type_option).click()

            # 4. From & To Dates (FIXED)
            dates = self.wait.wait_all_visible(Locators.date_inputs)

            dates[0].clear()
            dates[0].send_keys("2025-12-20")
            dates[0].send_keys(Keys.TAB)

            dates[1].clear()
            dates[1].send_keys("2025-12-25")
            dates[1].send_keys(Keys.TAB)

            # 5. Assign Button
            self.wait.wait_clickable(Locators.confirm_assign_button).click()

            # 6. Validate success toast (FIXED TEXT CHECK)
            success_msg = self.wait.wait_visible(Locators.leave_success_toast).text
            logger.info(f"Toast message: {success_msg}")

            if "Assigned" in success_msg:
                logger.info("Leave assigned successfully")
                return True
            logger.warning("Leave assignment successful but success message not matched")
            return False

        except TimeoutException as e:
            logger.exception("Timeout during leave assignment")
            return False

        except Exception as e:
            logger.exception("Unexpected error during leave assignment")
            return False