# Check if a number is a palindrome (e.g., 121, 1331).

try:
    num = int(input("Enter a number: "))
    x = abs(num)
    rev = 0

    while (x!=0):
        digit = x%10
        rev = (rev*10) + digit
        x//=10

    if num == rev:
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not palindrome")
except ValueError:
    print("Please enter a valid integer!")