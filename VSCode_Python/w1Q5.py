#5.五個數字(計算出平均數、變異數、標準差)
#輸入字串，並切割
a=input()
a=a.split(' ')
#平均數，x是變數，in+參數(參考的數字)
    #a[:]=[int(x)for x in a]
    #x=a[0]+a[1]+a[2]+a[3]+a[4]
    #aver=x/5
x1=int(a[0])
x2=int(a[1])
x3=int(a[2])
x4=int(a[3])
x5=int(a[4])
ave=(x1+x2+x3+x4+x5)/5
y1=int(ave*100)/100
print('%.2f'%y1)
#變異數
var=((x1-ave)**2+(x2-ave)**2+(x3-ave)**2+(x4-ave)**2+(x5-ave)**2)/5
y2=int(var*100)/100
print('%.2f'%y2)
#標準差(**0.5就是開根號)
ad=var**(0.5)
y3=int(ad*100)/100
print('%.2f'%y3)