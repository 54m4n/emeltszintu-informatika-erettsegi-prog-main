import os
import sys

os.system('cls')

#--1--
def mpbe(h,m,s):
    sec=h*3600+m*60+s
    return sec

#--2--
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}hivas.txt')
l=f.readlines()
f.close()

input=[]

for i in range(len(l)):
    input.append(l[i].split())

#--3--
print('--3--')

c=0
elsohivas=input[0][0]

for i in range(len(input)):    
    if elsohivas==input[i][0]:
        c=c+int(input[i][0].count(elsohivas))
    else:        
        print(f'{elsohivas}: {c}')
        elsohivas=input[i][0]
        c=1
        
#--4--
print('--4--')
max=0
for i in range(len(input)):
    h1=int(input[i][0])
    m1=int(input[i][1])
    s1=int(input[i][2])
    h2=int(input[i][3])
    m2=int(input[i][4])
    s2=int(input[i][5])
    start=int(mpbe(h1,m1,s1))
    stop=int(mpbe(h2,m2,s2))
    if(stop-start)>=max:
        max=stop-start

print(f'leghosszabb hivas masodpercben: {max}')