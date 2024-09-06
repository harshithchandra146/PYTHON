import math
class Shape:
    def __init__(self):
        self.area = 0
        self.name = ""
    def showArea(self):
        print("the area of the",self.name,"is",self.area,"units")
        
class circle(Shape):
    def __init__(self,radius):
        self.area = 0
        self.name = "circle"
        self.radius = radius
    def calcArea(self):
        self.area = math.pi * self.radius * self.radius
    
class rectangle(Shape):
    def __init__(self,length,breadth):
        self.area = 0
        self.name = "rectangle"
        self.length = length
        self.breadth = breadth
    def calcArea(self):
        self.area = self.length * self.breadth
        
class triangle(Shape):
    def __init__(self,base,height):
        self.area = 0
        self.name = "triangle"
        self.base = base
        self.height = height
    def calcArea(self):
        self.area = self.base * self.height / 2
            
c1 = circle(5)
c1.calcArea()
c1.showArea()
r1 = rectangle(4,5)
r1.calcArea()
r1.showArea()
t1 = triangle(3,4)
t1.calcArea()
t1.showArea()
