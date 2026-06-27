class Fruits:
    def apple(self):
        print("Apple is 50/kg")
class Veg():
    def potato(self):
        print("Potato is 34/kg")
class Store(Veg,Fruits):
    def product(self):
        print("Store Open")

s1=Store()

s1.potato()
s1.apple()
s1.product()
