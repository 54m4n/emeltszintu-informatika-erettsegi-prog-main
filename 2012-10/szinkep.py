import os

#--1---

path=os.path.dirname(__file__)
f=open(f'{path}{os.sep}src{os.sep}kep.txt')

temp=[]
for i in f:    
    temp.append(i.split())    
f.close()

kep = []
t=0
for i in range (50):
    new = []
    for j in range (50):
        new.append(temp[t])
        t=t+1
    kep.append(new)

#--2--
print('--2--')

beker=['200','96','64']

van="nem letezik"
for i in range(50):
    for j in range(50):
        if beker==kep[i][j]:
            van="letezik"
            break

print(f'a bekert rgb kod ({beker}) {van} a kepen')

#--3--
print('--3--')

keres=kep[34][7]
sorban=kep[34].count(keres)
oszlopban=0

for i in range(50):
    if kep[i][7]==keres:
        oszlopban=oszlopban+1
    
print(f'sorban: {sorban}, oszlopban: {oszlopban}')

#--4--
print('--4--')

voros=['255','0','0']
zold=['0','255','0']
kek=['0','0','255']

r=0
g=0
b=0



for i in range(50):
    for j in range(50):
        if kep[i][j]==voros:
            r=r+1
        if kep[i][j]==zold:
            g=g+1
        if kep[i][j]==kek:
            b=b+1

if r>=g and r>=b:
    max="voros"
if g>=r and g>=b:
    max="zold"
if b>=r and b>=g:
    max="kek"

print(f'a voros/zold/kek kozul a {max}-bol van a legtobb')

#--5--
print('--5--')



for i in range(50):
    for j in range(50):
        if (i<=2 or i>=len(kep)-3):
            kep[i][j]=['0','0','0']

        if (j<=2 or j>=47):
            kep[i][j]=['0','0','0']


#--6--
print('--6--')
f2=open(f'{path}{os.sep}src{os.sep}keretes.txt','w')

for i in range(50):
    for j in range(50):
        beir=str(kep[i][j])
        f2.write(beir.replace()
        f2.write('\n')
    