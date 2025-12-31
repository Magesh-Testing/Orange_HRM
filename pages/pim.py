import logging
from HRM_Project.pages.locators import Locators
from HRM_Project.pages.explicit_waits import UserWait

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class HRM_Myinfopresence:
    def __init__(self, myinfodriver):
        self.driver = myinfodriver
        self.wait = UserWait(self.driver)
    logger.info("My info menu's sub items initiated")
    def my_infopresence(self):
        self.wait.wait_clickable(Locators.Myinfo_locators).click()

        self.wait.wait_visible(Locators.personal_details)

        link_items = [
            Locators.contact_details,
            Locators.emergency_contact,
            Locators.dependent,
            Locators.immigration,
            Locators.job,
            Locators.salary,
            Locators.reportto,
            Locators.qualification,
            Locators.membership
        ]

        for item in link_items:
            self.wait.wait_clickable(item).click()
        return True
    logger.info("My info's sub menu validation completed")