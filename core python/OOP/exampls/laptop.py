class laptop:
    def __init__(self, lmodel, lram, lstorage):
        self.model = lmodel
        self.ram = lram
        self.storage = lstorage

    def getmodel(self):
        return self.model

    def setmodel(self, newmodel):
        self.model = newmodel

    def getram(self):
        return self.ram

    def setram(self, newram):
        self.ram = newram

    def getstorage(self):
        return self.storage

    def setstorage(self, newstorage):
        self.storage = newstorage

    def display(self):
        print(f"Model={self.model}\t Ram={self.ram}\t Storage={self.storage}")


l1 = laptop("Asus", "12gb", "512gb")
l2 = laptop("Dell", "16gb", "512gb")

l1.display()
l2.display()