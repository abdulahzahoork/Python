# Problem 15 — No Newline
# Print numbers 1 to 5 using a loop on a single line:
# Expected Output:
# 1 2 3 4 5

for x in range(1, 6):
    if x == 5: 
        print(x)
    else: 
        print(x, end=" ")