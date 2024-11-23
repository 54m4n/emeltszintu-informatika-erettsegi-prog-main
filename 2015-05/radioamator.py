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
    nap=wolf[i].split()[0]
    srsz=wolf[i].split()[1]    
    if nap not in rec:
        rec.append(nap)
    

print(rec)