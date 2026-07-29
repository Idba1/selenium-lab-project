# 🛒 SauceDemo Test Automation Framework

A robust **Selenium Test Automation Framework** built using **Python**, **Pytest**, and the **Page Object Model (POM)** to automate the core functionalities of the SauceDemo web application.

This project demonstrates industry-standard automation practices such as reusable page objects, explicit waits, logging, screenshots on failure, and modular framework design.

---

## 📌 Project Overview

This framework automates the complete user journey of the SauceDemo application, including:

- 🔐 Login & Logout
- 🛍️ Product Inventory
- 🛒 Cart Management
- 💳 Checkout Process
- ✅ Order Completion
- ❌ Validation & Negative Test Cases

The framework is designed to be clean, scalable, reusable, and easy to maintain.

---

# 🚀 Technologies Used

- Python 3
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Pytest HTML Report
- Logging Module
- Page Object Model (POM)

---

# 📁 Project Structure

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
├── wrappers/
│   └── selenium_wrapper.py
│
├── utilities/
│   ├── logger.py
│   └── screenshot.py
│
├── screenshots/
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# ⚙️ Framework Architecture

This project follows the **Page Object Model (POM)** architecture.

```
Tests
   │
   ▼
Page Objects
   │
   ▼
Base Page
   │
   ▼
Selenium Wrapper
   │
   ▼
WebDriver
```

### Benefits

- Reusable Code
- Easy Maintenance
- Better Readability
- Scalable Automation Framework
- Reduced Code Duplication

---

# ✨ Features

- ✅ Page Object Model (POM)
- ✅ Custom Selenium Wrapper
- ✅ Explicit Waits
- ✅ Reusable Methods
- ✅ Screenshot on Failure
- ✅ Logging Support
- ✅ Configurable Test Data
- ✅ HTML Test Report
- ✅ Modular Framework
- ✅ Clean Folder Structure

---

# 🧪 Automated Test Scenarios

## 🔐 Login Module

### Positive Test Cases

- Valid Login
- Logout

### Negative Test Cases

- Invalid Username
- Invalid Password
- Locked User Login
- Empty Username
- Empty Password
- Empty Username & Password

---

## 🛍️ Inventory Module

- Add Single Product
- Add Multiple Products
- Remove Product
- Cart Badge Verification
- Open Cart

---

## 🛒 Cart Module

- Product Visible in Cart
- Remove Product from Cart
- Continue Shopping
- Checkout Navigation

---

## 💳 Checkout Module

### Checkout Flow

- Enter Customer Information
- Checkout Overview
- Finish Order
- Order Completion

### Validation Test Cases

- Empty First Name
- Empty Last Name
- Empty Postal Code
- Cancel Checkout
- Back Home Navigation

---

# 📸 Screenshot on Failure

Whenever a test fails, the framework automatically captures a screenshot.

```
screenshots/
```

This helps identify UI issues quickly during debugging.

---

# 📝 Logging

Every important automation step is logged.

Example:

```
Launching Chrome Browser

Login process started

Entering Username

Entering Password

Clicking Login

Login Completed

Opening Cart

Checkout Started

Closing Browser
```

Logging makes debugging much easier.

---

# ⏳ Synchronization

The framework uses **Explicit Waits** instead of `time.sleep()`.

Example:

```python
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(locator)
)
```

Benefits:

- Faster Execution
- More Stable Tests
- Better Reliability

---

# ▶️ Running the Project

## Clone the Repository

```bash
git clone https://github.com/Idba1/selenium-pom-automation-framework
```

Move into the project directory.

```bash
cd selenium-pom-automation-framework
```

---

## Create Virtual Environment

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

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Execute Tests

Run all tests

```bash
pytest -v
```

Run Login Tests

```bash
pytest tests/login_test.py -v
```

Run Inventory Tests

```bash
pytest tests/inventory_test.py -v
```

Run Cart Tests

```bash
pytest tests/cart_test.py -v
```

Run Checkout Tests

```bash
pytest tests/checkout_test.py -v
```

---

# 📊 Generate HTML Report

```bash
pytest --html=reports/report.html
```

After execution, open:

```
reports/report.html
```

in your browser.

---

# 📈 Current Automation Coverage

| Module | Status |
|---------|--------|
| Login | ✅ |
| Logout | ✅ |
| Inventory | ✅ |
| Cart | ✅ |
| Checkout | ✅ |
| Checkout Validation | ✅ |
| Screenshot on Failure | ✅ |
| Logging | ✅ |
| Selenium Wrapper | ✅ |

---

# 💡 Best Practices Followed

- Page Object Model (POM)
- Explicit Wait
- Reusable Components
- Clean Code Principles
- Config Driven Framework
- Logging
- Screenshot on Failure
- Modular Design
- Easy Maintenance

---

# 🔮 Future Enhancements

The following features can be added in future versions:

- Product Sorting Tests
- Data Driven Testing
- Cross Browser Testing
- Parallel Execution
- Jenkins CI/CD
- GitHub Actions
- Docker Integration
- Allure Reporting
- Headless Browser Execution
- Excel Data Integration

---

# 👩‍💻 Author

**Monira Islam**

B.Sc. in Software Engineering

Daffodil International University

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

Happy Testing! 🚀
