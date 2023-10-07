# This program is about learning about class creation in Python.A class is a blue print of objects , where an object is a real world entity .
 # Here, as you can see, i created "animal" class , which have attributes of 'kind' and 'color' . The method is 'Display' which prints the object(instance) .



class animal:
    def __init__(self,kind,color):
        self.kind=kind
        self.color=color
    def display(self):
        print(self.kind,self.color)
c1=animal("dog","white")
c1.display()

# output: dog white 
