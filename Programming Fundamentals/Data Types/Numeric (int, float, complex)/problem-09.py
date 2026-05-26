# Calculate the area of a circle given its radius as a float.

try:
    radius = float(input("Enter radius of circle: "))
    if radius < 0:
        print("Radius cannot be negative")
    else:
        area = 3.14 * (radius ** 2)
        print(f"Area of Circle: {area:.2f}")
except ValueError:
    print("Please enter valid input!")