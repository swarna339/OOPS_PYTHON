from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class circle(shape):
    def area(self,a):
        print("circle area:",(22/7)*a*a)
    
class triangle(shape):
    def area(self,b,c):
        print("triangle area:",(1/2)*b*c)
    
class square(shape):
    def area(self,a):
        print("square area:",a*a);

t=triangle()
t.area(4,2)

c=circle()
c.area(7)

sq=square()
sq.area(5)
