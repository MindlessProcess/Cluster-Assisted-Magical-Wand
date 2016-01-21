#!/usr/bin/env python

import math

class KColor:
    def __init__(self, RGB = (0, 0, 0)):
        self.color = RGB
        
    # Returns 1 if colors are neighbors
    def distance(self, RGB):
        R = (self.color[0] - RGB[0]) ** 2
        G = (self.color[1] - RGB[1]) ** 2
        B = (self.color[2] - RGB[2]) ** 2
        return math.sqrt(R + G + B)

class KPos:
    def __init__(self, XY = (0, 0)):
        self.pos = XY
        self.old = (0, 0)

    def get_pos(self):
        return self.pos

    def distance(self, XY):
        if type(XY) == type(KPos()):
            XY = XY.get_pos()
        X = (self.pos[0] - XY[0]) ** 2
        Y = (self.pos[1] - XY[1]) ** 2
        return math.sqrt(X + Y)

    # 0: equidistance | -x : pos1 is closer | x : pos2 is closer
    def compare(self, pos1, pos2):
        return self.distance(pos1) - self.distance(pos2)

    def move(self, dot_vector, weight):
        self.old = self.pos
        if type(dot_vector) == type(KPos()):
            vector = dot_vector.get_pos()
        X = (vector[0] - self.pos[0]) * weight
        Y = (vector[1] - self.pos[1]) * weight
        self.pos = (X, Y)

    def has_converged(self):
        return self.old == self.pos

def main():
    color = KColor((1, 1, 2))
    print "True" if 1 == color.distance((1, 1, 1)) else "False"

    pos = KPos()
    pos2 = KPos((1, 2))
    pos3 = KPos((3, 1))
    print "(0, 0) -> (1, 2) | (1, 4)"
    print pos.compare(pos2, (1, 4))
    print "(0, 0) -> (3, 1) | (1, 2)"
    print pos.compare(pos3, pos2)

    old = KPos(pos.get_pos())
    pos.move(pos2, 0.1)
    print pos.get_pos()
    print old.get_pos()

if __name__ == "__main__":
    main()
