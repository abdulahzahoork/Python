# Your task:
# Ask the user what year they were born
# Convert their answer into a number
# Calculate their age using the current year
# Print a friendly message showing their age

birthYear = int(input("Enter birth year: "))
currentYear = 2026
age = currentYear - birthYear

print(f"Your age is {age}.")