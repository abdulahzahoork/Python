# Count how many digits are in a given integer.

num = int(input("Enter a number: "))
x = abs(num)
count = 0

while (x!=0): 
    digit = x%10
    count+=1
    x//=10

print(f"Total no. of digits: {count}")