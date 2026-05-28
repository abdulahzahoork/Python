# 1. Positive, Negative, or Zero
# Write a program that takes a number and prints whether it is positive, negative, or zero.

try:
    num = int(input("Enter a number: "))

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else: 
        print("Zero")
except ValueError:
    print("Please enter a valid number!")