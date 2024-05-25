################################
# Sonam Choki
# 1ME
# 02230272
################################
# REFERENCES
# https://www.scribd.com/document/457278570/Code-for-Bank-Application
#https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
################################
# Read the input.accounts.txt
import random

class Account:
    def __init__(self, account_number, password, balance=0):
        self.account_number = account_number
        self.password = password
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. Current balance: {self.balance}"
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal successful. Current balance: {self.balance}"
        else:
            return "Insufficient funds."
    
    def delete_account(self):
        self.account_number = None
        self.password = None
        self.balance = None
        return "Account deleted successfully."


class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_type):
        account_number = random.randint(100000, 999999)
        password = "password"  # Default password
        account = Account(account_number, password)
        self.accounts[account_number] = account
        self.save_accounts()
        return f"Account created successfully. Account number: {account_number}, Default password: {password}"
    
    def save_accounts(self):
        with open("accounts.txt", "w") as file:
            for account_number, account in self.accounts.items():
                file.write(f"{account_number},{account.password},{account.balance}\n")
    
    def load_accounts(self):
        try:
            with open("accounts.txt", "r") as file:
                for line in file:
                    account_number, password, balance = line.strip().split(",")
                    balance = float(balance)
                    account = Account(int(account_number), password, balance)
                    self.accounts[int(account_number)] = account
        except FileNotFoundError:
            # Create the file if it doesn't exist
            open("accounts.txt", "w").close()
    
    def login(self, account_number, password):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.password == password:
                return account
            else:
                return "Incorrect password."
        else:
            return "Account does not exist."
    
    def transfer_money(self, sender_account_number, receiver_account_number, amount):
        if sender_account_number in self.accounts and receiver_account_number in self.accounts:
            sender_account = self.accounts[sender_account_number]
            receiver_account = self.accounts[receiver_account_number]
            if sender_account.balance >= amount:
                sender_account.balance -= amount
                receiver_account.balance += amount
                self.save_accounts()
                return "Transfer successful."
            else:
                return "Insufficient funds."
        else:
            return "Invalid sender or receiver account number."


def main():
    bank = Bank()
    bank.load_accounts()

    while True:
        print("\nWelcome to the Banking Application")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_type = input("Enter account type (Personal/Business): ").capitalize()
            print(bank.create_account(account_type))

        elif choice == "2":
            account_number = int(input("Enter account number: "))
            password = input("Enter password: ")
            account = bank.login(account_number, password)
            if isinstance(account, Account):
                print(f"Login successful. Account balance: {account.balance}")
                while True:
                    print("\nAccount Menu")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer Money")
                    print("4. Delete Account")
                    print("5. Logout")

                    account_choice = input("Enter your choice: ")

                    if account_choice == "1":
                        amount = float(input("Enter deposit amount: "))
                        print(account.deposit(amount))

                    elif account_choice == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        print(account.withdraw(amount))

                    elif account_choice == "3":
                        receiver_account_number = int(input("Enter receiver's account number: "))
                        amount = float(input("Enter transfer amount: "))
                        print(bank.transfer_money(account.account_number, receiver_account_number, amount))

                    elif account_choice == "4":
                        confirmation = input("Are you sure you want to delete your account? (yes/no): ").lower()
                        if confirmation == "yes":
                            print(account.delete_account())
                            del bank.accounts[account_number]
                            bank.save_accounts()
                            break

                    elif account_choice == "5":
                        break

                    else:
                        print("Invalid choice.")

            else:
                print(account)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()