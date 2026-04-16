# Print Even Numbers

# Problem:
# Print all even numbers from 1 to N.

n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

# Sum of N Numbers

# Problem:
# Find sum of first N natural numbers.

n = int(input())
total = 0

for i in range(1, n + 1):
    total += i

print(total)

# Reverse Counting

# Problem:
# Print numbers from N to 1.

n = int(input())

for i in range(n, 0, -1):
    print(i)

# Print Numbers from 1 to 20

# Problem:
# Print numbers from 1 to 20 using a loop.

for i in range(1, 21):
    print(i)

# Print Odd Numbers

# Problem:
# Print all odd numbers between 1 and N.

n = int(input())

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

# Print Squares of Numbers

# Problem:
# Print squares of numbers from 1 to N.


n = int(input())

for i in range(1, n + 1):
    print(i * i)

# Print Multiples of 5

# Problem:
# Print all multiples of 5 up to N.

n = int(input())

for i in range(1, n + 1):
    if i % 5 == 0:
        print(i)

# Count Numbers

# Problem:
# Count how many numbers are between 1 and N.

n = int(input())
count = 0

for i in range(1, n + 1):
    count += 1

print(count)