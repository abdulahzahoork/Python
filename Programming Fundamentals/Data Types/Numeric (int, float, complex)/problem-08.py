# Take a temperature in Celsius and convert it to Fahrenheit. (Formula: F = C × 9/5 + 32)

try: 
    cel = float(input("Enter temperature in Celsius: "))
    fah = cel * (9/5) + 32
    print(f"Temperature in Fahrenheit: {fah:.2f}")
except ValueError:
    print("Please enter valid input!")