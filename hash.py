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
    def __init__(self, readfile=False, *args):
        self.table = [None for i in range(20)]

        if readfile:
            temparr = read('./ContactList.txt')
        else:
            temparr = args

        for i in temparr:
            h = self.__gethash__(i['number'])
            if self.table[h] is None:
                self.table[h] = i
            else:
                """
                ИСПРАВИТЬ
                сейчас при возникновении коллизии элементы
                дописываются в конец, расширяя массив
                """
                self.table.append(i)

    def __str__(self):
        temp = ''
        for i in self.table:
            temp += (str(i)+'\n')
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

    class Contact:
        def __init__(self, name, number):
            self.name = name
            self.number = number
            self.nextContact = None


a = Hash_table('456')
print(a)
