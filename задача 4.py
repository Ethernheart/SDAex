#Паркетный пол разделен на n×m дощечек. Паркет для очистки разделили по прямой
#на две части. Определите, можно ли таким образом отделить участок пола,
#состоящий ровно из k дощечек. Программа должна вывести YES или NO.
n = int(input())
m = int(input())
k = int(input())
if (k%n==0 or k%m==0) and n*m>k:
    print('YES')
else:
    print('NO')
