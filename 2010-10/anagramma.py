import os

# -- 1 --
print("-- 1 --")
def karszamol(s):
    vltmr=[]
    for i in range(len(s)):
        aktkar=s[i:i+1:]
        if aktkar not in vltmr:
            vltmr.append(aktkar)
        karszam=len(vltmr)
    return vltmr,karszam

#sztring=input("kerem a szoveget: ")
sztring="miafaszvan"
        
print(f'a(z) "{sztring}" szoban {karszamol(sztring)[1]} db. kulonbozo betu talalhato:')

for i in range(int(karszamol(sztring)[1])):
    print(sztring[i], end=', ')
print("\n")

# -- 2 / 3 --
print("-- 2 / 3 --")
def szo2list(szo):
    szolista=[]
    aktszo=""
    for i in range(len(szo)):
        szolista.append(szo[i:i+1:])
    szolista.sort()
    for i in range(len(szolista)):
        aktszo=aktszo+szolista[i]
    
    return(aktszo,szolista)

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}szotar.txt','r')
lines=f.readlines()
f.close()
szavak=[]
for line in lines:
    szavak.extend(line.strip().split())

f2=open(f'{path}{os.sep}src{os.sep}abc.txt','w')
for i in range(len(szavak)):
    f2.write(szo2list(szavak[i])[0])
    f2.write("\n")
f2.close()

# -- 4 --
print("-- 4 --")

def anagrammae(eszo,mszo):
    if len(eszo)==len(mszo):
        n=karszamol(eszo)[0]
        n.sort()
        k=karszamol(mszo)[0]
        k.sort()

        if n==k and karszamol(eszo)[1]==karszamol(mszo)[1]:
            anagrammae=True
        else:
            anagrammae=False
    else:
        anagrammae=False
    return anagrammae
    
#elsoszo=input("kerem az elso szot: ")
#masodikszo=input("kerem a masodik szot: ")
    
elsoszo="faszgeci"
masodikszo="gecifasz"    

print(f'a ket szo ({elsoszo},{masodikszo}) vajon anagramma-e: {anagrammae(elsoszo,masodikszo)}')

# -- 5 --
print("-- 5 --")

#beker=input("kerem a szot a kereseshez: ")

beker="napokkal" # van talalat
#beker="pina" # nincs talalat
anagrammak=[]

for i in range(len(szavak)):
    if anagrammae(szavak[i],beker)==True:
        anagrammak.append(szavak[i])

if len(anagrammak)>0:
    print(f'a bekert szo ("{beker}") anagrammai:')
    for i in range(len(anagrammak)):
        print(anagrammak[i])
else:
    print(f'a bekert szonak ("{beker}") nincsenek anagrammai a szotarban.')
    
# -- 6 --
print("-- 6 --")
max=0
for i in range(len(szavak)):
    if len(szavak[i])>max:
        max=len(szavak[i])

leghosszabbszavak=[]

for i in range(len(szavak)):
    if len(szavak[i])==max:
        leghosszabbszavak.append(szavak[i])

agrammak=[]

for i in range(len(leghosszabbszavak)):
    aktszo=leghosszabbszavak[i]
    for j in range(len(leghosszabbszavak)):
        if anagrammae(aktszo,leghosszabbszavak[j])==True and leghosszabbszavak[j] not in agrammak and aktszo!=leghosszabbszavak[j]:
            agrammak.append(leghosszabbszavak[j])

print(f'leghosszabb szo: {max} karakter')
print("anagrammak ezzel a hosszal:")
for i in range(len(agrammak)):            
    print(agrammak[i])
    
# -- 7 --
print("-- 7 --")

ujszavak=[]

for i in range(len(szavak)):
    for j in range(len(szavak)):
        if len(szavak[j])==max:
            ujszavak.append(szavak[j])
    if max!=1:
        max=max-1

ujszavak.reverse()
agr=[]
for i in range(len(ujszavak)):
    
    for j in range(len(ujszavak)):
        if anagrammae(ujszavak[i],ujszavak[j])==True and ujszavak[j] != ujszavak[i]:
            agr.append(ujszavak[j])
    print(ujszavak[i],end=',')
    if len(agr)!=0:
        
        for k in range(len(agr)):
            print(agr[k],end=',')
    else:
        print()
    print()
    agr=[]
    
    
    
        