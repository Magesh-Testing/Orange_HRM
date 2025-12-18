#Calling function from POM homepage
import pytest
import logging
import time

# Page Object imports
from HRM_Project.pages.homepage import HRM_Homepage
from HRM_Project.pages.create_user import HRM_create_user
from HRM_Project.pages.pim import HRM_Myinfopresence
from HRM_Project.pages.search_user import Search_user
from HRM_Project.pages.assign_leave import AssignLeave
from HRM_Project.pages.assign_claim import Assign_Claim

# Utility & locator imports
from HRM_Project.pages.locators import Locators
from HRM_Project.pages.explicit_waits import UserWait

# Test data utilities
from HRM_Project.read_data_from_excel import get_valid_credentials, get_invalid_credentials

#Read application URL from config.ini
from configparser import ConfigParser
config = ConfigParser()
config.read("C:/Users/wndows/PyCharmMiscProject/HRM_Project/config.ini")
link_to_open = config["HomepageURL"]["url"]

def get_test_data():
    from read_data_from_excel import get_credentials
    return get_credentials()

#Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Fixture: Create User (Executed once per test class)
@pytest.fixture(scope="class")
def created_user(setup_driver):
    driver = setup_driver    
    logger.info("Launching OrangeHRM application")
    driver.get(link_to_open)

    homepage = HRM_Homepage(driver)
    uname, pwd = get_valid_credentials()[0]  # take first valid credential
    homepage.validate_valid_username_password(uname, pwd)

    page = HRM_create_user(driver)

    unique_username = f"Dhiya_{int(time.time())}"
    page.create_user(
                    "Admin",
                    "Enabled",
                    "James Butler",
                    unique_username,
                    "Dhiya@1234",
                    "Dhiya@1234"
                )

    logger.info(f"User created successfully: {unique_username}")
    return unique_username

# Test Class: Project Scenarios
def test_validate_url(setup_driver):
    driver = setup_driver
    logger.info("Validating application URL")
    driver.get(link_to_open)
    actual_url = driver.current_url
    logger.info(f"Current URL: {actual_url}")
    assert actual_url == link_to_open, f"URL not matched. Expected: {link_to_open} result url {actual_url}"
    logger.info("URL validation successful")


class TestProjectScenario:
# Testcase 2: Verify whether the title of the webpage is correct.
    def test_validate_title(self,setup_driver):
        driver = setup_driver
        logger.info("Opening Homepage to validate title")
        driver.get(link_to_open)
        title = driver.title
        logger.info(f"Page title found: {title}")
        assert "OrangeHRM" == title, "Title mismatch"
        logger.info("Title validation successful")

    #TestCase 3: Validate presence of login fields on the homepage
    def test_validate_presence_of_login_fields(self, setup_driver):
        driver = setup_driver
        driver.get(link_to_open)
        homepage = HRM_Homepage(driver)
        homepage_assert = homepage.validate_presence_of_login_fields()
        assert  homepage_assert is True, "Logon field not working"
        logger.info("Login fields are validated successfully")

    # Validate login with invalid credentials (negative testing)
    @pytest.mark.parametrize('invalid_uname, invalid_pwd', get_invalid_credentials())
    def test_invalid_login_credentials(self, setup_driver, invalid_uname, invalid_pwd):
        driver = setup_driver
        driver.get(link_to_open)
        homepage = HRM_Homepage(driver)
        login_status = homepage.is_login_error_displayed(invalid_uname, invalid_pwd)
        assert login_status is True, "Login passed with invalid credentials"
        logger.info("When logged in with incorrect credentials Login not successful")

    #TestCase 7: Verify "Forgot Password" link functionality
    @pytest.mark.parametrize("uname", ["Admin"])
    def test_forgot_password_functionality(self, setup_driver, uname):
        driver = setup_driver
        driver.get(link_to_open)
        homepage = HRM_Homepage(driver)
        logger.info("Starting forgot password flow")
        message_element = homepage.forgot_password(uname)
        assert "reset password link" in message_element.text
        logger.info("Forgot password functionality validated successfully")

    # TestCase 1: Validate login with invalid credentials (negative testing)
    @pytest.mark.parametrize('valid_uname, valid_pwd', get_valid_credentials())
    def test_valid_login_credentials(self, setup_driver, valid_uname, valid_pwd):
        driver = setup_driver
        driver.get(link_to_open)
        homepage = HRM_Homepage(driver)
        login_status = homepage.validate_valid_username_password(valid_uname, valid_pwd)
        assert login_status is True, "Login failed with valid credentials"
        logger.info("Login successful with valid credentials")

    #TestCase 4: Verify visibility and clickability of main menu items after login
    @pytest.mark.parametrize('uname,pwd', get_valid_credentials())
    def test_user_management_menu_items(self, setup_driver, uname, pwd):
        driver = setup_driver
        wait = UserWait(driver)
        driver.get(link_to_open)

        # homepage = HRM_Homepage(driver)
        # assert homepage.validate_valid_username_password(uname, pwd), "Login failed with valid credentials"

        assert wait.wait_visible_and_clickable(Locators.admin_locators).is_enabled(), "Admin menu not enabled"
        assert wait.wait_visible_and_clickable(Locators.PIM_locators).is_enabled(), "PIM menu not enabled"
        assert wait.wait_visible_and_clickable(Locators.leave_locators).is_enabled(), "Leave menu not enabled"
        assert wait.wait_visible_and_clickable(Locators.time_locators).is_enabled(), "Time menu not enabled"
        assert wait.wait_visible_and_clickable(Locators.recruitment_locators).is_enabled(), "Recruitment menu not enabled"
        assert wait.wait_visible_and_clickable(Locators.Myinfo_locators).is_enabled(), "My Info menu not enabled"
        assert wait.wait_visible_and_clickable(Locators.Performance_locators).is_enabled(), "Performance menu not enabled"
        assert wait.wait_visible_and_clickable(Locators.dashboard).is_enabled(), "Dashboard menu not enabled"
        logger.info("Main menu items are validated successfully")

    #TestCase 5: Create a new user and validate login
    def test_create_user(self, created_user):
        assert created_user is not None
        logger.info(f"User creation verified: {created_user}")

    #TestCase 8: Validate the presence of menu items under “My Info”
    @pytest.mark.parametrize('uname,pwd', get_valid_credentials())
    def test_my_info_presence(self, setup_driver, uname, pwd):
        driver = setup_driver
        driver.get(link_to_open)
        homepage = HRM_Homepage(driver)
        assert homepage.validate_valid_username_password(uname, pwd), "Login failed with valid credentials"
        hrm_myinfo = HRM_Myinfopresence(driver)
        assert hrm_myinfo.my_infopresence(), "Some of the links are not active"
        logger.info("My Info menu items validated")

    #TestCase 6: Validate presence of the newly created user in the admin user list
    @pytest.mark.parametrize('uname,pwd', get_valid_credentials())
    def test_presence_of_new_user(self, setup_driver, uname, pwd, created_user):
        driver = setup_driver
        driver.get(link_to_open)
        homepage = HRM_Homepage(driver)
        homepage.validate_valid_username_password(uname, pwd)
        search_user = Search_user(driver)
        is_user_listed = search_user.search_user(created_user)
        assert is_user_listed is True, "Newly created user not found"
        logger.info("Newly created user verified in Admin list")

    #TestCAse 9: Assign leave to an employee and verify assignment
    @pytest.mark.parametrize('uname,pwd', get_valid_credentials())
    def test_assign_leave(self, setup_driver, uname, pwd):
        driver = setup_driver
        driver.get(link_to_open)
        homepage = HRM_Homepage(driver)
        assert homepage.validate_valid_username_password(uname, pwd), "Login failed"
        logger.info("Assigning leave to employee")
        assign_leave_for_employee = AssignLeave(driver)
        result = assign_leave_for_employee.user_leave_assigning()
        assert result is False, "Leave assignment failed"
        logger.info("Leave assigned successfully")

    #TestCAse 10: Assign claim to an employee and verify claim
    @pytest.mark.parametrize('uname,pwd', get_valid_credentials())
    def test_claim(self, setup_driver, uname, pwd):
        driver = setup_driver
        logger.info("Launching application for Claim test")
        driver.get(link_to_open)
        homepage = HRM_Homepage(driver)
        logger.info("Logging in with valid credentials")
        assert homepage.validate_valid_username_password(uname, pwd), "Login failed"
        logger.info("Assigning claim request")
        claim_request = Assign_Claim(driver)
        logger.info("Assigning claim to employee")
        assert claim_request.fill_claim_assign(), "Claim assignment failed"
        logger.info("Opening Add Expense page")
        assert claim_request.claim_expense_page(), "Claim expense button not working"
        logger.info("Adding expense to claim")
        assert  claim_request.add_expense(), "Add Expense page not opening"