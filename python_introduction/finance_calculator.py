interest_rate = 0.05
number_of_months = 12

income_input = input("Enter your monthly income: ")
monthly_income = float(income_input)


expenses_input = input("Enter your total monthly expenses: ")
monthly_expenses = float(expenses_input)

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * number_of_months
total_interest = annual_savings * interest_rate

projected_annual_savings = annual_savings + total_interest

print(f"Your Monthly Savings are: ${monthly_savings}")
print(f"Your Projected Annual Savings after interest are: ${projected_annual_savings}")