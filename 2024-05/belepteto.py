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


print(secbe("10:45"))
print(secbe("10:50"))

bentvannak=[]
i=0

while secbe(be[i][1])<secbe("10:50"):
    if be[i][0] not in bentvannak and be[i][2]=="1":
        bentvannak.append(be[i][0])
    if be[i][0] in bentvannak and be[i][2]=="2":
        print(bentvannak[bentvannak.index(be[i][0])])
    i=i+1
