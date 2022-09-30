import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030))  # Привязываем серверный сокет к localhost и 3030 порту.
print('Запуск сервера')
time.sleep(1)

s.listen(1)  # Начинаем прослушивать входящие соединения.
print('Начало прослушивания порта')
time.sleep(1)

conn, addr = s.accept()  # Метод который принимает входящее соединение.
print('Подключение клиента')
print('Прием данных от клиента')
time.sleep(1)

while True:
    data = conn.recv(1024)  # Получаем данные из сокета.
    if not data:
        break
    conn.sendall(data)  # Отправляем данные в сокет.
    print(data.decode('utf-8'))
    print('Отправка данных клиенту')
conn.close()
time.sleep(1)
print('Остановка сервера')
