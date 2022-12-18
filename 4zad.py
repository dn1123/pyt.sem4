from random import randint

K = int(input('Введите степень k: '))

for i in range(K, 0, -1):          # range(старт, стоп, шаг)
    ratio = randint(1, 101)
    # if ratio == 0: # randint начинается от 1
    #     continue
    if ratio == 1:
        ratio = ''
    else:
        ratio = f'{ratio}·x^{i} +' if i != 1 else f'{ratio}·x +'
        print(ratio, end=' ')

print(f'{randint(1, 101)} = 0')