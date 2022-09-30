import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030))
print('Запуск сервера')
time.sleep(1)

s.listen(1)
print('Начало прослушивания порта')
time.sleep(1)

conn, addr = s.accept()
print('Подключение клиента')
print('Прием данных от клиента')
time.sleep(1)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
    print(data.decode('utf-8'))
    print('Отправка данных клиенту')
conn.close()
time.sleep(1)
print('Остановка сервера')
