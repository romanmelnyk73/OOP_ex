# Write the class Point as outlined in the instructions
import numpy as np

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
    def distance_to_origin(self):
        distance = np.sqrt(np.square(self.x) + np.square(self.y))
        return distance
    def reflect(self, axis):
        if axis == 'x':
            self.y = - self.y
        elif axis == 'y':
            self.x = - self.x
        else:
             print('Error')

if __name__ == '__main__':

    pt = Point(x=3.0)
    pt.reflect("y")
    print((pt.x, pt.y))
    pt.y = 4.0
    print(pt.distance_to_origin())