# class Duck:
#     sound = 'Quack Quack'
#     movement = 'Walk like duck'
#
#     def quack(self):
#         print(self.sound)
#
#     def move(self):
#         print(self.movement)


class Animal:
    # constructor used to initialize class
    def __init__(self, **kwargs):
        if 'type' in kwargs:
            self._type = kwargs['type']
        if 'name' in kwargs:
            self._name = kwargs['name']
        if 'sound' in kwargs:
            self._sound = kwargs['sound']

    # getter setter
    def type(self, t=None):
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n=None):
        if n:
            self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s:
            self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None

    # String representation of object
    def __str__(self):
        return f'The {self.type()} is name {self.name()} makes {self.sound()}'


# def print_animal(o):
#     if not isinstance(o, Animal):
#         raise TypeError('print_animal(): requires an Animal')
#     print(f'the {o.type()} is named {o.name()} and says {o.sound()}')

class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)


class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, s):
        print(f'{self.name()} will now kill all {s}')

def main():
    # donald = Duck()
    # donald.quack()
    # donald.move()
    a0 = Kitten(name='fuffy', sound='rwar')
    a1 = Duck(name='doooc', sound='quack')
    a0.kill('rats')
    print(a0)
    print(a1)

if __name__ == "__main__":
    main()
