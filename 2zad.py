num = int(
    input('Введите натуральное число для нахождения его простых множителей числа: '))
multiplier = 2
list1 = []
while multiplier <= num:
    if num % multiplier == 0:  
        list1.append(multiplier)
        num //= multiplier
    else:
        multiplier += 1
print('Простые множители введенного числа (делятся на 1 и само себя):', *list1)