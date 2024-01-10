import os

# -- 1 --
print("-- 1 --")
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}pitypang.txt','r')
lines=f.readlines()
f.close()
foglal=[]
for line in lines:
    foglal.append(line.split())
foglal.remove(foglal[0])

f2=open(f'{path}{os.sep}src{os.sep}honapok.txt','r')
lines=f2.readlines()
honapok=[]
for line in lines:
    honapok.append(line[0:len(line)-1:])

# -- 2 --
print("-- 2 --")
max=0
for i in range(len(foglal)):
    tartozkodas=(int(foglal[i][3]))-(int(foglal[i][2]))
    if tartozkodas>=max:
        max=tartozkodas
        srsz=foglal[i][0]
        nev=foglal[i][6]    
print('a leghosszabb idot a szallodaban tartozkodo adatai:')
print(f'{nev} ({srsz}) - {max}')

# -- 3 --
print("-- 3 --")

#tavasz 01.01-04.30. | 1-91     -> 9000
#nyar   05.01-08.31. | 92-213   -> 10000
#osz    09.01-12.31. | 214-366  -> 8000
f2=open(f'{path}{os.sep}src{os.sep}bevetel.txt','w')
bevetel=0
for i in range(len(foglal)):
    enap=int(foglal[i][2])
    tnap=int(foglal[i][3])
    osszeg=0
    for j in range(enap,tnap):
        if (j>=1) and (j<=91):
            osszeg=osszeg+9000
        if (j>=92) and (j<=213):
            osszeg=osszeg+10000
        if (j>=214) and (j<=366):
            osszeg=osszeg+10000
    osszeg=osszeg*int(foglal[i][4])
    osszeg=osszeg+((tnap-enap)*1000)

    
    #f2.write(f'{foglal[i][0]}:{osszeg}\n')
    bevetel=bevetel+osszeg
f2.close()
print(f'a szalloda ossz eves bevetele: {bevetel} Ft')

#minta
print("--------------------------------------------------------------------")
print("srsz szobasz enap    tnap    vendegeksz  reggeli nev"                )
print("1    5       3       13      1           1       Huszar_Hajnalka"    )
print("--------------------------------------------------------------------")
#minta


# -- 4 --
print("-- 4 --")
vej=0
aktnap=0
havi=[]

for i in range(12):
    havi.append(0)

#kibaszott csoves megoldas, de leszarom mert mar unom ezt a feladatot
for i in range(len(foglal)):
    enap=int(foglal[i][2])
    tnap=int(foglal[i][3])
    szorzo=int(foglal[i][4])    
    j=enap
    for j in range((tnap-enap)+1):
        aktnap=enap+j
        if aktnap>=1 and aktnap<=31:
            havi[0]=havi[0]+(1*szorzo)
        if aktnap>=32 and aktnap<=59:
            havi[1]=havi[1]+(1*szorzo)
        if aktnap>=60 and aktnap<=90:
            havi[2]=havi[2]+(1*szorzo)
        if aktnap>=91 and aktnap<=120:
            havi[3]=havi[3]+(1*szorzo)
        if aktnap>=121 and aktnap<=151:
            havi[4]=havi[4]+(1*szorzo)
        if aktnap>=152 and aktnap<=181:
            havi[5]=havi[5]+(1*szorzo)
        if aktnap>=182 and aktnap<=212:
            havi[6]=havi[6]+(1*szorzo)
        if aktnap>=213 and aktnap<=243:
            havi[7]=havi[7]+(1*szorzo)
        if aktnap>=244 and aktnap<=273:
            havi[8]=havi[8]+(1*szorzo)
        if aktnap>=274 and aktnap<=304:
            havi[9]=havi[9]+(1*szorzo)
        if aktnap>=305 and aktnap<=334:
            havi[10]=havi[10]+(1*szorzo)
        if aktnap>=335 and aktnap<=365:
            havi[11]=havi[11]+(1*szorzo)


for i in range(len(havi)):
    print(f'{i+1}: {havi[i]} vendegej')



# -- 5 --
print("-- 5 --")

szobak=[[]]

for i in range(26):
    szobak.insert(i,[])



def enapok(erk,tav):
    tnapok=[]
    i=erk
    for erk in range(tav-erk+1):
        tnapok.append(i)
        i=i+1
    return tnapok


for i in range(len(foglal)):
    sszam=int(foglal[i][1])
    #szobak[int(sszam)-1].append(enapok(int(foglal[i][2]),int(foglal[i][3])))
    for j in range(len(enapok(int(foglal[i][2]),int(foglal[i][3])))):
        szobak[int(sszam)-1].append(enapok(int(foglal[i][2]),int(foglal[i][3]))[j])
    
    

jon=20
megy=25
count=0

for i in range((megy-jon)+1):
    aktnap=jon+i
    for j in range(len(szobak)):
        print(j)