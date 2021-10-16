
from math import pi

class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi*d**2/4
        side = d*h
        area = round(circle+side,2)
        return  area

    def __init__(self, diameter, high):
        self.__dict__['dia'] = diameter
        self.__dict__['h'] = high
        self.__dict__['area'] = self.make_area(diameter, high)

    def __setattr__(self, attr, value):
        if attr == 'dia':
            self.__dict__['dia'] = value
            self.__dict__['area'] = self.make_area(self.__dict__['dia'], self.__dict__['h'])
        elif attr == 'h':
            self.__dict__['h'] = value
            self.__dict__['area'] = self.make_area(self.__dict__['dia'], self.__dict__['h'])
        elif attr =='area':
            print("You can't change area directly")
            # raise AttributeError


c  = Cylinder(2,4)
print(c.dia, c.h, c.area)


c.dia = 3
c.h = 5

print(c.area)
c.area = 12

print(c.__dict__)