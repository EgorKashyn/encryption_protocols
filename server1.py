import socket
import pickle
import random
def encrypt_message(K, message):
    return ''.join([chr(ord(message[i]) + K) for i in range(len(message))])
def decrypt_message(K, message):
    return ''.join([chr(ord(message[i]) - K) for i in range(len(message))])
b=random.randrange(1000,30000,1)
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
data = conn.recv(1024)
g,p,A=pickle.loads(data)
B=g**b%p
K=A**b%p
conn.send(pickle.dumps(B))
print(K)
while True:
    mess = pickle.loads(conn.recv(1024))
    message = decrypt_message(K, mess)
    print(message)
    mess=encrypt_message(K,message)
    conn.send(pickle.dumps(mess))
conn.close()

