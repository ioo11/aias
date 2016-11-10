"""
Класс предназначен для хранения контактов из ContactList.txt
Коллизии решаются с помощью линейных списков
Может выполнять:
1) Поиск элемента (берет имя, возвращает номер)
2) Удаление элемента (удаленный элемент помечается)
3) Считать коллизии
"""


class Contact:
    def __init__(self, name, number, readfile=False):
        if readfile:
            import 
        self.name = name
        self.number = number
        self.nextContact


class Hash_table:
    def __init__(self, *args):
        self.n = args

    def __gethash__(self):
        """
        хеш-функция складывает все цифры номера
        и берет остаток от деления на 50
        """
        h = 0
        for i in self.n:
            h += int(i)
        h %= 50
        return h

a = Hash_table('456')
print(a.__gethash__())