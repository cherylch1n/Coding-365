#2.一元二次方程式I
#匯入數學工具箱
import math
#輸入
a=input()
b=input()
c=input()
#字串變成整數
a=int(a)
b=int(b)
c=int(c)
#題目給的公式 (數學根號)
x1=((-b)+math.sqrt(b*b-4*a*c))/(2*a)
x2=((-b)-math.sqrt(b*b-4*a*c))/(2*a)
#輸出
print("%.1f"%x1)
print("%.1f"%x2)