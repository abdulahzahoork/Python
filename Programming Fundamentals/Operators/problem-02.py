# Q2. Write a program that takes a number and checks whether it is even or odd using the modulus (%) operator.

try: 
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Number is Even")
    else: 
        print("Number is Odd")
except ValueError:
    print("Please enter valid integer!")