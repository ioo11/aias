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
        self.table = [[] for i in range(101)]
        self.max_num_of_collisions = 0
        self.all_num_of_collisions = 0

        temparr = read('./ContactList.txt')
        for i in temparr:
            h = self.__gethash__(i['name'])
            if self.table[h] != []:
                self.all_num_of_collisions+=1

            self.table[h].append(i)

            if len(self.table[h]) > self.max_num_of_collisions:
                self.max_num_of_collisions = len(self.table[h])

    def __str__(self):
        temp = ''
        j = 0
        for i in self.table:
            temp += (str(j) + ': ' + str(i)+'\n')
            j += 1
        return temp

    def __gethash__(self, name):
        """
        хеш-функция складывает все коды символов имени
        и берет остаток от деления на 100
        """
        h = 0
        for i in name:
            h += ord(i)
        h %= 100
        return h

    def addContact(self, contact):
        h = self.__gethash__(contact['name'])
        self.table[h].append(contact)

    def findContact(self, name):
        """
        считаем хеш-ключ, пробегаем по всем контактам,
        на которые он указывает и ищем совпадение по
        имени. если их нет, возвращаем строку.
        """
        h = self.__gethash__(name)
        counter = 0
        for j in self.table[h]:
            if j['name'] == name:
                return str(self.table[h][counter])
            counter += 1
        return 'Nothing was found'


    def deleteContact(self, name):
        """
        аналогично поиску, но не возвращаем, а печатаем
        затем удаляем.
        """
        h = self.__gethash__(name)
        counter = 0
        for j in self.table[h]:
            if j['name'] == name:
                print('Contact', self.table[h][counter], 'was destroyed')
                del self.table[h][counter]
            counter += 1


#Демонстрация:
#Создание таблицы:
a = Hash_table()
print(a)
# Добавление элемента:
# a.addContact({'name':'me', 'number':'132'})

# Поиск элемента:
# print(a.findContact('Clark'))
# print(a.findContact('me'))

# Удаление:
# a.deleteContact('me')
# print(a.findContact('me'))
# print(a)

# Подсчет коллизий:
# print(a.all_num_of_collisions)
# print(a.max_num_of_collisions)
