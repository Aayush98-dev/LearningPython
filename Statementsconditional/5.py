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