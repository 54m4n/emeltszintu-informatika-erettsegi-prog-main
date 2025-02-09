import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--

path=os.path.dirname(__file__)
rows=[]
f=open(f'{path}{os.sep}src{os.sep}ajto.txt','r')
for line in f:
    rows.append(line.strip().split(' '))
f.close()

#--2--
print('--2--')

print(f'elso bemeno szemely ID: {rows[0][2]}')

i=len(rows)-1
while rows[i][3]!="ki":
    i=i-1

print(f'utso kimeno szemely ID: {rows[i][2]}')

#--3 es 4--
print('--3 es 4--')
athaladas=[]
uniqid=[]
osszathaladas=[]
for i in range(len(rows)):
    athaladas.append(rows[i][2])
    if rows[i][2] not in uniqid:
        uniqid.append(rows[i][2])

bennmaradt=[]
fw=open(f'{path}{os.sep}src{os.sep}athaladas.txt','w')    
for i in range(len(uniqid)):
    fw.write(f'{uniqid[i]} {athaladas.count(uniqid[i])}\n')
    if (athaladas.count(uniqid[i])%2!=0):
        bennmaradt.append(uniqid[i])
fw.close()
bennmaradt.sort()
print(f'a vegen a tarsalgoban voltak: {bennmaradt}')

#--5--
bent=0
max=0
idopont=""

for i in range(len(rows)):
    if rows[i][3]=="be":
        bent=bent+1
        if bent>max:
            max=bent
            idopont=(f'{rows[i][0]}:{rows[i][1]}')
    else:
        bent=bent-1
    
print(f'{idopont}-kor voltak a legtobben a tarsalgoban')

#--6 es 7--
print('--6 es 7--')

emberid=22
jonmegy=[]
for i in range(len(rows)):
    if rows[i][2]=="22":
        jonmegy.append(f'{rows[i][0]}:{rows[i][1]}')

for i in range(len(jonmegy)):
    print(jonmegy[i])
    