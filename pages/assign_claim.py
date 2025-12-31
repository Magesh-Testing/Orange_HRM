import logging

from HRM_Project.pages.locators import Locators
from HRM_Project.pages.explicit_waits import UserWait
from selenium.webdriver.common.keys import Keys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Assign_Claim:
    def __init__(self, driver):
        self.driver = driver
        self.wait = UserWait(driver)

    def fill_claim_assign(self):
        try:
            logger.info("Navigating to Claim module")
            self.wait.wait_clickable(Locators.left_side_menu_claim).click()

            logger.info("Opening Assign Claim page")
            self.wait.wait_clickable(Locators.claim_assign_heading).click()

            logger.info("Entering employee name")
            emp = self.wait.wait_visible(Locators.claim_emp_name)
            emp.clear()
            emp.send_keys("a")

            logger.info("Selecting employee from suggestions")
            suggestions = self.wait.wait_presence_all_element(Locators.claim_emp_suggestion)
            suggestions[0].click()

            logger.info("Selecting claim event")
            self.wait.wait_clickable(Locators.claim_event).click()
            self.wait.wait_clickable(Locators.claim_event_item).click()

            logger.info("Selecting currency")
            self.wait.wait_clickable(Locators.claim_currency).click()
            self.wait.wait_clickable(Locators.claim_currency_selector).click()

            logger.info("Entering remarks")
            self.wait.wait_visible(Locators.remark_textbox).send_keys("Accommodation Expense")

            logger.info("Submitting claim")
            self.wait.wait_clickable(Locators.create_claim_btn).click()

            logger.info("Verifying Claim Details page")
            assert self.wait.wait_visible(Locators.claim_details_page).is_displayed()

            return True

        except Exception as e:
            logger.exception("Claim assignment failed")
            return False

    def claim_expense_page(self):
        try:
            logger.info("Clicking Add Expense button")
            self.wait.wait_clickable(Locators.claim_add_button).click()

            logger.info("Add Expense page opened")
            return True

        except Exception as e:
            logger.exception("Add Expense page not opening")
            return False

    def add_expense(self):
        try:
            logger.info("Entering expense type")
            self.wait.wait_visible(Locators.expense_type).send_keys("Accommodation")

            logger.info("Selecting date")
            date = self.wait.wait_visible(Locators.add_expense_date)
            date.clear()
            date.send_keys("2025-20-12")
            date.send_keys(Keys.TAB)

            logger.info("Entering amount")
            self.wait.wait_visible(Locators.add_expense_amount).send_keys("2000")

            logger.info("Submitting expense")
            self.wait.wait_clickable(Locators.add_expense_submit_btn).click()

            return True

        except Exception as e:
            logger.exception("Adding expense failed")
            return False