class Emp:
    def __init__(self,nm):
        self.name=nm

    def display(self):
        print("Display ")
#emp
class Devloper(Emp):
    def display(self):
        print("Disply of Dev")
#dev

class HR(Emp):
    def display(self):
        print("disply of Hr")
#Hr

class JrHR(HR):
    def display(self):
        print("I am from disply of Jr Hr")
#jr hr
class SrHR(HR):
    def display(self):
        print("I am from disply of Sr Hr")
#sr hr

class JrDev(Devloper):
    def display(self):
        print("I am from Jr Devoper")
#jr devloper

h1=HR("SACHIN")
h1.display()

s1=Emp("abc")
s1.display()

jhr=JrHR("Smriti")
jhr.display()

jrd=JrDev("Sachin")
jrd.display()



#super class have multiple sub class and the sub class have another multiple sub class.

#the jr dev is derived from devloper and devloper is derived from emp