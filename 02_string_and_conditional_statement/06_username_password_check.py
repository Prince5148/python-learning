correct_username="Tech_Prince"
correct_password="Prince@123"

username=input("Enter your username:")
password=input("Enter your password")

if correct_username==username:
    if correct_password==password:
        print("Login successful")
    else:
        print("Incorrect Password")
else:
    print("username not found")
