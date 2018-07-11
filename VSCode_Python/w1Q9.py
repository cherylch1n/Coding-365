#9.判斷何種三角形(直角、鈍角、銳角)
#輸入字串，並切割
x=input()
x=x.split(' ')
#將三個字串變成整數
a=int(x[0])
b=int(x[1])
c=int(x[2])
#不是三角形
if a+b<=c or b+c<=a or a+c<=b or a<=0 or b<=0 or c<=0:
    print('Not Triangle')
#直角三角形(兩個邊的平方和等於第三邊的平方)
elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
    print('Right Triangle')
#鈍角三角形(兩個邊的平方和小於第三邊的平方)
elif a**2+b**2<c**2 or b**2+c**2<a**2 or a**2+c**2<b**2:
    print('Obtuse Triangle')
#銳角三角形(兩邊的平方和大於第三邊的平方)
else :
    print('Acute Triangle')