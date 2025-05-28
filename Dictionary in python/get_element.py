dic = {
    "name": "Dinesh",
    "last_name": "Kumawat",
    "gender": "Male",
    "age": 22,
}


# print(dic["age"])
# print(dic["Name"]) # KeyError: 'Name' -> if key not exist.
# print(dic["gender"])
# print(dic) # output -> {'name': 'Dinesh', 'last_name': 'Kumawat', 'gender': 'Male', 'age': 22}

# to get a value

# r = dic.get("name")
# # r = dic.get("Age") # outout -> None , it note give error when wrong key print.
# print(r)

k = input("Enter a key = ")

result = dic.get(k)  # output Enter a key = name , Dinesh
# result = dic.get(k)  # Enter a key = Age, None

if result is not None:
    print(result)
else:
    print("key don't exist")
