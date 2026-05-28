# 7. FizzBuzz
# For a given number:

# Print "Fizz" if divisible by 3
# Print "Buzz" if divisible by 5
# Print "FizzBuzz" if divisible by both
# Otherwise, print the number itself

try:
    num = int(input("Enter a number: "))

    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

except ValueError:
    print("Please enter valid input!")