# 9. Simple Login System
# Store a username and password. Ask the user to enter both. Print:

# "Access granted" if both match
# "Wrong password" if the username is correct but the password isn't
# "User not found" if the username doesn't exist

try:
    username = "admin"
    password = "1234"

    un = input("Enter username: ")
    pw = input("Enter password: ")
     
    if username == un:
        if password == pw:
            print("Access granted")
        else:
            print("Wrong password")
    else:
        print("User not found")

except ValueError:
    print("Please enter valid input!")



    