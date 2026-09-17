class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid
    def display(self):
        print(f"id={self.id}\tName={self.name}\tSal={self.sal}")
    def calSal(self):
        print(f"Emp Sal= {self.sal}")


    def __str__(self):
        return f"Employee(id={self.id}, name={self.name}, sal={self.sal})"


# Emp Ends here................................

class Hr(Employee):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
    def getCom(self):
        return self.com
    def setcom(self,newcom):
        self.com=newcom
    def calSal(self):
        print(f"Fianl HR Sal= {self.com+self.getSal()}")
# Hr Ends HEre................................

class Dev(Employee):
    def __init__(self,id,name,sal,bonus):
        super().__init__(id,name,sal)
        self.bonus=bonus
    def getBonus(self):
        return self.bonus
    def setBonus(self,newbon):
        self.bonus=newbon
    def calSal(self):
        print(f"Fianl Dev Sal= {self.bonus+self.getSal()}")
# Developer Ends HEre................................


e1=Employee(12,"Sachin",9000000)
h1=Hr(18,"Smriti",500000,100000)
d=Dev(1,"Pravin",200000000,10000)
#e1.calSal()
#h1.calSal()
#d.calSal()



print(f"Employee = {e1}")