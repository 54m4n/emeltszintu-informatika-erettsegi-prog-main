import os
import sys

os.system('clear')

#--1--
def mpbe(h,m,s):
    sec=h*3600+m*60+s
    return sec


#--2--
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}hivas.txt')
l=f.readlines()
f.close()

input=[]

for i in range(len(l)):
    input.append([int(l[i].split()[0]),int(l[i].split()[1]),int(l[i].split()[2]),int(l[i].split()[3]),int(l[i].split()[4]),int(l[i].split()[5])])


#--3--
print("--3--")

c=0

uniq_ora=[]
all_ora=[]


for i in range(len(input)):
    all_ora.append(input[i][0])
    if input[i][0] not in uniq_ora:
        uniq_ora.append(input[i][0])

for i in range(len(uniq_ora)):
    print(f'{uniq_ora[i]} ora: {all_ora.count(uniq_ora[i])} hivas')
    
    
#--4--
print('--4--')
max=0
maxindex=0

for i in range(len(input)):
    if abs(mpbe(input[i][0],input[i][1],input[i][2])-mpbe(input[i][3],input[i][4],input[i][5]))>max:
        max=abs(mpbe(input[i][0],input[i][1],input[i][2])-mpbe(input[i][3],input[i][4],input[i][5]))
        maxindex=i+1
    
print(f'leghosszabb ideig vonalban levo hivo: {maxindex}, hivas hossza: {max} masodperc')
        
#--5--
print('--5--')
idopont=[10,11,12]
ido=mpbe(idopont[0],idopont[1],idopont[2])

meleje=mpbe(8,0,0)
mvege=mpbe(12,0,0)

i=0
c=0
beszelok=[]

while i<len(input)-150:
    aktkezdet=(mpbe(input[i][0],input[i][1],input[i][2]))
    aktvege=(mpbe(input[i][3],input[i][4],input[i][5]))
    if aktkezdet<=ido and aktvege>=ido:
        beszelok.append(i)
    i=i+1

print(f'idopont: {idopont[0]}:{idopont[1]}:{idopont[2]}, beszelo a(z) {beszelok[0]+1}. hivo, varakozok szama: {len(beszelok)-1}')

#--6-- & --7--
print('--6-- & --7--')

def mpbol(mp):
    h=int(mp/3600)
    mp=mp-(h*3600)
    m=int(mp/60)
    mp=mp-(m*60)
    s=mp
    mplista=[h,m,s]
    return mplista

mpidok=[]

for i in range(len(input)):
    hkezdet=(mpbe(input[i][0],input[i][1],input[i][2]))
    hvege=(mpbe(input[i][3],input[i][4],input[i][5]))
    mpidok.append([hkezdet,hvege])

valid=False
validhivasok=[]

for i in range(len(mpidok)):
    #valid a hivas ha a kezdete es a vege a munkaidoben van
    if mpidok[i][0]>meleje and mpidok[i][1]<mvege:
        valid=True
    #valid a hivas ha az eleje a munkaido elott kezdodott de a vege munkaidoben volt
    if mpidok[i][0]<meleje and mpidok[i][1]>meleje:
        valid=True
    #valid a hivas ha az eleje munkaido vege elott volt es a vege munkaidon tul
    if mpidok[i][0]<mvege and mpidok[i][1]>mvege:
        valid=True
    if valid==True:
        validhivasok.append([i,mpidok[i][0],mpidok[i][1]])
        valid=False


varakozas=0
sikeres=[]

if validhivasok[0][1]<meleje:
    kapcsolas=meleje
else:
    kapcsolas=validhivasok[0][2]

for i in range(len(validhivasok)):
    if kapcsolas<validhivasok[i][2]:
        varakozas=kapcsolas-validhivasok[i][1]
        sikeres.append([validhivasok[i][0]+1,mpbol(kapcsolas),mpbol(validhivasok[i][2]),varakozas])
        kapcsolas=validhivasok[i][2]

print(f'Az utso telefonalo az alabbi sorban van: {sikeres[len(sikeres)-1][0]}, varakozasi ido: {sikeres[len(sikeres)-1][3]} mp.')


print(sikeres[0])

f2=open(f'{path}{os.sep}src{os.sep}siker.txt','w')

for i in range(len(sikeres)):    
    f2.write(f'{sikeres[i][0]} {sikeres[i][1][0]} {sikeres[i][1][1]} {sikeres[i][1][2]} {sikeres[i][2][0]} {sikeres[i][2][1]} {sikeres[i][2][2]}\n')

    

f2.close()