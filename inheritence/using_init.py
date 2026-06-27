class Fruits:
    def __init__(self, fruit_name):
        self.fruit_name = fruit_name    


class Store(Fruits):
    def __init__(self,fruit_name):
        super().__init__(fruit_name)
        

    def display(self):
        print("Fruit:", self.fruit_name)
s1=Store("apple")


s1.display()
