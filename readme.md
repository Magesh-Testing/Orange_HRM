<h1>Orange HRM Automation Framework</h1>

<h3>Overview</h3>
This repository contains a <b>Selenium automation framework</b> for the <b>Orange HRM</b> web application built using <b>Python, Pytest, and Allure Reports</b>.
The framework follows the <b>Page Object Model (POM)</b> design pattern and demonstrates real‑world automation practices.
<br/>
Web Application: <u>https://opensource-demo.orangehrmlive.com/web/index.php/auth/login</u>
<br/><br/>
<h3>Table of Contents</h3>
Tech Requirement
Project Structure
Pre-requisites
Verify
Install Dependencies
Project Description

<h4>Tech Requirement</h4>
&bull; <b>Programming Language:</b> Python
&bull; <b>Automation Tool:</b> Selenium WebDriver
&bull; <b>Test Framework:</b> Pytest
&bull; <b>Design Patten:</b> Page Object Model (POM)
&bull; <b>Reporting:</b> Allure Report
&bull; <b>Browser:</b> Firefox
&bull; <b>IDE:</b> PyCharm
<br/><br/>
<h4>Project Structure</h4>
```

C:.
│   config.ini					# Application & environment configuration
│   conftest.py					# Pytest fixtures & hooks
│   README.md					# Project documentation
│   read_data_from_excel.py			# Utility file (Excel reader)
│   test_hrm.py					#Test cases
│   __init__.py
│   README.md
│               
├───pages					# Page Object classes
│   │   assign_claim.py
│   │   assign_leave.py
│   │   create_user.py
│   │   explicit_waits.py
│   │   homepage.py
│   │   locators.py
│   │   pim.py
│   │   search_user.py
│   │   __init__.py
│   │              
├───test_data
       credentials.xlsx  			# Excel file for Data Driven Testing Framework     


<h4>Prerequisites</h4>
&bull; Python 3.10 or above
&bull; Firefox
&bull; Allure Comandline
&bull; Git

<h4>Verify</h4>
```
python --version
pip --version
allure --version
```
<h4>Install Dependencies</h4>
```
pip install -r requirements.txt

<h4>Project Description:</h4>

The automation is designed to simulate real-world usage patterns such as form interactions, menu navigation, and authentication validation. Tests will be executed across multiple browsers to ensure cross-browser compatibility. The system will interact with various web elements and execute test cases covering both positive and negative scenarios.

