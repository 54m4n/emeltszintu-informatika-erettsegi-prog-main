import os
import sys

os.system('cls') #if it is win
#os.system('clear') #if it is unix

#--1--
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}naplo.txt')
l=f.read().split('# ')
f.close()

hianyzasok=[]

for line in l:
    if not line.strip():
        continue    
    hianyzasok.append(line.split('\n'))

hiany=[]
ertek=[]

for i in range(len(hianyzasok)):
    honap=str(hianyzasok[i][0]).split(' ')[0]
    nap=str(hianyzasok[i][0]).split(' ')[1]
    for j in range(1,len(hianyzasok[i])):
        if len(hianyzasok[i][j])>0:
            ertek.append(hianyzasok[i][j])
    hiany.append([honap,nap,ertek])
    ertek=[]

#--2--
print('--2--')

c=0
for i in range(len(hiany)):
    c=c+len(hiany[i][2])

print(f'a naploban: {c} bejegyzes van')

#--3--
print('--3--')
igazolt=0
igazolatlan=0
for i in range(len(hiany)):
    for j in range(len(hiany[i][2])):
        for k in range(len(str(hiany[i][2][j]).split(' ')[2])):
            if (str(hiany[i][2][j]).split(' ')[2][k])=="X":
                igazolt=igazolt+1
            if (str(hiany[i][2][j]).split(' ')[2][k])=="I":
                igazolatlan=igazolatlan+1

print(f'igazolt: {igazolt} igazolatlan: {igazolatlan}')

#--4--
print('--4--')