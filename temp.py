"""
Пусть i - индекс начала массива,
j - индекс конца массива
p - индекс опорного элемента
"""
import random


def quick_sort(a):
    i = 0
    j = len(a)-1
    p = a[(len(a))//2]
    print('Зашел в новую сортировку\n', a)
    print('i = ', i)
    print('j = ', j)
    print('p = ', p)
    while i <= j:
        while a[i] < p:
            i += 1
        print('i =', i)

        while a[j] > p:
            j -= 1
        print('j =', j)
        print('a[i], a[j], которые хочу менять ', a[i], a[j])
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        print(i, j)
        print(a)
    if j > 0:
        a[:j+1] = quick_sort(a[:j+1])
    if i < len(a)-1:
        a[i:] = quick_sort(a[i:])
    return a


print(quick_sort([random.randint(0, 10) for i in range(0, 10)]))
