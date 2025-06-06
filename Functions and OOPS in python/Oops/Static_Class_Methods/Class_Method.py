# class Student:

#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def display(self):
#         print(f"Student Name: {self.name}")
#         print(f"Student Age: {self.age}")
#         print(f"Student Gender: {self.gender}")


# c1 = Student("Dinesh", 24, "Male")

# c1.display()


## Using Class Method


class Student:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student Gender: {self.gender}")

    @classmethod
    def display_Data_using_parameter(cls, name, age, gender):
        obj = cls(name, age, gender)
        return obj

    @classmethod
    def display_data_using_file(cls, filename):
        f = open(filename, "r")
        student_data = f.read()
        name, age, gender = student_data.split()

        obj = cls(name, age, gender)
        return obj


c1 = Student.display_Data_using_parameter("Dinesh", 23, "Male")  # using parameters
c1.display()

c2 = Student.display_data_using_file("class_method.txt")  # using file
c2.display()
