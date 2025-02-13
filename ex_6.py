#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import Timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = r"C:\Users\Соня\PycharmProjects\laba2\data_light_cp1251.json"

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return sorted(list(unique(field(arg, 'job-name'), ignore_case=True)))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))
    # return list(filter(lambda x: re.match(r'Программист',x['job-name']), data))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


salary = []
@print_result
def f4(arg):
    for i, j in zip(arg, gen_random(100000, 200000, 100)):
        salary.append(i + ', зарплата ' + str(j) + ' руб')
    return salary


with Timer():
    f4(f3(f2(f1(data))))
