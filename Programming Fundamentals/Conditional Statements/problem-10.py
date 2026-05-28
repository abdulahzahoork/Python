# 10. Tax Calculator
# Given an annual income, calculate tax based on brackets:

# Up to 10,000 → 0% tax
# 10,001–40,000 → 10% tax on the amount above 10,000
# 40,001–80,000 → 20% tax on the amount above 40,000
# Above 80,000 → 30% tax on the amount above 80,000

try: 
    income = float(input("Enter annual income: "))

    if income < 0:
        print("Income must be positive.")
    elif income <= 10000:
        tax = 0
    elif income <= 40000:
        tax = (income - 10000) * 0.10
    elif income <= 80000:
        tax = (30000 * 0.10) + (income - 40000) * 0.20
    else:
        tax = (30000 * 0.10) + (40000 * 0.20) + (income - 80000) * 0.30

    if income >= 0:
        print(f"Tax: {tax:.2f}")

except ValueError:
    print("Please enter valid input!")