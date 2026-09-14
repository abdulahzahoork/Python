# Your task:
# Ask the user for two numbers
# Try to divide the first number by the second
# If the division works, print the result
# If any error happens, print a friendly message instead of crashing

try: 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a/b
    print(f"{a} / {b} = {c}")
except: 
    print("Oops! An Error occured.")