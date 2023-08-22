#SIMPLE CALCULATOR:

def add(x, y):
    print("By Adding")
    return x + y

def subtract(x, y):
    print("By Subtracting")
    return x - y

def multiply(x, y):
    print("By Multiplying")
    return x * y

def divide(x, y):
    print("By Dividing")
    return x / y

print("SIMPLE CALCULATOR")

print("Operations are: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    i = input("Select operation (1/2/3/4): ")

    if i in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if i == '1':
            result = add(num1, num2)
        elif i == '2':
            result = subtract(num1, num2)
        elif i == '3':
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)

        print("Result is :", result)
        break
    else:
        print("Invalid choice. Please try again.")
