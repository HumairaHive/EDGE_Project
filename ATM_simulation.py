class ATMSimulation:
    def __init__(self):
        self.balance = 0.0

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit_money(self):
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Deposit amount must be positive.")
            else:
                self.balance += amount
                print(f"Successfully deposited ${amount:.2f}. Your new balance is ${self.balance:.2f}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw_money(self):
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > self.balance:
                print("Insufficient balance. Transaction failed.")
            else:
                self.balance -= amount
                print(f"Successfully withdrew ${amount:.2f}. Your new balance is ${self.balance:.2f}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def run(self):
        while True:
            print("\n--- ATM Simulation ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATMSimulation()
    atm.run()