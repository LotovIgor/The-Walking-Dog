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
    # return x,y
    pass


# Игорь
def up(x, y):
    if city[x][y + 1] == 0:
        city[x][y + 1] = 1
        return x, y + 1
    else:
        return x, y


# Игорь
def down(x, y):
    pass


# Игорь
def right(x, y):
    pass


# Игорь
def left(x, y):
    pass


# Игорь
def walk(x, y):
    # Шаг собаки
    rnd = random.randint(1,4)
    if rnd == 1:
        # up
        pass
    if rnd == 2:
        # right
        pass
    if rnd == 3:
        # down
        pass
    if rnd == 4:
        # left
        pass
    pass


# Оля
def blind_alley(x, y):
    # (Тупик)
    # Проверка всех направлений на то была ли там собака
    pass


# Оля
def border(x, y):
    # проверка на границу города
    # Заканчивается ли таблица с одной из сторон
    pass


# Игорь
def dog(n):
    #  Просчитывает одно путешествие собаки в городе
    pass


# Арсений
if __name__ == '__main__':
    # Множество повторений функции и вероятность
    pass
