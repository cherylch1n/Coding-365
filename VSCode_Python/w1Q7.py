#7.書錢及折扣
#輸入
x=input()
y=input()
z=input()
#字串變成整數
x=int(x)
y=int(y)
z=int(z)
#  定價 1~10本 11~20本 21~30本 31本以上
#A 380  原價   9折     8.5折   8折
if x<=10:
    a=x*380
elif x<=20:
    a=x*380*0.9
elif x<=30:
    a=x*380*0.85
else :
    a=x*380*0.8
#B 1200 原價 9.5折 8.5折 8折
if y<=10:
    b=y*1200
elif y<=20:
    b=y*1200*0.95
elif y<=30:
    b=y*1200*0.85
else :
    b=y*1200*0.8
#C 180 原價 8.5折 8折 7折
if z<=10:
    c=z*180
elif z<=20:
    c=z*180*0.85
elif z<=30:
    c=z*180*0.8
else :
    c=z*180*0.7
# %d以整數的方式輸出
print('%d'%(a+b+c))