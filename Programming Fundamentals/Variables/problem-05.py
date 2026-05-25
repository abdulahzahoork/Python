# 5. Type Casting
# Task: You are given these variables:
num_str = "42"
pi_str = "3.14"
age = 19

# Convert num_str to an integer and add 8 to it
# Convert pi_str to a float and multiply it by 2
# Convert age to a string and join it with " years old"
# Print all three results

num_str_to_int = int(num_str) + 8
pi_str_to_float = float(pi_str) * 2
age_to_str = str(age) + " years old"

print(num_str_to_int, pi_str_to_float, age_to_str, sep="\n")