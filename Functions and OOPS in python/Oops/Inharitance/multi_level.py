class GrandFather:

    def __init__(self, grandFather):
        self.grandfather = grandFather


class Father(GrandFather):

    def __init__(self, fatherName, grandFather):
        self.fathername = fatherName

        GrandFather.__init__(self, grandFather)


class Child(Father):

    def __init__(self, grandFather, fatherName, childName):
        self.childname = childName

        Father.__init__(self, fatherName, grandFather)

    def all_Name(self):
        print(f"Grand Father Name : {self.grandfather} ")
        print(f"Father Name : {self.fathername}")
        print(f"Child Name : {self.childname}")


c1 = Child("Dasharath", "Ram", "love_Khush")
c1.all_Name()
