# Print Sum Until User Enters 0

# Problem:
# Keep taking numbers and add them until user enters 0

total = 0

while True:
    num = int(input())
    
    if num == 0:
        break
    
    total += num

print(total)


# Print Numbers Using While Loop

# Problem:
# Print numbers from 1 to N using while.

n = int(input())
i = 1

while i <= n:
    print(i)
    i += 1

# Count Vowels

# Problem:
# Count vowels in a string.

text = input()
count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print(count)