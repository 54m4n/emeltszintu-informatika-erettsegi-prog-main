import os
import sys
import platform

if platform.system()!="Windows":
    os.system('clear') #if it is unix
else:
    os.system('cls') #if it is win

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

def hetnapja(honap, nap):
    napok=["hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat", "vasarnap"]
    hnapszam=[0,31,59,90,120,151,181,212,243,273,304,335]
    napsorszam=hnapszam[honap-1]+nap
    return napok[(napsorszam-1)%7]

#--5--
print('--5--')
print(hetnapja(1,1))

#--6--
print('--6--')
#mivel arrol kurvara nincs szo h igazolt v igazolatlan hianyzast keresunk, igy kiiratom mindet a faszba

napnev="szerda"
orasrsz=3
h=0

for i in range(len(hiany)):
    hnap=int(hiany[i][0])
    nap=int(hiany[i][1])
    napneve=hetnapja(hnap,nap)
    if napneve==napnev:
        akthianyzasok=str(str(hiany[i][2]).split(' ')[2]).split("'")[0]
        aktorastatusz=akthianyzasok[orasrsz-1:orasrsz:1]
        if aktorastatusz=="I" or aktorastatusz=="X":
            h=h+1

print(f'az alabbi napokon: {napnev} az alabbi sorszamu oran: {orasrsz}, osszesen {h} hianyzas volt')
    
#--7--
print('--7--')
thiany=[]

for i in range(len(hiany)):
    for j in range(len(hiany[i][2])):
        tanulonev=(str(hiany[i][2][j]).split(" ")[0])+" "+(str(hiany[i][2][j]).split(" ")[1])
        akthiany=(str(hiany[i][2][j]).split(" ")[2])
        c=akthiany.count("X")+akthiany.count("I")
        #print(tanulonev,akthiany,c)
        if tanulonev not in thiany:
            thiany.append(tanulonev)
            thiany.append(c)
        elif tanulonev in thiany:
            thiany[thiany.index(tanulonev)+1]=thiany[thiany.index(tanulonev)+1]+c

#print(max(thiany)) itt faszra fut, erdekes hibauzi a max fuggvenybol gondolom: TypeError: '>' not supported between instances of 'int' and 'str'

max=0

for i in range(0,len(thiany),2):
    if int(thiany[i+1])>max:
        max=int(thiany[i+1])
    
tstring=""
for i in range(0,len(thiany),2):
    if int(thiany[i+1]==max):
        tstring=tstring+" "+(thiany[i])
    
print(f'a legtobbet hianyzott tanulo(k):{tstring}')