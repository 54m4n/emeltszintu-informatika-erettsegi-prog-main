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
       

    
    
#--4--
print('--4--')

f=0
t=0
tmp=0

iscity=False
cway=0

for i in range(len(ut)):       
    if len(str(ut[i][1]))<4 and iscity==True:
        cway=cway+(ut[i-1][0]-ut[i][0])
    if len(str(ut[i][1]))>=4:
        iscity=True
    if isinstance(ut[i][1],int)==False and str(ut[i][1][0])==']':
        iscity=False

print(f'Az ut {round(abs(cway)/(sumroad/100),2)}%-a vezet telepulesen.')
        
