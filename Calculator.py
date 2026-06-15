# Simple Calculator

n = float(input("Enter first number= "))
o = input("Enter operator (+, -, *, /):= ")
m = float(input("Enter second number= "))


if o == "+":
    print("Result =", n + m)

elif o == "-":
    print("Result =", n - m)

elif o == "*":
    print("Result =", n * m)

elif o == "/":
    if m != 0:
        print("Result =", n / m)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")