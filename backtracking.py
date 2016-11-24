"""
7. Есть п предметов, каждый i предмет имеет массу Mi
и стоимость Ci. Есть рюкзак; максимальная масса
предметов, которую он выдерживает, равна М. Надо
выбрать предметы для укладки в рюкзак так, чтобы
сумма стоимости их была максимальной, а суммарная
масса не превышала M. 
1) Создается массив из словарей вида
    {'item':str, 'cost':int, 'weight':int}
2) Сортируется по возрастанию цены
3) Алгоритм перебора с возвратом
"""


def read_file(path):
    try:
        file = open(path)
        result = []
        for row in file:
            temp = row.split(' ')
            temp = {'item': temp[0],
                    'weight': int(temp[1]),
                    'cost': int(temp[2].rstrip('\n'))}
            result.append(temp)
        return result
    except Exception as e:
        print(e)
    finally:
        file.close()

def quick_sort(a):
    i = 0
    j = len(a)-1
    p = a[(len(a))//2]
    while i <= j:
        while a[i]['cost'] < p['cost']:
            i += 1
        while a[j]['cost'] > p['cost']:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if j > 0:
        a[:j+1] = quick_sort(a[:j+1])
    if i < len(a)-1:
        a[i:] = quick_sort(a[i:])
    return a







a = read_file('./itemlist.txt')
b = quick_sort(a)
for x in b:
    print(x)