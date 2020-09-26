import random
import turtle
# Таблицу назовем city
# 0 - собака не была
# 1 - была
city = []
n = int(input())
for d in range(n):
    city.append([])
    for t in range(n):
        city[d].append(0)


# Оля
def point(n):
    # Помещение собаки в город на рандомные координаты
    x = random.randint(1, n-2)
    y = random.randint(1, n-2)
    city[x][y] = 1
    return [x, y]


# Игорь
def walk(s):
    # Шаг собаки
    sch = 0
    if city[s[0]][s[1]+1] == 0:
        sch += 1
    if city[s[0]][s[1]-1] == 0:
        sch += 1
    if city[s[0]+1][s[1]] == 0:
        sch += 1
    if city[s[0]-1][s[1]] == 0:
        sch += 1
    rnd = random.randint(1, sch)
    if city[s[0]][s[1]+1] == 0:
        rnd -= 1
        if rnd == 0:
            city[s[0]][s[1]+1] = 1
            return s[0], s[1]+1
    if city[s[0]+1][s[1]] == 0 and rnd != 0:
        rnd -= 1
        if rnd == 0:
            city[s[0]+1][s[1]] = 1
            return s[0]+1, s[1]
    if city[s[0]][s[1]-1] == 0 and rnd != 0:
        rnd -= 1
        if rnd == 0:
            city[s[0]][s[1]-1] = 1
            return s[0], s[1]-1
    if city[s[0]-1][s[1]] == 0 and rnd != 0:
        rnd -= 1
        if rnd == 0:
            city[s[0]-1][s[1]] = 1
            return s[0]-1, s[1]


# Оля
def border(s):
    # проверка на границу города
    # Заканчивается ли таблица с одной из сторон
    # функция должна выводить 0(несработала) или 1(сработала)
    x = s[0]
    y = s[1]
    if x <= 0 or x >= n-1 or y <= 0 or y >= n-1:
        return 1
    else:
        return 0


# Оля
def blind_alley(s):
    # (Тупик)
    # Проверка всех направлений на то была ли там собака
    # функция должна выводить 0(несработала) или 1(сработала)
    a = 0
    x = s[0]
    y = s[1]
    if border([x, y]) == 0:
        if city[x+1][y] == 1:
            a += 1
        if city[x-1][y] == 1:
            a += 1
        if city[x][y+1] == 1:
            a += 1
        if city[x][y-1] == 1:
            a += 1
        if a == 4:
            return 1
        else:
            return 0
    else:
        return 0


# Игорь
def dog(n):
    s = point(n)
    x = s[0]
    y = s[1]
    while border([x, y]) == 0 and blind_alley([x, y]) == 0:
        x, y = walk([x, y])
    if blind_alley([x, y]) == 1:
        return 0
    else:
        return 1

    #  Просчитывает одно путешествие собаки в городе
    # выводит 0 при тупике и 1 при выходе из города


# Арсений
def prob(n, m):
    # e выходы, m повторения, r результат действия функции собаки
    e = 0
    # Множество повторений функции и вероятность
    for d in range(m):
        r = dog(n)
        if r == 1:
            e += 1
    print(round(e / m * 100, 6), "% - Шанс собаки выйти из города")


# Игорь
def visual(n):
    turtle.setup(width=900, height=1000)
    turtle.speed('fastest')
    turtle.ht()
    turtle.up()
    turtle.goto(-400, -400)
    factor = 800/(n-1)
    turtle.pensize(80/n)
    turtle.pencolor('black')

    for i in range(n-1):
        turtle.down()
        turtle.goto(-400 + i * factor, 400)
        turtle.up()
        turtle.goto(-400 + (i + 1) * factor, -400)
    turtle.down()
    turtle.goto(-400 + (i + 1) * factor, 400)
    turtle.up()
    turtle.goto(-400, -400)

    for i in range(n-1):
        turtle.down()
        turtle.goto(400, -400 + i * factor)
        turtle.up()
        turtle.goto(-400, -400 + (i + 1) * factor)
    turtle.down()
    turtle.goto(400, -400 + (i + 1) * factor)
    turtle.up()

    s = point(n)
    x = s[0]
    y = s[1]
    turtle.pencolor('red')
    turtle.goto(-400 + (x) * factor, -400 + (y) * factor)
    turtle.dot(160/n, 'red')
    turtle.down()
    turtle.speed(1)
    while border([x, y]) == 0 and blind_alley([x, y]) == 0:
        x, y = walk([x, y])
        turtle.goto(-400 + (x) * factor, -400 + (y) * factor)
        turtle.dot(160/n, 'red')
    turtle.up()
    turtle.speed('fastest')
    turtle.pencolor('black')
    if border([x, y]) == 1:
        turtle.goto(-400, 420)
        turtle.write('Собака вышла из города!', font=("Arial", 40, "normal"))
    else:
        turtle.goto(-400, 420)
        turtle.write('Собака попала в тупик :(', font=("Arial", 40, "normal"))
    turtle.exitonclick()


if __name__ == '__main__':
    m = int(input())
    prob(n, m)
