a = int(input("Enter the first number:"))
opertor = input("Enter the operator:")
b = int(input("Enter the second number:"))

if opertor == "+":
    print(a + b)
elif opertor == "-":
    print(a - b )
elif opertor == "/":
    print(a % b )
elif opertor == "*":
    print(a * b)
elif opertor == "**":
    print(a ** b)
else:
    print("hatt bc")

