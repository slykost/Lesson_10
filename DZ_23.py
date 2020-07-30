# ДЗ-23. Реверс словаря
# Дан словарь (смотрите пример ниже) ключами которого являются английские слова,
# а занчениями - списки латинских слов. Необходимо развеннуть словарь.
# Другими словами, необходимо, на основании заданного словаря, создать новый словарь,
# у которого в качестве ключей будут взяты латинские слова, из исходного словаря,
# а значениями будет список, соответствующих им, английских слов.


d = {

   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'popum'],

   'punishment': ['malum', 'multa']

}

new_dict = {}

for key, value in d.items():
    for value in value:
        new_dict[value] = []
        for i in d.keys():
            if value in d[i]:
                new_dict[value].append(i)
print(new_dict)