import socket
import pickle
import random
def encrypt_message(K, message):
    return ''.join([chr(ord(message[i]) + K) for i in range(len(message))])
def decrypt_message(K, message):
    return ''.join([chr(ord(message[i]) - K) for i in range(len(message))])
a=random.randrange(1000,30000,1)
g=random.randrange(1000,30000,1)
p=random.randrange(1000,30000,1)
A=g**a%p
sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(pickle.dumps((g,p,A)))
B = int(pickle.loads(sock.recv(1024)))
K=B**a%p
print(K)

while True:
    message=input('Введите сообщение: ')
    sock.send(pickle.dumps(encrypt_message(K,message)))
    mess = pickle.loads(sock.recv(1024))
    message=decrypt_message(K,mess)
    print(message)
sock.close()
