class Fruits:
    def apple(self):
        print("Apple is 50/kg")

class Store(Fruits):
    def product(self):
        super().apple()
        print("Store Open")

s1=Store()



s1.product()
