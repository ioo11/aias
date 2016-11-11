"""
Предназначен для хранения контактов из ContactList.txt
Коллизии решаются с помощью линейных списков
Может выполнять:
1) Поиск элемента (берет имя, возвращает номер)
2) Удаление элемента (удаленный элемент помечается)
3) Считать коллизии
"""

from readfile import read_file as read


class Hash_table():
    def __init__(self, *args):
        self.table = [None for i in range(20)]
        temparr = read('./ContactList.txt')
        for i in temparr:
            h = self.__gethash__(i['number'])
            i['NextContact'] = None
            if self.table[h] is None:
                self.table[h] = i
            else:
                self.table[h]['NextContact'] = i

    def __str__(self):
        temp = ''
        j = 0
        for i in self.table:
            temp += (str(j) + ': ' + str(i)+'\n')
            j += 1
        return temp

    def __gethash__(self, number):
        """
        хеш-функция складывает все цифры номера
        и берет остаток от деления на 20
        """
        h = 0
        for i in number:
            h += int(i)
        h %= 20
        return h


a = Hash_table('456')
print(a)
