#initial balance
account_balance = 0.0

#Account details
account_details = {
    "1": {"account_number": 1234567890, "account_balance": account_balance, "transaction_history": []},
    "2": {"account_number": 987654321, "account_balance": account_balance, "transaction_history": []},
    "3": {"account_number": 1122334455, "account_balance": account_balance, "transaction_history": []},
    "4": {"account_number": 5566778899, "account_balance": account_balance, "transaction_history": []},
    "5": {"account_number": 9988776655, "account_balance": account_balance, "transaction_history": []},

}

#All accounts.
accounts = {
    1234567890: account_details["1"],
    987654321: account_details["2"],
    1122334455: account_details["3"],
    5566778899: account_details["4"],
    9988776655: account_details["5"],
}

#Function to create a unique account number and store account details
def create_account(account_number, initial_balance):
    if account_number in accounts:
        print("Account already exists.")
    else:
        accounts[account_number] = {
            "account_number": account_number,
            "account_balance": initial_balance,
            "transaction_history": []
        }
        print(f"Account {account_number} created successfully.")


     

#define function to deposit money into an account, updating the balance and transaction history
def deposit(account_number, amount):
    if account_number in accounts:
        accounts[account_number]["account_balance"] += amount
        accounts[account_number]["transaction_history"].append(f"Deposited: {amount}")
        print(f"You have successfully deposited £{amount} into account {account_number}. Your new balance is: {accounts[account_number]['account_balance']}")
    else:
        print("Account not found.")


#Function to withdraw money from an account, updating the balance and transaction history
def withdraw(account_number, amount):
    if account_number in accounts:
        if accounts[account_number]["account_balance"] >= amount:
            accounts[account_number]["account_balance"] -= amount
            accounts[account_number]["transaction_history"].append(f"Withdrawn: {amount}")
            print(f"You have successfully withdrawn £{amount} from account {account_number}. Your new balance is: {accounts[account_number]['account_balance']}")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")


#Function to view account balance 
def view_balance(account_number):
    if account_number in accounts:
        print("\n--- Account Balance ---")
        print(f"Account Number: {accounts[account_number]['account_number']}")
        print(f"Account Balance: £{accounts[account_number]['account_balance']:.2f}")
    else:
        print("Account not found.")
        


#Function to view transaction history
def view_transaction_history(account_number):
    if account_number in accounts:
        print("\n--- Transaction History ---")
        print(f"Account Number: {accounts[account_number]['account_number']}")
        for transaction in accounts[account_number]["transaction_history"]:
            print(transaction)
    else:
        print("Account not found.")


#User Interface: Create a simple command-line interface to interact with the banking system.
#Allow users to create accounts, deposit, withdraw, view balance, and transaction history.
def main():
    while True:
        print("\n--- Welcome to SecureSave Banking System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = int(input("Enter account number: "))
            initial_balance = float(input("Enter initial balance: "))
            create_account(account_number, initial_balance)
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            deposit(account_number, amount)
        elif choice == "3":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            withdraw(account_number, amount)
        elif choice == "4":
            account_number = int(input("Enter account number: "))
            view_balance(account_number)
        elif choice == "5":
            account_number = int(input("Enter account number: "))
            view_transaction_history(account_number)
        elif choice == "6":
            print("Thank you for using SecureSave Banking System, see you next time.")
            break
        else:
            print("Invalid choice. Please try again.")
                        
            # Call the main function to start the program
if __name__ == "__main__":
                main()