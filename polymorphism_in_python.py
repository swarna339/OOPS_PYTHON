class Vehicle:
    def __init__(self,name):
        self.name=name
    def s(self):
        pass
class car(Vehicle):
    def s(self):
        print(self.name ,"horns like Vroom! Vroom! ")
        
class bicycle(Vehicle):
     def s(self):
         print(self.name,"horns like Tring Tring")
         
class boat(Vehicle):
    def s(self):
        print(self.name,"sounds like Splish! Splash!")

c=car("kia")
c.s()
b=bicycle("cycle")
b.s()
a=boat("ship")
a.s()
