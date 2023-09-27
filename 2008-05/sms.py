# hat ez meg az elozo geci, kajakra mennyivel normalisabb mar mint az a buzi kemias feladat? megkeresem azt a faszt aki anno azt csinalta es kerdorevonom
import os

# -- 1 --
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}sms.txt')
hossz=int(f.readline()[:-1])
f.close()

f=open(f'{path}{os.sep}src{os.sep}sms.txt')
smsek=[]
ujsmsek=[]
for i in range((hossz*2)+1):
    smsek.append(f.readline()[:-1])

for i in range(1,hossz*2,2):
    ujsmsek.append([smsek[i],smsek[i+1]])
f.close()

# -- 2 --
print("-- 2 -- ")
print(f'legujabb uzenet: {ujsmsek[len(ujsmsek)-1][1]}')

# -- 3 --
print("-- 3 -- ")
max=0
min=len(ujsmsek[0][1])


for i in range(len(ujsmsek)):
    if len(ujsmsek[i][1])>=max:
        max=len(str(ujsmsek[i][1]))
        maxszoveg=(f'leghosszabb sms: {ujsmsek[i][0].split()[0]} ora, {ujsmsek[i][0].split()[1]} perckor erkezett, tartalma: {ujsmsek[i][1]}')
    if len(ujsmsek[i][1])<=min:
        min=len(str(ujsmsek[i][1]))
        minszoveg=(f'legrovidebb sms: {ujsmsek[i][0].split()[0]} ora, {ujsmsek[i][0].split()[1]} perckor erkezett, tartalma: {ujsmsek[i][1]}')
print(minszoveg)
print(maxszoveg)

# -- 4 --
print("-- 4 -- ")
count=[0,0,0,0,0]
for i in range(len(ujsmsek)):
    if len(ujsmsek[i][1])>=1 and len(ujsmsek[i][1])<=20:
        count[0]=count[0]+1
    if len(ujsmsek[i][1])>=21 and len(ujsmsek[i][1])<=40:
        count[1]=count[1]+1
    if len(ujsmsek[i][1])>=41 and len(ujsmsek[i][1])<=60:
        count[2]=count[2]+1
    if len(ujsmsek[i][1])>=61 and len(ujsmsek[i][1])<=80:
        count[3]=count[3]+1
    if len(ujsmsek[i][1])>=81 and len(ujsmsek[i][1])<=100:
        count[4]=count[4]+1

print(f'sms hossz statisztikak:\n1-20: {count[0]} db.\n21-40: {count[1]} db.\n41-60: {count[2]} db.\n61-80: {count[3]} db.\n81-100: {count[4]} db.')

# -- 5 --
print("-- 5 --")

counter=1
ccounter=0

for i in range(0,len(ujsmsek)):
    aktora=ujsmsek[i][0].split()[0]
    eora=ujsmsek[i-1][0].split()[0]
    if eora==aktora:
        counter=counter+1
        if counter>10:
            ccounter=ccounter+1
    else:
        counter=1
print(f'ez az Erno nevu faszinger hivhatja fel a kozpontot: {ccounter} sms miatt...')        

# -- 6 --
print("-- 6 --")
sunaszam="123456789"
smsidok=[]

for i in range(len(ujsmsek)):
    if ujsmsek[i][0].split()[2]==sunaszam:
        aktora=int(ujsmsek[i][0].split()[0])
        aktperc=int(ujsmsek[i][0].split()[1])
        smsidok.append((aktora*60)+aktperc)

maxido=0
if len(smsidok)==1:
    print("nincs eleg mintavetel a sunahoz")
else:
    for i in range(1,len(smsidok)):
        if smsidok[i]-smsidok[i-1]>maxido:
            maxido=smsidok[i]-smsidok[i-1]
    print(f'a suna sms kuldesi idejei kozott a leghosszabb ido ami eltelt: {maxido//60} ora, {maxido-((maxido//60)*60)} perc.')

# -- 7 --
print("-- 7 --")

f=open(f'{path}{os.sep}src{os.sep}sms.txt','a')
print("-> kerem a kesett sms adatait: <-")

ora=input('ora: ')
perc=input('perc: ')
telszam=input('telszam: ')
szoveg=input('szoveg: ')

f.write(f'\n{ora} {perc} {telszam}')
f.write(f'\n{szoveg}')
f.close()

# -- 8 -- 
# az elozo feladatban felvitt adatokat azert nem olvassa be, mert az elso sorba beleciganykodtak a 30-as szamot ami alapjan dolgoztam. fosok ra, nem nagy kaland, ezert nem irom at.
print("-- 8 --")

uniqtelszamok=[]
for i in range(len(ujsmsek)):
    if ujsmsek[i][0].split()[2] not in uniqtelszamok:
        uniqtelszamok.append(ujsmsek[i][0].split()[2])

uniqtelszamok.sort()        

for i in range(len(uniqtelszamok)):
    print(uniqtelszamok[i])
    for j in range(len(ujsmsek)):
        if uniqtelszamok[i]==ujsmsek[j][0].split()[2]:
            print(ujsmsek[j][0].split()[0],ujsmsek[j][0].split()[1],ujsmsek[j][1])