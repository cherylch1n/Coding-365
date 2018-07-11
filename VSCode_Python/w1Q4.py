#4.判斷何種三角形
#輸入
x=input()
#依題目，三個字串切割(以空格做分割)
x=x.split(' ')
#輸入的一行有三個字串，將字串變成整數
a=int(x[0])
b=int(x[1])
c=int(x[2])
#不能成為三角形：任兩邊和不大於第三邊，或任一邊長不大於 0，輸出1
if a+b<=c or a+c<=b or b+c<=a or a<=0 or b<=0 or c<=0:
    print(1)
#正三角形：三個邊相等，輸出2
elif a==b==c:
    print(2)
#等腰三角形：任兩邊相等，平方和大於第三邊的平方，輸出3
elif a==b!=c or a==c!=b or b==c!=a:
    print(3)
#一般三角形：非正三角形與等腰三角形，輸出4
else:
    print(4)