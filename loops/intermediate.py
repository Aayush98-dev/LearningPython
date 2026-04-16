# Factorial of a Number

# Problem:
# Find factorial of a number.

n = int(input())
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

# Sum of Digits

# Problem:
# Find sum of digits of a number.

n = int(input())
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    n //= 10

print(sum_digits)

# Palindrome Number

# Problem:
# Check if a number is palindrome.

n = int(input())
original = n
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# Multiplication Table (1 to 10)

# Problem:
# Print tables from 1 to 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()

# Skip Multiples of 3

# Problem:
# Print numbers from 1 to N but skip multiples of 3.

n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i)

# Print Reverse of a String

# Problem:
# Print a string in reverse using loop.

text = input()

for i in range(len(text) - 1, -1, -1):
    print(text[i], end="")