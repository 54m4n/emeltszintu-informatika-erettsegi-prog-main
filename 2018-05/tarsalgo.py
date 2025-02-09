import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--

path=os.path.dirname(__file__)
rows=[]
f=open(f'{path}{os.sep}src{os.sep}ajto.txt','r')
for line in f:
    rows.append(line.strip().split(' '))
f.close()

#--2--
print('--2--')

print(f'elso bemeno szemely ID: {rows[0][2]}')

i=len(rows)-1
while rows[i][3]!="ki":
    i=i-1

print(f'utso kimeno szemely ID: {rows[i][2]}')

#--3 es 4--
print('--3 es 4--')
athaladas=[]
uniqid=[]
osszathaladas=[]
for i in range(len(rows)):
    athaladas.append(rows[i][2])
    if rows[i][2] not in uniqid:
        uniqid.append(rows[i][2])

bennmaradt=[]
fw=open(f'{path}{os.sep}src{os.sep}athaladas.txt','w')    
for i in range(len(uniqid)):
    fw.write(f'{uniqid[i]} {athaladas.count(uniqid[i])}\n')
    if (athaladas.count(uniqid[i])%2!=0):
        bennmaradt.append(uniqid[i])
fw.close()
bennmaradt.sort()
print(f'a vegen a tarsalgoban voltak: {bennmaradt}')

#--5--
bent=0
max=0
idopont=""

for i in range(len(rows)):
    if rows[i][3]=="be":
        bent=bent+1
        if bent>max:
            max=bent
            idopont=(f'{rows[i][0]}:{rows[i][1]}')
    else:
        bent=bent-1
    
print(f'{idopont}-kor voltak a legtobben a tarsalgoban')

#--6 es 7--
print('--6 es 7--')

emberid=39
jonmegy=[]
for i in range(len(rows)):
    if rows[i][2]==str(emberid):
        jonmegy.append(f'{rows[i][0]}:{rows[i][1]}')

for i in range(0,len(jonmegy),2):
    try:
        print(jonmegy[i],jonmegy[i+1])
    except:
        print(jonmegy[i])
        
#--8--
print('--8--')

delta=0

def percbe(o,p,o2,p2):
    delta=abs((o*3600+p*60)-(o2*3600+p2*60))
    return round(delta/60)

if len(jonmegy)%2!=0:
    ig=len(jonmegy)-1
    delta=percbe(int(str(jonmegy[len(jonmegy)-1]).split(':')[0]),int(str(jonmegy[len(jonmegy)-1]).split(':')[1]),15,0)
else:
    ig=len(jonmegy)



for i in range(0,ig,2):
    delta=delta+percbe(int(str(jonmegy[i]).split(':')[0]),int(str(jonmegy[i]).split(':')[1]),int(str(jonmegy[i+1]).split(':')[0]),int(str(jonmegy[i+1]).split(':')[1]))
    
if len(jonmegy)%2!=0:    
    print(f'az alabbi user: {emberid} benntoltott ideje {delta} perc, a megfigyeles vegen bentvolt')
else:
    print(f'az alabbi user: {emberid} benntoltott ideje {delta} perc')