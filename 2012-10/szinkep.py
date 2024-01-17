import os

#--1---

path=os.path.dirname(__file__)

f=open(f'{path}{os.sep}src{os.sep}kep.txt')

temp=[]

for i in f:    
    temp.append(i.split())    
f.close()

kep=[[]]
'''
kep=[[]]
kep[0].append("fing")
kep[0].append("segg")
print(kep[0])
'''


k=0
t=0

for i in range(50):
    print(k)
    for j in range(50):
        kep[k].append(temp[t])
        t=t+1
    k=k+1

print(kep[i])
