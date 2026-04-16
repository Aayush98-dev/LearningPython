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