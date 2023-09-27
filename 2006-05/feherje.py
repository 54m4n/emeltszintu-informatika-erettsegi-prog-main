# a budos kurva anyjaba se adnek egy kemikusnak feladatot, hogy irjon erettsegi tetelt. ez a kinkeserves fos legalabb 4 orat vett igenybe, amibol 3,5 ora csak a feladatok ertelmezese volt... botrany.

import os

path=os.path.dirname(__file__)
f=open(f'{path}\src\\aminosav.txt',"r")

atomtomegek=[12,1,16,14,32]

# --- 2 ---
# kiszamolja a relativ molekulatomeget, ahol n az iteralando tomb elso szameleme
def tomegszamol(n):
    atomeg=0
    for i in range(5):
        atomeg=atomeg+(int(aminosavak[n+i])*atomtomegek[i])
    return atomeg

# --- 1 --- 
aminosavak=f.read().split()
f.close()
relatomtomeg=[]

sorted=[]

# --- 3 ---
for i in range(0,int(len(aminosavak)),7):
    relatomtomeg.append([aminosavak[i],tomegszamol(i+2)])    
relatomtomeg.sort(key=lambda col: (col[1]), reverse=False)

f=open(f'{path}\src\eredmeny.txt',"w")

for i in range(len(relatomtomeg)):
    #print(f'{relatomtomeg[i][0]} {relatomtomeg[i][1]}')
    f.write(f'{relatomtomeg[i][0]} {relatomtomeg[i][1]}\n')
f.close()

# --- 4 --- azt a jo budos kurva anyadat aki ezt a feladatot leirta bazdmeg!
f=open(f'{path}\src\\bsa.txt','r')

bsa=f.read().split()
f.close()

osszegkeplet=[0,0,0,0,0]

for i in range(len(bsa)):
    aktindex=aminosavak.index(bsa[i])
    k=0
    for j in range(aktindex+1,aktindex+6):
        aktertek=aminosavak[j]
        osszegkeplet[k]=osszegkeplet[k]+int(aktertek)        
        k=k+1
    
osszegkeplet[1]=osszegkeplet[1]-(len(bsa)-1)*2 #hidrogen kivonasa
osszegkeplet[2]=osszegkeplet[2]-((len(bsa)-1)) #oxigen kivonasa


f=open(f'{path}\src\eredmeny.txt',"a")
print(f'C {osszegkeplet[0]} H {osszegkeplet[1]} O {osszegkeplet[2]} N {osszegkeplet[3]} S {osszegkeplet[4]}')
f.write(f'C {osszegkeplet[0]} H {osszegkeplet[1]} O {osszegkeplet[2]} N {osszegkeplet[3]} S {osszegkeplet[4]}')
f.close()

# --- 5 --- rohadj meg te kemikusgeci! leszoptam magam mire egyaltalan felfogtam mi a geci az a 'hasitas' bazmeg.
hossz=0
max=0
helye=0

for i in range(len(bsa)):
    if bsa[i] != "Y" and bsa[i] != "W" and bsa[i] != "F":
        hossz=hossz+1
        
    else:        
        if hossz>=max:
            max=hossz
            helye=i-max
            elsoelem=bsa[i-max]
            utolsoelem=bsa[i-1]

        hossz=0
    
print(f'A fasszopo Kimotripszin enzimmel szetbaszott BSA lanc lehosszabb darabjanak hossza: {max}\nhelye: {helye}\nelso elem: {elsoelem}\nutolso elem: {utolsoelem}')

# ---  6 --- ua mint az elozo csak 2 elemu sztringet vizsgalok. es a jo budos kurva anyjat akkoris aki leirta ezeket a feladatokat bazmeg ATOMOKKAL... ANYAD!!
i=0
megvan=False

while megvan!=True:
    if bsa[i]=="R" and (bsa[i+1]=="A" or bsa[i+1]=="V"):
        megvan=True
        index=i
    i=i+1
    
megvan=False
hasitott=[]
i=1

while megvan!=True:
    if bsa[index+i]=="R" and (bsa[index+i+1]=="A" or bsa[index+i+1]=="V"):
        megvan=True
    else:
        hasitott.append(bsa[index+i])
        i=i+1

print(f'A retkes Factor XI hasitas soran keletkezett feherjelanc reszeben {hasitott.count("C")} db. cisztein talalhato.. geci!')


























    