#Выведите все элементы списка с нечетными индексами
list = input().split()
for i in range(1, len(list)):
  if i%2!=0:
    print(list[i], end=' ')
