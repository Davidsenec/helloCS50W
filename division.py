import sys

try:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
except ValueError:
    print("Bruh that aint an integer. That's it, you're getting banned!")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Boi you know dividing by 0 is stupid")
    sys.exit(1)

print(f"The result of {x} divided by {y} is {result}.")