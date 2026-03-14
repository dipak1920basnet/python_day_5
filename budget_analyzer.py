def main():
    income= 40000
    food_expense=3800 
    rent_expense= 15000
    transport_expense= 10000

    total_expense = calculate_total_expense(food_expense, rent_expense, transport_expense)
    savings = calculate_savings(income, total_expense)
    budget_evaluation = evaluate_budget(income, total_expense, savings)

    print(f"Total expense: {total_expense}")
    print(f"Savings {savings}")
    print(f"Budget evaluations: {budget_evaluation}")


def calculate_total_expense(b,c,d):
    return b+c+d

def calculate_savings(income, total_expense):
    return income - total_expense

def evaluate_budget(income, expense=0, savings=0):
    if expense >= income:
        return "Risky"
    else:
        return "Good"

if __name__ == "__main__":
    main()