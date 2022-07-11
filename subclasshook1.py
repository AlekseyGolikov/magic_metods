"""
    Пример переопределения специального метода __subclasshook__
    Данный метод вызывается при использовании функций issubclass(cls, tuple_of_classes)
    или isinstance(inst, tuple_of_classes)
    Специальный метод __subclasshook__(cls, subclass) определяется из абстрактного класса
"""
from abc import ABCMeta
from collections import ChainMap

class Obj(metaclass=ABCMeta):
    """
        Сравнение типов необходимо осуществлять относительно данного класса Obj

    """
    @classmethod
    def __subclasshook__(self, subclass):
        """
            Метод обязательно должен вызываться как метод класса
            Первым аргументом ему можно передавать cls и self
            Этим методом переопределяются функции isinstance(inst, tuple_of_classes) и
            issublass(cls, tuple_of_classes)
        """
        methods = ['x', 'y']
        # for m in methods:
        #     print(m)
        # print('----------------------')
        attrs = ChainMap(*(superclass.__dict__ for superclass in subclass.__mro__))
        # for a in attrs.keys():
        #     print(a)
        if all(method in attrs for method in methods):
            return True
        return False

class A:
    def x(self):
        pass
    def y(self):
        pass

class B:
    def x2(self):
        pass
    def y(self):
        pass

class C:
    pass

print(isinstance(A(), Obj))
print(issubclass(A, Obj))
print(issubclass(C, Obj))
