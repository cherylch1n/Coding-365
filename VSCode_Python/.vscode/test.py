#5
a=input()
a=a.split(" ")
x1=int(a[0])
x2=int(a[1])
x3=int(a[2])
x4=int(a[3])
x5=int(a[4])
ave=(x1+x2+x3+x4+x5)/5.0
y1=int(ave*100)/100
print('%.2f'%ave)
var=((x1-ave)**2+(x2-ave)**2+(x3-ave)**2+(x4-ave)**2+(x5-ave)**2)/5.0
y2=int(var*100)/100
print('%.2f'%y2)
ad=(var)**(0.5)
y3=int(ad*100)/100
print('%.2f'%y3)