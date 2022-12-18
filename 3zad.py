from random import randrange

quantity = 10
list1 = [randrange(5) for i in range(quantity)]
print('Список из случайных чисел:', *list1)

list2 = []
for k in list1:
    b = 0
    for g in list1:
        if k == g:
            b += 1
    if b == 1:
        list2.append(k)
print('Уникальные элементы списка:', *list2)