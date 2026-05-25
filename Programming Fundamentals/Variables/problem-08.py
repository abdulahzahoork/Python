# 8. Mini Project — Student Profile
# Task: Using everything you've learned, create a small student profile program:

# Store a student's name, age, marks (as a string "88"), and grade in variables using multiple assignment
# Cast marks from string to integer, then calculate marks out of 100 as a float percentage
# Print the full profile neatly
# At the end, delete the grade variable and confirm it's gone

name, age, marks, grade = "Abdullah", 22, "88", "A+"

marks = int(marks)
percentage = float(marks)

print(f"Name: {name} | Age: {age} | Marks: {percentage:.1f}% | Grade: {grade}")

del grade
print(grade)