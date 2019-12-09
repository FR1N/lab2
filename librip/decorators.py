# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно

def print_result(func):
    def wrapper(*args):
        print(func.__name__)
        if len(args) == 0:
            return_value = func()
        else:
            return_value = func(args[0])
        if type(return_value) == dict:
            for k, v in return_value.items():
                print(k, '=', v)
        elif type(return_value) == list:
            print(*return_value, sep='\n')
        else:
            print(return_value)
        return return_value
    return wrapper
