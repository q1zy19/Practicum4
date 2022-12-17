#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket, threading,sys

def server(conn, addr):
    while True:
        print('Получение данных от клиента')
        try:
            data = conn.recv(1024)
            print('Сообщение от клиента', addr, ':', data.decode)
            print('Отправка сообщения клиенту')
            conn.send(data)
        except (ConnectionResetError, ConnectionAbortedError):
            print('Соединение с клиентом прервано')
            raise


sys.tracebacklimit = 0
sock = socket.socket()
print('Запуск сервера')
sock.bind(('', 9090))
print('Начало прослушивания порта')
sock.listen(0)

while True:
    conn, addr = sock.accept()
    print("Подключение клиента:",addr)
    thread=threading.Thread(target = server, args = (conn, addr), daemon = True)
    thread.start()

print('Прекращение работы сервера')

