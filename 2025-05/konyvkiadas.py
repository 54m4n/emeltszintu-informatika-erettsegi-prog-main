import os
import platform

if platform.system()=='Windows':
    os.system('cls')
else:
    os.system('clear')

#--1--
path=os.path.dirname(__file__)
konyvek=[]
f=open(f'{path}{os.sep}src{os.sep}kiadas.txt', encoding="utf8")
for l in f:
    konyvek.append(l.strip().split(';'))
f.close()

#--2--
print('--2--')
szerzo='Benedek Elek'
c=0
for i in range(len(konyvek)):
    for j in range(len(konyvek[i])):
        if szerzo in konyvek[i][j]:
            c=c+1
print(f'{szerzo} osszesen {c} alkalommal szerepel.')

#--3--
print('--3--')
max=int(konyvek[0][len(konyvek[0])-1])
for i in range(len(konyvek)):
    if int(konyvek[i][len(konyvek[i])-1])>=max:
        max=int(konyvek[i][len(konyvek[i])-1])
c=0
for i in range(len(konyvek)):
    if int(konyvek[i][len(konyvek[i])-1])==max:
        c=c+1
print(f'legnagyobb peldanyszam: {max}, elofordult {c} alkalommal')

#--4--
print('--4--')
megvan=False
i=0
while i<len(konyvek) and megvan==False:
    if (konyvek[i][2]=="kf") and (int(konyvek[i][4])>=40000):        
        megvan=True
    i=i+1

print(f'{konyvek[i-1][0]}/{konyvek[i-1][1]} {konyvek[i-1][3]}')
    