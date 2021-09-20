import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('172.17.136.58', 2200))
server.listen(2)
c_socket, address = server.accept()

print('Connected:', address)

data1 = c_socket.recv(1024).decode()
unit = data1

x = ('а', 'е', 'и', 'о', 'у', 'ё', 'ю', 'я', 'ы', 'э', 'А', 'Е', 'И', 'О', 'У', 'Ё', 'Ю', 'Я', 'Ы', 'Э')
y = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ь')
wlen = len(unit)
a = 0
b = 0
c = 0
for i in unit:
    for j in x:
        if j in i:
            a += 1
for i in unit:
    for j in y:
        if j in i:
            b += 1
c = a/b
d = round(c, 3)
d = d * 100

c_socket.send((f"Кол-во символов: {wlen}, Кол-во гласных: {a}, Кол-во согласных: {b}, гл/согл: {d} %").encode())

c_socket.close()
