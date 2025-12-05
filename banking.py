class BankingBot:
    def __init__(self):
        self.balance = 0
        self.history = []

    def check_balance(self):
        print(f"\n Current Balance: ₹{self.balance}")
        self.history.append("Checked Balance")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        self.history.append(f"Deposited ₹{amount}")
        print(f" ₹{amount} deposited successfully!")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew ₹{amount}")
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient balance!")
            self.history.append("Failed withdrawal attempt")

    def show_history(self):
        print("\n Transaction History:")
        if not self.history:
            print("No transactions yet.")
        else:
            for item in self.history:
                print(f"- {item}")


def main():
    bot = BankingBot()
    while True:
        print("\n===== Banking Bot Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            bot.check_balance()
        elif choice == "2":
            bot.deposit()
        elif choice == "3":
            bot.withdraw()
        elif choice == "4":
            bot.show_history()
        elif choice == "5":
            print(" Thank you for using the Banking Bot!")
            break
        else:
            print(" Invalid choice, try again!")


if __name__ == "__main__":
    main()
