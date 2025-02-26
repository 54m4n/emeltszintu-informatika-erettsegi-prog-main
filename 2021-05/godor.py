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

print(f'a godor kiindulopontja: {x}m, kezdete: {kezdet}m, vege {veg}m')

print('--6b--')
maxgodor=[]
#if vangodor!=False:

for i in range(kezdet,veg):
    maxgodor.append(godor[i])

print(maxgodor)

maxgodor=[1,2,3,4,5,5,5,2,1]
print(maxgodor)
melyul=True

i=0
while i<=len(maxgodor) and maxgodor[i]!=max(maxgodor) and melyul==True:
    if maxgodor[i]>maxgodor[i+1]:
        melyul=False
    else:
        print(maxgodor[i])
        i=i+1
    if maxgodor[i]==max(maxgodor):
        while i!=len(maxgodor) and melyul==True:
            if maxgodor[i-1]>maxgodor[i]:
                melyul=False
            else:
                print(maxgodor[i])
            if i+1!=len(maxgodor):
                i=i+1




print()
print(melyul)

# 1,2,3,4,3,2,1
# 1,2,2,4,3,4,1