#8.最佳資費選擇
#五個輸入值，字串變成整數
a=input()
a=int(a)
b=input()
b=int(b)
c=input()
c=int(c)
d=input()
d=int(d)
e=input()
e=int(e)
#第n種租費
n=a*0.08+b*0.139+c*0.135+d*1.128+e*1.483
#租費小於等於183元，則用183型
if n<=183:
    x=183
#否則租費為n元
else:x=n
#第p種租費
p=a*0.07+b*0.130+c*0.121+d*1.128+e*1.483
#租費小於等於383元，則用383型
if p<=383:
    y=383
#否則租費為p元
else:y=p
#第q種租費
q=a*0.06+b*0.108+c*0.101+d*1.128+e*1.483
#租費小於等於983元，則用983型
if q<=983:
    z=983
#否則租費為q元
else:z=q
#x最小的情況下，使用183型
if x<y<z or x<z<y:
    print('183')
    print('%.f'%x)
#y最小的情況下，使用383型
elif y<x<z or y<z<x:
    print('383')
    print('%.f'%y)
#z最小的情況下，使用983型
else:
    print('983')
    print('%.f'%z)