# Sum of a list — Given numbers = [4, 7, 2, 9, 1, 5], use a loop to compute the sum without using sum().


numbers = [4, 7, 2, 9, 1, 5]
sum = 0

for n in numbers:
    sum += n

print(f"Sum: {sum}")
