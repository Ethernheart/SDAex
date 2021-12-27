#Дан список чисел. Выведите все элементы списка, которые меньше следующего
#элемента.
list=input().split()
m=int(input())
print("chisla men'she",m)
for i in range(len(list)):
    list[i]=int(list[i])
    if list[i]<m:
        print(list[i], end=' ')
