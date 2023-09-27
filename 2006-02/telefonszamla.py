import os
import math

path=os.path.dirname(__file__)
print(path)

f=open(f'{path}\src\HIVASOK.TXT')
hivasok=f.read().split()
f.close()

f=open(f'{path}\src\HIVASOK.TXT')
sorok=f.readlines()
f.close()

# nos mivel a feladatban a faszomse kerte, hogy kulturaltan eltaroljam az adatokat, ezert csak muveleteket fogok veluk vegezni csovesbe...

def minduration(h,m,s,h2,m2,s2):
    minduration=((h2*3600+m2*60+s2)-(h*3600+m*60+s))/60
    return math.ceil(minduration)
    
def csucsidoe(h):
    csucsidoe=False
    if h>=7 and h<18:
        csucsidoe=True
    return csucsidoe
        
def mobile(telszam):    
    mobile=False
    if telszam[0:2:1]=="39" or telszam[0:2:1]=="41" or telszam[0:2:1]=="71":
        mobile=True
    return mobile

# ...de legalabb kurvajok a def-ek 

countCsucsido=0
countSzamlazottPercek=0
countMobilPercek=0
fizetes=0
beszeltPercek=0
f=open(f'{path}\src\percek.txt','w')

for i in range(0,(len(hivasok)),7):
    actHour=int(hivasok[i])
    actMin=int(hivasok[i+1])
    actSec=int(hivasok[i+2])
    actEndHour=int(hivasok[i+3])
    actEndMin=int(hivasok[i+4])
    actEndSec=int(hivasok[i+5])
    telnumber=str(hivasok[i+6])
    
    beszeltPercek=int(minduration(actHour,actMin,actSec,actEndHour,actEndMin,actEndSec))
    countSzamlazottPercek=countSzamlazottPercek+beszeltPercek
    
    if csucsidoe(actHour):
        countCsucsido=countCsucsido+1
        if mobile(telnumber):
            fizetes=fizetes+(69.175*beszeltPercek)
        else:
            fizetes=fizetes+(30*beszeltPercek)
    
    
    if mobile(telnumber):
        countMobilPercek=countMobilPercek+beszeltPercek
    f.write(f'beszelt perc: {beszeltPercek}, hivott szam: {telnumber}\n')

f.close()
    
print(f'csucsidoben {countCsucsido} db hivas tortent, csucsidon kivul {(int(len(sorok)))-countCsucsido} db.')
print(f'osszesen {countSzamlazottPercek} percet telefontalt\nebbol vezetekes: {countSzamlazottPercek-countMobilPercek}, mobil: {countMobilPercek}')
print(f'az osszes csucsidon beluli hivas osszege: {round(fizetes,2)}')
