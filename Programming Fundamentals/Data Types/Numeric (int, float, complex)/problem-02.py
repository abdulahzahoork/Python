# Check if a given integer is even or odd.

try: 
    num = int(input("Enter a number: "))
    if num%2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
except ValueError:
    print("Please enter valid numbers!")