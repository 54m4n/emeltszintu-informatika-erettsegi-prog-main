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

#--5--
print('--5--')
ido=[10,11,12]
idosec=mpbe(ido[0],ido[1],ido[2])

megvan=False
i=0

varakozok=0
akthivonum=0

while i<len(input):
    h1=int(input[i][0])
    m1=int(input[i][1])
    s1=int(input[i][2])
    h2=int(input[i][3])
    m2=int(input[i][4])
    s2=int(input[i][5])
    if megvan!=True and (mpbe(h1,m1,s1)<idosec and mpbe(h2,m2,s2)>idosec):
        varakozok=varakozok+1
    
    if (mpbe(h1,m1,s1)>=idosec or mpbe(h2,m2,s2)>=idosec) and megvan!=True:
        megvan=True
        akthivonum=i+1
    i=i+1

<<<<<<< HEAD
print(i,akthivonum,varakozok) 
=======
print(i,akthivonum,varakozok)
>>>>>>> 964a9d62660d3e25f9941fd23df558bbbe25fede