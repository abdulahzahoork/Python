# Multiplication table — Use nested loops to print a 5×5 multiplication table.


for x in range(1, 6):
    for y in range(1, 6):
        print(f"{x} x {y} = {x*y}")
    print()