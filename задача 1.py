m=int(input())
h=0
while m>=60:
    m-=60
    h+=1
    if h==24:
        h-=24
print(h)
