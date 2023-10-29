from math import sqrt
class Point:
    __MinCoor = 0
    __MaxCoor = 7
    @classmethod
    def testCoor(cls, value):
        return cls.__MinCoor <= value <= cls.__MaxCoor

    def __init__(self, x, y):
        if self.testCoor(x) and self.testCoor(y):
            self.__x = x
            self.__y = y
        else:
            raise Exception('no')



    @staticmethod
    def gipo(x, y):
        return sqrt(x**2 + y**2)

