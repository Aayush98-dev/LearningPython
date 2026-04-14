lower_value = int(input("Enter the lowest range value: "))
upper_value = int(input("Enter the highest range value: "))
print("The prime numbers in the range are :")
for numbers in range(lower_value,upper_value+1):
    if (numbers>1):
        for i in range(2,numbers):
            if(numbers % i)==0:
                break
        else:
            print(numbers)