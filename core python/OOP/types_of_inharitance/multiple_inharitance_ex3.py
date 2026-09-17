class emp():
    def calsalary(self):
        print("emp class")

class hr(emp):
    def calsalary(self):
        print("hr class")

class developer(emp):
    def calsalary(self):
        print("developer class")

h = hr()
d = developer()

h.calsalary()
d.calsalary()