class Coor:
    def __set_name(self, owner, name):
        self._name = name


class Point:
    x = Coor()
