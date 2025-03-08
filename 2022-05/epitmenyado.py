import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}utca.txt')

i=0
arak=[]
ep=[]
for l in f:
    if i==0:
        arak=(l.strip().split())
    else:
        ep.append(l.strip().split())
    i=i+1

f.close()

print(ep[0])
print(arak)

#--2--
print('--2--')
print(f'{len(ep)} telek adatai talalhatoak a listaban')

#--3--
print('--3--')

tulaj="68396"
print(f'az alabbi tulajnak: {tulaj}\nitt vannak kecoi:')
for i in range(len(ep)):
    if ep[i][0]==tulaj:
        print(f'{ep[i][1]} utca {ep[i][2]}')

#--4--
def ado(kategoria,nm):
    if kategoria=="A":
        nmar=int(arak[0])
    if kategoria=="B":
        nmar=int(arak[1])
    if kategoria=="C":
        nmar=int(arak[2])    
        
    return int(nm)*nmar

#--5--
print('--5--')

osszado=[0,0,0]
a=0
b=0
c=0
for i in range(len(ep)):
    if ep[i][3]=="A":
        a=a+1
    if ep[i][3]=="B":
        b=b+1
    if ep[i][3]=="C":
        c=c+1
    if ep[i][3]=="A" and int(ep[i][4])*int(arak[0])>=10000:
        osszado[0]=int(osszado[0])+int(ep[i][4])*int(arak[0])            
    elif ep[i][3]=="B" and int(ep[i][4])*int(arak[1])>=10000:
        osszado[1]=int(osszado[1])+int(ep[i][4])*int(arak[1])
    elif ep[i][3]=="C" and int(ep[i][4])*int(arak[2])>=10000:
        osszado[2]=int(osszado[2])+int(ep[i][4])*int(arak[2])
    
print(f'A savba {a} telek esik, az ado: {osszado[0]}\nB savba {b} telek esik, az ado: {osszado[1]}\nC savba {c} telek esik, az ado: {osszado[2]}')

#--6--
print('--6--')
utcak=[]
kateg=[]
for i in range(len(ep)):
    if ep[i][1] not in utcak:
        utcak.append(ep[i][1])
        kateg.append(ep[i][3])
    

problemas=[]

for i in range(len(ep)):
    aktutca=ep[i][1]
    aktkateg=ep[i][3]
    aktindex=utcak.index(aktutca)
    if aktkateg!=kateg[aktindex]:
        if aktutca not in problemas:
            problemas.append(aktutca)
    
print('problemas utcak:')
for i in range(len(problemas)):
    print(problemas[i])

#--7--
print('--7--')
tulajok=[]
ertek=[]
for i in range(len(ep)):
    if ep[i][0] not in tulajok:
        tulajok.append(ep[i][0])
        ertek.append(0)
    
osszertek=[]

for i in range(len(ep)):
    aktindex=tulajok.index(ep[i][0])
    ertek[aktindex]=ertek[aktindex]+ado(ep[i][3],int(ep[i][4]))

for i in range(len(tulajok)):
    if ertek[i]<10000:
        print(tulajok[i],0)
    else:
        print(tulajok[i],ertek[i])

#na ezt megkurtam 1 ora alatt, pontosan 59 perc volt mindennel egyutt... YEAH MOTHERFUCKERS!!!!!!! :D