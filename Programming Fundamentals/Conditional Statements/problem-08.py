# 8. BMI Calculator
# Calculate BMI using weight / height² and classify:

# Below 18.5 → Underweight
# 18.5–24.9 → Normal
# 25–29.9 → Overweight
# 30 and above → Obese

try: 
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    if weight <=0 or height <=0:
        print("Height and Weight must be positive.")
    else:
        bmi = weight / (height ** 2)

        print(f"BMI: {bmi:.2f}")
        print("Classification: ", end="")

        if bmi >= 30: 
            print("Obese")
        elif bmi >= 25:
            print("Overweight")
        elif bmi >=18.5:
            print("Normal")
        else:
            print("Underweight")

except ValueError:
    print("Please enter valid input!")