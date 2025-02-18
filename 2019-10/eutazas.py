import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
path=os.path.dirname(__file__)

f=open(f'{path}{os.sep}src{os.sep}utasadat.txt')
utasadat=[]
for l in f:
    utasadat.append(l.strip().split())
f.close()

aktindex=0
utak=[]
tmptomb=[]
i=0

while i<=len(utasadat)-1:
    if aktindex==int(utasadat[i][0]):
        tmptomb.append(utasadat[i])
        if i+1==len(utasadat):
            utak.insert(aktindex,tmptomb)
    else:
        utak.insert(aktindex,tmptomb)
        tmptomb=[]
        aktindex=int(utasadat[i][0])
    i=i+1



#--2--
print('--2--')
print(f'{len(utasadat)} utas akart felszallni')


#--3--
print('--3--')

def y2d(ymd):
    ymd=str(ymd)
    y=int(ymd[0:4:1])
    m=int(ymd[4:6:1])
    d=int(ymd[6:8:1])
    dayz=y*365+m*31+d
    return(dayz)

ervenytelen=0

for i in range(len(utasadat)):
    if utasadat[i][3]=="JGY" and utasadat[i][4]=="0":
        ervenytelen=ervenytelen+1
    elif utasadat[i][3]!="JGY":
        felszall=y2d(utasadat[i][1][0:8:1])
        ervenyes=y2d(utasadat[i][4][0:8:1])
        if ervenyes<felszall:
            ervenytelen=ervenytelen+1
    
print(f'A buszra {ervenytelen} utas nem szallhatott fel.')


#--4--
print('--4--')
max=0
for i in range(len(utak)):
    if len(utak[i])>max:
        max=len(utak[i])
        megallo=utak[i][0][0]
    
print(f'A legtobb utas a(z) {megallo} megalloban szallt fel ({max} fo).')

#--5--
print('--5--')


kedvezmenyes=0
ingyenes=0
for i in range(len(utasadat)):
    if utasadat[i][3]!="JGY" and y2d(utasadat[i][1][0:8:1])<=y2d(utasadat[i][4][0:8:1]):
        if utasadat[i][3]=="TAB" or utasadat[i][3]=="NYB":
            kedvezmenyes=kedvezmenyes+1
        if utasadat[i][3]=="NYP" or utasadat[i][3]=="RVS" or utasadat[i][3]=="GYK":
            ingyenes=ingyenes+1
    
print(f'Ingyenesen utazok szama: {ingyenes} fo.\nKedvezmenyes utazok szama: {kedvezmenyes} fo.')

#--6--
#nagy lofaszt fogok en elore megadott pszeudo kod alapjan fuggvenyt csinalni, ugy csinalom, ahogy nekem tetszik.. oh wait.... mar megis csinaltam... :D

fw=open(f'{path}{os.sep}src{os.sep}figyelmeztetes.txt','w')
for i in range(len(utak)):
    for j in range(len(utak[i])):
        if utak[i][j][3]!="JGY" and y2d(utak[i][j][1][0:8:1])<y2d(utak[i][j][4][0:8:1]) and (y2d(utak[i][j][4][0:8:1])-y2d(utak[i][j][1][0:8:1])<=3):
            fw.write(f'{utak[i][j][2]} {utak[i][j][4][0:4:1]}-{utak[i][j][4][4:6:1]}-{utak[i][j][4][6:8:1]}\n')
fw.close()import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
path=os.path.dirname(__file__)

f=open(f'{path}{os.sep}src{os.sep}utasadat.txt')
utasadat=[]
for l in f:
    utasadat.append(l.strip().split())
f.close()

print(utasadat[0])

