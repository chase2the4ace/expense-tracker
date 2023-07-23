from Expense import Expense


def main():
    print(f"Running Expense Tracker")
    expense_file_path = "expenses.csv"

# Get user info for expenses
    expense = get_user_expense()
    budget = 2000

# Write the expenses to a file
    save_user_expense_to_file(expense, expense_file_path)

# Read file and summarize expenses
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print(f"Getting user expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "Food", "Home", "Work", "Fun", "Miscellaneous"
        ]

    while 1:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        selected_index = int(input("Enter category number: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                category=selected_category, name=expense_name, amount=expense_amount
                )

            return new_expense

        else:
            print("Invalid category, please try again!")


def save_user_expense_to_file(expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.category}, {expense.amount}, {expense.name}\n")


def summarize_expenses(expense_file_path, budget):
    print(f"Summarizing expenses")  
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_category, expense_amount, expense_name = line.strip().split(",")
            line_expense = Expense(category=expense_category, amount=float(expense_amount), name=expense_name)
            expenses.append(line_expense)

    amount_by_category = {}

    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses by category: ")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent ${total_spent} this month!")

    remaining_budget = budget - total_spent
    print(f"Budget remaining: {remaining_budget:.2f}")


if __name__ == "__main__":
    main()
