import task1_functions

print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
print ("5. Calculate CGPA")

options = int(input( "What do you want to do? choose from 1 to 5: "))

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))

if options == 1:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = (task1_functions.addition(num1, num2))
    print(f'{num1} Plus {num2} = {result}')


elif options == 2:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = (task1_functions.subtraction(num1, num2))
    print(f'{num1} Minus {num2} = {result}')

elif options == 3:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = (task1_functions.multiplication(num1, num2))
    print(f'{num1} Multiply by {num2} = {result}')


elif options == 4:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = (task1_functions.Division(num1, num2))
    print(f'{num1} Divide by {num2} = {result}')

elif options == 5:
    num1 = float(input('Enter Your 1ST semester GPA: '))
    num2 = float(input('Enter Your 2ND semester GPA: '))
    result = (task1_functions.cgpa(num1, num2))
    print(f'Your accumulated CGPA is {result}')

else:
    print ("Wrong input, press anykey to exit")