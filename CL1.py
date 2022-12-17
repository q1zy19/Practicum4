#!/usr/bin/env python
# coding: utf-8

# In[7]:


import socket

sock = socket.socket()
sock.setblocking(1)
print('Подключение клиента:')
sock.connect(('127.0.0.1', 9090))

while True:
    print('Для отключения от сервера введите: "exit"')
    msg = input('Введите сообщение:')
    data=msg.encode()
    sock.send(data)
    if msg == 'exit':
        break
    data = sock.recv(1024)
    print(f'Сообщение от сервера:', data.decode())

print('Отключение клиента')
sock.close()


# In[ ]:




