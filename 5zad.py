t = open('file1.txt', 'w', encoding = 'UTF-8')
t.write('2*x² + 4*x + 5')
t.close()

t = open('file2.txt', 'w', encoding = 'UTF-8')
t.write('41*x^3 + 6*x² + 2*x + 98')
t.close()

r = open('file1.txt', encoding = 'UTF-8')
h = r.read()
print(h)
r.close()

r = open('file2.txt', encoding = 'UTF-8')
b = r.read()
print(b)
r.close()

# сам создаст файл result.txt, если его нет
q = open('result.txt', 'w', encoding = 'UTF-8')
q.write(h + ' + ' + b + ' = 0')
q.close()

# теперь прочитаем его
q = open('result.txt', encoding = 'UTF-8')
b = q.read()
print(b)
r.close()