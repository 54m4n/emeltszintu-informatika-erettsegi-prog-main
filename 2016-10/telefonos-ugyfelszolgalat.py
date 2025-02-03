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

#--6--
print('--6--')

mpidok=[]

for i in range(len(input)):
    hkezdet=(mpbe(input[i][0],input[i][1],input[i][2]))
    hvege=(mpbe(input[i][3],input[i][4],input[i][5]))
    mpidok.append([hkezdet,hvege])

print(f'meleje: {meleje}, mvege: {mvege}')


hivaseleje=mpidok[0][0]
hivasvege=mpidok[0][1]


for i in range(len(mpidok)):
    print(i,mpidok[i])


for i in range(len(mpidok)):    
    if hivaseleje<mvege and mpidok[i][0]>=hivaseleje:
        hivaseleje=mpidok[i][0]
    
print(hivaseleje)