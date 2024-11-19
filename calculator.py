num1 = float(input("1st number: "))
num2 = float(input("2nd number: "))
operation = input("select operation('+' '-' '*' '/'): ")

if operation == "+":
    results=num1+num2
elif operation == "-":
    results=num1-num2
elif operation == "*":
    results=num1*num2
elif operation == "/":
    results=num1/num2

print(f"result: {results}")