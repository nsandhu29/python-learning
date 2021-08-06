class Parent(object):
    def __init__(self, value):
        self.value = value

    def spam(self):
        print('Parent.spam', self.value)

    def grok(self):
        print('Parent grok')
        self.spam()


class Child1(Parent):
    def yow(self):
        print('child.yow')

    # modify spam object
    def spam(self):
        print('Child1.spam', self.value)


class Child1(Parent):
    # Create wrapper for parent class object
    def spam(self):
        print('Child2.spam')
        super().spam()


class Child2(Parent):
    # Add more attributes to child class
    def __init__(self, value, extra):
        self.extra = extra
        super().__init__(value)  # Initialized parent


class Parent2():
    def yow(self):
        print('Parent2.yow')


# Having multiple parents
class Child3(Parent, Parent2):
    pass