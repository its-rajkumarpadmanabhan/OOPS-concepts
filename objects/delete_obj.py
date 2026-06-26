class Student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno

p1=Student("jhon",23,9) #p1 is the object


del p1 #delete p1 object
print(p1.name) #error occurs - p1 not defined

