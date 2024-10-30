from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def describe(self):
        print('docs')
class dog(Animal):
    def make_sound(self):
        print('haw haw haw')
class cat(Animal):
    def make_sound(self):
        print('new neaaaw meaw')
class cow(Animal):
    def make_sound(self):
        print('coooo')

if __name__ == '__main__':
    d=dog()
    ca=cat()
    co=cow()
    d.make_sound()
    ca.make_sound()
    co.make_sound()
    d.describe()
    ca.describe()
    co.describe()