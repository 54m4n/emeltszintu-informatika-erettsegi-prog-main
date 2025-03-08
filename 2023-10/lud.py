import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--

path=os.path.dirname(__file__)
osv=open(f'{path}{os.sep}src{os.sep}osvenyek.txt')
osvenyek=[]
for l in osv:
    osvenyek.append(l.strip())
osv.close()

dob=open(f'{path}{os.sep}src{os.sep}dobasok.txt')
dobasok=[]

for l in dob:
    dobasok=l.strip().split(' ')

#--2--
print('--2--')
print(f'osveny dbszam: {len(osvenyek)}, dobas dbszam: {len(dobasok)}')

#--3--
print('--3--')

maximum=len(osvenyek[0])

for i in range(len(osvenyek)):
    if len(osvenyek[i])>maximum:
        maximum=len(osvenyek[i])
        tmpi=i+1
    
print(f'az egyik leghosszabb osveny az alabbi sorban talalhato: {tmpi}. es {maximum} hosszu')

#--4--
print('--4--')
osvnum=9
gnum=5

#--5--
print('--5--')

m=0
e=0
v=0
print(osvenyek[osvnum-1])
for i in range(len(osvenyek[osvnum-1])):
    if osvenyek[osvnum-1][i]=="M":
        m=m+1
    if osvenyek[osvnum-1][i]=="E":
        e=e+1
    if osvenyek[osvnum-1][i]=="V":
        v=v+1

if m!=0:
    print(f'M: {m}')
if v!=0:
    print(f'V: {v}')
if e!=0:
    print(f'E: {e}')

#--6--
print('--6--')

for i in range(len(osvenyek[osvnum-1])):
    if osvenyek[osvnum-1][i]!="M":
        print(f'{i+1}\t{osvenyek[osvnum-1][i]}')

    
#--7--
print('--7--')

gamers=[]

for i in range(gnum):
    gamers.append(0)

j=0
i=0

while i<len(dobasok) and max(gamers)<=len(osvenyek[osvnum-1]):    
    gamers[j]=(int(gamers[j])+int(dobasok[i]))
    if j<len(gamers)-1:
        j=j+1
    else:
        j=0
    i=i+1

print(f'a jatek az alabbi kornel ert veget: {int(i/len(gamers))}., legtavolabb juto gamer sorszama: {gamers.index(max(gamers))+1}')


#--8--
print('--8--')

gamers=[]
for i in range(gnum):
    gamers.append(0)

kor=0
vege=False

while vege==False:
    for j in range(gnum):
        dobott=int(dobasok[kor*gnum+j])
        gamers[j]+=dobott

        if gamers[j]<=len(osvenyek[osvnum-1]):
            if osvenyek[osvnum-1][gamers[j]-1]=="E":
                gamers[j]+=dobott
            elif osvenyek[osvnum-1][gamers[j]-1]=="V":
                gamers[j]-=dobott
                if gamers[j]<0:
                    gamers[j]=0
        if gamers[j]>=len(osvenyek[osvnum-1]):
            vege=True
    kor+=1

print('nyertes(ek):',end='')
for idx,mezo in enumerate(gamers):
    if mezo>=len(osvenyek[osvnum-1]):
        print(idx+1,end=' ')

print('csirak:')
for idx,mezo in enumerate(gamers):
    if mezo<len(osvenyek[osvnum-1]):
        print(f'{idx+1}. gamer,{mezo}. pozi')
