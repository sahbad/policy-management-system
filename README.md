# Policy Management System

**Course:** BAN 6420 – Programming in R & Python
**Module:** 3 – Milestone Assignment 1
**Author:** Adebowale Saheed Badru
**Institution/Program:** Nexford University/Master of Science, Data Analytics
**Date:** October 2025

---

## 📘 Project Overview

The **Policy Management System** is a Python-based application that simulates how an insurance company manages policyholders, insurance products, and payments. It was developed using object-oriented programming (OOP) principles to demonstrate the use of classes, methods, and interactions between different objects.

This system allows the company to:

* Register, suspend, and reactivate policyholders
* Create, update, and suspend insurance products
* Process payments with automated reminders and penalty calculations
* Display account details for each policyholder

---

## 🧩 Project Structure

```bash
policy_mgmt/
│
├── product.py          # Defines the Product class and handles product CRUD
├── policyholder.py     # Defines the Policyholder class and manages registration/lifecycle
├── payment.py          # Handles payment processing, reminders, and penalties
├── main.py             # Demonstrates functionality with sample data
└── README.md           # Documentation and instructions
```

---

## 🏗️ How It Works

### Product Management (`product.py`)

* Create and manage insurance products with unique codes, names, and premiums.
* Update product information such as premium changes.
* Suspend or reactivate products.

### Policyholder Management (`policyholder.py`)

* Register new policyholders.
* Suspend, reactivate, or cancel accounts.
* Assign one or more insurance products to each policyholder.

### Payment Management (`payment.py`)

* Record and track payments.
* Send payment reminders (console simulation).
* Apply penalties for late payments.

> **Penalty Model:** 0.5% of the payment amount per day late, capped at 15% total.

### Demonstration (`main.py`)

* Creates sample products and policyholders.
* Demonstrates registration, product updates, and payment processing.
* Displays output in the terminal with details for each policyholder.

---

## ⚙️ Installation and Setup

### Requirements

* Python 3.10 or higher
* (Optional) Visual Studio Code for editing and running the project

### Steps

1. Create a folder named `policy_mgmt`.
2. Copy all `.py` files and `README.md` into the folder.
3. Open a terminal in the project directory.
4. Run the main program:

   ```bash
   python main.py        # macOS/Linux
   # OR
   py main.py            # Windows
   ```

When you run it, you’ll see printed output showing two sample policyholders, their assigned products, and payment details (including penalties if applicable).

---

## 💻 Example Output

```bash
--- Policyholder ---
PH1001 | Adaeze Okoye | REGISTERED | Products: BAS01
  - BAS01 (since 2025-10-24)
Last payment: 15000.0 | penalty: 0.0

--- Policyholder ---
PH1002 | Femi Badru | REGISTERED | Products: FAM10
  - FAM10 (since 2025-10-24)
Last payment: 40000.0 | penalty: 3000.0
```

*(Exact values depend on your chosen penalty settings and due dates.)*

---

## 🧠 Personalization and Notes

* Penalty policy customized to **0.5% per day late**, capped at **15% total**.
* The rate was selected to promote fairness and timely payments.
* Product codes and names can easily be changed to reflect real insurance offerings.
* The code was written manually and tested step-by-step to ensure readability and correctness.

---

## 🧪 Testing Tips

* Modify `late_due` in `main.py` to test different delay periods.
* Switch `penalty_policy` between `flat` and `percent` to compare logic.
* Add a third policyholder to test scalability.
* Suspend and reactivate products to verify state changes.

---
