import math

class Transformation(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def translate(self, a, b):
        #Translations - ie. offsetting the X and Y co-ordinates by a given amount
        print "Offsetting the matrix (%.2f, %.2f) by a given amount (%.2f, %.2f)"%(self.x, self.y, a, b)
        self.x += a
        self.y += b
        print "The new set of points : (%.2f, %.2f)"%(self.x, self.y)
    
    def rotate(self, a, b, c):
        #Rotations by an arbitrary angle around a given point
        print "Rotations by an arbitrary angle %f around a given point (%.2f, %.2f)"%(c, a, b)
        dx = math.cos(-c) * ( self.x - a) - math.sin(-c) * (self.y - b);
        dy = math.sin(-c) * ( self.x - a) + math.cos(-c) * (self.y - b);
        self.x = a + dx;
        self.y = b + dy;
        print "The new set of points are (%.2f, %.2f)"%(self.x, self.y)
        """
        
        
        dx = self.x - a
        dy = self.y - a
        
        hypot_len = (dx ** 2 + dy ** 2) * 0.5
        
        try:
            start_angle = math.atan(dy/dx)
        except ZeroDivisionError:
            if dy < 0:
                start_angle = 3 * math.pi/2
            elif dy > 0:
                start_angle = math.pi/2
            else:
                return
        new_angle = start_angle - c
        
        self.x = a + math.cos(new_angle) * hypot_len
        self.y = b + math.sin(new_angle) * hypot_len
        """
    #code
    def scale(self, a, b, c):
        print "Scale relative to a point (%.2f, %.2f) with scale factor %f"%(a, b, c)
        dx = self.x - a
        dy = self.y - b
        self.x = a + (dx * c)
        self.y = b + (dy * c)
        print "The new set of points are (%.2f, %.2f)"%(self.x, self.y) 
        
    def reflect(self, axis):
        print "Reflection over the %c axis"%(axis)
        if axis.lower() == 'x'.lower():
            self.y = -self.y
        elif axis.lower() == 'y'.lower():
            self.x = -self.x
        else:
            print "Enter correct value"
        print "The new set of points are (%.2f, %.2f)"%(self.x, self.y)
            
    def finish(self):
        print (float("%.2f"%self.x), float("%.2f"%self.y))
        """
(0, 5)
-->(0.0, 5.0)
translate(3, 2)
-->(3.0, 7.0)
scale(1,3,0.5)
-->(2.0, 5.0)
rotate(3,2,1.57079632679)
-->(6.0, 3.0)
reflect(X) 
-->(6.0, -3.0)
translate(2,-1)
-->(8.0, -4.0)
scale(0,0,-0.25)
-->(-2.0, 1.0)
rotate(1,-3,3.14159265359)
-->(4.0, -7.0)
reflect(Y)
-->(-4.0, -7.0)
finish()
"""

xy_shape = Transformation(int(raw_input("Enter value for X Axis")), int(raw_input("Enter value for Y axis")))
xy_shape.translate(3, 2)
xy_shape.scale(1, 3, 0.5)
xy_shape.rotate(3, 2, 1.57079632679)
xy_shape.reflect('X')
xy_shape.finish()
xy_shape.translate(2,-1)
xy_shape.scale(0,0,-0.25)
xy_shape.rotate(1,-3,3.14159265359)
xy_shape.reflect('Y')
xy_shape.finish()
    
