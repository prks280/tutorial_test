from abc import ABC, abstractmethod

class Abs(ABC):

    @abstractmethod
    def f1(self): pass

    @abstractmethod
    def f2(self): pass


class Test(Abs):
    def f1(self):
        print('f1 implented')

    # def f2(self):
    #     print('f2 implented')


t = Test()
t.f1()
# t.f2()