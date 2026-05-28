# 5. Leap Year Checker
# Write a program that checks if a given year is a leap year. A year is a leap year if:
# - Divisible by 4, and
# - Not divisible by 100, unless also divisible by 400.

try: 
    year = int(input("Enter a year: "))

    if year <= 0:
        print("Please enter a valid year!")
    elif (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        print("Leap year")
    else:
        print("Normal Year")
except ValueError:
    print("Please enter a valid integer!")