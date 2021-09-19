import socket
ban = []
n = 0
m = 0


def create_server():
    global server
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    server.bind((socket.gethostname(), 12321))

    print(socket.gethostbyname(socket.gethostname()))
    user_connecting()

def user_connecting():
    try:
        server.listen(1)
        user, user_address = server.accept()
        print("Проверка на бан")
        if isban(user_address):
            print(f"Доступ запрещён для игрока {user_address}")
            send(user, "Доступ запрещён: це бан")
            send(user, "exit")
            user_connecting()
        else:
            game(user, user_address)
    except ConnectionResetError:
        user_ex()


def newban(address):
    ban.append(address[0])
    user_ex()


def isban(address):
    for i in range(0, len(ban)):
        if address[0] == ban[i]:
            return True
    return False


def send(user, str):
        user.send(f"{str}".encode("utf-8"))
        while True:
            data = user.recv(8).decode("utf-8")
            if data == "1":
                break

def game(user, user_address):
        send(user, "answer")
        send(user, "Введите число: ")
        incoming(user, user_address)


def uatrys(user, address, str):
    send(user, str)
    send(user, "answer")
    send(user, "Введите число:")
    incoming(user,address)


def uatry(user, address):
    send(user, "answer")
    send(user, "Введите число:")
    incoming(user, address)


def incoming(user, address, typemsg = ""):
    global n, m
    if typemsg == "ch":
        choise = user.recv(1024).decode("utf-8")
        if choise == "y":
            print("new game")
            game(user, address)
        else:
            user_end(user)
    else:
        ansstr = user.recv(1024).decode("utf-8")
        try:
            ans = int(ansstr)
            if not n == 0:
                m = 1
            ran = 123
            #ran = random.randint(0, 1000)
            if ans == ran:
                 send(user, "Вы выиграли! Хотите испытать удачу снова?")
                 send(user, "answer")
                 send(user, "Да(y), нет(*):")
                 incoming(user, address, "ch")
            else:
                send(user, f"Что ж, вы не угадали, было загадано: {ran}. Хотите повторить?")
                send(user, "answer")
                send(user, "Да(y), нет(*)")
                incoming(user, address, "ch")
        except ValueError:
            if m == 0:
                n += 1
                if n == 1:
                    uatrys(user, address, "Кажется, вы ввели не число, попробуйте снова")
                elif n == 2:
                    uatrys(user, address,"О , нет! Не повезло! Кажется, вы снова не попали на нужную клавишу...\n"
                        " Что ж, попробуйте снова.")
                elif n == 3:
                    uatrys(user, address," Просто напомню, как выглядят числа: 1 2 3 4 5 6 7 8 9 ...\n "
                          "Можете просто скопировать и вставить при помощи мыши или сенсорной панели")
                elif n == 4:
                     uatrys(user, address, "\x1B[3;37m\"Эта идея настолько безумна, что вполне может и сработать."
                          "\"\x1B[0m  -  Лиз Гилберт")
                elif n == 5:
                    uatrys(user, address,"Что ж, только упорный способен постичь истину")
                elif n == 6:
                    uatrys(user, address,"...")
                elif n == 7:
                    uatrys(user, address,"...")
                elif n == 8:
                    uatry(user, address)
                elif n == 9:
                    uatry(user, address)
                elif n == 10:
                    ran = random.randint(0,1000)
                    send(
                        user, "Что ж, проверим ответ:\n"
                        f"Пусть {ansstr} = x, тогда, если ответ верный, то справедливо равенство:\n"
                        f"x+{ran}-n!*0 + sqrt(0) - x + YourIQ = {ran}"
                        f" Решим полученное уравнение:\n {ran} = {ran} - "
                        f"следовательно, ответ верен"
                        f" Вы выиграли!!! Ура!"
                        )
                    newban(address)
            else:
                uatrys(user, address, "Мы это уже проходили, просто сделайте так же, как"
                           "и в тот раз, когда получилось...")

def user_end(user):
    global n, m
    m = 0
    n = 0
    user.close()
    print("User has downed")
    user_connecting()

def user_ex():
    global n, m
    m = 0
    n = 0
    print("User has downed with exception")
    user_connecting()
create_server()
