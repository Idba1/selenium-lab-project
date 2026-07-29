# SauceDemo Test Automation Framework

A Selenium Test Automation Framework built with **Python**, **Pytest**, and **Page Object Model (POM)** to automate the SauceDemo website.

---

# Project Overview

This project automates the core functionalities of the SauceDemo web application.

Framework Features:

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Explicit Waits
- Custom Selenium Wrapper
- Logging
- Screenshot on Failure
- HTML Test Report
- Config Management

---

# Project Structure

```
selenium-lab-project/
│
├── config/
│   └── config.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests/
│   ├── login_test.py
│   ├── inventory_test.py
│   ├── cart_test.py
│   ├── checkout_test.py
│   └── checkout_validation_test.py
│
├── utilities/
│   ├── logger.py
│   └── screenshot.py
│
├── wrappers/
│   └── selenium_wrapper.py
│
├── screenshots/
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python 3.13
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Pytest HTML
- Logging
- Page Object Model

---

# Framework Design

The framework follows the **Page Object Model (POM)** architecture.

Every webpage has its own Page Class.

Example:

```
Login Page
↓

Inventory Page
↓

Cart Page
↓

Checkout Page
↓

Overview Page
↓

Complete Page
```

This makes the framework:

- Reusable
- Easy to maintain
- Scalable
- Cleaner code

---

# Implemented Features

## Phase 1 – Login Module

### Positive Test Cases

- Valid Login
- Logout

### Negative Test Cases

- Invalid Username
- Invalid Password
- Locked User
- Empty Username
- Empty Password
- Empty Username & Password

---

## Phase 2 – Inventory & Cart

Implemented:

- Add Single Product
- Add Multiple Products
- Remove Product
- Cart Badge Verification
- Open Cart
- Product Visible in Cart
- Continue Shopping
- Remove Product from Cart

---

## Phase 3 – Checkout

Implemented:

### Checkout Process

- Checkout Information
- Checkout Overview
- Finish Order
- Order Completion

### Checkout Validation

- Empty First Name
- Empty Last Name
- Empty Postal Code
- Cancel Checkout
- Back Home *(Currently under verification)*

---

# Selenium Wrapper

A reusable wrapper class has been implemented to avoid duplicate Selenium code.

Methods:

- click()
- type()
- get_text()
- is_displayed()
- is_element_present()

Benefits:

- Cleaner code
- Less duplication
- Easy maintenance

---

# Logging

Custom logging is implemented.

Example:

```
Login process started

Entering username

Entering password

Clicking Login button

Login process completed
```

---

# Screenshot on Failure

Whenever a test fails,

the framework automatically captures a screenshot.

Location:

```
screenshots/
```

Example:

```
test_logout.png
```

---

# Explicit Wait

Framework uses Explicit Wait for synchronization.

Example:

```python
WebDriverWait(driver,10).until(
    EC.element_to_be_clickable(locator)
)
```

---

# Test Execution

Run all tests

```bash
pytest -v
```

Run specific file

```bash
pytest tests/login_test.py -v
```

Run checkout tests

```bash
pytest tests/checkout_test.py -v
```

Run validation tests

```bash
pytest tests/checkout_validation_test.py -v
```

---

# Generate HTML Report

```bash
pytest --html=reports/report.html
```

---

# Current Automation Coverage

| Module | Status |
|---------|--------|
| Login | ✅ Completed |
| Logout | ✅ Completed |
| Inventory | ✅ Completed |
| Cart | ✅ Completed |
| Checkout Flow | ✅ Completed |
| Checkout Validation | ✅ Mostly Completed |
| Screenshot on Failure | ✅ Completed |
| Logging | ✅ Completed |
| Selenium Wrapper | ✅ Completed |

---

# Future Enhancements

The following features are planned for future implementation:

- Product Sorting Tests
- Product Details Verification
- Social Media Links Validation
- Footer Verification
- About Page Navigation
- Reset App State
- Menu Verification
- Cross Browser Testing
- Parallel Execution
- Data Driven Testing
- Excel Integration
- Jenkins CI/CD Integration
- GitHub Actions CI
- Docker Support
- Allure Reporting
- Headless Execution

---

# Best Practices Followed

- Page Object Model (POM)
- Reusable Components
- Explicit Waits
- Config Driven Data
- Clean Code
- Logging
- Screenshot on Failure
- Modular Design
- Reusable Wrapper Methods

---

# Author

**Monira Islam**

B.Sc. in Software Engineering

Daffodil International University

---

# Project Status

Current Progress:

✅ Login Module Completed

✅ Inventory Module Completed

✅ Cart Module Completed

✅ Checkout Module Completed

🟡 Checkout Validation (Final Verification Remaining)

⏳ Phase 4 (Product Sorting & Advanced Automation) — Planned

---

Thank you for visiting this project.
