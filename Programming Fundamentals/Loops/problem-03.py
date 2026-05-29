# FizzBuzz — Print numbers 1–50. For multiples of 3 print "Fizz", multiples of 5 print "Buzz", multiples of both print "FizzBuzz".

for n in range (1, 50+1):
    if n %3 ==0 and n%5==0:
        print(f"{n} - FizzBuzz")
    elif n%3==0:
        print(f"{n} - Fizz")
    elif n%5==0:
        print(f"{n} - Buzz")
    else:
        print(n)