import time
def after(seconds, func):
    time.sleep(seconds)
    func()

def hello():
    print('Hello world')


names = ['dave', 'Thomas', 'Lewis', 'paula']
names.sort(key = lambda name: name.upper())

def add(x, y):
    def do_add():
        print(f'Adding {x} + {y} --> {x + y}')
        return x + y
    return do_add