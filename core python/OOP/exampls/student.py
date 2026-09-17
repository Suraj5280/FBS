class Student:
    inName = "FBS"

    def __init__(self, rollno, name, batch):
        self.rollno = rollno
        self.name = name
        self.batch = batch

    def getRollNo(self):
        return self.rollno

    def getName(self):
        return self.name

    def getBatch(self):
        return self.batch

    def setRollNo(self, rollno):
        self.rollno = rollno

    def setName(self, name):
        self.name = name

    def setBatch(self, batch):
        self.batch = batch

    def display(self):
        print(f"RollNo={self.getRollNo()}\tName={self.getName()}\tBatch={self.getBatch()}\tInstituteName={Student.inName}")


s1 = Student(12, "suraj", "julypython")
s2 = Student(13, "swaraj", "julypython")
s3 = Student(1, "ritik", "junepython")

s1.display()
s2.display()
s3.display()

Student.inName = "Firstbitsolutions"

print("+++++++++++++++++++++++++++++++++++")

s1.display()
s2.display()
s3.display()




#create a class for placed students with the following attributes: name,frn,