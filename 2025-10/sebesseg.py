import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
print('--1--')

path=os.path.dirname(__file__)

f=open(f'{path}{os.sep}src{os.sep}ut.txt')

ut=[]
c=0
for i in f:
    if c==0:
        sumroad=int(i)
    else:
        a=int(i.strip().split()[0])
        try:
            b=int(i.strip().split()[1])
        except:
            b=i.strip().split()[1]        
        ut.extend([[a,b]])
    c=c+1
f.close()

#--2--
print('--2--')

for i in range(len(ut)):
    if len(str(ut[i][1]))>=4:
        print(ut[i][1])
       
    
    
#--3--
print('--3--')

