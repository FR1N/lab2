# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5

import time

class Timer:

    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        print(time.time() - self.start)