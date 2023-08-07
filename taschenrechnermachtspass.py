# plus
def add(x, y):
    return x + y

# minus
def subtract(x, y):
    return x - y

# mal
def multiply(x, y):
    return x * y

# geteilt
def divide(x, y):
    return x / y

print("HELLO AND WELCOME TO MY BEAUTIFUL CALCULATOR")
print("AND LET'S BEGIN")
print("1 = add a number to another number")
print("2 = subtract a number from another number")
print("3 = multiply a number to another number")
print("4 = divide a number from another number")
Rechenzeichen = input("1, 2, 3, or 4? \n")

if Rechenzeichen in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if Rechenzeichen == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif Rechenzeichen == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif Rechenzeichen == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif Rechenzeichen == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Wrong input! Only 1, 2, 3, and 4 work.")
input()