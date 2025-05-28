dic = {
    "name": "Dinesh",
    "last_name": "Kumawat",
    "gender": "Male",
    "age": 22,
}

print(dic)
print(type(dic))

dic = {
    "name": "Dinesh",
    "last_name": "Kumawat",
    "gender": "Male",
    "age": 22,
    "marks": [45, 56],
    # [223, 78]: 56, # TypeError: unhashable type: 'list'
    1: 2,
    2: 1,
}

print(dic)
print(type(dic))
