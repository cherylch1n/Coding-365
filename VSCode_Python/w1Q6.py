#6.一元二次方程式2
import math
a=int(input())
b=int(input())
c=int(input())
T=b*b-4*a*c
#實根
if T>=0:
    x1=int((-b+math.sqrt(T))/(2*a)*10)/10.0
    x2=int((-b-math.sqrt(T))/(2*a)*10)/10.0
    print('%.1f'%x1)
    print('%.1f'%x2)
#虛根(x3是實數部分，x4是虛數部分)
elif T<0:
    x3=int((-b)/(2*a)*10)/10.0
    x4=int((math.sqrt(abs(T)))/(2*a)*10)/10.0
#虛數部分，手動變號
    if x4<0:
        x4=abs(x4)
        print('%.1f-%.1fi'%(x3,x4))
        print('%.1f+%.1fi'%(x3,x4))
    elif x4>=0:
        print('%.1f+%.1fi'%(x3,x4))
        print('%.1f-%.1fi'%(x3,x4))
