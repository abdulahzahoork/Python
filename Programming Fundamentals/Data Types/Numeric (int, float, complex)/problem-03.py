# Find the greatest common divisor (GCD) of two integers without using any built-in function.

try: 
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
    while (b!=0):
        a, b = b, a%b
    print(f"GCD: {a}")
except ValueError: 
    print("Please enter valid input!")