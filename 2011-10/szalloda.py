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
print(honapok)
