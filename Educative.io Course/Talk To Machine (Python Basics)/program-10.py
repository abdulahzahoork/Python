# ---------------------------------------------------------------------

# Print numbers from 1 to 10.

# for i in range(1, 11):
#     print(i, end=" ")

print(*range(1, 11)) # an alternative approach

# ---------------------------------------------------------------------

# Print even numbers from 1 to 20.

print("Even numbers: ", end="")
for i in range(2, 21, 2): 
    print(i, end=" ")

# ---------------------------------------------------------------------

# Find the sum of numbers from 1 to 100

total = 0
for i in range(1, 101):
    total += i

print("\nSum:", total)

# alternative approach

# total = sum(range(1, 101))
# print("Sum:", total)

# ---------------------------------------------------------------------

# Print multiplication table of 7

for i in range (1, 11):
    print(f"7 x {i} = {7*i}")

