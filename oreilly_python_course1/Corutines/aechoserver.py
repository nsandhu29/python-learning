from socket import *
import asyncio


async def echo_server(address, loop):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    sock.setblocking(False)
    while True:
        client, addr = await loop.sock.accept(sock)
        print('Connection from', addr)
        loop.create_task(echo_handler(client, loop))
        # t = threading.Thread(target=echo_handler, args=(client,))
        # t.start()
        # echo_handler(client)


def echo_handler(client, loop):
    while True:
        data = await loop.sock_recv(100000)
        if not data:
            break
        await loop.sock_senall(client, b'Got:' + data)
        # client.sendall(b'Got:' + data)
    print('Connection Closed')
    client.close()


if __name__ == 'main':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(echo_server('', 25000), loop)
