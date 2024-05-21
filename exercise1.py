
username1 = ("Umar")
pas1 = "12345"

username = str(input('Enter your username: '))
pas = str(input('Enter your password: '))

if username == username1 and pas == pas1:
    print("Approved")
else:
    print("Incorrect username or password")