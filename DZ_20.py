""" ДЗ-20. Конвертер чисел.

Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).

Небольшая подсказка. В этой задаче вам может понадобиться:

- список
- метод 'revers()' (или срез [::-1], или вместо 'revers()' использовать 'insert()' тогда не придётся
  разворачивать список), чтоб развернуть список, метод 'join()'

- строка 'ascii_uppercase' из модуля 'string' (её можно получить если сделать
  импорт 'from string import ascii_uppercase'), она содержит все буквы латинского алфавита."""


from string import ascii_uppercase

def convert(n, b):
    s = '0123456789' + ascii_uppercase
    while n > 0:
        n, i = n // b, n % b
        lst.append(s[i])
    lst.reverse()

n = int(input('Введите число: '))
sys_ischesl = int(input('Введите систему исчесления: '))
lst = []
convert(n, sys_ischesl)
print(''.join(lst))