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

#minta
print("--------------------------------------------------------------------")
print("srsz szobasz enap    tnap    vendegeksz  reggeli nev"                )
print("1    5       3       13      1           1       Huszar_Hajnalka"    )
print("--------------------------------------------------------------------")
#minta

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

# -- 4 --
print("-- 4 --")
vej=0
aktnap=0
havi=[]
for i in range(len(foglal)):
    vej=vej+int(foglal[i][4])*(int(foglal[i][3])-int(foglal[i][2]))
    enap=int(foglal[i][2])
    tnap=int(foglal[i][3])

    

'''
januar
31
1
februar
28
32
marcius
31
60
aprilis
30
91
majus
31
121
junius
30
152
julius
31
182
augusztus
31
213
szeptember
30
244
oktober
31
274
november
30
305
december
31
335
'''