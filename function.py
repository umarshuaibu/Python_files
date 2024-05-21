# def sing_happy_birthday():
#     print('Happy Birthday to you')
#     print('Happy Birthday to you')
#     print('Happy Birthday to you')
#     print('Happy Birthday to you')

# sing_happy_birthday()
# sing_happy_birthday()

# def addition(num1, num2):
#     return num1 + num2
# print(addition(10, 100))
# print(addition(4, 50))

# def divide(num1, num2):
#     return num1 / num2
# print(divide(umar10, 100))
# print(round(divide(3, 9)),2)

# def password_length(password):
#     length = len(password)
#     return length
# password = str(input('Enter password: '))
# print(password_length(password))

def password_checker(password):
    length = len(password)
  
    if length < 7:
        print('Password too short, try lengthy one')
    else:
        print('It is success')
password = str(input('Enter your password: '))
print(password_checker(password))