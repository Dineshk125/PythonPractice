import pickal_unpickal
import pickle


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student("Dinesh", 23)

f = open("name.txt", "wb")
pickle.dump(s, f)
f.close()
