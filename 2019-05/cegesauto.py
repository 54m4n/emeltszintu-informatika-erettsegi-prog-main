import os
import platform

if platform.system()!="Windows":
    os.system('clear')
else:
    os.system('cls')

#--1--
    
path=os.path.dirname(__file__)
autok=[]
f=open(f'{path}{os.sep}src{os.sep}autok.txt')
for line in f:
    autok.append(line.strip().split())
f.close()

#--2--
print('--2--')
print(f'{autok[len(autok)-1][0]}. nap, rendszám: {autok[len(autok)-1][2]}')

#--3--
print('--3--')

nap=4
i=0
j=0

print(f'forgalom az alabbi napon: {nap}')
while int(autok[i][0])!=nap:
    i=i+1
    while int(autok[i+j][0])==nap:
        if int(autok[i+j][5])==0:
            irany="ki"
        else:
            irany="be"
        print(f'{autok[i+j][1]} {autok[i+j][2]} {autok[i+j][3]} {irany}')
        j=j+1
        
print(autok[0])

#--4--
print('--4--')
rendszamok=[]
behajtasok=[]
for i in range(len(autok)):
    if autok[i][2] not in rendszamok:
        rendszamok.append(autok[i][2])
        behajtasok.append(autok[i][5])
    behajtasok[rendszamok.index(autok[i][2])]=autok[i][5]
        
print(f'a honap vegen {behajtasok.count("0")} autot nem hoztak vissza')

#--5--
print('--5--')

rendszamok.sort()
elsout=[0,0,0,0,0,0,0,0,0,0]
utsout=[0,0,0,0,0,0,0,0,0,0]

i=0
c=0
while c<10:
    aktindex=rendszamok.index(autok[i][2])    
    if elsout[aktindex]==0:
        elsout[aktindex]=(int(autok[i][4]))
        c=c+1
    i=i+1

i=len(autok)-1

c=0
while c<10:
    aktindex=rendszamok.index(autok[i][2])    
    if utsout[aktindex]==0:
        utsout[aktindex]=(int(autok[i][4]))
        c=c+1
    i=i-1

for i in range(len(rendszamok)):
    print(f'{rendszamok[i]} {utsout[i]-elsout[i]} km')



#--6--
print('--6--')

maxutak=[]

for i in range(len(rendszamok)):
    maxutak.append(0)

for i in range(len(autok)):
    aktindex=rendszamok.index(autok[i][2])
    if maxutak[aktindex]==0:
        maxutak[aktindex]=int(autok[i][4])
    else:
        megtettut=int(autok[i][4])-maxutak[aktindex]
        if megtettut>maxutak[aktindex]:
            maxutak[aktindex]=megtettut            
        else:
            maxutak[aktindex]=int(autok[i][4])
            

print(maxutak)