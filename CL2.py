#!/usr/bin/env python
# coding: utf-8

# In[6]:


import socket, threading

def receiving():
    while True:
        try:
            msg= sock.recv(1024).decode('utf-8')
            if msg == 'login':
                sock.send(login.encode('utf-8'))
            else:
                print(msg)
        except:
            print("Отключение клиента")
            sock.close()
            break

def sending():
    while True:
        phrase=input()
        msg=login+':'+phrase
        sock.send(msg.encode('utf-8'))
        if phrase=='exit':
            print("Отключение клиента")
            sock.close()
            break
            
login = input("Введите логин: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9090))
threading.Thread(target=receiving).start()
threading.Thread(target=sending).start()


# In[ ]:




