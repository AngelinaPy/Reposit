class Point:
    __x = 0
    __y = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        print(f'object was been created: {self}')

    def setCoor(self, x, y):
        self.__x = x
        self.__y = y

    def getCoor(self):
        return self.__x, self.__y

    def __del__(self):
        print(f'Объект {self} удалён')
