# 4. Object Reference
# Task:
# - Assign a = 50, then b = a
# - Print both a and b
# - Now change b = 99
# - Print both again
# - What happened to a? Write a comment in your code explaining why.

a = 50
b = a
print(a, b)

b = 99
print(a, b)

# When we write b = a, both b and a point to the SAME object (50) in memory.
# When we reassign b = 99, Python creates a NEW object (99) and b points to it.
# a still points to the original object (50), so it remains unchanged.
# This is because variables store REFERENCES to objects, not the values directly.