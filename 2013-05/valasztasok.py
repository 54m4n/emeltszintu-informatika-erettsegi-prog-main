import os
import math

#--1--

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}szavazatok.txt')

szavazatok=[]

for i in f:
    szavazatok.append(i.split())

#['5', '19', 'Ablak', 'Antal', '-']

#--2--
print('--2--')

print(f'a helyhatosagi valasztasokon {len(szavazatok)} kepviselojelolt indult')

#--3--
print('--3--')

vnev="Kapor"
knev="Karola"

#vnev=str(input('kerem a vezeteknevet: '))
#knev=str(input('kerem a keresztnevet: '))


van=False
for i in range(len(szavazatok)):
    if szavazatok[i][2]==vnev and szavazatok[i][3]==knev:
        print(f'{vnev} {knev} osszesen {szavazatok[i][1]} db szavazatot kapott')
        van=True

if van==False:
    print(f'{vnev} {knev} nem szerepel az adatbazisban')

#--4--
print('--4--')

total=0
for i in range(len(szavazatok)):    
    total=total+int(szavazatok[i][1])

ossztabor=12345
arany=total/(ossztabor/100)

print(f'a valasztason {total} allampolgar vett reszt a {ossztabor}-bol, ami {round(arany,2)}%-os reszvetel')


#--5--
print('--5--')

partok=[
    ['Gyumolcsevok Partja',0],
    ['Husevok Partja',0],
    ['Tejivok Szovetsege',0],
    ['Zoldsegevok Partja',0],
    ['Fuggetlen Jeloltek',0]]


for i in range(len(szavazatok)):
    if szavazatok[i][4]=='GYEP':
        partok[0][1]=partok[0][1]+int(szavazatok[i][1])
    if szavazatok[i][4]=='HEP':
        partok[1][1]=partok[1][1]+int(szavazatok[i][1])
    if szavazatok[i][4]=='TISZ':
        partok[2][1]=partok[2][1]+int(szavazatok[i][1])
    if szavazatok[i][4]=='ZEP':
        partok[3][1]=partok[3][1]+int(szavazatok[i][1])
    if szavazatok[i][4]=='-':
        partok[4][1]=partok[4][1]+int(szavazatok[i][1])


for i in range(len(partok)):
    print(f'{partok[i][0]}={round(int(partok[i][1])/((total/100)),2)}%')


#--6--
print('--6--')

jeloltek=[]

max=0


for i in range(len(szavazatok)):
    if int(szavazatok[i][1])>=max:
        max=int(szavazatok[i][1])

for i in range(len(szavazatok)):    
    if int(szavazatok[i][1])==max:
        jeloltek.append(szavazatok[i])

print('legtobb szavazatot kapott/kaptak:\n')

for i in range(len(jeloltek)):
    tpart=jeloltek[i][4]
    if tpart=="-":
        tpart="fuggetlen"

    print(f'{jeloltek[i][0]} {jeloltek[i][2]} {jeloltek[i][3]} {tpart}')