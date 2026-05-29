# Count to N — Ask the user for a number N, then print every integer from 1 to N.

try:
    num = int(input("Enter a number: "))
    if num < 1:
        print("Please enter a positive integer.")
    else:
        for n in range(1, num + 1):
            print(n, end=" ")
except ValueError:
    print("That's not a valid number.")