class Student:
    inName="FBS"
    stdCount=0
    def __init__(self,rollno,name,bach):
        self.rollNo=rollno
        self.name=name
        self.bach=bach
        Student.stdCount+1
        