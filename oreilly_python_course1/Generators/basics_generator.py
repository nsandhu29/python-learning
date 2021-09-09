names = ['AA', 'Yahoo', 'IBM']
for name in names:
    print(name)

# Underneath for loop
it = names.__iter__()
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
#print(it.__next__())  # Raises StopIteration exception


# Customize for loop define generator function

def countdown(n):
    print('Counting from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')

for x in countdown(5):
    print(x)

# under the covers
c = countdown(5)
print(c) # nothing happens gives <generator object countdown at 0x0000023DF8BE2AC0>
# to initiate countdown
it = c.__iter__()
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())


# grep in unix
def grep(pattern, filename):
    with open(filename) as f:
        for line in f:
            if pattern in line:
                yield line

# grep in generator comprehensions
f = open('filename')
ibm = (line for line in f if 'IBM' in line)
for line in ibm:
    print(line)



nums = [1, 2, 3, 4, 5]
squares = [x*x for x in nums]

#generators
gensquares = (x*x for x in nums)

for x in gensquares:
    print(x)

#Generator run once, to do repeatedly we can use classes:

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


c = Countdown(5)
for x in c:
    print(x)