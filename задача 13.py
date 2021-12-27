#Дана последовательность натуральных чисел, завершающаяся словом «stop».
#Определите, какое наименьшее число подряд идущих элементов этой
list=[]
i=0
while True:
    list.append(input())
    if list[i]=='stop':
        break
    i+=1
list.remove('stop')
min=list[0]
for i in range(1,len(list)):
    if list[i]<list[i-1]:
        min=list[i]
print(min)
