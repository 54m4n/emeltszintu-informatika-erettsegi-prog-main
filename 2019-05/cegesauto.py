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
maxmegtettut=0
maxszemely=""
for i in range(len(rendszamok)):
    maxutak.append(0)

for i in range(len(autok)):
    aktindex=rendszamok.index(autok[i][2])
    if maxutak[aktindex]==0:
        maxutak[aktindex]=int(autok[i][4])
    else:
        megtettut=int(autok[i][4])-maxutak[aktindex]
        if megtettut>maxmegtettut:
            maxmegtettut=megtettut
            maxszemely=autok[i][3]
        if megtettut>maxutak[aktindex]:
            maxutak[aktindex]=megtettut            
        else:
            maxutak[aktindex]=int(autok[i][4])
            

print(f'leghosszabb ut: {maxmegtettut} km, szemely: {maxszemely}')

#--7--
print('--7--')

rndsz="CEG304"
dataki=[]
databe=[]

for i in range(len(autok)):
    if autok[i][2]==rndsz and autok[i][5]=="0":
        dataki.append([autok[i][3],autok[i][0],autok[i][1],autok[i][4],autok[i][5]])
    if autok[i][2]==rndsz and autok[i][5]=="1":
        databe.append([autok[i][3],autok[i][0],autok[i][1],autok[i][4],autok[i][5]])

fw=open(f'{path}{os.sep}src{os.sep}{rndsz+"_menetlevel.txt"}','w')
for i in range(len(dataki)):
    try:
        fw.write(f'{dataki[i][0]}\t{dataki[i][1]}\t{dataki[i][2]}\t{dataki[i][3]} km\t{databe[i][0]}\t{databe[i][1]}\t{databe[i][2]}\t{databe[i][3]} km\n')
    except:
        fw.write(f'{dataki[i][0]}\t{dataki[i][1]}\t{dataki[i][2]}\t{dataki[i][3]} km\n')
fw.close()
#^itt ennel a resznel fostam a tabulatoros formazasra, mert aztirta, hogy 'tabulatorral elvalasztva'. 4 es 5 kozotti km karakterszamoknal elcsuszik a gecibe de mivagyok-en valami dizajner?