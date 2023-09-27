import os

#-- 1 --
print("-- 1 --")
maganhangzok=["a","e","i","o","u"]

#beker=input("kerem a szot: ")
beker="akarmi"

van=False
i=0
while van==False and i<len(maganhangzok):
    if str(maganhangzok[i]) in beker:
        van=True
    i=i+1
if van==True:
    print(f'a(z) {beker} szoban VAN maganhangzo')
else:
    print(f'a(z) {beker} szoban NINCS maganhangzo')
    
# -- 2 --
print("-- 2 --")
path=(f'{os.path.dirname(__file__)}')
f=open(f'{path}{os.sep}src{os.sep}szoveg.txt',"r")
szoveg=f.readlines()
f.close()
leghosszabbszo=""
for i in range(len(szoveg)):
    if len(szoveg[i][0:len(szoveg[i])-1:])>=len(leghosszabbszo):
        leghosszabbszo=szoveg[i][0:len(szoveg[i])-1:]
print(f'a leghosszabb szo: "{leghosszabbszo}", ami {len(leghosszabbszo)} db. karakter')

# -- 3 --
print("-- 3 --")
mhangzok=0
szocount=0
for i in range(len(szoveg)):
    if i!=len(szoveg)-1:
        aktszo=szoveg[i][0:len(szoveg[i])-1:]
    else:
        aktszo=szoveg[i][0:len(szoveg[i]):]
    for j in range(len(maganhangzok)):
        mhangzok=mhangzok+aktszo.count(maganhangzok[j])
    if mhangzok>=len(aktszo)-mhangzok:
        szocount=szocount+1
    mhangzok=0
    
print("a msh-nal tobb mgh-t tartalmazo szavak/osszes szo : szazalekos arany")

print(f'{szocount}/{len(szoveg)} : {round(szocount/(len(szoveg)/100),2)}%')    

# -- 4 --
print("-- 4 --")
otbetus=[]

for i in range(len(szoveg)):
    aktszo=((szoveg[i][0:len(szoveg[i])-1:]))
    if len(aktszo)==5:
        otbetus.append(aktszo)

#kozep=input("kerem a szoletra kozepet /3 betut/: ")
kozep="isz"

for i in range(len(otbetus)):
    if str(otbetus[i][1:4:])==kozep:
        print(otbetus[i],end=" ")
print()
# -- 5 --
print("-- 5 --")
f2=open(f'{path}{os.sep}src{os.sep}letra.txt','w')

letrak=[]
uniqletrak=[]
for i in range(len(otbetus)):
    letrak.append(otbetus[i][1:4:])

for i in range(len(letrak)):
    if letrak.count(letrak[i])!=1 and letrak[i] not in uniqletrak:
        uniqletrak.append(letrak[i])
        
for i in range(len(uniqletrak)):
    for j in range(len(otbetus)):
        aktszo=otbetus[j]
        if uniqletrak[i]==aktszo[1:4:]:
            #f2.write(f'{aktszo}\n')
            f2.write(f'{aktszo}\n')
    f2.write("\n")

 