import os
import sys

os.system('cls')

#--1--
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}penztar.txt')
l=f.read().split("\nF\n")
f.close()

#--2--
print("--2--")
print(f'{len(l)} alkalommal fizettek a penztarnal')

#--3--
print("--3--")
akt=l[1].split("\n")
print(f'az elso vasarlonak {len(akt)} db arucikkje volt')

#--4--
print("--4--")
input=[]

for i in range(len(l)):
    akt=l[i].split("\n")
    input.append(akt)

arucikk="kefe"

i=0
while str(arucikk) not in input[i] and i+1!=len(input):
    i=i+1
eloszor=i+1

i=len(input)-1
while str(arucikk) not in input[i] and i+1!=len(input):
    i=i-1
utoljara=i+1

#--5.a.--
print("--5.a.--")
print(f'az alabbi termeket: {arucikk}\neloszor {eloszor}. alkalommal\nutoljara {utoljara}. alkalommal vasaroltak meg.')

#--5.b.--
print("--5.b.--")
#a jo budos kurva anyjukat, hogy a peldaban 32-ot irnak, pedig kurvara 39 bazdmeg... ez egy hibas fos mintaszoveg..
i=0
c=0
while i<len(input):
    c=c+input[i].count(arucikk)
    i=i+1

print(f'osszesen {c} alkalommal vasaroltak ebbol: {arucikk}')

#--6--
print("--6--")

def ertek(db):
    if db==1:
        e=500
    if db==2:
        e=950
    if db==3:
        e=1350
    if db>3:
        e=(db*400)+150
    return e,db

print(f'{ertek(10)[1]} db vasarlas eseten fizetendo: {ertek(10)[0]}')

#--7--
print("--7--")

vasarlas=2
vltmr=[]

for i in range(len(input[vasarlas-1])):
    if (input[vasarlas-1][i]) not in vltmr:
        vltmr.append(input[vasarlas-1][i])

for i in range(len(vltmr)):
    print(f'{input[vasarlas-1].count(vltmr[i])} db {vltmr[i]}')

#--8--
print("--8--")

c=0



for k in range(len(input)):
    vltmr=[]
    for i in range(len(input[k])):
        if (input[k][i]) not in vltmr:
            vltmr.append(input[k][i])
        c=0
        for j in range(len(vltmr)):
            c=c+ertek(input[k].count(vltmr[j]))[0]
    print(f'{k+1}: {c}')
    

#ja es most baszok bele hogy ez igy szep-e vagy nem ..|..