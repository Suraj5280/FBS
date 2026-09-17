class book:
    def __init__(self, title, auther, price):
        self.title = title
        self.auther = auther
        self.price = price

    def gettitle(self):
        return self.title

    def settitle(self, newtitle):
        self.title = newtitle

    def getauther(self):
        return self.auther

    def setauther(self, newauther):
        self.auther = newauther

    def getprice(self):
        return self.price

    def setprice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Title={self.title}\t Auther={self.auther}\t price={self.price}")


b1 = book("python", "Guido", 500)
b2 = book("Java", "james", 400)

b1.setprice(550)
b1.display()
b2.display()