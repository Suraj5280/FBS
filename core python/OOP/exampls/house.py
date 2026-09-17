class house:
    def __init__(self, area, room, price):
        self.area = area
        self.room = room
        self.price = price

    def getarea(self):
        return self.area

    def setarea(self, newarea):
        self.area = newarea

    def getroom(self):
        return self.room

    def setroom(self, newroom):
        self.room = newroom

    def getprice(self):
        return self.price

    def setprice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Area={self.area}\t Room={self.room}\t price={self.price}")


h1 = house("1200 sqft", "2bhk", 8500000)
h2 = house("1000 sqft", "2bhk", 7800000)

print(h1.getarea())
h1.setprice(8800000)
h1.display()

print(h2.getprice())
h2.setarea("900 sqft")
h2.display()