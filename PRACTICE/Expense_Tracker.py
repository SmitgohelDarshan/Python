expenses = [] # list of expense dictionaries
print("Welcome to Expense Tracker 💸")

while True:
    print("\n======= MENU =======")
    print("1 Add Expense")
    print("2 View All Expenses")
    print("3 View Total Spending")
    print("4 View Spending by Category")
    print("5 Exit")
    print("=====================")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category (Food, Travel, Shopping, etc): ")

        description = input("Enter short description: ")
        amount = float(input("Enter amount (₹): "))
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        print("\nExpense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("\n No expenses recorded yet.")
        else:
            print("\n--- All Expenses ---")
        i = 1
        for e in expenses:
            print(f"{i}. {e['date']} | {e['category']} | {e['description']} | ₹{e['amount']}")
            i += 1
        print("---------------------")

    elif choice == "3":
        total = 0
        for e in expenses:
            total += e["amount"]

        print(f"\nTotal Spending = ₹{total}")    

    elif choice == "4":
        if len(expenses) == 0:
            print("\nNo expenses recorded yet.")
        else:
            summary = {}  # Create empty dictionary to store category totals
            for e in expenses:
                cat = e["category"]  # Get the category of current expense
                if cat in summary:
                    summary[cat] += e["amount"]  # Add amount to existing category
                else:
                    summary[cat] = e["amount"]  # Create new entry with this amount

            print("\nSpending by Category:")    
            for cat, amt in summary.items():
                print(f"{cat}: ₹{amt}")

    elif choice == "5":
        print("\nThanks for using Expense Tracker! Bye!")
        break

    else:
        print("\nInvalid choice. Please try again.")        