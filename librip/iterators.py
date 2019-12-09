from types import GeneratorType


# Итератор для удаления дубликатов
class Unique(object):
    ignore_case = False
    current_list = []
    current = 0

    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
            self.items = items
        if type(items) == GeneratorType:
            self.items = list(items)
        else:
            self.items = items

    def __next__(self):
        if self.current != len(self.items):
            a = self.items[self.current]
            self.current += 1
            if self.ignore_case:
                a = a.lower()
            if a not in self.current_list:
                self.current_list.append(a)
                return a
            else:
                return next(self)
        else:
            raise StopIteration

    def __iter__(self):
        del self.current_list[:]
        self.current = 0
        return self
