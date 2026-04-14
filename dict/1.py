info = {
    "key" : "value",
    "name" : "ayush",
    "companyname" : "Ayush States"
}

print(info)

# Nested dictionary

student = {
    "name" : "Ayush",
    "Rollno" : 21,
    "subjects" : {
        "Math" : 74,
        "chem" : 87,
        "phy" : 54
    }
}

print(student["subjects"])
print(student["subjects"]["Math"])



# show how to show our dictionary key like how many lists are in there in a dictionary

student = {
    "name" : "Ayush",
    "Age" : 74,
    "subjects" : {
        "math" : 74,
        "chem" : 85,
        "phy" : 95
    }
}


print(student.keys())                     # output is : dict_keys(['name', 'Age', 'subjects'])
print(list(student.keys()))                       # output is : dict_keys(['name', 'Age', 'subjects'])
print(len(list(student.keys())))                   # output is : dict_keys(['name', 'Age', 'subjects'])

print(len(student))                                       # output is : 3


print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))


pairs = list(student.items())
print(pairs[2][1])

print(student.get("Age"))
print(student.get("subjects"))


# ************** updating the new data in our present dictionary

student.update({"City" : "Lucknow"})                        #output is : {'name': 'Ayush', 'Age': 74, 'subjects': {'math': 74, 'chem': 85, 'phy': 95}, 'City': 'Lucknow'}
print(student)

new_data = {"city":"Lucknow"}
student.update(new_data)

print(student)         # if i am updating new value then it can store new data in oour old data like it can change the old data with new one

new_data = {"name":"Aishwarya" , "city" : "Lucknow"}
student.update(new_data)

print(student)                                       #ooutput is : {'name': 'Aishwarya', 'Age': 74, 'subjects': {'math': 74, 'chem': 85, 'phy': 95}, 'city': 'Lucknow'}
