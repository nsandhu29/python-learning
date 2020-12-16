# understanding generators
def infinite_sequence():
    num = 0
    while True:
        return num
        num += 1


def gen_infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        yield "This is the second yield statement"


def finite_sequence():
    nums = [1, 2, 3]
    for num in nums:
        yield num


num_squared_lc = [num ** 2 for num in range(5)]
nums_square_gc = (num ** 2 for num in range(5))


def gen_countdown(x):
    while x > 0:
        print('print first iteration')
        yield x
        x -= 1


for i in gen_countdown(10):
    print(i)


def finder(x):
    while True:
        input_text = yield
        if x in input_text:
            print(input_text)


# native coroutines
def greet(name):
    return 'Hello' + name

async def _greet(name):
    return 'Hello' + name

