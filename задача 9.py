#По данному натуральному m вычислите сумму 12+22+32+...+n2
n=int(input())
summ=0
for i in range(n+1):
    summ=summ+i**2;
print(summ)
