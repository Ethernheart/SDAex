#Дан список чисел. Выведите значение наименьшего элемента в списке, а затем
#индекс этого элемента в списке (если их несколько – выведите индекс последнего
#из них). Если все числа равные, вывести «Наименьшего нет»
list = input().split()
minn=list[0]
iminn=0
for i in range(len(list)):
    if minn>=list[i]:
        minn=list[i]
        iminn=i
if len(set(list))==1:
    print("naimen'shego net")
else:
    print("index -", iminn, "chislo -",minn )
