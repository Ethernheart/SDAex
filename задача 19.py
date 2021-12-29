#Найдите сумму первых индексов (S1) и сумму вторых индексов (S2) всех вхождений
#минимального элемента. Выведите два числа: S1 и S2. Если все числа равны,
#выведите «Минимального элемента нет». Программа получает на вход размеры
#массива n и m, затем n строк по m чисел в каждой
n = int(input())
m = int(input())
mat = [[int(input()) for j in range(m)] for i in range(n)]
minn = mat[0][0]
s1 = 0
s2 = 0
check = 0
for i in range(n):
    for j in range(m):
        if minn > mat[i][j]:
            minn = mat[i][j]
for i in range(n):
    for j in range(m):
        if minn == mat[i][j]:
            check += 1
if check != n*m:
    for i in range(n):
        for j in range(m):
            if mat[i][j] == minn:
                s1 += i
                s2 += j
    print('S1 = ', s1,' S2 = ', s2)
else:
    print('Minimalnogo elementa net')
