# Check whether a number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print("Neither prime nor composite.")
else: 
    isPrime = True

    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            isPrime = False
            break

    if isPrime:
        print(f"{num} is Prime")
    else:
        print(f"{num} is Composite")
