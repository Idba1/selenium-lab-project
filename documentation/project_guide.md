# SauceDemo Automation Framework - Project Guide

This document explains how to set up, run, understand, and explain the project during interviews or academic demonstrations.

---

# Project Objective

The goal of this project is to automate the SauceDemo website using Selenium WebDriver with Python while following industry-standard automation practices.

The project demonstrates:

- Selenium Automation
- Python
- Pytest
- Page Object Model (POM)
- Explicit Wait
- Logging
- Screenshot on Failure
- Test Automation Best Practices

---

# Prerequisites

Before running the project, install:

- Python 3.10+
- Google Chrome
- Git
- VS Code (Recommended)

Verify installation:

```bash
python --version
```

```bash
git --version
```

---

# Clone the Project

```bash
git clone https://github.com/Idba1/selenium-pom-automation-framework

cd selenium-lab-project
```

Example:

```bash
git clone https://github.com/Idba1/selenium-pom-automation-framework
```

---

# Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

CMD

```bash
venv\Scripts\activate
```

Git Bash

```bash
source venv/Scripts/activate
```

PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

If activated successfully:

```
(venv)
```

will appear before your terminal.

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run All Tests

```bash
pytest -v
```

---

# Run Login Tests

```bash
pytest tests/login_test.py -v
```

---

# Run Inventory Tests

```bash
pytest tests/inventory_test.py -v
```

---

# Run Cart Tests

```bash
pytest tests/cart_test.py -v
```

---

# Run Checkout Tests

```bash
pytest tests/checkout_test.py -v
```

---

# Generate HTML Report

```bash
pytest --html=reports/report.html
```

After execution,

open

```
reports/report.html
```

using any browser.

---

# Folder Structure

```
config/
```

Contains project configuration.

Example:

- URL
- Username
- Password
- Wait Time

---

```
pages/
```

Contains Page Object classes.

Each webpage has one class.

Example

```
LoginPage

InventoryPage

CartPage

CheckoutPage
```

---

```
tests/
```

Contains all automation test cases.

Example

```
login_test.py

inventory_test.py

cart_test.py

checkout_test.py
```

---

```
utilities/
```

Contains reusable utilities.

Example

```
logger.py

screenshot.py
```

---

```
wrappers/
```

Contains reusable Selenium wrapper methods.

Example

```
click()

type()

get_text()

is_displayed()

is_element_present()
```

---

# Automation Flow

```
Launch Browser
        ↓
Open SauceDemo
        ↓
Login
        ↓
Inventory
        ↓
Cart
        ↓
Checkout
        ↓
Overview
        ↓
Finish
        ↓
Complete
        ↓
Close Browser
```

---

# Why Page Object Model?

Without POM:

- Duplicate locators
- Duplicate code
- Difficult maintenance

With POM:

- Reusable code
- Easy maintenance
- Clean framework
- Better scalability

---

# Why Selenium Wrapper?

Instead of writing

```python
driver.find_element(...).click()
```

again and again,

we simply write

```python
self.click(locator)
```

Advantages:

- Cleaner code
- Less duplication
- Easy debugging

---

# Why Explicit Wait?

Instead of

```python
time.sleep(5)
```

we use

```python
WebDriverWait
```

Benefits:

- Faster execution
- Stable automation
- Less flaky tests

---

# Logging

Every important action is logged.

Example:

```
Login Started

Entering Username

Entering Password

Click Login

Login Completed
```

This helps identify failures easily.

---

# Screenshot on Failure

Whenever any test fails,

Pytest automatically captures a screenshot.

Location

```
screenshots/
```

Example

```
test_login_failed.png
```

---

# Current Test Coverage

## Login

✓ Valid Login

✓ Logout

✓ Invalid Login

✓ Empty Username

✓ Empty Password

✓ Locked User

---

## Inventory

✓ Add Product

✓ Remove Product

✓ Multiple Products

✓ Cart Badge

✓ Open Cart

---

## Cart

✓ Product Visible

✓ Continue Shopping

✓ Remove Product

---

## Checkout

✓ Checkout Information

✓ Checkout Validation

✓ Finish Order

✓ Order Complete

---

# Common Interview Questions

## What is Selenium?

Selenium is an open-source browser automation tool used for testing web applications.

---

## Why Pytest?

Pytest provides:

- Simple syntax
- Assertions
- Fixtures
- HTML Reports
- Plugins

---

## What is Page Object Model?

POM is a design pattern where every webpage is represented by a separate class containing locators and methods.

---

## Why use BasePage?

BasePage contains common reusable methods inherited by all page classes.

---

## Why Selenium Wrapper?

To reduce duplicate Selenium code and improve maintainability.

---

## Difference Between Implicit Wait and Explicit Wait

Implicit Wait

- Applied globally
- Waits for all elements

Explicit Wait

- Waits for a specific condition
- Faster
- More reliable

---

## Why Logging?

Logging helps identify:

- Which step failed
- Which method executed
- Execution sequence

---

## Why Screenshot?

Screenshots provide visual evidence when a test fails, making debugging easier.

---

## What is Fixture?

A fixture is reusable setup and teardown code.

Example:

- Launch Browser
- Close Browser

---

## Why use WebDriver Manager?

No need to manually download ChromeDriver.

It automatically downloads the correct driver version.

---

## Why Config File?

Instead of hardcoding

- URL
- Username
- Password

everything is stored in one place.

---

# Best Practices Followed

- Page Object Model
- Reusable Methods
- Explicit Wait
- Config Driven Data
- Logging
- Screenshot on Failure
- Modular Framework
- Clean Folder Structure
- Maintainable Code

---

# Future Improvements

- Data Driven Testing
- Cross Browser Testing
- Parallel Execution
- Jenkins Integration
- GitHub Actions
- Docker
- Allure Report
- Headless Execution
- Excel Integration

---

# Author

Monira Islam

B.Sc. in Software Engineering

Daffodil International University

---

Happy Testing!
