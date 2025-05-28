# Method -> 1, dict to dict

student = {
    "Dinesh": {
        "roll_no.": 121,
        "gender": "Male",
        "Physics": 88,
        "Chemistry": 96,
        "math": 100,
    },
    "Vishal": {
        "roll_no.": 122,
        "gender": "Male",
        "Physics": 80,
        "Chemistry": 86,
        "math": 90,
    },
    "Vinit": {
        "roll_no.": 123,
        "gender": "Male",
        "Physics": 90,
        "Chemistry": 95,
        "math": 80,
    },
}

print(student["Dinesh"]["gender"])
print(student["Vishal"]["roll_no."])
print(student["Vinit"]["Physics"])

print(
    student["Dinesh"]["Physics"]
    + student["Vishal"]["Chemistry"]
    + student["Vinit"]["math"]
)

for name, details in student.items():
    # print(name)
    # print(details)
    total = details["Physics"] + details["Chemistry"] + details["math"]
    print(f"Total of {name} subjects are {total}")

print(
    student["Dinesh"]["Physics"]
    + student["Dinesh"]["Chemistry"]
    + student["Dinesh"]["math"]
)

# Method -> 2, dict to dict to list

student = {
    "Dinesh": {
        "roll_no.": 121,
        "gender": "Male",
        "Physics": 88,
        "Chemistry": 96,
        "math": 100,
        "marks": [88, 96, 100],
    },
    "Vishal": {
        "roll_no.": 122,
        "gender": "Male",
        "Physics": 80,
        "Chemistry": 86,
        "math": 90,
        "marks": [80, 86, 90],
    },
    "Vinit": {
        "roll_no.": 123,
        "gender": "Male",
        "Physics": 90,
        "Chemistry": 95,
        "math": 80,
        "marks": [90, 95, 80],
    },
}


print(student["Dinesh"]["marks"])
print(student["Vishal"]["marks"])
print(student["Vinit"]["marks"])


for name, details in student.items():
    # print(name)
    # print(details)

    total = sum(details["marks"])
    print(f"total sum of {name} marks is : {total}")


# Method -> 3, dict to dict to dict


student = {
    "Dinesh": {
        "roll_no.": 121,
        "gender": "Male",
        "Physics": 88,
        "Chemistry": 96,
        "math": 100,
        "marks": {"Physics": 88, "Chemistry": 96, "math": 100},
    },
    "Vishal": {
        "roll_no.": 122,
        "gender": "Male",
        "Physics": 80,
        "Chemistry": 86,
        "math": 90,
        "marks": {"Physics": 80, "Chemistry": 86, "math": 90},
    },
    "Vinit": {
        "roll_no.": 123,
        "gender": "Male",
        "Physics": 90,
        "Chemistry": 95,
        "math": 80,
        "marks": {"Physics": 90, "Chemistry": 95, "math": 80},
    },
}

print(student["Dinesh"]["marks"]["Physics"])
print(student["Vishal"]["marks"]["Physics"])
print(student["Vinit"]["marks"]["Physics"])

for name, details in student.items():
    total = details["marks"]["Physics"]
    print(total)

for name, details in student.items():
    total = (
        details["marks"]["Physics"]
        + details["marks"]["Chemistry"]
        + details["marks"]["math"]
    )
    print(f"Total marks of {name} is {total}")
