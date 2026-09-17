class Mec:
    def diplay(self):
        print("Machnical")
class Electric:
    def diplay(self):
        print("I am from Electrical")
class Mecatronix(Electric,Mec):             #this controls the sequance of execution.
    def abc():
        print("I am in mactroinx")
m=Mecatronix()
m.diplay()


#in this type the derived class have multiple base class, means the the sub class is derived from
#multiple super class.

#hear the machatronix is derived form electorincs and machanical class