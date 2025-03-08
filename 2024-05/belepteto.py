import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}bedat.txt')

be=[]

for l in f:
    be.append(l.strip().split(' '))
f.close()

print(be[0])

#--2--
print('--2--')
print(f'elso tanulo ekkor lepett be: {be[0][1]}\nutolso tanulo ekkor lepett ki: {be[len(be)-1][1]}')

#--3--
print('--3--')

eddig=False
i=0

while eddig==False and i<len(be):
    acth=int(str(be[i][1]).split(':')[0])
    actm=int(str(be[i][1]).split(':')[1])
    if (acth==7 and actm>50) or (acth==8 and actm<=15):
        print(f'{be[i][1]} {be[i][0]}')
    if acth==8 and actm>15:
        eddig=True
    i=i+1

#itt nem lesz file-ba iras ..|..

#--4--
print('--4--')
c=0
for i in range(len(be)):
    if be[i][2]=='3':
        c=c+1

print(f'ennyien zabaltak: {c}')

#--5--
print('--5--')
kolcsonzott=[]

for i in range(len(be)):
    if be[i][2]=='4' and be[i][0] not in kolcsonzott:
        kolcsonzott.append(be[i][0])
    
print(f'ennyien kolcsonoztek a kt-ban: {len(kolcsonzott)}')

if len(kolcsonzott)>c:
    print(f'a kt nepszerubb')
elif len(kolcsonzott)<c:
    print(f'az ebedlo nepszerubb')
else:
    print(f'egyforman nepszeru a kt es a kajalda')
                
#--6--
# belepes: 1, kilepes: 2

print('--6--')

def secbe(ido):
    h=int(ido.split(':')[0])
    m=int(ido.split(':')[1])
    s=(h*3600+m*60)
    return(s)



bentvannak=[]
i=0

while secbe(be[i][1])<secbe("10:50"):
    if be[i][0] not in bentvannak and be[i][2]=="1":
        bentvannak.append(be[i][0])
    elif be[i][0] in bentvannak and be[i][2]=="2":
        del bentvannak[bentvannak.index(be[i][0])]
    i=i+1


print(f'renitens kis szardarabok:')

while secbe(be[i][1])<secbe("11:00"):
    if be[i][0] in bentvannak and be[i][2]=="1":
        print(be[i][0],end=' ')
    i=i+1
print()    
#--7--
print('--7--')

sid="ZOOM"
gotu=False
i=0
bejott=0
kiment=0

while i<len(be) and gotu!=True:
    if be[i][0]==sid and be[i][2]=="1":
        bejott=(secbe(be[i][1]))
        gotu=True
    i=i+1

if gotu!=False:
    i=len(be)-1
    gotu=False

    while i>0 and gotu!=True:
        if be[i][0]==sid and be[i][2]=="2":
            kiment=(secbe(be[i][1]))
            gotu=True
        i=i-1
        

    h=(kiment-bejott)//3600
    m=((kiment-bejott)-(h*3600))//60
    
    print(f'{sid} id-ju tanulo ennyit tartozkodott a suliban: {h} ora {m} perc')
else:
    print(f'{sid} id-ju tanulot a faszom se latta ma a suliban')