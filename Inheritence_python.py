class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
class Dog(animal):
    def __init__(self,name,breed):
        super().__init__(name,"Dog")
        self.breed=breed
    def bark(self):
        print(f"{self.name} (a {self.species}) is barking!")
class cat(animal):
    def __init__(self,name,color):
        super().__init__(name,"cat")
        self.color=color
    def meow(self):
        print(f"{self.name} (a {self.species}) is meowing!")

class bird(animal):
    def __init__(self,name,wings):
        super().__init__(name,"bird")
        self.wings=wings
    def tweet(self):
        print(f"{self.name} (a {self.species}) is tweeting!")
        
d=Dog("puppy","golden retrival")
d.bark()

c=cat("kitty","black")
c.meow()

b=bird("crow","black wings")
b.tweet()
