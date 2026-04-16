# Character Type

# Problem:
# Check whether a character is:

# Alphabet
# Digit
# Special character

ch = input()

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")


# Triangle Validity

# Problem:
# Check if three angles form a valid triangle.

a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("Valid Triangle")
else:
    print("Invalid Triangle")



# Find Second Largest

# Problem:
# Find second largest among three numbers.

a = int(input())
b = int(input())
c = int(input())

if (a > b and a < c) or (a > c and a < b):
    print(a)
elif (b > a and b < c) or (b > c and b < a):
    print(b)
else:
    print(c)


# Login System

# Problem:
# Check username and password.

username = input()
password = input()

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")