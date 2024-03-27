import os

#meghatarozom az aktualis python file-om directoryjat, onnan fogom elerni a mellette levo forras txt file-t
path=os.path.dirname(__file__)

#megnyitom a szukseges txt-t, az os.sep meg azert jo, mert a path-ban az os szeparator Windows alatt a \, Linux alatt a /, es igy mindenhol is mukodni fog
f=open(f'{path}{os.sep}42_eredmenyek.txt', encoding="utf8")

#soronkent beolvasom egybe
sorok = f.readlines()
#szetfogom szedni az adatokat de elotte deklaralok egy ures listat
s=[]
#a c-t hivjuk count-nak, az elso sort nemakarom beirni a listamba, ez azert kell, hogy megtudjam allapitani
c=0

#soronkent vegigmegyek, ha a c==0, akkor ugrok, minden mas esetben:
#1. a sorban a kettospontot kicserelem / jelre
#2. az aktualis sort / jelenkent elszeparalom, igyfog kinezni: nev,aktpontszam,osszpontszam
#3. hozzafuzom a szetbaszott sort a listahoz
for sor in sorok:        
    if c!=0:
        sor=sor.replace(":","/")
        sor=sor.strip().split("/")
        s.append(sor)
    c=c+1
f.close()

#abbol indulok ki, hogy ez nem egy dankoros iskola, szoval az osszpontszam mindenkinek ugyanannyi, vagyis ha az elso ertek osszpontszamat nezem, akkor az vonatkozik mindenkire is
osszpontszam=int(s[0][2])

#kesobb ezekre a valtozokra szuksegem lesz, szoval deklaralom
atlag=0
ujrair=0
dicseret=0

#megnyitom irasra az osztaly.txt file-t, ekezetek miatt encodingot is allitok szinten
f=open(f'{path}{os.sep}osztaly.txt', 'w', encoding="utf8")

print("Nev\t | Aktpontszam\t | Szazalek\t | Erdemjegy")
print("----------------------------------------------------")

#ciklus az s nevu lista elejetol a vegeig
for i in range(len(s)):
    #megallapitom az aktualis nevet
    aktnev=s[i][0]
    
    #megallapitom az aktualis pontszamot
    aktpontszam=int(s[i][1])
    
    #kiszamolom ezekbol az aktualis szazalekot
    aktszazalek=round(aktpontszam/(osszpontszam/100))
    
    #if feltetelekkel megallapitom az aktualis erdemjegyet a szazalek alapjan
    if aktszazalek<=50:
        erdemjegy="1"
    
        #ha egyes, ujrair valtozot novelem
        ujrair=ujrair+1
    elif aktszazalek>=51 and aktszazalek<=60:
        erdemjegy="2"
    elif aktszazalek>=61 and aktszazalek<=70:
        erdemjegy="3"
    elif aktszazalek>=71 and aktszazalek<=80:
        erdemjegy="4"
    elif aktszazalek>=81 and aktszazalek<=99:
        erdemjegy="5"
    else:
        erdemjegy="5*"
        
        #ha csillagos 5os, akkor a dicseret valtozot novelem
        dicseret=dicseret+1
    
    #a mindenkori aktualis listamhoz a vegehez hozzafuzom az erdemjegyet, mert az kelleni fog majd
    s[i].append(erdemjegy)
    
    #az atlag szamolashoz ugyebar osszekell adnom az erdemjegyeket, ez kerul az atlag valtozoba
    atlag=atlag+int(erdemjegy[0])
    
    #tabokkal kiprintelem az eredmenyt hogy valahogy azert kinezzen
    print(f'{aktnev}\t | {aktpontszam}\t\t | {aktszazalek}%\t\t | {erdemjegy}')
    
    #egybol bele is irom a fileba
    f.write((f'{aktnev}\t | {aktpontszam}\t\t | {aktszazalek}%\t\t | {erdemjegy}\n'))


#az osztalyatlagot az elobb osszeadott erdemjegyek segitsegevel kiszamolom, az osztaly letszama ugye az s tomb hossza
osztalyatlag=round(atlag/int(len(s)),2)    

#szepen kiirogatom ami kell
print(f'osztaly atlag: {osztalyatlag}')
print(f'ujra irja: {ujrair}')
print(f'dicseret: {dicseret}')

#szepen beleirogatom a fileba ami kell
f.write(f'osztaly atlag: {osztalyatlag}\n')
f.write(f'ujra irja: {ujrair}\n')
f.write(f'dicseret: {dicseret}\n')

#az atlag felettiekhez minden adat a rendelkezesemre all, es ujra vegigkell mennem a tombon emiatt
atlagfelett=0

for i in range(len(s)):
    #nagyon fontos: az s[i], az az aktualis lista egy sora (pl: Bela, 25, 80, 1)
    #az s[i][3] az aktualis sor 3. eleme, vagyis az erdemjegy (pl 1)
    #az s[i][3][0] az aktualis sor 3. elemenek 0. eleme! ez ugyebar a csillagos otos miatt kell. Bela eseteben az s[i][3][0] az siman 1, viszont Ildiko eseteben az s[i][3] az a 5* lenne, az s[i][3][0] az siman az 5, szoval azt mar tudom int-e konvertalni
    if int(s[i][3][0])>osztalyatlag:
        atlagfelett=atlagfelett+1
        
#szepen kiirogatok es beleirogatok ahogy kell        
print(f'atlag felett: {atlagfelett}')
f.write(f'atlag felett: {atlagfelett}\n')

#file-t bezarom hogy ne baszodjon a memoriaba
f.close()