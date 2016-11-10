"""Быстрая сортировка"""


def quick_sort(a):
    i = 0
    j = len(a)-1
    p = a[(len(a))//2]
    while i <= j:
        while a[i] < p:
            i += 1
        while a[j] > p:
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
