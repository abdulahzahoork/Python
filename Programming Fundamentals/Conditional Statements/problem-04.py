# 4. Grade Calculator
# Given a score (0–100), print the letter grade:

# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → F

try: 
    score = int(input("Enter a number: "))

    if not (0 <= score <= 100):
        print("Score does not exist!")
    elif score >=90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else: 
        print("Grade: F")
except ValueError:
    print("Please enter a valid integer!")