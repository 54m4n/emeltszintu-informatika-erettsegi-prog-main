import os
import math

# -- 1 --
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}program.txt','r')
hossz=int((len(f.readlines())))
f.close()
f=open(f'{path}{os.sep}src{os.sep}program.txt')
prog=[]
for i in range(hossz):
    prog.append(f.readline().split())
del prog[0]
f.close()

# -- 2 --
print("-- 2 --")
#utasitas=int(input("kerem az utasitas sorszamat: "))
utasitas=8

utasitas=utasitas-1

print("-- 2a. --")
sorhossz=len(str(prog[utasitas][0]))
ellentetek=["ED","DE","KN","NK"]

e=False
i=0
while e!=True and i<=sorhossz:
    aktpar=prog[utasitas][0][i:i+2:1]
    if len(aktpar)==2 and aktpar in ellentetek:
        e=True
    else:
        i=i+1

if e==True:
    print(f'a(z) {utasitas+1}. sor egyszerusitheto')
else:
    print(f'a(z) {utasitas+1}. sor NEM egyszerusitheto')

print("-- 2b. --")
#nemkell beszarni, hamar rajottem. szoval akarmerre megy, vagy EK, EN, DK, DN iranyban visszalehet takarodni a 0 pozicioba. marcsak azt kell eldonteni, melyik iranyba ment tobbet, mert az ellenkezobe kell a ketto kulonbseget visszamenni. pl.: ha fel ment 15-ot, le 10-et, akkor 15-10-et (5) kell LE menni, ugyanez a vizszintes iranyban.
#a feladat meg ocskan ellett kurva, ugyanis azt hazudja:
#'A választ a következ formában jelenítse meg: 3 lépést kell tenni az ED, 4 lépést a KN tengely mentén.'
#tehat mar eleve a pelda atbasz, mert NEM csak az a lenyeg, hogy ED tengelyen mennyit kell menni, hanem az, hogy MERRE! FAAAAASZ!

e,d,k,n=0,0,0,0

for i in range(int(len(str(prog[utasitas][0])))):
    aktkar=str(prog[utasitas][0])[i:i+1:1]
    if aktkar=="E":
        e=e+1
    if aktkar=="D":
        d=d+1
    if aktkar=="K":
        k=k+1
    if aktkar=="N":
        n=n+1
#elvegzem a szukseges muveleteket, majd torlom a szuksegtelen valtozot, hogy a kesobbiekben feltetelkent szabhassam meg, hogy letezik-e
if e>=d:
    d=e-d
    del e
else:
    e=d-e
    del d
if k>=n:
    n=k-n
    del k
else:
    k=n-k
    del n
szoveg=""
print("vissza a picsaba a legegyszerubb uton: ")
if "e" in locals():
    szoveg=szoveg+(f'E iranyba {e} lepes, ')
if "d" in locals():
    szoveg=szoveg+(f'D iranyba {d} lepes, ')
if "k" in locals():
    szoveg=szoveg+(f'K iranyba {k} lepes.')
if "n" in locals():
    szoveg=szoveg+(f'N iranyba {n} lepes.')
print(szoveg)

print("-- 2c. --")
# itt se kell befosni, a koordinatak altal hatarolt negyszog atloja (derekszogu haromszog szamitas) lesz a maxatlo, vagyis a "legvonal".
e,d,k,n=0,0,0,0
maxatlo=0
atlo=0
lepes=0
for i in range(len(prog[utasitas][0])):
    aktkar=str(prog[utasitas][0])[i:i+1:1]
    #novelem az egtajak szerinti tavolsagot
    if aktkar=="E":
        e=e+1
    if aktkar=="D":
        d=d+1
    if aktkar=="K":
        k=k+1
    if aktkar=="N":
        n=n+1
    #atlot szamolok es ellenorzom, hogy meguti-e a maxatlo szintjet. ha igen, csere.
    if e!=0 and k!=0:
        atlo=math.sqrt(pow(k,2)+pow(e,2))
        if atlo>=maxatlo:
            maxatlo=atlo
            lepes=i
    if e!=0 and n!=0:
        atlo=math.sqrt(pow(n,2)+pow(e,2))
        if atlo>=maxatlo:
            maxatlo=atlo
            lepes=i
    if d!=0 and k!=0:
        atlo=math.sqrt(pow(k,2)+pow(d,2))
        if atlo>=maxatlo:
            maxatlo=atlo
            lepes=i
    if d!=0 and n!=0:
        atlo=math.sqrt(pow(n,2)+pow(d,2))
        if atlo>=maxatlo:
            maxatlo=atlo
            lepes=i

print(f'a robot a(z) {lepes}. lepesnel volt legvonalba a legtavolabb, vagyis ennyire: {round(maxatlo,3)}')

# -- 3 --
print("-- 3 --")
for j in range(hossz-1):
    energia=0
    for i in range(len(prog[j][0])-1):
        if i==0: #vagyis a start
            energia=energia+2
        aktkar=str(prog[j][0])[i:i+1:1] #aktualis karakter
        kovkar=str(prog[j][0])[i+1:i+2:1] #az aktualist koveto karakter
        if aktkar!=kovkar: #ha a ketto nem egyezik az iranyvaltas
            energia=energia+2
        if aktkar==kovkar: #ha egyezik, az sima egyenes haladas
            energia=energia+1
    if energia<=100:
        print(f'a(z) {j+1}. utasitas energiaigenye: {energia}, tehat boven jo a 100 egysegnyi kis akksi.')
    else:
        print(f'a(z) {j+1}. utasitas energiaigenye: {energia}, tehat FOS a 100 egysegnyi kis akksi, ide az 1000-es kell.')

# -- 4 --
print("-- 4 --")
f2=open(f'{path}{os.sep}src{os.sep}ujprog.txt','w')
for j in range(hossz-1):
    ujkod=""
    aktcount=1
    u=str(prog[j][0])
    for i in range(int(len(str(u)))):
        aktkar=str(u)[i:i+1:1]
        kovkar=str(u)[i+1:i+2:1]
        if aktkar==kovkar:
            aktcount=aktcount+1
        else:
            if aktcount==1:
                ujkod=ujkod+aktkar
            else:
                ujkod=ujkod+str(aktcount)+aktkar
            aktcount=1
    f2.write(f'{ujkod}\n')
    print(f'{ujkod}')
f2.close()

# -- 5 --
print("-- 5 --")
szoveg=""
f3=open(f'{path}{os.sep}src{os.sep}ujprog.txt')
prog2=[]
for i in range(hossz):
    prog2.append(f3.readline().split())
f3.close()

for k in range(hossz-1):
    u=prog2[k][0]
    for i in range(len(u)):
        aktkar=u[i:i+1:1]
        kovkar=u[i+1:i+2:1]
        if aktkar.isnumeric():
            for j in range(int(aktkar)-1):
                szoveg=szoveg+kovkar
        else:
            szoveg=szoveg+aktkar
    print(szoveg)
