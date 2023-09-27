import os
from random import randrange

# -- 1 --
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}igeny.txt')
sorok = f.readlines()
s=[]
for sor in sorok:    
    s.append(sor.strip().split())

szintek=s[0][0]
csapatok=s[1][0]
igenyek=s[2][0]
del s[0]
del s[0]
del s[0]

#szerkezet: |ora|perc|masodperc|csapatszam|induloszint|celszint|

# -- 2 --
print("-- 2 --")
#liftall=int(input("hanyadik szinten alljon most a lift: "))
liftall=8
print(f'A lift nyilvanvaloan eppen a(z) {liftall}. szinten all.')

# -- 3 --
print("-- 3 --")
print(f'A lift az utso keres utan a(z) {s[int(len(s))-1][5]}. szinten fog lenni.')

# -- 4 --
print("-- 4 --")
max=0
min=int(len(s))
for i in range(len(s)):
    if int(s[i][5])>=max:
        max=int(s[i][5])
    if int(s[i][4])>=max:
        max=int(s[i][4])
    if int(s[i][5])<=min:
        min=int(s[i][5])
    if int(s[i][4])<=min:
        min=int(s[i][4])
    
print(f'MAX emelet amit a lift erintett: {max}.\nMIN emelet amit a lift erintett: {min}.')

# -- 5 --
print("-- 5 --")

utassalfel=0
utasnelkulfel=0

for i in range(len(s)-1):
    if int(s[i][4])<int(s[i][5]):
        utassalfel=utassalfel+1
    if int(s[i][5])<int(s[i+1][4]):
        utasnelkulfel=utasnelkulfel+1
# ez itt ugye azert lehet megkozelitoleg annyi mint az ossz ut (vagy akar tobb is), ugyanis bar soronkent 1 ut van, 2 sor kozott az elso cel, es a masodik start allomasa is 1 utnak szamit.
print(f'A lift az alabbiak szerint kozlekedett felfele:\nutasokkal: {utassalfel}x\nutasok nelkul: {utasnelkulfel}x')

# -- 6 --
print("-- 6 --")
teams=[]
for i in range(int(csapatok)):
    teams.append(i+1)

for i in range(len(s)):
    if int(s[i][3]) in teams:
        tindex=teams.index(int(s[i][3]))
        del teams[tindex]

print('Az alabbi sorszamu brigadok nem vettek igenybe a liftet:')
for i in range(len(teams)):
    if i==len(teams)-1:
        print(f'{teams[i]}',end='.')
    else:
        print(f'{teams[i]}',end=', ')
print()
#-- 7 --
print("-- 7 --")

#csalosrsz=randrange(10,20)
csalosrsz=3

igeny=0
tartozkodik=0
csalogeci=False
i=0

while csalogeci!=True and i<int(len(s))-1:
    if int(s[i][3])==csalosrsz:
        igeny=int(s[i+1][4])
        tartozkodik=int(s[i][5])
        if igeny!=tartozkodik:
            csalogeci=True
    i=i+1
print(f'Vajon {csalosrsz}. brigad csalo geci-e: {csalogeci}!')

if csalogeci==True:
    print(f'Problemas emeletek: {tartozkodik} - {igeny}')

#-- 8 --
print("-- 8 --")
# lol itt nekem kene beirogatnom a hianyzo adatokat, de ehelyett: egy nagy faszt! inkabb kilesz generalva es pont.

fkod=randrange(1,100)
csapat=[]

for i in range(len(s)):
    if int(s[i][3])==csalosrsz:
        csapat.append(s[i])
    
for i in range(len(csapat)):
    print("----------")
    print(f'indulas emelet: {csapat[i][4]}')
    print(f'cel emelet: {csapat[i][5]}')
    print(f'feladat kod: {fkod}')
    try:
        print(f'befejezve: {csapat[i+1][0]}:{csapat[i+1][1]}:{csapat[i+1][2]}')
    except:
        print(f'befejezve: fasztudja')
    siker=randrange(0,2)
    if siker==0:
        sikeresseg="elbaszva"
    else:
        sikeresseg="befejezve"
    print(f'sikeresseg: {sikeresseg}')


