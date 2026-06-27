class Fruits:
    def apple(self):
        print("Apple is 50/kg")
class Veg(Fruits):
    def potato(self):
        print("Potato is 34/kg")


v1=Veg()

v1.potato()
v1.apple()
