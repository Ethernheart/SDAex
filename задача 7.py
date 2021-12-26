#Дано пятизначное число. Найдите сумму его цифр.
num = int(input())
summ=0
for i in range(5):
  summ+=num%10
  num=num//10
print(summ)  
