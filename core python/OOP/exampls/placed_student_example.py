class PlacedStudent:
    institute_name = "First_bit_solutions"

    def __init__(self, frn, rollno, name, branch, company, package):
        self.frn = frn
        self.rollno = rollno
        self.name = name
        self.branch = branch
        self.company = company
        self.package = package

    def getFRN(self):
        return self.frn
    
    def getRollNo(self):
        return self.rollno

    def getName(self):
        return self.name

    def getBranch(self):
        return self.branch

    def getCompany(self):
        return self.company

    def getPackage(self):
        return self.package
    



    def setFRN(self, frn):
        self.frn = frn

    def setRollNo(self, rollno):
        self.rollno = rollno

    def setName(self, name):
        self.name = name

    def setBranch(self, branch):
        self.branch = branch

    def setCompany(self, company):
        self.company = company

    def setPackage(self, package):
        self.package = package

    def display(self):
        print(f"FRN={self.getFRN()}\tRollNo={self.getRollNo()}\tName={self.getName()}")
        print(f"Branch={self.getBranch()}\tCompany={self.getCompany()}\tPackage={self.getPackage()} LPA")
        print(f"Institute={PlacedStudent.institute_name}")
        print("                                                            ")


s1 = PlacedStudent(101, 12, "Suraj", "python", "TCS", 4.5)
s2 = PlacedStudent(102, 13, "Sarthak", "python", "Infosys", 5.0)
s3 = PlacedStudent(103, 1, "chetan", "java", "Wipro", 4.0)

s1.display()
s2.display()
s3.display()

print("+++++++++++++++++++++++++++++++++++++++++++++")


#change company and
s1.setCompany("Apple")
s1.setPackage(6.0)

s1.display()