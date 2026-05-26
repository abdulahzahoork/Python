# Q7. A person can vote if they are 18 or older AND a citizen. 
# Write a Python expression using logical operators to check this given age = 20 and is_citizen = True.

try: 
    age = int(input("Enter your age: "))
    is_Citizen = bool(input("Are you a citizen [True/False]: "))

    if (age >= 18 and is_Citizen == True):
        print("Person can vote.")
    else:
        print("Person cannot vote.")

except ValueError: 
    print("Please enter valid input!")