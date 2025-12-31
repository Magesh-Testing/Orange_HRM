from selenium.webdriver.common.by import By

class Locators:

 #Common POM element
    dashboard = (By.XPATH, "//h6[text()='Dashboard']")

#Locators for Homepage
#Login page locators
    login_username = (By.NAME, "username")
    login_password = (By.NAME, "password")
    login_submit = (By.XPATH, "//button[@type='submit']")
    login_error = (By.CSS_SELECTOR, "p.oxd-alert-content-text")

#Logout page locators
    logout_dropdown = (By.XPATH, "//span[contains(@class,'oxd-userdropdown-tab')]")
    logout = (By.XPATH, "//a[text()='Logout']")

 #Locators for Forgot password functionality
    forgot_password = (By.XPATH, "//p[contains(@class, 'orangehrm-login-forgot-header')]")
    forgot_password_username = (By.NAME, "username")
    forgot_password_reset = (By.XPATH, "//button[@type='submit']")
    forgot_password_reset_message = (By.XPATH, "//p[contains(., 'A reset password link')]")

#menu Left sidebar
#Locators for User Management
    user_management_heading = (By.XPATH, "//h6[text()='User Management']")
    admin_locators = (By.XPATH, "//span[text()='Admin']")
    PIM_locators = (By.XPATH, "//span[text()='PIM']")
    leave_locators = (By.XPATH, "//span[text()='Leave']")
    time_locators = (By.XPATH, "//span[text()='Time']")
    recruitment_locators = (By.XPATH, "//span[text()='Recruitment']")
    Myinfo_locators = (By.XPATH, "//span[text()='My Info']")
    Performance_locators = (By.XPATH, "//span[text()='Performance']")
    dashboard_menu_locators = (By.XPATH, "//span[text()='Dashboard']")

#Locators for creating new user
    create_user_add_button = (By.XPATH, "//button[@type='button']//i[contains(@class,'plus')]")
    user_role = (By.XPATH, "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    status_dropdown = (By.XPATH, "//label[text()='Status']/../following-sibling::div//div[contains(@class, 'oxd-select-text-input')]")
    employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    employee_first_option = (By.XPATH, "//div[@role='listbox']//div[@class='oxd-autocomplete-option']/span")
    create_username = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
    create_password = (By.XPATH, "//label[text()='Password']/../following-sibling::div/input")
    create_confirm_password = (By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div/input")
    create_user_save_button = (By.XPATH, "//button[text()=' Save ']")

 #Locators for links in My info
    personal_details = (By.XPATH, "//a[text()='Personal Details']")
    contact_details = (By.XPATH, "//a[text()='Contact Details']")
    emergency_contact = (By.XPATH, "//a[text()='Emergency Contacts']")
    dependent = (By.XPATH, "//a[text()='Dependents']")
    immigration = (By.XPATH, "//a[text()='Immigration']")
    job = (By.XPATH, "//a[text()='Job']")
    salary = (By.XPATH, "//a[text()='Salary']")
    reportto = (By.XPATH, "//a[text()='Report-to']")
    qualification = (By.XPATH, "//a[text()='Qualifications']")
    membership = (By.XPATH, "//a[text()='Memberships']")

 #Search user
    search_text = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input")
    search_btn = (By.XPATH, "//button[@type='submit']")
    admin_table_rows = ("xpath", "//div[@class='oxd-table-body']//div[@role='row']")

 # Leave Page Locators
    leave_locators = (By.XPATH, "//span[text()='Leave']")
    assign_leave_menu = (By.XPATH, "//a[text()='Assign Leave']")

    employee_name_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
    employee_autosuggest = (By.XPATH, "//div[@role='option']")

    leave_type_dropdown = (By.XPATH, "//div[text()='-- Select --']")
    leave_type_option = (By.XPATH, "//span[text()='CAN - Personal']")

    date_inputs = (By.XPATH, "//input[@placeholder='yyyy-dd-mm']")

    assign_leave_submit = (By.XPATH, "//button[@type='submit']")
    leave_success_toast = (By.XPATH, "//p[contains(text(),'Successfully')]")

    confirm_assign_button = (By.XPATH, "//button[normalize-space()='Confirm']")

 #Locators for claim
    left_side_menu_claim = (By.XPATH, "//span[text()='Claim']")
    claim_assign_heading = (By.XPATH, "//a[text()='Assign Claim']")
    claim_emp_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    claim_emp_suggestion = (By.XPATH, "//div[@role='listbox']//span")
    claim_event = (By.XPATH, "//label[text()='Event']/following::div[contains(@class,'oxd-select-text')][1]")
    claim_event_item = (By.XPATH, "//div[@role='option']//span[normalize-space()='Accommodation']")

    claim_currency = (By.XPATH, "//label[text()='Currency']/following::div[contains(@class,'oxd-select-text')][1]")
    claim_currency_selector = (By.XPATH, "//div[@role='option']//span[normalize-space()='Indian Rupee']")
    remark_textbox = (By.XPATH, "//label[text()='Remarks']/following::textarea")
    create_claim_btn = (By.XPATH, "//button[@type='submit']")

    claim_details_page = (By.XPATH, "//h6[normalize-space()='Claim']")
    claim_add_button = (By.XPATH, "//button[normalize-space()='Add']")

    add_expense = (By.XPATH, "//p[text()='Add Expense']")
    expense_type = (By.XPATH, "//label[text()='Expense Type']/following::input[1]")
    add_expense_date = (By.XPATH, "//input[@placeholder='yyyy-dd-mm']")
    add_expense_amount = (By.XPATH, "//label[text()='Amount']/following::input[1]")
    add_expense_note = (By.XPATH, "//label[text()='Note']/following::textarea")
    add_expense_submit_btn = (By.XPATH, "//button[normalize-space()='Save']")