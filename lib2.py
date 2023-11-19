class Teacher:
    __MinAge = 20
    __MaxAge = 80

    def __init__(self, old, name, subject):
        self.__old = old
        self.__name = name
        self.__subject = subject

    def __setattr__(self, key, value):
        if key == "_Teacher__old":
            self.TestCoor(value)
        if key == "_Teacher__name":
            name = value
            if len(name.split()) != 3:
                raise Exception("Должно быть 3 слова")
        object.__setattr__(self, key, value)

    @classmethod
    def TestCoor(cls, old):
        if old > cls.__MaxAge or old < cls.__MinAge:
            raise Exception("Указан неверный возраст")

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value


class Coor:
    def __set_name(self, owner, name):
        self._name = '_' + name

        def __get_(self, instance, owner):
            return getattr(instance, self.name)

        def __set_(self, instance, value):
            setattr(instance, self.name, value)


class Point:
    x = Coor()

        