class camera:
    def __init__(self, brand, megapixel, price):
        self.brand = brand
        self.megapixel = megapixel
        self.price = price

    def getbrand(self):
        return self.brand

    def setbrand(self, newbrand):
        self.brand = newbrand

    def getmegapixel(self):
        return self.megapixel

    def setmegapixel(self, newmegapixel):
        self.megapixel = newmegapixel

    def getprice(self):
        return self.price

    def setprice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Brand={self.brand}\t Megapixel={self.megapixel}\t Price={self.price}")


c1 = camera("Sony", "102mp", 45000)
c2 = camera("Canon", "120mp", 52000)

c1.setprice(48000)
c1.display()

print(c2.getprice())
c2.display()