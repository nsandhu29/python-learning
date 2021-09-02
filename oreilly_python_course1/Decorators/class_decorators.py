def logformat(fmt):
    def logged(func):
        # Idea: give me function i will put logging
        # around it
        print('Adding logging to', func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)

        return wrapper

    return logged

def logmethods(cls):
    for key, value in list(vars(cls).items()):
        if callable(value):
           # Is it method?
            setattr(cls, key, logged(value))
    return cls




@logmethods

class Spam():
    def __init__(self, value):
        self.value = value

    def yow(self):
        print('Yow!')

    def grok(self):
        print('Grok!')

