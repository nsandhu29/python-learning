from socket import *
import threading

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        print('Connection from', addr)
        t = threading.Thread(target=echo_handler, args=(client,))
        t.start()
        #echo_handler(client)

def echo_handler(client):
    while True:
        data = client.recv(100000)
        if not data:
            break
        client.sendall(b'Got:' + data)
    print('Connection Closed')
    client.close()

if __name__ == 'main':
    echo_server('', 25000)
