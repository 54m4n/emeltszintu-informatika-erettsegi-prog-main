import os


#--1--

path=os.path.dirname(__file__)

f1=open(f'{path}{os.sep}src{os.sep}foglaltsag.txt','r')
f2=open(f'{path}{os.sep}src{os.sep}kategoria.txt','r')

foglaltsag=[]
kategoria=[]

for f in f1:
    foglaltsag.append(f.split())
for f in f2:
    kategoria.append(f.split())

f1.close()
f2.close()



#--2--
print('--2--')

#s=int(input('kerem a sor szamat (1-15): '))
#o=int(input('kerem a szek szamat (1-20): '))

s=3
o=4

if (foglaltsag[s-1][0][o-1])=="o":
    print(f'a(z) {s}. sor {o}. szek: FOGLALT')
else:
    print(f'a(z) {s}. sor {o}. szek: SZABAD')


#--3--
print('--3--')

osszhely=15*20
foglalt=0


for i in range(len(foglaltsag)):
    for j in range(20):
        if (foglaltsag[i][0][j])=="x":
            foglalt=foglalt+1

print(f'Az eloadasra eddig {foglalt} jegyet adtak el, ami az osszes {round(foglalt/(osszhely/100))}%-a')

#--4--
print('--4--')

sz=[0,0,0,0,0]


for i in range(len(kategoria)):
    for j in range(20):
        aktkateg=int(kategoria[i][0][j])
        if foglaltsag[i][0][j]=="x":
            sz[aktkateg-1]=sz[aktkateg-1]+1

print(f'a legtobb jegyet a(z) {sz.index(max(sz))+1}. arkategoriaban ertekesitettek')


#--5--
print('--5--')

arak=[5000,4000,3000,2000,1000]
osszar=0

for i in range(len(foglaltsag)):
    for j in range(20):
        if foglaltsag[i][0][j]=='x':
            aktkategar=arak[int(kategoria[i][0][j])-1]
            osszar=osszar+aktkategar
        
print(f'a szinhaz bevetele a jelenlegi eladasok alapjan: {osszar} Ft')

#--6--
print('--6--')

egyall=0

for i in range(len(foglaltsag)):
    for j in range(20):
        akt=str(foglaltsag[i][0][j])
        try:
            next=str(foglaltsag[i][0][j+1])
            prev=str(foglaltsag[i][0][j-1])
        except:
            IndexError
        if akt=='o' and (prev=='x' and next=='x'):
            egyall=egyall+1

print(f'{egyall} db. egyedulallo hely van')
            
#--7--
print('--7--')

for i in range(len(foglaltsag)):
    for j in range(20):
        if foglaltsag[i][0][j]=='o':
            print(kategoria[i][0][j],end='')
        else:
            print(foglaltsag[i][0][j],end='')
    print()
