# 💰 SecureSave Banking System

A simple command-line banking system built in Python for managing account operations such as deposits, withdrawals, and balance inquiries, along with maintaining a transaction history.

---

## 🏦 Business Introduction

SecureSave Bank is a newly established financial institution aiming to provide its customers with a secure and efficient way to manage their money. As part of its initial service offerings, the bank requires a lightweight system to handle core banking operations:

- Creating accounts  
- Depositing and withdrawing funds  
- Checking account balances  
- Viewing transaction history  

---

## ❗ Detailed Challenges

The system must be able to:

- ✅ Create new customer accounts with unique account numbers and initial balances  
- ✅ Process deposits and update account balances, while recording transactions  
- ✅ Process withdrawals, ensuring sufficient funds and recording the transaction  
- ✅ Allow customers or staff to check the balance of an account  
- ✅ Provide a full transaction history (deposits and withdrawals) per account  

---

## 💡 Proposed Solution

SecureSave Bank proposes the development of a **Python-based CLI application** to manage customer accounts. This lightweight system will:

- Store account data in memory during runtime
- Provide a menu-driven interface to perform operations
- Use standard Python data structures such as dictionaries and lists
- Demonstrate core programming concepts: functions, loops, conditionals, and error handling

---

## 🛠 Features

- 🆕 Create new bank accounts  
- 💰 Deposit funds  
- 💸 Withdraw funds  
- 🧾 View current account balance  
- 📜 View transaction history  
- 🧑‍💼 Preloaded with five default accounts  

---

## 🧩 Implementation Plan

1. **Define Data Structures**  
   Use dictionaries to store account details (`account_number`, `account_balance`, `transaction_history`) and a main dictionary to manage all accounts.

2. **Account Creation**  
   Implement a function to create new accounts with unique numbers and initial balances.

3. **Deposit Functionality**  
   Develop a function to process deposits, update balances, and record transactions.

4. **Withdrawal Functionality**  
   Implement logic to process withdrawals, check for sufficient funds, and log transactions.

5. **Balance Inquiry**  
   Provide a function to retrieve and display a specific account’s balance.

6. **Transaction History Viewing**  
   Implement functionality to display all past transactions for a given account.

7. **User Interface (CLI)**  
   Create an interactive text-based menu using loops and conditionals to guide the user through all available operations.

8. **Basic Error Handling**  
   Handle invalid account numbers and insufficient fund scenarios gracefully.

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.x installed on your machine

### ▶️ Running the Program

```bash
python banking_system.py
