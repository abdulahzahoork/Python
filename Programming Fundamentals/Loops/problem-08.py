# Prime checker — Write a loop that prints all prime numbers between 1 and 100.

for n in range(2, 101):
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n%i  == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")