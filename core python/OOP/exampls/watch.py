class watch:
    def __init__(self, brand, type, price):
        self.brand = brand
        self.type = type
        self.price = price

    def getbrand(self):
        return self.brand

    def setbrand(self, newbrand):
        self.brand = newbrand

    def gettype(self):
        return self.type

    def settype(self, newtype):
        self.type = newtype

    def getprice(self):
        return self.price

    def setprice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Brand={self.brand}\t Type={self.type}\t Price={self.price}")


w1 = watch("Fossil", "Analog", 23000)
w2 = watch("Tissot", "Analog", 54000)
w3 = watch("Samsung", "smart", 36000)

print(w1.getbrand())
w1.display()

w2.settype("smart")
w2.display()

print(w3.getprice())
w3.display()