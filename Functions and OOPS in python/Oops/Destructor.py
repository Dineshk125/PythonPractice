class Student:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def __del__(self):
        print("Distructor")


s1 = Student("Dinesh", 23, "Male")
del s1
