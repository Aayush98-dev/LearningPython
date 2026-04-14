salary = int(input("Enter salary : "))

if(salary >= 50000):
    tax1 = salary * 0.2
    print("Your tax is : ",tax1)
elif(salary <= 50000 and salary > 20000):
    tax2 = salary * 0.1
    print("Your tax is : ",tax2)
else:
    print("No tax")