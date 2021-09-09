async def greeting(name):
    return 'Hello ' + name

g = greeting('Navjot')
print(g)

# when calling this function nothing is shown in output to run this function we need to use asyncio library
import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(g)

# Corutine run under management

async def hello():
    names = ['Preety', 'Navjot', 'Jaiteg']
    for name in names:
        print(await greeting(name))
h = hello()
print(h)


async def fib(n):
    if n <= 2:
        return 1
    else:
        return await fib(n-1) + fib(n-2)

