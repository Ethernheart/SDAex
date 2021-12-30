import re
n = int(input())
txt = [input() for i in range(n)]
for i in range(n):
    txt[i] = txt[i].replace(',',' ')
    txt[i] = txt[i].replace('.',' ')
    txt[i] = txt[i].replace('-',' ')
    txt[i] = txt[i].replace('...',' ')
    txt[i] = txt[i].replace('"',' ')
    txt[i] = txt[i].replace('!',' ')
    txt[i] = txt[i].replace('?',' ')
    txt[i] = txt[i].replace(';',' ')
    txt[i] = txt[i].replace(':',' ')
for i in range(n):
    txt[i] = txt[i].split()
for i in range(n):
    for j in range(len(txt[i])):
        txt[i][j]=len(txt[i][j])
for i in range(n):
    txt[i].sort()
for i in range(n):
    for j in range(1, len(txt[i])):
        if txt[i][j]!=txt[i][j-1]:
            print(txt[i][j])
            
