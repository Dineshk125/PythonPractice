class Student:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        self._gender = new_gender


s1 = Student("Dinesh", 23, "Male")

print(s1._name)
print(s1._age)
print(s1._gender)
print()

s2 = Student("Sonu", 24, "Male")
s2._gender = "Female"
print(s2._name)
print(s2._age)
print(s2._gender)
