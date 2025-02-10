import os
import platform

if platform.system()=="Windows":
    os.system('cls')
else:
    os.system('clear')

#--1--
path=os.path.dirname(__file__)

f=open(f'{path}{os.sep}src{os.sep}utasadat.txt')
utasadat=[]
for l in f:
    utasadat.append(l.strip().split())
f.close()

print(utasadat[0])
print("--------")

u=[]
utak=[]

for i in range(len(utasadat)):
    aktindex=int(utasadat[i][0])
    j=i
    while aktindex==int(utasadat[j][0]) and j<=len(utasadat):
        u.append(utasadat[j])
        j=j+1
    utak.insert(aktindex,u)
    u=[]
    i=j

print(utak[0])