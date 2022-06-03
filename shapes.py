
from math import pi

class circle:
    def __init__(self,radius):
        self.radius=radius
    def  area(self):
        areaofcircle=pi*self.radius**2
        return f"The area is {areaofcircle}cm squared"
    def circumference(self):
        circle_circumference=2*pi*self.radius
        return f"The circumference {circle_circumference}"    

mycircle=circle(radius=10)
print(mycircle.radius)
print(mycircle.area())   
print(mycircle.circumference())       


class square:
    def __init__(self,side):
        self.side=side

    def  area(self):
        area=self.side**2
        return area

    def perimeter(self):
     perimeter=4*self.side
     return perimeter

    
squaree=square(side=9)
print(squaree.side)
print(squaree.area())  



class Rectangle:
    def __init__(self,l,w,):
        self.length=l
        self.width=w

    def  area(self):
        areas=self.length* self.width
        return areas

    def perimeter(self):
     peri=2*self.length+2*self.width
     return  f"recta peri{peri}"

    
newrectangle=Rectangle(3,5)
print(newrectangle.area())
print(newrectangle.perimeter()) 


class sphere:
    def __init__(self,r):
        self.r=r
        

    def  surface_area(self):
        area= 4*pi*self.r
        return area

    def volume(self):
     vol=1.33333333333*pi*self.r**3
     return vol

    
newsphere=sphere(9)
print(newsphere.surface_area())
print(newsphere.volume()) 