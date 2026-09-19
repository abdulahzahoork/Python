# Count vowels in string.

s = "programming"
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count+=1

print("No. of vowels in string:", count)

# ---------------------------------------------------------------------------------

# Find the largest element in List

l = [12, 45, 7, 89, 23]
largest = l[0]

for i in l:
    if i > largest:
        largest = i

print(f"Largest element in list: {largest}")

# alternative approach

print(f"Largest element: {max(l)}")


# ---------------------------------------------------------------------------------

# Create a new list containing only even numbers


li = []

for i in range(100, 201, 2):
    li.append(i)

print(f"New List: {li}")