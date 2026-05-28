# 6. Triangle Validity
# Given three sides, check if they can form a valid triangle (the sum of any two sides must be greater than the third).

try:
    a = int(input("Enter length of first side: "))
    b = int(input("Enter length of second side: "))
    c = int(input("Enter length of third side: "))
    
    if a<=0 or b<=0 or c<=0:
        print("Sides must be positive!")
    elif (a+b) > c and (a+c) > b and (b+c) > a:
        print("It is a triangle.")
    else:
        print("It is not a triangle.")

except ValueError:
    print("Please enter valid input!")