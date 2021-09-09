async def greeting(name):
    print('Hello ' + name)

import asyncio

g = greeting('Navjot')
loop = asyncio.get_event_loop()
loop.run_until_complete(g)


def gen():
    n = 5
    while n > 0:
        yield n
        n -= 1

g = gen()

for x in g:
    print(x)

def coro():
    n = 0
    while True:
        result = yield n
        print('Got:', result)
        n += 1
c = coro()