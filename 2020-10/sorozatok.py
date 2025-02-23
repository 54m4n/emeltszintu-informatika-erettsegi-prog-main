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
tmpsori=[]
sztring=""

i=0

for l in f:
    if "x" in l.split('\n')[0]:
        tmpsori.append(l.split('\n')[0].split('x')[0])
        tmpsori.append(l.split('\n')[0].split('x')[1])
    else:
        tmpsori.append(l.split('\n')[0])
    
    if i!=0 and i%4==0:
        sorozat.append(tmpsori)
        tmpsori=[]
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
nemlatta=0
for i in range(len(sorozat)):
    if sorozat[i][5]=="0":
        nemlatta=nemlatta+1
print(nemlatta,len(sorozat)-nemlatta,len(sorozat))      
print(f'A faszi {round(100-(nemlatta/(len(sorozat)/100)),2)}%-at latta az ossz epizodnak.')

#--4--
print('--4--')
min=0
for i in range(len(sorozat)):
    if sorozat[i][5]=="1":
        min=min+int(sorozat[i][4])

nap=int(min/(60*24))
ora=int((min-((24*60)*int(min/(60*24))))/60)
perc=min-((nap*(24*60))+(ora*60))
print(f'A teljes sorizassal toltott ido: {nap} nap, {ora} ora, {perc} perc.')

#--5--
print('--5--')

datumy=2017
datumm=10
datumd=18

for i in range(len(sorozat)):
    if sorozat[i][0]!="NI" and sorozat[i][5]=="0":
        ev=int(sorozat[i][0][0:4:1])
        honap=int(sorozat[i][0][5:7:1])
        nap=int(sorozat[i][0][8:10:1])
        if ev<=datumy and honap<=datumm and nap<=datumd:
            print(f'{sorozat[i][2]}x{sorozat[i][3]} {sorozat[i][1]}')
            
#--6 es 7--
print('--6 es 7--')

'''
Függvény hetnapja(ev, ho, nap : Egész) : Szöveg
napok: Tömb(0..6: Szöveg)= (″v″, ″h″, ″k″, ″sze″,
″cs″, ″p″, ″szo″)
honapok: Tömb(0..11: Egész)= (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
Ha ho < 3 akkor ev := ev -1
hetnapja := napok[(ev + ev div 4 – ev div 100 + ev div 400 + honapok[ho-1] + nap) mod 7]
Függvény vége
'''


def hetnapja(ev,ho,nap):
    napok=['v','h','k','sze','cs','p','szo']
    honapok=[0,3,2,5,0,3,5,1,4,6,2,4]
    if ho<3:
        ev=ev-1
    hetnapja=napok[(ev+ev//4-ev//100+ev//400+honapok[ho-1]+nap)%7]
    return hetnapja

day="cs"
adottnapon=[]

for i in range(len(sorozat)):
    if sorozat[i][0]!="NI":
        hn=hetnapja(int(sorozat[i][0][0:4:1]),int(sorozat[i][0][5:7:1]),int(sorozat[i][0][8:10:1]))
        if hn==day:
            if (sorozat[i][1]) not in adottnapon:
                adottnapon.append(sorozat[i][1])

if len(adottnapon)>0:
    print(f'Az alabbi sorik mennek a megadott napon ({day}):')
    for i in range(len(adottnapon)):
        print(adottnapon[i])
else:
    print(f'lofaszsse megy a megadott napont -> {day}')
    

#--8--
print('--8--')

snev=[]
osszido=[]

for i in range(len(sorozat)):
    if sorozat[i][1] not in snev:
        snev.append(sorozat[i][1])
        aktindex=snev.index(sorozat[i][1])
        osszido.insert(aktindex,[0,0])
       

for i in range(len(sorozat)):
    aktindex=snev.index(sorozat[i][1])
    osszido[aktindex][1]=osszido[aktindex][1]+int(sorozat[i][4])
    if int(sorozat[i][3])>osszido[aktindex][0]:
        osszido[aktindex][0]=int(sorozat[i][3])
    

for i in range(len(snev)):
    print(f'{snev[i]} {osszido[i][1]} {osszido[i][0]}')