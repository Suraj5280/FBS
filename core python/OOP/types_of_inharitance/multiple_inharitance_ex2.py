class A:
    def add(self):
        print("add A")

class B:
    def add(self):
        print("add B")

class C(B,A):
    def add():
        print("add c")

c1=(C)
c1.add()

#the output shows add c becouse the derived class is called first then the base class is called in the order of inheritance.
#the c has attribute so the program will not go to inheritance class for the output.