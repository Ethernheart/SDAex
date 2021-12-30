#Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его
#числами – суммами индексов элементов. Выведите полученный массив на экран,
#разделяя элементы массива пробелами.
n = int(input())
m = int(input())
mat1 = [[i+j for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if i+j<10:
            print(mat1[i][j], end= '  ')
        else:
            print(mat1[i][j], end=' ')
    print()
        
