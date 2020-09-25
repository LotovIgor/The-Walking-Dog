import random
# Таблицу назовем city
# 0 - собака не была
# 1 - была
#  сделал city глобально вместе с считыванием n
city = []
n = int(input())
for i in range(n):
    city.append([])
    for j in range(n):
        city[i].append(0)
# Оля
def point(n):
    # Помещение собаки в город на рандомные координаты
    x = random.randint(1, n-1)
    y = random.randint(1, n-1)
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
if __name__ == '__main__':
    # e выходы, m повторения, r результат действия функции собаки
    e = 0
    m = 10000
    r = 0
    # Множество повторений функции и вероятность
    for d in range(m):
        r = dog(n)
        if r == 1:
            e += 1
    print(e/m)
