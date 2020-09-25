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
    x = random.randint(0, n)
    y = random.randint(0, n)
    return x,y
    pass


# Игорь
def walk(x0, y0):
    # Шаг собаки
    sch = 0
    if city[x0][y0+1] == 0:
        sch += 1
    if city[x0][y0-1] == 0:
        sch += 1
    if city[x0+1][y0] == 0:
        sch += 1
    if city[x0-1][y0] == 0:
        sch += 1
    rnd = random.randint(1, sch)
    if city[x0][y0+1] == 0:
        rnd -= 1
        if rnd == 0:
            city[x0][y0+1] = 1
            return x0, y0+1
    if city[x0+1][y0] == 0 and rnd != 0:
        rnd -= 1
        if rnd == 0:
            city[x0+1][y0] = 1
            return x0+1, y0
    if city[x0][y0-1] == 0 and rnd != 0:
        rnd -= 1
        if rnd == 0:
            city[x0][y0-1] = 1
            return x0, y0-1
    if city[x0-1][y0] == 0 and rnd != 0:
        rnd -= 1
        if rnd == 0:
            city[x0-1][y0] = 1
            return x0-1, y0


# Оля
def blind_alley(x, y):
    # (Тупик)
    # Проверка всех направлений на то была ли там собака
    # функция должна выводить 0(несработала) или 1(сработала)
    pass


# Оля
def border(x, y):
    # проверка на границу города
    # Заканчивается ли таблица с одной из сторон
    # функция должна выводить 0(несработала) или 1(сработала)
    pass


# Игорь
def dog(n):
    x, y = point(n)
    while blind_alley(x, y) == 0 or border(x, y) == 0:
        x, y = walk(x, y)
    if blind_alley(x, y) == 1:
        return 0
    else:
        return 1

    #  Просчитывает одно путешествие собаки в городе
    # выводит 0 при тупике и 1 при выходе из города


# Арсений
if __name__ == '__main__':
    # Множество повторений функции и вероятность
    pass
