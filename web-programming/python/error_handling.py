import sys

try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError:
    print("Error: Division cannot be dont to the string")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")


