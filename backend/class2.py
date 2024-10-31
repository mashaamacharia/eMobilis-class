from sympy.physics.units import volume
from wasabi import color


class Cylinder:
    def __init__(self,radius,height,color):
        self.r = radius
        self.h = height
        self.rangi = color

    def cal_area(self, is_closed = True):
        if is_closed==True:
            area= 2*22/7*self.r **2 + 2*22/7 *self.r*self.h
            print(f"Area of closed cylinder is : {area}")
        else:
            area=22/7 *self.r**2 +2 *22/7*self.r*self.h
    def calc_volume(self):
        v=22/7* self.r **2 * self.h
        print(f"Volume of cylinder is: {v}")

c1= Cylinder(10,12,"Red")
c2= Cylinder(10,12,"Blue")
c1.calc_volume()
c1.cal_area(is_closed=False)