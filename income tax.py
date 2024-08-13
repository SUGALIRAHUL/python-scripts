def calculate_income_tax(income):
    tax = 0
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 10
    else:
        tax = 10000 * 0.1 + (income - 20000) * 20
    return tax

income = float(input("Enter the taxable income: $"))
income_tax = calculate_income_tax(income)
print("Income tax payable: $", income_tax)
