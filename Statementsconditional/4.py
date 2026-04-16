# Problem:
# Check if a year is a leap year.
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# Simple Calculator

# Problem:
# Take two numbers and an operator (+, -, *, /) and perform operation.
a = int(input())
b = int(input())
c = input()

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
else:
    print("Invalid operator")