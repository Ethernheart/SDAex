#Даны четыре целых числа. Определите, сколько среди них совпадающих.
#Программа должна вывести одно из чисел: 4 (если все совпадают), 3 (если
#совпадают 3), 2 (если два совпадает) или 0 (если все числа различны).
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == b == c ==d:
    print(4)
elif a == b == c or a == c == d or b == c == d or b == a == d:
    print(3)
elif a == b or a == c or a == d or b == c or b == d or c == d:
    print(2)
else:
    print(0)
