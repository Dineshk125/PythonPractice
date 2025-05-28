dic = {
    "name": "Dinesh",
    "last_name": "Kumawat",
    "gender": "Male",
    "age": 22,
}

print(dic)

# Method 1 add/update

dic["name"] = "Vishal"
print(dic)

# Method 2 add/update

dic.update({"name": "Dinesh", "marks": 100, "address": "Sikar"})
print(dic)
