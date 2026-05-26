# Write a program to reverse the digits of an integer (e.g., 1234 → 4321).

num = int(input("Enter a number: "))
x = abs(num)
revNum = 0

while (x!=0):
    digit = x%10
    revNum = (revNum*10) + digit
    x//=10

print(f"Number: {num}")
print(f"Reversed: {revNum}")