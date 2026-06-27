class Car:
    def __init__(self,model):
        self.model=model
    def drive(self):
        print("Car  Moves")
    
class Ship:
    def __init__(self,model):
        self.model=model
    def drive(self):
        print("Ship Sails")
    
c1=Car("BMW")
s1=Ship("Titanic")

for x in (c1,s1):
    x.drive()