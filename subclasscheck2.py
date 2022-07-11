"""
    Другой пример переопределения специального метода __subclasscheck__
    Данный метод вызывается при использовании функции issubclass(cls, tuple_of_classes)
    В данном примере переопределение метода __subclasscheck__ выполняется
    с помощью функции-декоратора
"""
from collections import ChainMap

class Obj(type):
    """
        Класса Obj объявляется как метакласс и обязательно наследует от метакласса type
    """
    def __subclasscheck__(self, subclass):
        """
            Переопределение функции issubclass(_cls, _tuple_of_clss)
            Первым параметров может передаваться как cls, так и self.
            Как метод класса данный метод объявлять нельзя, т.к. объявляемый класс Obj
            может служить только для создания другого класса, который и будет эталонным (_tuple_of_clss)
            для метода issubclass
        """
        methods = (method for method in self.__dict__)
        attrs = ChainMap(*(superclass.__dict__ for superclass in subclass.__mro__))
        if all(method in attrs for method in methods):
            return True
        return False


def decor(cls):
    class Wrapper(metaclass=Obj):
        def x(self):
            pass
        def y(self):
            pass
    return Wrapper


@decor
class A:
    pass


class B:
    def x(self):
        pass

    def y(self):
        pass

print(A.__dict__.keys())
print(B.__dict__.keys())
print(issubclass(B, A))