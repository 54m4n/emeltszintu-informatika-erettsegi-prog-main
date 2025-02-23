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