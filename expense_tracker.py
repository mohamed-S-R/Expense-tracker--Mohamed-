
import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description=""):
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        for expense in self.expenses:
            print(expense)

    def category_summary(self, category):
        total = sum(e['amount'] for e in self.expenses if e.get('category') == category and isinstance(e.get('amount'), (int, float)))
        print(f"Total spent on {category}: {total}")

    def monthly_summary(self, month, year):
        total = 0
        for e in self.expenses:
            try:
                date_obj = datetime.strptime(e['date'], "%Y-%m-%d %H:%M:%S")
                if date_obj.month == month and date_obj.year == year and isinstance(e.get('amount'), (int, float)):
                    total += e['amount']
            except (ValueError, TypeError):
                continue
        print(f"Total expenses for {month}/{year}: {total}")

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            category = input("Enter category: ")
            tracker.category_summary(category)
        elif choice == '4':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            tracker.monthly_summary(month, year)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
