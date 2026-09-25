import random
num = 0
condition = True
while (condition == True):
    rNum = random.randint(1, 101)
    num += rNum
    print(f"New Number: {rNum}")
    ans = input("Enter your Answer: ")
    
    if num%3==0 and num%5==0 and ans=="FizzBuzz":
        print("Win")
    elif num%3==0 and ans=="Fizz":
        print("Win")
    elif num%5==0 and ans=="Buzz":
        print("Win")
    elif num%3!=0 and num%5!=0 and ans=="Skip": 
        print("Skipped")
    else:
        print("You Lose!")
        condition == False
        break