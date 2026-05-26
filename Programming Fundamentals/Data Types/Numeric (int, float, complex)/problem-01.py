# Write a program that takes two integers and prints their sum, difference, product, quotient, and remainder.

try: 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Sum: {a+b}")
    print(f"Difference: {a-b}")
    print(f"Product: {a*b}")
    if b!=0:
        print(f"Quotient: {a//b}")
        print(f"Remainder: {a%b}")
    else:
        print("Math Error! Division by 0 is not possible.")
except ValueError: 
    print("Please enter valid numbers!")
    