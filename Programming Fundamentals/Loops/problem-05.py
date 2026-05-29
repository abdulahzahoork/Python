# Count vowels — Loop through a string and count how many vowels (a, e, i, o, u) it contains.

s = input("Enter a string: ")
count = 0

for char in s:
    if char.lower() in 'aeiou':
        count += 1

print(f"No. of vowels: {count}")
