from math import pi
correct = int(input('Задайте точность числа Пи: '))
stroka = str(pi)
print(float(stroka[0:correct + 2]))