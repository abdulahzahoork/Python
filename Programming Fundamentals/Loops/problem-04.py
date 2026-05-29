# Reverse a string — Use a loop to reverse "hello world" without using slicing or reversed().

word = "hello world"
rev = ""
for s in range(len(word)-1, -1, -1):
    rev += word[s]

print(rev)