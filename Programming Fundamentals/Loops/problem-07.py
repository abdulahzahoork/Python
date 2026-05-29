# Find duplicates — Given items = [3, 1, 4, 1, 5, 9, 2, 6, 5], use a loop to find which numbers appear more than once.

items = [3, 1, 4, 1, 5, 9, 2, 6, 5]
counts = {}

for item in items: 
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

for item, count in counts.items():
    if count > 1:
        print(f"Duplicate: {item}")