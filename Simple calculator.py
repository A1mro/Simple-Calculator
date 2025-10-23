


# Simple Math Calculator
# Author: A1mro
# Description: Basic calculator for addition, subtraction, multiplication, and division

print("Insert two values")

x = int(input("x = "))
y = int(input("y = "))

print("Now select the calculation method:")
operation = input("(+) . (-) . (/) . (x) = ")

if operation == "+":
    print(f"{x} + {y} = {x + y}")
elif operation == "-":
    print(f"{x} - {y} = {x - y}")
elif operation == "/":
    if y != 0:
        print(f"{x} / {y} = {x / y}")
    else:
        print("Error: You cant division by zero!")
elif operation == "x":
    print(f"{x} x {y} = {x * y}")
else:
    print("Invalid operation")
