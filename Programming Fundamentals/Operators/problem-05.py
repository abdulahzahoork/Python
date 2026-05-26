# Q5. Write a program that compares two numbers entered by the user and prints which one is greater, or if they are equal.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 > num2:
        print(f"{num1} is greater")
    elif num2 > num1:
        print(f"{num2} is greater")
    else:
        print("Both numbers are equal")

except ValueError:
    print("Please enter valid numbers!")