#По данному натуральному числу N найдите наименьшую целую степень двойки,
#превосходящую N. Выведите показатель степени и саму степень. Операцией
#возведения в степень пользоваться нельзя!
m = int(input())
i=1
n=2
while n<=m:
    n=n*2
    i+=1
print(i,n)
