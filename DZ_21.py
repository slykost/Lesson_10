""" ДЗ-21. Реверс списка.

Необходимо написать функцию которая разворачивает исходный список наоборот.

Алгоритм прост и ваши действия заключаются в следующем: мы меняем местами 0-ый элемент с последним,
1-ый с предпоследним и д.т.

Итого количество таких обменов будет равно половине длины списка.
Иначе элементы поменяются местами по-второму кругу и вернутся в первоначальное положение.

Применять функцию revers() или срезы с шагом -1 нельзя. Так же, нельзя использовать дополнительные переменные
(можно использовать переменную цикла for) и списки."""

from random import randint

lst = [randint(0, 100) for _ in range(int(input('Введите количество чисел в списке: ')))]
print(lst)

def rev_list(lst):
    if len(lst) % 2 == 1:
        middle_lst = len(lst) // 2
        for i in range(len(lst)):
            if i == middle_lst:
                break
            lst[i], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[i]
    else:
        middle_lst = (len(lst) // 2) - 1
        for i in range(len(lst)):
            if i > middle_lst:
                break
            lst[i], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[i]

rev_list(lst)
print(lst)