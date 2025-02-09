import os
import platform
import random

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')
    
#--1--
path=os.path.dirname(__file__)

kerites=[]

f=open(f'{path}{os.sep}src{os.sep}kerites.txt')
for l in f:
    kerites.append(l.strip().split(' '))
f.close()

#--2--
print('--2--')
print(f'{len(kerites)} db. telket adtak el az utcaban')

#--3 es 4--
print('--3 es 4--')
paros=0
paratlan=-1
hsz=0
hazak=[]
szinek=[]
for i in range(len(kerites)):
    if kerites[i][2] not in szinek and (kerites[i][2]!=":" and kerites[i][2]!="#"):
        szinek.append(kerites[i][2])
    if int(kerites[i][0])==0:
        paros=paros+2
        hazak.append([paros,kerites[i][0],kerites[i][1],kerites[i][2]])
    else:
        paratlan=paratlan+2
        hazak.append([paratlan,kerites[i][0],kerites[i][1],kerites[i][2]])

if int(kerites[len(kerites)-1][0])==0:
    print(f'Az utolso eladott telek a paros oldalon van es a hazszama: {paros}')
else:
    print(f'Az utolso eladott telek a paratlan oldalon van es a hazszama: {paratlan}')

egyezik=False
i=0
while egyezik!=True and i<len(hazak)-1:
    if (hazak[i][3]==hazak[i+1][3]) and (hazak[i][3]!=":")or (hazak[i][3]!="#"): 
        egyezik=True
    i=i+1
        
print(f'A szomszedossal egyezik a kerites szine: {hazak[i-1][0]} hsz.')

#--5--
print('--5--')

hsz=83
i=0

while int(hazak[i][0])!=hsz:
    i=i+1
print(hazak[i])
srsz=i
abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
denyszinek=str(hazak[i-1][3])+str(hazak[i][3])+str(hazak[i+1][3])

truecolors=[]

for i in range(len(abc)):
    character=abc[i:i+1:1]
    truecolors.append(character)


truecolors.remove(denyszinek[0])
truecolors.remove(denyszinek[1])
truecolors.remove(denyszinek[2])

print(f'kerites szine/allapota: {hazak[srsz][3]}')
print(f'lehetseges festesi szin: {truecolors[random.randrange(0,len(truecolors))]}')

#--6--
print('--6--')
hazpattern=""
hszpattern=""

for i in range(len(hazak)):
    if hazak[i][0]%2!=0:
        hsz=hazak[i][0]
        index=int(hazak[i][2])
        allapot=hazak[i][3]
        hszpattern=hszpattern+str(hsz)
        for j in range(index):
            hszpattern=hszpattern+" "
            hazpattern=hazpattern+allapot
            
f=open(f'{path}{os.sep}src{os.sep}utcakep.txt','w')
f.write(f'{hazpattern}\n')
f.write(f'{hszpattern}')
f.close()
