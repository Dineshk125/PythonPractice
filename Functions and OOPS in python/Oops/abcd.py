import pickal_unpickal
import pickle


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


f = open("name.txt", "rb")
st = pickle.load(f)
f.close()

print(st.name)
print(st.age)
