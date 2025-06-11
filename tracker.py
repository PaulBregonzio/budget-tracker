import os

BALANCE_FILE = "balance.txt"

def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as file:
            return float(file.read())
    else:
        return 0.0

def save_balance(balance):
    with open(BALANCE_FILE, "w") as file:
        file.write(str(balance))

def show_menu():
    print("\n===== Budget Tracker =====")
    print("1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. Exit")

def main():
    balance = load_balance()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            amount = float(input("Enter income amount: $"))
            balance += amount
            save_balance(balance)
            print(f"Income added. New balance: ${balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter expense amount: $"))
            balance -= amount
            save_balance(balance)
            print(f"Expense added. New balance: ${balance:.2f}")

        elif choice == "3":
            print(f"Current balance: ${balance:.2f}")

        elif choice == "4":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1–4.")

if __name__ == "__main__":
    main()
