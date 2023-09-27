import os

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}musor.txt',"r")
zenek=f.read().split("\n")
f.close()

# szetszedi az adatszerkezetet ugy, hogy minden elem a tomb x. eleme legyen
def parser(str):
    ujtomb=[]
    actch=""
    i=0
    while len(ujtomb)<=2:
        while str[i]!=" ":
            actch=actch+str[i]
            i=i+1
        if i==1:
            if actch=="1":
                actch="Pina FM"
            if actch=="2":
                actch="Csocs FM"
            if actch=="3":
                actch="Segg FM"                
        ujtomb.append(actch)
        actch=""
        i=i+1    
    ujtomb.append(str[i::].split(":")[0])
    ujtomb.append(str[i::].split(":")[1])    
    return ujtomb

# a kapott perc masodpercet atvaltja ora, perc, masodpercre, es egy abszolutmasodperccel is visszatud terni
def minsecatvalt(m,s):
    sec=m*60+s
    hour=sec//3600
    min=(sec-(hour*3600))//60
    sec=sec-((hour*3600)+(min*60))
    abssec=(min*60)+sec
    return hour,min,sec,abssec

countPinaFM=0
countCsocsFM=0
countSeggFM=0

ujtomb=[]

# a tomb, amely normalizalva tartalmazza a beolvasott adatokat. leszarom, hogy 1-2-3 volt a radio neve (hogy elkeruljek a "reklamot" hahahah..). en inkabb elneveztem.
for i in range(1,int(zenek[0])+1):
    ujtomb.append(parser(zenek[i]))
    if ujtomb[i-1][0]=="Pina FM":
        countPinaFM=countPinaFM+1
    if ujtomb[i-1][0]=="Csocs FM":
        countCsocsFM=countCsocsFM+1
    if ujtomb[i-1][0]=="Segg FM":
        countSeggFM=countSeggFM+1

# -- 2 ---
print(f'csatornakon hallgathato szamok szamossaga:\nPina FM: {countPinaFM} db., Csocs FM: {countCsocsFM} db., Segg FM: {countSeggFM} db.')

m=0
s=0

# -- 3 --
for i in range(len(ujtomb)):
    if ujtomb[i][0]=="Pina FM" and ujtomb[i][3]=="Eric Clapton":
        m=m+int(ujtomb[i][1])
        s=s+int(ujtomb[i][2])
print(f'az elso es utolso Eric Clapton szam kozott a Pina FM-en eltelt ido: {minsecatvalt(m,s)[0]} ora, {minsecatvalt(m,s)[1]} perc, {minsecatvalt(m,s)[2]} masodperc')

# -- 4 -- majdnem leszoptam magam mire ez sikerult. egyebkent meg szerintem elvan baszva a musor.txt, ugyanis az egyik adonak az adasa mar reg veget ert, hiaba irja a szoveg, hogy biztos lehetsz benne, hogy van adas mind a ket adon. egy nagy FASZT!
i=0
while not (ujtomb[i][3]=="Omega" and ujtomb[i][4]=="Legenda"):
    i=i+1
   
omegaLegendaAdo=ujtomb[i][0]

abssec=0
abssec1=0
abssec2=0

# nagyon jampi megoldas, igy hatarozom meg azt a 2 adot, amin nem ment a kerdeses szam
radiok=["Pina FM","Csocs FM","Segg FM"]
radiok.remove(ujtomb[i][0])
print(radiok)

# kiszamolom az osszes ado musoridejet abszolut masodperc ertekben. itt latszik, hogy az egyik adon az adas mar reg vegetert
for j in range(i):
    if ujtomb[j][0]==omegaLegendaAdo:
        abssec=abssec+minsecatvalt(int(ujtomb[j][1]),int(ujtomb[j][2]))[3]
    if ujtomb[j][0]==radiok[0]:
        abssec1=abssec1+minsecatvalt(int(ujtomb[j][1]),int(ujtomb[j][2]))[3]
    if ujtomb[j][0]==radiok[1]:
        abssec2=abssec2+minsecatvalt(int(ujtomb[j][1]),int(ujtomb[j][2]))[3]   
        
absseceleje=abssec-minsecatvalt(int(ujtomb[i][1]),int(ujtomb[i][2]))[3]
omegaLegendaSzamhossz=minsecatvalt(int(ujtomb[i][1]),int(ujtomb[i][2]))[3]

print(f'Az Omega - Legenda c. szama a(z) {omegaLegendaAdo} adon volt hallhato.\namugy ekkor kezdodott: {absseceleje}\nekkor ert veget: {abssec}')        

abssec1t=abssec1
abssec2t=abssec2

k=0
i=0
abssec1=0
abssec2=0

# hibakezeles, ha nemlenne adas az egyik adon a kerdeses idopontban
eloado1,szamcim1,eloado2,szamcim2="N/A","N/A","N/A","N/A"

for i in range(len(ujtomb)):
    if ujtomb[i][0]!=omegaLegendaAdo:
        if ujtomb[i][0]==radiok[0] and (abssec1<=absseceleje or abssec1>=abssec) and abssec1t>=absseceleje:
            abssec1=abssec1+(minsecatvalt(int(ujtomb[i][1]),int(ujtomb[i][2]))[3])
            eloado1=ujtomb[i][3]
            szamcim1=ujtomb[i][4]

        if ujtomb[i][0]==radiok[1] and (abssec1<=absseceleje or abssec1>=abssec) and abssec2t>=absseceleje:
            abssec2=abssec2+(minsecatvalt(int(ujtomb[i][1]),int(ujtomb[i][2]))[3])
            eloado2=ujtomb[i][3]
            szamcim2=ujtomb[i][4]
            
print(f'amikor az Omega - Legenda c. szama szolt a(z) {omegaLegendaAdo}-n, akkor:\n a masik 2 csatornan ezek:\n-{eloado1} - {szamcim1}\n-{eloado2} - {szamcim2}')

# -- 5 -- ezt a fasz megfogalmazast! nem a "gaoaf" sztringet kell keresni, mert az NINCS. hanem bekerni valamit. ez fika volt
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}keres.txt',"w")

keres=input("kerek egy sztringet: ")

i=0
print(f'a(z) "{keres}" sztringet tartalmazo szamok:')
for i in range(len(ujtomb)):
    if keres.lower() in ujtomb[i][3].lower() or keres.lower() in ujtomb[i][4].lower():
        print(f'{i}. {ujtomb[i][3]} - {ujtomb[i][4]}')
        f.write(f'{i}. {ujtomb[i][3]} - {ujtomb[i][4]}\n')
f.close()


# -- 6 --favago modszer, de mukodik
i=0
elteltido=0
aktora=0

pinatomb=[]
osszido=0
for i in range(len(ujtomb)):
    if ujtomb[i][0]=="Pina FM":
        pinatomb.append(ujtomb[i])
i=0


while i<=len(pinatomb)-1:
    
    elteltido=elteltido+60
    aktszamhossz=minsecatvalt(int(pinatomb[i][1]),int(pinatomb[i][2]))[3]
    if elteltido+aktszamhossz<=aktora*3600:
        elteltido=elteltido+aktszamhossz
    else:
        elteltido=elteltido+180
        aktora=aktora+1
    i=i+1

h=elteltido//3600
m=(elteltido-(h*3600))//60
s=elteltido-((h*3600)+(m*60))

print(f'a Pina FM uj musorideje: {h}:{m}:{s}')