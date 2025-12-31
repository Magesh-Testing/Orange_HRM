from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserWait:

    def __init__(self, user_driver, timeout=20):
        self.driver = user_driver
        self.wait = WebDriverWait(user_driver, timeout)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_visible_and_clickable(self, locator):
        self.wait_visible(locator)
        return self.wait_clickable(locator)

    def wait_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_presence_all_element(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_visible_all(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))