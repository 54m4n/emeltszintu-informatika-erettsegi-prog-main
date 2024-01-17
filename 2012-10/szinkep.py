import os

#--1---

path=os.path.dirname(__file__)

f=open(f'{path}{os.sep}src{os.sep}kep.txt')

kep=[]

for i in f:
    kep.append(i.split())
f.close()

#--2--
print('--2--')

i=0


'''
beker=[]
for i in range(3):
    beker.append(str(input(f'kerem a(z) {i+1}. erteket: ')))
'''
beker=['255','0','255']


talal=False
van=False
i=0


while talal!=True:
    if i==len(kep):
        talal=True
        break
    if kep[i]==beker:
        talal=True
        van=True
    i=i+1

if van==True:
    print(f'a bekert ertek ({beker}): VAN ({i}. sor)')
else:
    print(f'a bekert ertek ({beker}): NINCS')


#--3--
print('--3--')

for i in range(50):
    for j in range(50):
        if i==34 and j==7:
            keppontkeres=kep[i]

print(keppontkeres)