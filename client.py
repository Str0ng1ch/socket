import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 3030))
print('Соединение с сервером')
time.sleep(1)

print('Отправка данных серверу')
time.sleep(1)

s.sendall('Вот мое сообщение!'.encode('utf-8'))
print('Прием данных от сервера')
time.sleep(1)

data = s.recv(1024)
s.close()
print('Разрыв соединения с сервером')
