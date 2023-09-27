import os
import math

# -- 1 --
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}eladott.txt','r')
lines=f.readlines()
f.close()
vonal=[]

for line in lines:
    vonal.append(line.strip().split())

eladott=int(vonal[0][0])
vonalhossz=int(vonal[0][1])
jegyper10km=int(vonal[0][2])


# -- 2 --
print("-- 2 --")
print("utso adatai:")
print(f'ules: {vonal[len(vonal)-1][0]}, megtett tav: {int(vonal[len(vonal)-1][2])-int(vonal[len(vonal)-1][1])}km')

# -- 3 --
print("utasok sorszama akik megtettek az egesz tavot:")
for i in range(0,len(vonal)):
    if int(vonal[i][1])==0 and int(vonal[i][2])==vonalhossz:
        print(f'{i}',end=' ')
print()        
# -- 4 --
print("-- 4 --")
bevetel=0
for i in range(1,len(vonal)):
    megtettut=round(int(vonal[i][2])-int(vonal[i][1]))    
    megtettut=round(megtettut/10)
    bevetel=round(bevetel)+(megtettut*jegyper10km)
print(f'a tarsasag ossz bevetele: {bevetel} Ft')

# -- 5 --
print("-- 5 --")
max=0
for i in range(1,len(vonal)):
    if int(vonal[i][2])<vonalhossz and int(vonal[i][2])>=max:
        max=int(vonal[i][2])
        

felszall=0
leszall=0
for i in range(1,len(vonal)):
    if int(vonal[i][1])==max:
        felszall=felszall+1
    if int(vonal[i][2])==max:
        leszall=leszall+1
        
print(f'az utolso elotti allomasnal ({max}km) leszallo: {leszall} fo, felszallo {felszall} fo')

# -- 6 --
print("-- 6 --")
megallok=[]

for i in range(1,len(vonal)):
    if int(vonal[i][1]) not in megallok:
        megallok.append(int(vonal[i][1]))
    if int(vonal[i][2]) not in megallok:
        megallok.append(int(vonal[i][2]))

print(f'megallok szama: {len(megallok)}db')
megallok.sort()

# -- 7 --
print("-- 7 --")

pont=int(input(f'kerem a megallo szamat (max: {len(megallok)}): '))
ules=[]
utas=[]
for i in range(1,len(vonal)):
    if int(vonal[i][2])>megallok[pont-1] and int(vonal[i][1])<=megallok[pont-1]:
        ules.append(int(vonal[i][0]))
        utas.append(i)        

f2=open(f'{path}{os.sep}src{os.sep}kihol.txt','w')

print(f'busz telitettsege a(z) {pont}. megallonal:')
for i in range(1,49):
    try:
        if i in ules:
            print(f'{i}. ules: {utas[ules.index(i)]}. utas')
            f2.write(f'{i}. ules: {utas[ules.index(i)]}. utas\n')
        else:
            print(f'{i}. ules: ures')
            f2.write(f'{i}. ules: ures\n')
    except:
        pass
f2.close()


   