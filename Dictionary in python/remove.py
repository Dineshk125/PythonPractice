dic = {
    "name": "Dinesh",
    "last_name": "Kumawat",
    "gender": "Male",
    "age": 22,
    "marks": 33,
}
print(dic)

dic.pop("name")
dic.pop("age")
print(dic)

x = dic.popitem()
print(x)
print(dic)
