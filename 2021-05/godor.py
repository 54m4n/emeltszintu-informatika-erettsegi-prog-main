import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')
    
#--1--
print('--1--')
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}melyseg.txt')
godor=[]
for l in f:
    godor.append(int(l.strip()))
f.close()
    
print(f'az adatforras {len(godor)} adatot tartalmaz')

#--2--
print('--2--')
#x=int(input(f'bazd ide a tavolsag erteket (max {len(godor)} lehet a szam):'))
x=9
vangodor=False
if godor[x]!=0:
    print(f'a godor a megadott tavolsagerteken ({x} meter) pontosan {godor[x]} m mely')
    vangodor=True
else:
    print(f'itt bizony nincs godor ({x} meteren)')


#--3--
print('--3--')
c=0
for i in range(len(godor)):
    if godor[i]==0:
        c=c+1
print(f'pontosan {round(c/(len(godor)/100),2)}%-a erintetlen a teruletnek')

#--4--

f2=open(f'{path}{os.sep}src{os.sep}godor.txt','w')
i=0
godorcount=0
aktgodor=""
while i<=len(godor)-1:
    if godor[i]!=0:
        j=i
        while godor[j]!=0:
            aktgodor=aktgodor+str(f'{godor[j]} ')
            j=j+1
        i=j-1
    i=i+1
    if aktgodor!="":
        f2.write(f'{aktgodor}\n')
        godorcount=godorcount+1
    aktgodor=""
f2.close()

#--5--
print(f'--5--')
print(f'a godrok szama: {godorcount}')

#--6--
print('--6--')

print('--6a--')

kezdet=x
veg=x

while godor[kezdet]!=0:
    kezdet=kezdet-1
kezdet=kezdet+1
while godor[veg]!=0:
    veg=veg+1

print(f'a godor kiindulopontja: {x}m, kezdete: {kezdet+1}m, vege {veg}m')

print('--6b--')
maxgodor=[]
#if vangodor!=False:

for i in range(kezdet,veg):
    maxgodor.append(godor[i])


melyul=True
i=0
while maxgodor[i]!=max(maxgodor) and melyul==True:
    if maxgodor[i]<maxgodor[i-1]:
        melyul=False
    i=i+1
    if maxgodor[i]==max(maxgodor):
        j=i+1
        while j<len(maxgodor) and melyul==True:
            if maxgodor[j]>maxgodor[j-1]:
                melyul=False
            j=j+1

if melyul==True:
    print(f'Melyul folyamatosan.')
else:
    print(f'Nem melyul folyamatosan.')

#--6c--
print('--6c--')
print(f'a godor legnagyobb melysege: {max(maxgodor)}m')

#--6d--
print(f'--6d--')

tf=0
for i in range(len(maxgodor)):
    tf=tf+maxgodor[i]*10
print(f'a gopdor terfogata: {tf}m3')

#--6e--
print(f'--6e--')

print(f'viz befogado kepesseg: {tf-len(maxgodor)*10}m3')