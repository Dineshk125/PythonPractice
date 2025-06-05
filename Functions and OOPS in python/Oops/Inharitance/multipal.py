class Father:

    fatherName = ""

    def fathername(self):
        print(f"Father Name : {self.fatherName}")


class Mother:

    motherName = ""

    def mothername(self):
        print(f"Mother Name : {self.motherName}")


class Child(Father, Mother):
    def perents(self):
        print(f"Father Name : {self.fatherName} ")
        print(f"Mother Name : {self.motherName}")


c1 = Child()
c1.fatherName = "Ram"
c1.motherName = "Sita"
c1.perents()
