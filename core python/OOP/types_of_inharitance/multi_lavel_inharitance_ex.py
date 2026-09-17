class Emp:
    def __init__(self,nm):
        self.name=nm

    def display(self):
        print("Display ")
#emp
class HR(Emp):
    def display(self):
        print("Disply of Hr")
#hr
class jrHR(HR):
    def display(self):
        print("i am form display jr Hr")
#jr hr

h1=HR("SACHIN")     #for hr
h1.display()

s1=Emp("jdjd")      #for emp
s1.display()

jhr=jrHR("Smriti") #for jr Hr
jhr.display()


#the derived class is from other derived class which is derived from base class ,means the super 
#class has 1 sub class and the sub class has another sub class.

#the jr Hr is derived form HR and HR is derived form emp