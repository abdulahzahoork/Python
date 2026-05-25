# 6. Deleting a Variable
# Task: Create a variable temp = 100, print it, then delete it using del. After deleting, try to print it again and observe the error. 
# Write a comment explaining what the error means.

temp = 100
print(temp)

del temp
print(temp)

# NameError: name 'temp'is not defined
# This means that the variable 'temp' that we are trying to print does not exist in our program.