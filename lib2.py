class Teacher:
    __MinAge = 20
    __MaxAge = 80

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get_(self, instance, owner):
        return getattr(instance, self.name)

    def __set_(self, instanse, value):
        if self.name == "_fio":
            if len(value.split()) != 3:
                raise Exception("No")
        setattr(instanse, self.name, value)


class Data:
    fio = Teacher()

    def __init__(self, fioValue):
        self.fio = fioValue


class Coor:
    def __set_name(self, owner, name):
        self._name = '_' + name

        def __get_(self, instance, owner):
            return getattr(instance, self.name)

        def __set_(self, instance, value):
            setattr(instance, self.name, value)


class Point:
    x = Coor()
