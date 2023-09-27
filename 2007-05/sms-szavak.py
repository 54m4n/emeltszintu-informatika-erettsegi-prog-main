import os

betuk={
    "a":"2",
    "b":"22",
    "c":"222",
    "d":"3",
    "e":"33",
    "f":"333",
    "g":"4",
    "h":"44",
    "i":"444",
    "j":"5",
    "k":"55",
    "l":"555",
    "m":"6",
    "n":"66",
    "o":"666",
    "p":"7",
    "q":"77",
    "r":"777",
    "s":"7777",
    "t":"8",
    "u":"88",
    "v":"888",
    "w":"9",
    "x":"99",
    "y":"999",
    "z":"9999",
}

# -- 1 --
beker=input("kerek egy betut: ")
#beker="h"
print(f'a(z) "{beker}" betut az alabbi koddal lehet kiirni: {betuk[beker]}')

# -- 2 --
beker=input("kerek egy szot: ")
#beker="fityfasz"
print(f'a(z) "{beker}" szot az alabbi kodsorral lehet beirni:')
for i in range (len(beker)):
    print(f'{betuk[beker[i:i+1:1]]}',end=" ")
print()    

# -- 3 --
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}szavak.txt',"r")
szavak=[]
szavak=f.read().split()
f.close()

# -- 4, 5 -- 
max=0
maxszo=""
rovidszo=[]
for i in range(len(szavak)):
    if len(szavak[i])>=max:
        max=len(szavak[i])
        maxszo=szavak[i]
    if len(szavak[i])<=5:
        rovidszo.append(szavak[i])
print(f'az egyik leghosszabb szo a(z) "{maxszo}", melynek hossza {max} karakter')

print("rovid szavak (max 5 karakter):")
for i in range(len(rovidszo)):
    print(rovidszo[i],end=' ')
print()

# -- 6 --
f2=open(f'{path}{os.sep}src{os.sep}kodok.txt',"w")
for i in range(len(szavak)):
    f2.write(f'{szavak[i]} ')
    for j in range(len(szavak[i])):
        f2.write(f'{betuk[szavak[i][j:j+1:1]]} ')
    f2.write("\n")
f2.close()

# -- 7 --
f2=open(f'{path}{os.sep}src{os.sep}kodok.txt',"r")
hossz=f2.readlines()
f2.close()

kodok=[]

f2=open(f'{path}{os.sep}src{os.sep}kodok.txt',"r")
for i in range(len(hossz)):
    kodok.append(f2.readline().split())
f2.close()
    
beker=input("kerem a kodot: ")
#beker="225"
print(f'a(z) {beker} kodhoz az alabbi szavak egeszulnek ki:')    
for i in range(len(kodok)):
    for j in range(len(beker)):        
        if beker[j]==str(kodok[i][j+1])[0:1:1]:
            ezaz=True
        else:
            ezaz=False
            break
    if ezaz==True:
        print(kodok[i][0])
print("-------------")

# -- 8 --
aktkod=""
szavakeskodok=[]
csakkod=[]

for i in range(len(kodok)):
    aktszo=kodok[i][0]
    for j in range(1,len(kodok[i])):
        aktkod=aktkod+str(kodok[i][j])[0:1:1]
    szavakeskodok.append([aktszo,aktkod])
    csakkod.append(str(aktkod))
    aktszo=""
    aktkod=""

csakkoduniq=[]
for i in range(len(csakkod)):
    if csakkod.count(csakkod[i])>1:
        if csakkod[i] not in csakkoduniq:
            csakkoduniq.append(csakkod[i])
tobbszo=[]

for i in range(len(csakkoduniq)):
    kod=str(csakkoduniq[i])
    for j in range(len(szavakeskodok)):
        if szavakeskodok[j][1]==kod:
            #print(f'{szavakeskodok[j][0]} : {szavakeskodok[j][1]}',end='; ')
            tobbszo.append([szavakeskodok[j][0],szavakeskodok[j][1]])

# -- 9 --
c=0
max=0
for i in range(len(tobbszo)):
    akt=tobbszo[i][1]    
    for j in range(len(tobbszo)):
        if str(tobbszo[j][1])==str(akt):
            c=c+1
    if c>=max:
        max=c
        kod=akt
    c=0

print(f'a(z) legtobb kodhoz ({kod}) tartozo szavak:')
for i in range(len(tobbszo)):
    if kod==tobbszo[i][1]:
        print(tobbszo[i][0],tobbszo[i][1])