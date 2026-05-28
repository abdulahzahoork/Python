# 3. Largest of Two Numbers
# Take two numbers as input and print the larger one. If they're equal, print "Both are equal."


# <---------------- Explicit Version ---------------->
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print("Both are equal.")

except ValueError:
    print("Please enter valid integers!")


# <---------------- Optimized Version ---------------->

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a == b:
        print("Both are equal.")
    else:
        print(f"{max(a, b)} is greater than {min(a, b)}")

except ValueError:
    print("Please enter valid integers!")