#Дан список чисел. Выполнить его сортировку по возрастанию.
list = input().split()
for i in range(len(list)):
    list[i]=int(list[i])
list=sorted(list)
for i in range(len(list)):
    print(list[i], end=' ')
