import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        
        self.expenses.append({"category": category, "amount": amount, "date": datetime.date.today()})

    def add_expenses(self, categories, amounts):
       
        if len(categories) != len(amounts):
            raise ValueError("Length of categories and amounts should match.")
        for category, amount in zip(categories, amounts):
            self.add_expense(category, amount)

    def get_monthly_summary(self):
        today = datetime.date.today()
        current_month = today.strftime("%B")
        monthly_expenses = [expense["amount"] for expense in self.expenses if expense["date"].strftime("%B") == current_month]
        total_expenses = sum(monthly_expenses)
        return {"month": current_month, "total_expenses": total_expenses}

    def get_category_wise_expenditure(self):
        category_wise_expenditure = {}
        for expense in self.expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category in category_wise_expenditure:
                category_wise_expenditure[category] += amount
            else:
                category_wise_expenditure[category] = amount
        return category_wise_expenditure


tracker = ExpenseTracker()

# Adding expenses
tracker.add_expenses(["Food", "Transport", "grocery"], [2000, 500, 1500])


print("Monthly Summary:", tracker.get_monthly_summary())


print("Category-wise Expenditure:", tracker.get_category_wise_expenditure())


    