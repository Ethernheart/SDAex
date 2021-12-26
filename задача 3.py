gr1 = int(input())
gr2 = int(input())
gr3 =int(input())
if gr1%2==0:
    tbl=gr1/2 
else:
    tbl=gr1//2+1
if gr2%2==0:
    tbl+=gr2/2 
else:
    tbl+=gr2//2+1
if gr3%2==0:
    tbl+=gr3/2 
else:
    tbl+=gr3//2+1
print(int(tbl))
