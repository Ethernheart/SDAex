#Дан двумерный массив и два числа: i и j. Поменяйте в массиве строки с
#номерами i и j и выведите результат. Выведите полученный массив на экран,
#разделяя элементы массива пробелами. Программа получает на вход размеры
#массива n и m, затем элементы массива, затем числа i и j.
s1 = int(input())
s2 = int(input())
n = int(input())
m = int(input())
mat1 = [[int(input()) for j in range(m)] for i in range(n)]
mat2=[]
j=0
for i in range(n):
    mat2.append(mat1[s1][j])
    j+=1
for i in range(n):
    for j in range(m):
        if i == s1:
            mat1[s1][j] = mat1[s2][j]
for i in range(n):
    for j in range(m):
        if i == s2:
            mat1[s2][j]=mat2[j]
for i in range(n):
    for j in range(m):
        print(mat1[i][j], end= ' ')
    print()
        
