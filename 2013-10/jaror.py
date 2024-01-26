import os


#--1--

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}jarmu.txt','r')
ell=[]

for i in f:
    ell.append(i.split())

f.close()


#--2--
print('--2--')
print(f'a desztok ennyi orat dolgozatk: {int(ell[len(ell)-1][0])-int(ell[0][0])+1}')

#--3--
print('--3--')

i=1
akt=ell[i][0]

while i<len(ell):
    akt=ell[i-1][0]
    if i==1:
        print(f'{ell[i][0]}. ora: {ell[i-1][3]}')
    elif akt!=ell[i][0]:
        print(f'{ell[i][0]}. ora: {ell[i-1][3]}')
        akt=ell[i][3]
    i=i+1

#   08 46 51 FD-2717

#--4--
print('--4--')

b=0
k=0
m=0
s=0

for i in range(len(ell)):
    if ell[i][3][0:1:1]=="B":
        b=b+1
    elif ell[i][3][0:1:1]=="K":
        k=k+1
    elif ell[i][3][0:1:1]=="M":
        m=m+1
    else:
        s=s+1

print('ellenorzotpont elott athaladt jarmuvek kategoriankent:\n')
print(f'busz: {b} db')
print(f'kamion: {k} db')
print(f'motor: {m} db')
print(f'szgjm: {s} db')


#--5--
print('--5--')

def atvalt(h,m,s):
    sumsec=(int(h)*3600)+(int(m)*60)+s    
    return(sumsec)

deltat=0
akt=0

for i in range(len(ell)):
    try:
        t=(atvalt(int(ell[i+1][0]),int(ell[i+1][1]),int(ell[i+1][2])))-(atvalt(int(ell[i][0]),int(ell[i][1]),int(ell[i][2])))
        if t>=deltat:
            deltat=t
            akt=i
    except:
        IndexError

print('leghosszabb forgalommentes idoszak:')
print(f'{ell[akt][0]}:{ell[akt][1]}:{ell[akt][2]} - {ell[akt+1][0]}:{ell[akt+1][0]}:{ell[akt+1][0]}')


#--6--
print('--6--')
#UB-9408

validak=[]

kersz="L*7***"

for i in range(len(ell)):
    valid=True
    rendsz=(ell[i][3].replace('-',''))

    for j in range(len(rendsz)):
        if (kersz[j]!=rendsz[j]) and kersz[j]!="*":
            valid=False

    if valid==True:
        validak.append(rendsz)


print(f'keresett rendszamra ({kersz}) illeszkedo rendszamok:')

for i in range(len(validak)):
    print(validak[i])

