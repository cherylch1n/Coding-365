#3.數值運算
#輸入
num1=input()
num2=input()
#字串變成整數
num1=int(num1)
num2=int(num2)
#加減乘除
x1=num1+num2
x2=abs(num1-num2)
x3=num1*num2
x4=num1/num2
#會四捨五入，但不影響結果
a=('%.2f'%x1)
b=('%.2f'%x2)
c=('%.2f'%x3)
#題目:結果需輸出到小數點第二位→如果四捨五入會影響結果，所以不要四捨五入，直接取到小數點第二位
d=x4*100
d=int(d)
e=d/100
e=('%.2f'%e)
#輸出
print('Sum:'+a)
print('Difference:'+b)
print('Product:'+c)
print('Quotient:'+e)