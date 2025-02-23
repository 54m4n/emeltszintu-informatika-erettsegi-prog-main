import os
import platform

if platform.system()=='Windows':
    os.system('cls')
else:
    os.system('clear')

#--1--
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}lista.txt')

c=0
i=0
sorozat=[]
sztring=""

for l in f:
    sztring=str(sztring)+" "+str(l.strip())
    if i%4==0 and i!=0:
        sorozat.append(sztring.split())
        sztring=""
        i=-1
    i=i+1
f.close()

print(sorozat[0])
#--2--
print('--2--')
count=0
for i in range(len(sorozat)):
    if sorozat[i][0]=="NI":
        count=count+1
print(f'{len(sorozat)-count} epizod air-on datuma ismert.')

#--3--
print('--3--')
latta=0
nemlatta=0
for i in range(len(sorozat)):
    if sorozat[i][4]=="0":
        nemlatta=nemlatta+1
    else:
        latta=latta+1
        
print(latta,nemlatta,len(sorozat))
    
print(f'{(len(sorozat)/100)*count}')