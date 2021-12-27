#Последовательность состоит из натуральных чисел и завершается словом «stop».
#Определите, сколько элементов этой последовательности больше предыдущего
#элемента в два раза.
list=[]
i=0
cnt=0
while True:
    list.append(input())
    if list[i]=='stop':
        break
    i+=1
list.remove('stop')
for i in range(len(list)):
    list[i]=int(list[i])
for i in range(1, len(list)):
    if list[i]==(2*list[i-1]):
        cnt+=1
print(cnt)
