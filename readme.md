<h1>Orange HRM Automation Framework</h1>

<h3>Overview</h3>
This repository contains a <b>Selenium automation framework</b> for the <b>Orange HRM</b> web application built using <b>Python, Pytest, and Allure Reports</b>.
The framework follows the <b>Page Object Model (POM)</b> design pattern and demonstrates real‑world automation practices.
<br/>
Web Application: <u>https://opensource-demo.orangehrmlive.com/web/index.php/auth/login</u>
<br/><br/>
<h3>Table of Contents</h3>
Tech Requirement<br/>
Project Structure<br/>
Pre-requisites<br/>
Verify<br/>
Install Dependencies<br/>
Project Description<br/>

<h4>Tech Requirement</h4>
&bull; <b>Programming Language:</b> Python<br/>
&bull; <b>Automation Tool:</b> Selenium WebDriver<br/>
&bull; <b>Test Framework:</b> Pytest<br/>
&bull; <b>Design Patten:</b> Page Object Model (POM)<br/>
&bull; <b>Reporting:</b> Allure Report<br/>
&bull; <b>Browser:</b> Firefox<br/>
&bull; <b>IDE:</b> PyCharm<br/>
<br/><br/>
<h4>Project Structure</h4>
---
C:<br/>
│   conftest.py							# Pytest fixtures & hooks<br/>
│   README.md							# Project documentation<br/>
│   read_data_from_excel.py				# Utility file (Excel reader)<br/>
│   test_hrm.py							#Test cases<br/>
│   __init__.py<br/>
│   README.md<br/>
│               
├───pages								# Page Object classes<br/>
│   	│   assign_claim.py<br/>
│   	│   assign_leave.py<br/>
│   	│   create_user.py<br/>
│   	│   explicit_waits.py<br/>
│   	│   homepage.py<br/>
│   	│   locators.py<br/>
│   	│   pim.py<br/>
│   	│   search_user.py<br/>
│   	│   __init__.py<br/>
│   	│              <br/>
├───test_data<br/>
       | credentials.xlsx  				# Excel file for Data Driven Testing Framework  
|───utils
       | autosuggets.py
       | config.ini					# Application & environment configuration<br/>
---

<h4>Prerequisites</h4>
&bull; Python 3.10 or above<br/>
&bull; Firefox<br/>
&bull; Allure Comandline<br/>
&bull; Git<br/>

<h4>Verify</h4>

python --version<br/>
pip --version<br/>
allure --version<br/>

<h4>Install Dependencies</h4>

pip install -r requirements.txt

<h4>Project Description:</h4>

The automation is designed to simulate real-world usage patterns such as form interactions, menu navigation, and authentication validation. Tests will be executed across multiple browsers to ensure cross-browser compatibility. The system will interact with various web elements and execute test cases covering both positive and negative scenarios.

