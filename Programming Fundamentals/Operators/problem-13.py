# Q14. Write a ternary expression to find the maximum of three numbers a = 10, b = 25, c = 18.

a, b, c = 10, 25, 18

greatest = a if (a>b and a>c) else b if (b>a and b>c) else c
print(f"{greatest} is the greatest")