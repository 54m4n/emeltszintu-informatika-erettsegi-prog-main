import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--

path=os.path.dirname(__file__)
osv=open(f'{path}{os.sep}src{os.sep}osvenyek.txt')
osvenyek=[]
for l in osv:
    osvenyek.append(l.strip())
osv.close()

dob=open(f'{path}{os.sep}src{os.sep}dobasok.txt')
dobasok=[]

for l in dob:
    dobasok=l.strip().split(' ')

#--2--
print('--2--')
print(f'osveny dbszam: {len(osvenyek)}, dobas dbszam: {len(dobasok)}')

#--3--
print('--3--')

max=len(osvenyek[0])

for i in range(len(osvenyek)):
    if len(osvenyek[i])>max:
        max=len(osvenyek[i])
        tmpi=i+1
    
print(f'az egyik leghosszabb osveny az alabbi sorban talalhato: {tmpi}. es {max} hosszu')

#--4--
print('--4--')
osvnum=9
gamers=5

#--5--
print('--5--')

m=0
e=0
v=0
print(osvenyek[osvnum-1])
for i in range(len(osvenyek[osvnum-1])):
    if osvenyek[osvnum-1][i]=="M":
        m=m+1
    if osvenyek[osvnum-1][i]=="E":
        e=e+1
    if osvenyek[osvnum-1][i]=="V":
        v=v+1

if m!=0:
    print(f'M: {m}')
if v!=0:
    print(f'V: {v}')
if e!=0:
    print(f'E: {e}')

#--6--
print('--6--')

for i in range(len(osvenyek[osvnum-1])):
    if osvenyek[osvnum-1][i]!="M":
        print(f'{i+1}\t{osvenyek[osvnum-1][i]}')