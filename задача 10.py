#По данному натуральном n вычислите сумму 1!+3!+5!+7!+...+n! Если n – число, то
#последним в сумме взять предшествующее n нечетное число. В решении этой задачи
#можно использовать только один цикл.
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)


n = int(input())
if n%2==0:
    n=n-1
summ=0
for i in range(1,n+1,2):
    summ=summ+fact(i)
print(summ)

