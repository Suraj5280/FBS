class Emp:
    def __init__(self,nm):
        self.name =nm
    def display(self):
        print("Display")
class HR(Emp):
        def display(self):
            print("display of Hr")
h1 = HR("sachin")
h1.display()
s1=Emp("jdjd")
s1.display()


#this has 1base class and 1dirived class.

#the Hr class is derived form emp base class