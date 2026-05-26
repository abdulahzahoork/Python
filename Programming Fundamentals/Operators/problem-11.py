# Q11. What will this print? Explain the difference between == and is:
a = [1, 2, 3] 
b = [1, 2, 3]
c = a
print(a == b) # True
print(a is b) # False
print(a is c) # True

# == checks if two variables have the same value.
# is checks if two variables point to the same object in memory (same address).