import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 3030))  # Подключаемся к нашему серверу.
print('Соединение с сервером')
time.sleep(1)

print('Отправка данных серверу')
time.sleep(1)

s.sendall('Hello, Habr!'.encode('utf-8'))  # Отправляем фразу.
print('Прием данных от сервера')
time.sleep(1)

data = s.recv(1024)  # Получаем данные из сокета.
s.close()
print('Разрыв соединения с сервером')
