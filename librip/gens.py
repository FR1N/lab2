import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(d, *args):
    if len(args) == 1:
        for i in range(len(d)):
            if d[i].get(*args) is not None:
                yield d[i].get(*args)
    else:
        for i in range(len(d)):
            x = list(d[i])
            s = d[i].copy()
            for k in range(len(x)):
                if x[k] not in args:
                    s.pop(x[k])
            if len(s) != 0:
                yield s


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(a, b, c):
    for i in range(c):
        yield random.randint(a, b)
    # Необходимо реализовать генератор
