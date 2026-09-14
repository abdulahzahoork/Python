# Check hour and print message

hour = int(input("Enter hour: "))

if hour < 12:
    print("Good Morning!")
elif hour < 18:
    print("Good Afternoon!")
else: 
    print("Good Evening!")