# Print all prime numbers between 1 and 100.

print("Prime Number between 1 and 100: ", end=" ")
for x in range(2, 101):
    for y in range(2, int(x**0.5) + 1):
        if x % y == 0:
            break
    else:
        print(x, end=" ")  