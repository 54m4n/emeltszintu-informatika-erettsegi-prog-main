import os

#--1--
path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}veetel.txt','r')
wolf=[]
i=0
for l in f:    
    wolf.append(l)
f.close()

#--2--
print('--2--')

print(f'1. rogzites RA szama: {wolf[0].split()[1]}')
print(f'2. rogzites RA szama: {wolf[len(wolf)-2].split()[1]}')

#--3--
print('--3--')

for i in range(len(wolf)):
    if wolf[i].find("farkas")!=-1:
        print(f'nap: {wolf[i-1].split()[0]} RA szam: {wolf[i-1].split()[1]}')

#--4--
print('--4--')

rec=[]
for i in range(0,len(wolf),2):    
    rec.append(wolf[i].split())
udays=[]

for i in range(len(rec)):
    if (int(rec[i][0])) not in udays:
        udays.append(int(rec[i][0]))

udays.sort()
urecs=[]

for i in range(len(udays)):
    urecs.append(0)

for i in range(len(rec)):
    urecs[int(rec[i][0])-1]=urecs[int(rec[i][0])-1]+1

for i in range(len(udays)):
    print(f'{udays[i]}. nap: {urecs[i]} radioamator')
    
#--5--
print('--5--')
resetrow=[]


for i in range(1,len(wolf),2):
    if (wolf[i-1].split()[0])=="1":
        aktsor=(wolf[i].split('\n')[0])
        print(wolf[i-1].split()[0])
        print(aktsor)

        
        